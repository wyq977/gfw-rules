#!/usr/bin/python
# -*- coding: UTF-8 -*-
COMMENT = "#"  # ; or # both can be used
CONFIGSEP = "\n\n"
AUTHOR = "zorro"

from datetime import date
import os
import argparse
import json


def get_lines_from_file(filename):
    f = open(filename, "r")
    text_list = [l.rstrip("\n") for l in f]
    f.close()
    return text_list


def get_json(filename):
    f = open(filename)
    out = json.load(f)
    f.close()
    return out


def get_file_str(filename):
    f = open(filename, "r")
    out_str = f.read()
    f.close()
    return out_str


class Conf:
    def __init__(
        self, filename, is_ios, config_dir, dns, policy, server_filter, filter_remote
    ):
        self.filename = filename
        self.is_ios = is_ios
        self.config_dir = config_dir
        self.dns = get_lines_from_file(dns)
        self.policy = get_json(policy)
        self.server_filter = get_json(server_filter)
        self.filter_remote = get_lines_from_file(filter_remote)  # a list of csv

        # TODO: make it less Loon dependent
        # csv or json would be good
        # filter: local + remote
        # rewrite: local + remote
        # script: local + remote + plugin

    def make_header(self):
        header = ""
        header += "{} Date:   {}\n".format(COMMENT, date.today())
        header += "{} Author: {}\n".format(COMMENT, AUTHOR)
        header += "\n\n"
        return header


class LoonConf(Conf):
    # https://github.com/Loon0x00/LoonExampleConfig/blob/master/example.conf

    # [General]
    def make_general(self):
        dns = self._make_dns()
        out_str = get_file_str(os.path.join(self.config_dir, "general.conf"))
        return out_str + "\n" + dns + CONFIGSEP

    # [Proxy] [Remote Proxy]
    def make_server(self):
        out_str = get_file_str(os.path.join(self.config_dir, "server.conf"))
        server_filter = "[Remote Filter]\n"
        for k, v in self.server_filter.items():
            server_filter += "{}\n".format(self._parse_json_to_str(k, v))

        return out_str + CONFIGSEP + server_filter + CONFIGSEP

    # [Proxy Group]
    def make_policy(self):
        out_str = "[Proxy Group]\n"

        for k, v in self.policy.items():
            out_str += "{}\n".format(self._parse_json_to_str(k, v))

        return out_str + CONFIGSEP

    # [Rule] [Remote Rule]
    # TODO: make it more than just a copy and paste
    def make_filter(self):
        out_str = get_file_str(os.path.join(self.config_dir, "filter.conf"))
        filter_remote = "[Remote Rule]\n"
        # link, policy=全球直连, tag=Custom全球直连, enabled=true

        for rule in self.filter_remote:
            rule_list = rule.split(",")
            # skip ad blocking in mac
            if rule_list[2] == "iPhoneOnly" and not self.is_ios:
                continue
            filter_remote += "{}, policy={}, tag={}, enabled={}\n".format(
                rule_list[0], rule_list[1], rule_list[2], rule_list[3]
            )

        return out_str + CONFIGSEP + filter_remote + CONFIGSEP

    # [URL Rewrite] [Remote Rewrite]
    # TODO: make it more than just a copy and paste
    def make_rewrite(self):
        out_str = get_file_str(os.path.join(self.config_dir, "rewrite.conf"))
        return out_str + CONFIGSEP

    # [Script] [Remote Script] [Plugin]
    # TODO: make it more than just a copy and paste
    def make_script(self):
        if self.is_ios:
            out_str = get_file_str(os.path.join(self.config_dir, "script.conf"))
        else:
            out_str = get_file_str(os.path.join(self.config_dir, "script_mac.conf"))
        return out_str + CONFIGSEP

    # [Mitm]
    def make_local(self):
        out_str = get_file_str(os.path.join(self.config_dir, "local.conf"))
        return out_str + CONFIGSEP

    def _make_dns(self, is_system=True):
        dns_str = ",".join(self.dns)
        if is_system:
            out_str = "dns-server = system," + dns_str
        else:
            out_str = "dns-server = " + dns_str

        return out_str + "\n"

    @staticmethod
    def _parse_json_to_str(name: str, p: dict):
        """Parse json entry to string"""
        if p["mode"] == "select":
            # 代理节点 = select,手动切换,自动选择,DIRECT,img-url=xxx
            return "{}=select,{},img-url={}".format(
                name, ",".join(p["policy"]), p["img"]
            )
        if p["mode"] == "url-test":
            # 自动选择 = url-test,订阅名,url=xxx,interval=300,tolerance=100,img-url=xxx
            config = "url={},interval={},tolerance={}".format(
                p["url"], p["interval"], p["tolerance"]
            )
            return "{}=url-test,{},{},img-url={}".format(
                name, ",".join(p["policy"]), config, p["img"]
            )
        if p["mode"] == "ssid":
            # default=代理节点,cellular=代理节点,"SSID"=代理节点
            config = "default={},cellular={}".format(p["default"], p["cellular"])
            wifi_list = []
            for k, v in p["wifi"].items():
                wifi_list.append('"{}"={}'.format(k, v))
            return "{}=ssid,{},{}".format(name, config, ",".join(wifi_list))
        if p["mode"] == "NameRegex":
            # 香港节点 = NameRegex, FilterKey = "(?i)(港|HK|Hong)"
            return '{} = NameRegex, FilterKey = "{}"'.format(name, p["filterkey"])

        return ""

    def write_conf(self):

        conf = ""
        conf += self.make_header()
        conf += self.make_general()
        conf += self.make_server()
        conf += self.make_policy()
        conf += self.make_filter()
        conf += self.make_rewrite()
        conf += self.make_script()
        conf += self.make_local()

        f = open(self.filename, "w+")
        f.writelines(conf)
        f.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--loon", dest="loon", action="store_true")
    args = parser.parse_args()

    if args.loon:
        loon = LoonConf(
            "local/loon_config_ios.conf",
            True,
            "Loon",
            "dns.txt",
            "policy.json",
            "server_filter.json",
            "filter_remote.csv",
        )
        loon.write_conf()
        loon = LoonConf(
            "local/loon_config_mac.conf",
            False,
            "Loon",
            "dns.txt",
            "policy.json",
            "server_filter.json",
            "filter_remote.csv",
        )
        loon.write_conf()


if __name__ == "__main__":
    main()
