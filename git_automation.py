import time
import sys
from colorama import init, Fore, Back, Style
import argparse
import os
import git
from termcolor import cprint
from main import decorator


def create_new_branch(branch_name):
    cprint('Creating a new branch', 'white', 'on_cyan')
    os.system('git checkout -b'+branch_name)
    os.system('git branch')

# This function is called when there is no requirements.txt file available in the repo


def install_package_from_imports():
    cprint('Installing packages from imports', 'cyan')
    os.system('pipreqs '+path)


def install_packages(package_manager_type):
    print("\n\n")
    cprint('Installing the packages', 'green')
    if package_manager_type == 'pip':
        with open(path+'/requirements.txt', "r") as file:
            package = file.read()
            os.system('pip install '+package)
    elif package_manager_type == 'no_requirements_file':
        install_package_from_imports()
    elif package_manager_type == 'package.json':
        os.system('npm install')


def check_package_manager_type(lang):
    cprint('\n\n Checking the package manager type', 'white', 'on_green')
    os.chdir(path)
    if lang == 'py':
        if os.path.exists(path+'/requirements.txt'):
            install_packages('pip')
        else:
            install_packages('no_requirements_file')

    elif os.path.exists(path+'/package.json'):
        install_packages('package.json')


def clone(user, repo, lang):
    print('\n*********************************************\n\n')

    cprint('Cloning the repo', 'white', 'on_blue')
    if os.path.exists(path):
        print('Repo is already created')
    else:
        repo_name = "https://github.com/"+user+"/"+repo+".git"
        git.Git('').clone(repo_name)

    if lang == 'py':
        initialize_venv()


def initialize_venv():
    cprint('Creating a virtual environment', 'blue')
    os.chdir(path)
    os.system('py -3 -m venv venv')
    os.system('venv\Scripts\activate')


def saveandpush(message):
    # getting the name of the folder in the current path
    repo_name = list(filter(os.path.isdir, os.listdir(os.curdir)))[0]
    path = os.getcwd() + '/'+repo_name
    os.chdir(path)
    print('\n*********************************************\n\n')
    cprint("Pulling the changes", 'white', 'on_blue')
    # os.system('git pull')

    cprint("Commiting the changes", 'white', 'on_green')
    os.system('git add *')
    git.Git('').commit('-m',
                       message, author='annujolly17@gmail.com')

    cprint("Pushing the changes", 'white', 'on_magenta')
    os.system('git push --set-upstream origin feature_branch1')
    print('\n\n *********************************************\n')


path = os.getcwd()+'/'+"azuredeployment_ "


def animation(counter, length):
    stage = counter % (length * 2 + 2)
    if stage < length + 1:
        left_spaces = stage
    else:
        left_spaces = length * 2 - 1 - stage
    return '*' + ' ' * left_spaces + '' + ' ' * (length - left_spaces) + '*'


@decorator
def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('--cmd', type=str, required=True)
    # parser.add_argument('--repo')
    # parser.add_argument('--lang')
    # parser.add_argument('--branch')
    # parser.add_argument('--msg')
    # args = parser.parse_args()
    print(Back.BLUE + 'GIT AUTOMATION')
    print(Style.RESET_ALL)
    print('*********************************************\n\n')

    user = os.popen('git config user.name').read().replace("\n", "")
    # cmd_type = args.cmd
    path = ''
    cmd_type = input(Fore.GREEN + "Enter command: ")

    if cmd_type == 'clone':
        """
        - git clone <>
        - cd repo
        - if lang=py, then create venv
        - if lang=py
            . if requirements.txt: install packages
            . else from import stmt, create requirements.txt file and then import
        - if lang=js, import from package.json file
        - if --branch, do git checkout to the branch
        """
        repo = input(Fore.CYAN + "Enter repo name: ")
        lang = input(Fore.BLUE + "Enter language: ")
        branch = input(Fore.MAGENTA + "Enter branch: ")
        for i in range(10):
            sys.stdout.write('\b\b\b')
            sys.stdout.write(animation(i, 6))
            sys.stdout.flush()
            time.sleep(0.2)
        clone(user, repo, lang)
        check_package_manager_type(check_package_manager_type)
        if branch:
            create_new_branch(branch)

    elif cmd_type == 'save':
        """
        git add *
        git commit -m
        git pull
        git push
        """
        msg = input(Fore.CYAN + "Enter commit msg: ")
        saveandpush(msg)


main()
