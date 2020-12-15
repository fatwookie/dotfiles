from invoke import task
import os
from shutil import copyfile
from pathlib import Path

@task(name = "dotfiles")
def dotfiles(dot_context):
    homedir = os.getenv("HOME")

    print("Installing dotfiles in: " + homedir)

    print("fish_variables")
    Path(homedir + "/.config/fish").mkdir(parents=True, exist_ok=True)
    copyfile('fish/fish_variables', homedir + '/.config/fish/fish_variables')

    print(".vimrc")
    copyfile('vim/.vimrc', homedir + '/.vimrc')

    print(".gitconfig")
    copyfile('gitstuff/.gitconfig', homedir + '/.gitconfig')
