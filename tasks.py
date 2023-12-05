from invoke import task

@task
def start(ctx):
    ctx.run("uipython3 src/number_theory_ui.py", pty = True)

@task
def test(ctx):
    ctx.run("coverage run --branch -m pytest src", pty=True)

@task(test)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)

@task
def lint(ctx):
    ctx.run("pylint src", pty=True)