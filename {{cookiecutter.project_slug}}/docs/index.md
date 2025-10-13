# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}


## package build

```bash
pixi run mojo package  src/{{cookiecutter.project_slug}}/ -o {{cookiecutter.project_slug}}.mojopkg
```
or 

```bash
make package
```

## test

```bash
pixi run test 
```

or 

```bash
make test
```

## version

version {{cookiecutter.version}}

