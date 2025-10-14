.PHONY: build

test:
	pixi run test 

package:
	pixi run mojo package  src/{{cookiecutter.project_slug}}/ -o {{cookiecutter.project_slug}}.mojopkg

upload:
	export PREFIX_API_KEY={$PREFIX_API_KEY} & bash scripts/publish.sh

build:
	rattler-build build -r src -c https://prefix.dev/mojo-force -c https://repo.prefix.dev/modular-community -c https://conda.modular.com/max-nightly -c conda-forge --skip-existing=all

doc:
	mkdocs serve

shell:
	pixi shell

clean:
	rm -rf output/
