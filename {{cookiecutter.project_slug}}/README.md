# {{cookiecutter.project_name}}

{{cookiecutter.project_short_description}}


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

## add new package

```bash
pixi add {{cookiecutter.project_name}} --platform linux-64
```

## publish package

```bash
make upload
```

## version

version {{cookiecutter.version}}

