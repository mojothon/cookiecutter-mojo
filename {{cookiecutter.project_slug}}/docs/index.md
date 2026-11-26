# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}

## requirements

- Mojo >=1.2.0 (installed by `pixi`)

## package build

```bash
pixi run mojo precompile src/{{cookiecutter.project_slug}}/ -o {{cookiecutter.project_slug}}.mojoc
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

