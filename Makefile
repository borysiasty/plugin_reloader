PLUGINNAME = $(shell basename $(PWD))
VERSION = $(shell sed -n 's/version=//p' metadata.txt)
ZIPFILE = $(HOME)/$(PLUGINNAME).$(VERSION).zip
.PHONY: help pylint pep8 zip lupdate

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  pep8        check Python code with pep8"
	@echo "  pylint      check Python code with pylint"
	@echo "  flake       check Python code with flake8"
	@echo "  zip         build zip package"
	@echo "  lupdate     update translation files"


pep8:
	@pep8 --config=pep8 *.py


pylint:
	@pylint --disable=C0103,C0415,E0401,R0903,W0201 *.py


flake:
	@flake8 *py


zip:
	rm -f ${ZIPFILE}
	cd ..; zip -9r $(ZIPFILE) $(PLUGINNAME) -x "*.git/*" "*.gitignore" "*pyc" "*__pycache__/*" "*doc/*"
	@echo "Successfully zipped to" $(ZIPFILE)

lupdate:
	@pylupdate6 . \
	-ts i18n/plugin_reloader_pl.ts \
	-ts i18n/plugin_reloader_de.ts \
	-ts i18n/plugin_reloader_fr.ts \
	-ts i18n/plugin_reloader_it.ts \
	-ts i18n/plugin_reloader_ja.ts \
	-ts i18n/plugin_reloader_es.ts
