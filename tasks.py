from invoke import task
import os
from shutil import copyfile

@task(name = "dotfiles")
def dotfiles(dot_context):
    homedir = os.getenv("HOME")

    print("Installing dotfiles in: " + homedir)

    print("fish_variables")
    copyfile('fish/fish_variables', homedir + '/.config/fish/fish_variables')

    print(".vimrc")
    copyfile('vim/.vimrc', homedir + '/.vimrc')

    print(".gitconfig")
    copyfile('gitstuff/.gitconfig', homedir + '/.gitconfig')
