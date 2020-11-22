from invoke import task

@task(name = "build")
def build(c, where, clean=False):
    pass

@task
def clean(what):
    pass