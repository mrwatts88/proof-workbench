.PHONY: help validate status index test

PYTHON ?= python3

help:
	@$(PYTHON) scripts/proofctl.py --help

validate:
	@$(PYTHON) scripts/proofctl.py validate

status:
	@$(PYTHON) scripts/proofctl.py status

index:
	@$(PYTHON) scripts/proofctl.py index

test:
	@$(PYTHON) -m unittest discover -s tests -v

