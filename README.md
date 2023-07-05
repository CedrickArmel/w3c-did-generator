# W3C DID Generator
This app generate ED25519 keys.
[![version](https://img.shields.io/github/v/release/okp4/template-python?style=for-the-badge&logo=github)](https://github.com/okp4/template-python/releases)
[![lint](https://img.shields.io/github/actions/workflow/status/okp4/template-python/lint.yml?label=lint&style=for-the-badge&logo=github)](https://github.com/okp4/template-python/actions/workflows/lint.yml)
[![build](https://img.shields.io/github/actions/workflow/status/okp4/template-python/build.yml?label=build&style=for-the-badge&logo=github)](https://github.com/okp4/template-python/actions/workflows/build.yml)
[![test](https://img.shields.io/github/actions/workflow/status/okp4/template-python/test.yml?label=test&style=for-the-badge&logo=github)](https://github.com/okp4/template-python/actions/workflows/test.yml)
[![codecov](https://img.shields.io/codecov/c/github/okp4/template-python?style=for-the-badge&token=G5OBC2RQKX&logo=codecov)](https://codecov.io/gh/okp4/template-python)
[![conventional commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-yellow.svg?style=for-the-badge&logo=conventionalcommits)](https://conventionalcommits.org)
[![contributor covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg?style=for-the-badge)](https://github.com/okp4/.github/blob/main/CODE_OF_CONDUCT.md)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg?style=for-the-badge)](https://opensource.org/licenses/BSD-3-Clause)


## System requirements

### Python

The repository targets python `3.9` and higher.

### Poetry

The repository uses [Poetry](https://python-poetry.org) as python packaging and dependency management. Be sure to have it properly installed before.

```sh
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
```

### Docker

You can follow the link below on how to install and configure **Docker** on your local machine:

- [Docker Install Documentation](https://docs.docker.com/install/)

## What's included

This template provides the following:

- [poetry](https://python-poetry.org) for dependency management.
- [flake8](https://flake8.pycqa.org) for linting python code.
- [mypy](http://mypy-lang.org/) for static type checks.
- [pytest](https://docs.pytest.org) for unit testing.
- [click](https://palletsprojects.com/p/click/) to easily setup your project commands

The project is also configured to enforce code quality by declaring some CI workflows:

- conventional commits
- lint
- unit test
- semantic release

## Everyday activity

### Build

Project is built by [poetry](https://python-poetry.org).

```sh
poetry install
```

### Usage

```sh
poetry run didgen --help
```

Will give something like

```console
Usage: didgen [OPTIONS] COMMAND [ARGS]...

  W3C Decentralized Identifier Generator

Options:
  --help  Show this message and exit.

Commands:
  generate  Generate the W3C Decentralized Identifier
  version   Print the application version information
```

Example:

```sh
poetry run didgen generate -n2
```

### Lint

> ⚠️ Be sure to write code compliant with linters or else you'll be rejected by the CI.

**Code linting** is performed by [flake8](https://flake8.pycqa.org).

```sh
poetry run flake8 --count --show-source --statistics
```

**Static type check** is performed by [mypy](http://mypy-lang.org/).

```sh
poetry run mypy .
```

To improve code quality, we use other linters in our workflows, if you don't want to be rejected by the CI,
please check these additional linters.

**Markdown linting** is performed by [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli).

```sh
markdownlint "**/*.md"
```

**Docker linting** is performed [hadolint](https://github.com/hadolint/hadolint).

```sh
hadolint Dockerfile
```

### Unit Test

> ⚠️ Be sure to write tests that succeed or else you'll be rejected by the CI.

Unit tests are performed by the [pytest](https://docs.pytest.org) testing framework.

```sh
poetry run pytest -v
```

### Build & run docker image (locally)

Build a local docker image using the following command line:

```sh
docker build -t didgen .
```

Once built, you can run the container locally with the following command line:

```sh
docker run -ti --rm didgen
```
