.PHONY: all
all: develop

PIP := python -m pip --disable-pip-version-check


develop:
	@echo "--> first task, this is a test"

build-site: build-index
	@echo "Building static site..."
	marimo export html-wasm gamblers_ruin.py -o docs/gamblers_ruin/index.html

build-index: docs/index.html style.css
	@echo "Building index page..."

style.css:
	# npx @tailwindcss/cli -i ./input.css -o ./docs/style.css --config tailwind.config.js
	npx @tailwindcss/cli -i ./input.css -o ./docs/style.css

docs/index.html: index.md index.template.html
	@echo "Converting $< to HTML..."
	@pandoc index.md -o docs/index.html  --template=index.template.html --standalone