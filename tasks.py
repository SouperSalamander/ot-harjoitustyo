from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/number_theory.py", pty = True)

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(test)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("poetry add pylint --group dev pylint src", pty=True)