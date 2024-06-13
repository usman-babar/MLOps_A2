import requests
from bs4 import BeautifulSoup
import csv
import os
import subprocess


## Task 03 - DVC Implementation
def setup_dvc():
    os.system('git init')
    os.system('dvc init')
    os.system('dvc remote add -d gdrive gdrive://16LZL8gIRHmE-CBqebr5qZ7ACAAyqdhJO')

def add_data_to_dvc():
    os.system('dvc add C:/Users/Usman Babar/Desktop/Mlops_Assignment02/data/preprocessed_data.csv')
    os.system('git add C:/Users/Usman Babar/Desktop/Mlops_Assignment02/data/preprocessed_data.csv.dvc C:/Users/Usman Babar/Desktop/Mlops_Assignment02/data/.gitignore')
    os.system('git commit -m "First time commit"')
    os.system('dvc commit')

def push_to_remote():
    os.system('dvc push')

def integrate_with_git():
    os.system('git add .dvc/')
    os.system('git commit -m "Add DVC metafiles"')
    subprocess.run(['git', 'remote', 'add', 'origin', 'https://github.com/usman-babar/MLOps_A2.git'])
    subprocess.run(['git', 'branch', '-M', 'main'])
    subprocess.run(['git', 'push', '-u', 'origin', 'main'])
# Set up DVC
setup_dvc()

# Add data and metafiles to DVC
add_data_to_dvc()

# Push data and metafiles to remote repository
push_to_remote()

# Integrate with Git
integrate_with_git()