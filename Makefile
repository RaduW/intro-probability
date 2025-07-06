.PHONY: all
all: develop

PIP := python -m pip --disable-pip-version-check


develop:
	@echo "--> first task, this is a test"

build-site: build-index
	@echo "Building static site..."
	marimo export html-wasm gamblers_ruin.py -o docs/gamblers_ruin/index.html

build-index: docs/index.html
	@echo "Building index page..."


%.html: %.md
	@echo "Converting $< to HTML..."
	@pandoc $< -o $@ --css=style.css --standalone