all: loon

.PHONY: loon clean

loon:
	python3 make_conf.py --loon

clean:
	rm local/loon_config.conf
