PLUGINNAME = $(shell basename $(PWD))
VERSION = $(shell sed -n 's/version=//p' metadata.txt)
ZIPFILE = $(HOME)/$(PLUGINNAME).$(VERSION).zip
.PHONY: help pylint pep8 zip

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  pep8        check Python code with pep8"
	@echo "  pylint      check Python code with pylint"
	@echo "  zip         build zip package"


pep8:
	@pep8 --config=pep8 *.py


pylint:
	@pylint *py


zip:
	rm -f ${ZIPFILE}
	cd ..; zip -9r $(ZIPFILE) $(PLUGINNAME) -x "*.git/*" "*.gitignore" "*pyc" "*__pycache__/*" "*doc/*"
	@echo "Successfully zipped to" $(ZIPFILE)
