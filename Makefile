.PHONY: help

help: ## Show this help message.
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

ansible_roles:
    cd playbooks && cp template.yml ${name}.yml && sed -e 's/foobar/${name}/' ${name}.yml
    cd roles && ansible-galaxy init ${name}