import nox

locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.10.4"])
def tests(session):
    session.run("poetry", "install", external=True)
    session.run("pytest", "--cov")


# noxfile.py
@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=["3.8"])
def lint(session):
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)
