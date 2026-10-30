# Contributing

Contributions are welcome, for instance new ASCII art objects or options for the ASCII file format.

## Reporting issues

Open an issue on [GitHub](https://github.com/dhondta/python-asciistuff/issues) and include:

- the ASCIIstuff version and the Python version;
- the exact code or command and its output.

## Security

Please do **not** report vulnerabilities in public issues. See the [security policy](https://github.com/dhondta/python-asciistuff/blob/main/SECURITY.md): report them privately through the repository's *Security* tab (*Report a vulnerability*).

Dependencies are monitored by Dependabot and audited with [pip-audit](https://github.com/pypa/pip-audit) by the `security` workflow (`.github/workflows/security.yml`), on every push and pull request to `main` and weekly.

## Development setup

```console
$ git clone https://github.com/dhondta/python-asciistuff
$ cd python-asciistuff
$ pip install -e .
$ pip install pytest pytest-cov
$ pytest --cov=asciistuff
```

pytest and coverage are configured in `pyproject.toml`. CI (`.github/workflows/python-package.yml`) runs the tests on Python 3.10 to 3.13 and publishes the coverage badge to the `coverage-badge` branch.

## Releasing

The version is stored in `src/asciistuff/VERSION.txt`. On every push to `main`, CI checks whether that version is already on PyPI. If not, it builds the package and publishes it.

## Building this documentation

```console
$ pip install -r docs/requirements.txt
$ mkdocs serve -f docs/mkdocs.yml          # live preview at http://127.0.0.1:8000
$ mkdocs build --strict -f docs/mkdocs.yml # what Read the Docs runs
```

Read the Docs builds the site from `.readthedocs.yaml` at the root of the repository.
