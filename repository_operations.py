"""This module will clone, zip repository & delete local files"""
import logging
import shutil
import os
from shutil import Error as shutilError
from git import Repo, GitError
from dotenv import load_dotenv

load_dotenv()

def clone_repository():
    '''
    this method will clone repo
    '''
    print("Clonning Repository.....")
    try:
        Repo.clone_from(os.getenv('REPOSITORY_GITHUB_URL'),os.getenv('SOURCE_DIRECTORY'))
        print("Respository Cloned Succesfull")
    except GitError as error:
        logging.error(error)
        return False
    return True

def zip_file():
    '''
    this method will zip the cloned repository
    '''
    print("Zipping Clone Repository")
    try:
        shutil.make_archive(os.getenv('FILE_NAME'),os.getenv('FORMATE'),os.getenv('ROOT_DIRECTORY'))
        
        print("Repository Zipped")
    except shutilError as error:
        logging.error(error)
        return False
    return True

def delete_local_files():
    '''
    this method will delete the old cloned directory which is cloned now
    '''
    print("Deleting Local Files")
    try:
        shutil.rmtree(os.getenv('FILE_NAME'))
        os.remove(os.getenv('UPLOAD_FILE_NAME'))
        print("Local Files Deleted")
    except shutilError as error:
        logging.error(error)
        return False
    return True
