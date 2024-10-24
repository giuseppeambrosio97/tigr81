import pathlib as pl

import tigr81.commands.core.gitw as gitw


def test_is_cookiecutter_template_given_non_cookiecutter_template():
    repo_url = "https://github.com/primefaces/primereact-examples"
    checkout = "main"
    directory = pl.Path(".")

    assert not gitw.is_cookiecutter_template(
        repo_url=repo_url,
        checkout=checkout,
        directory=directory,
    )


def test_is_cookiecutter_template_given_a_cookiecutter_template():
    repo_url = "https://github.com/drivendataorg/cookiecutter-data-science"
    checkout = "master"
    directory = pl.Path(".")

    assert gitw.is_cookiecutter_template(
        repo_url=repo_url,
        checkout=checkout,
        directory=directory,
    )
