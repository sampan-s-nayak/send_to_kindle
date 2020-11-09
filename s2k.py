#! /usr/bin/env python3

import os
import subprocess
import argparse
import getpass
from termcolor import colored 


# config
OUTPUT_FORMAT = '.mobi'
FORMATS_TO_IGNORE = ['mobi','azw3']
PROCESSED_FILES_PATH = os.path.join('/home',getpass.getuser(),'Processed_Ebooks')
KINDLE_PATH = os.path.join('/','media',getpass.getuser(),'Kindle')
EBOOK_FILE_FORMATS = ['pdf','mobi','azw3','ePub','.txt','htm']

# argument parser
parser = argparse.ArgumentParser(description='send ebooks to kindle (files are converted if necessary)')
parser.add_argument("-d", "--dir", help="accepts the path to the directory containing the ebook files", action="store_true")
parser.add_argument("-f", "--file", help="accepts the path to the ebook file", action="store_true")
parser.add_argument("path",help="input path",default='.')
args = parser.parse_args()

def generate_output_file_name(file_name):
    output_file_name = ''
    split_file_name = file_name.split('.')
    for i in range(len(split_file_name)-1):
        output_file_name += split_file_name[i]
    output_file_name += OUTPUT_FORMAT
    return output_file_name

def get_file_extension(file_name):
    return file_name.split('.')[-1]

def is_kindle_mounted():
    """
        checks whether kindle is mounted(returns true). if kindle is not connected, returns false.
    """
    if(os.path.exists(KINDLE_PATH)):
        return True
    else:
        return False

def perform_initial_check(path):
    if(not os.path.exists(path)):
        print(path)
        print(colored("specified path does not exist","red"))
        exit(1)
    if(not is_kindle_mounted()):
        print(colored("Kindle not mounted","red"))
        exit(1)
    if(not os.path.exists(PROCESSED_FILES_PATH)):
        os.mkdir(PROCESSED_FILES_PATH) 

    return True

def convert_file(file_path):
    f = file_path.split('/')[-1]
    final_file_name = generate_output_file_name(f)
    extension = get_file_extension(f)
    if(extension not in EBOOK_FILE_FORMATS):
        print(colored(f"{file_name} is not a valid ebook","yellow"))
        print(colored(f"skippiing {file_name}..... ","yellow"))
        return
    if (extension not in FORMATS_TO_IGNORE):
        print(colored(f"Converting : {f}","blue"))
        try:
            subprocess.call(["ebook-convert",file_path,os.path.join(KINDLE_PATH,final_file_name)]) 
            s = os.rename(file_path, os.path.join(PROCESSED_FILES_PATH,f))
            print(s)
        except Exception as e:
            print(colored(e,'red'))
    else:
        os.rename(file_path, os.path.join(KINDLE_PATH,final_file_name))

def remove_dir_if_empty(dir_path):
    try: 
        os.rmdir(dir_path) 
        print(colored("Directory '% s' has been removed successfully" % dir_path,"blue")) 
    except OSError as error: 
        print(colored("directory is not empty","yellow")) 

if __name__=="__main__":
    if(args.dir and args.file):
        print(colored("cannot use both -d and -f flags together","red"))
    elif(args.dir):
        path = args.path
        perform_initial_check(path)
        raw_files = [os.path.join(path,f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        for file_path in raw_files:
            convert_file(file_path)
        remove_dir_if_empty(path)
    else:
        path = args.path
        if(not os.path.isfile()(path)):
            print(colored("enter a valid path","red"))
            exit(1)
        perform_initial_check(path)
        convert_file(path)