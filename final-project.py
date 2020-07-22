#####
# Author: Rachel Lee
# Assignment: Final Project
# Date: 7/23/2020
#####

# import libraries 
import os
from os import listdir
import subprocess
import shutil
import easygui
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import simpledialog
from distutils.dir_util import copy_tree
from fnmatch import fnmatch
import psutil
import platform
from datetime import datetime
import time
from columnar import columnar




class Files:
    
    def _init__(self, files):
        self.files = files # files is list input
        # private variables (only accessible by instance of class)
        self.__src_path = None
        self.__dest_path= None

    # Get File's source path attribute
    def __get_src_path(self):
        return self.__src_path 
    
    # Set File's source path attribute
    def __set_src_path(self, src):
        self.__src_path = src

    # Get File's destination path attribute
    def __get_dest_path(self):
        return self.__dest_path
    
    # Set File's destination path attribute
    def __set_dest_path(self, dest):
        self.__dest_path = dest

    src_path = property(fget=__get_src_path, fset=__set_src_path)
    dest_path = property(fget=__get_dest_path, fset=__set_dest_path)

    # Copy file(s)
    def copy(self):
        return shutil.copy2(self.__src_path, self.__dest_path)

    # Move file(s)
    def move(self):
        return shutil.move(self.__src_path, self.__dest_path)
    
    # Rename file(s)
    def rename(self, name):
        return os.rename(self.__src_path, name)

    # Delete file(s)
    def delete(self):
        return os.remove(self.__src_path)



class Folders:
    
    def _init__(self):
        # private variables (only accessible by instance of class)
        self.__src_path = None
        self.__dest_path= None

    # Get Folder's source path attribute
    def __get_src_path(self):
        return self.__src_path
    
    # Set Folder's source path attribute    
    def __set_src_path(self, src):
        self.__src_path = src

    # Get Folder's destination path attribute
    def __get_dest_path(self):
        return self.__dest_path
    
    # Set Folder's destination path attribute
    def __set_dest_path(self, dest):
        self.__dest_path = dest

    src_path = property(fget=__get_src_path, fset=__set_src_path)
    dest_path = property(fget=__get_dest_path, fset=__set_dest_path)

    # Copy folder(s)
    def copy(self):
        return copy_tree(self.__src_path, self.__dest_path)

    # Move folder(s)
    def move(self):
        return shutil.move(self.__src_path, self.__dest_path)
    
    # Rename folder(S)
    def rename(self):
        return os.rename(self.__src_path, self.__dest_path)

    # Delete folder(s)
    def delete(self):
        return shutil.rmtree(self.__src_path)


class System_Tasks:

    def __init__(self):
        # private variables (only accessible by instance of class)
        self.__src_path = None
        self.__dest_path= None
        # public variables
        self.sys_info = None

    # Get Folder's source path attribute
    def __get_src_path(self):
        return self.__src_path
    
    # Set Folder's source path attribute    
    def __set_src_path(self, src):
        self.__src_path = src

    # Get Folder's destination path attribute
    def __get_dest_path(self):
        return self.__dest_path
    
    # Set Folder's destination path attribute
    def __set_dest_path(self, dest):
        self.__dest_path = dest

    src_path = property(fget=__get_src_path, fset=__set_src_path)
    dest_path = property(fget=__get_dest_path, fset=__set_dest_path)

    # Method to retrieve information of local system
    def system_info(self):   
        # returns dict of values
        info = platform.uname()
        self.sys_info = {
            'System OS': info.system,
            'System Name': info.node,
            'Release Version': info.version,
            'Machine': info.machine,
            'Processor': info.processor
        }
        return self.sys_info

    # Mthod to find files that contains user desired extension (i.e. .zip, .pdf. .png, .jpg, .txt, etc)
    def find_files_ext(self):
        dir_list = os.listdir(self.__src_path)
        file_list = []
        for item in dir_list:
            if item.endswith(self.__dest_path):
                file_list.append(item)
        # print(f'Files with ext {file_type}:\n{file_list}')
        return file_list

    # Method to find files that contains entered 'string'
    def find_files_contains(self):  
        dir_list = os.listdir(self.__src_path)
        file_list = []
        for val in dir_list:
            if fnmatch(val, self.__dest_path):
                file_list.append(val)
        return file_list

    # Method to return dict of files and subdirectories and their creation_date, modified_date, size
    def folder_info(self):
        dir_items = listdir(self.__src_path)
        items = {}
        for i in dir_items:
            tmp = os.stat(f'{self.__src_path}/{i}')
            items[i] = {
                'Created': time.ctime(tmp.st_ctime),
                'Modified': time.ctime(tmp.st_atime),
                'Size (bytes)': tmp.st_size
                }
        return items

    # Method to return list of files and subdirectories
    def folder_contents(self):
        return listdir(self.__src_path)

    # Method to return size of file
    def file_size(self):
        return os.stat(self.__src_path).st_size


# Function to convert list of files to formatted column view
def format_file_list(file_items):
    headers = ['File Name']

    final_list = []
    for val in file_items:
        tmp = []
        tmp.append(val)
        final_list.append(tmp)
    table = columnar(final_list, headers, no_borders=True)
    print(table)

# Function to display in formatted column view of folder_info() method in Folders class
def display_folder_info(folder_items):
    headers = ['Item', 'Created', 'Modified', 'Size']
    
    convert_list = []
    for key, val in folder_items.items():
        tmp = []
        tmp.append(key)
        print(f'Key: {key}, Val: {val}')
        for k, v in val.items():
            print(f'Key: {k}, Val: {v}')
            tmp.append(v)
        print(f'tmp: {tmp}')
        convert_list.append(tmp)
    print(f'convert_list: {convert_list}')
    table = columnar(convert_list, headers, no_borders=True)
    print(table)


# Function to call Main Menu view
def main_menu():
    print("=========================================================")
    print("==========    Python System Automation Tool    ==========")
    print("==========              Main Menu              ==========")
    print("=========================================================")
    print("")
    print("Enter 1 - to Copy/Move/Delete/Rename File")
    print("Enter 2 - to Copy/Move/Delete/Rename Folder")
    print("Enter 3 - to Get System Information")
    print("")
    user_input = input("Enter option:  ")
    return int(user_input)

# Function to call File Menu view
def file_menu():
    print("=========================================================")
    print("==========              File Menu              ==========")
    print("=========================================================")
    print("")
    print("Enter 1 - to Copy File")
    print("Enter 2 - to Mopy File")
    print("Enter 3 - to Delete File")
    print("Enter 4 - to Rename File")
    print("")
    user_input = input("Enter option:  ")
    return int(user_input)

# Function to call Folder Menu view
def folder_menu():
    print("=========================================================")
    print("==========             Folder Menu             ==========")
    print("=========================================================")
    print("")
    print("Enter 1 - to Copy Folder")
    print("Enter 2 - to Mopy Folder")
    print("Enter 3 - to Delete Folder")
    print("Enter 4 - to Rename Folder")
    print("")
    user_input = input("Enter option:  ")
    return int(user_input)

# Function to call System Menu view
def system_menu():
    print("=========================================================")
    print("==========          System Tasks Menu          ==========")
    print("=========================================================")
    print("")
    print("Enter 1 - to Get System Information")
    print("Enter 2 - to Get a List of all contents in a Folder")
    print("Enter 3 - to Get a List of [Create Date, Modified Date, Size] of all contents in a Folder")
    print("Enter 4 - to Get the Size of a File")
    print("Enter 5 - to Search for all Files in a Folder with extension of choice")
    print("Enter 6 - to Search for all Files in a Folder containing 'string' of choice")
    print("")
    user_input = input("Enter option:  ")
    return int(user_input)
    

# Run Python System Automation Tool
def main():
    
    ### START of MAIN ###

    file = Files()
    '''COPY FILE'''
    # print("Choose file to copy.")
    # time.sleep(2)
    # file.src_path = easygui.fileopenbox()
    # print("Choose destination path. ")
    # time.sleep(2)
    # file.dest_path = filedialog.askdirectory()

    # file.copy()
    '''DELETE FILE'''
    # print("Choose file to delete.")
    # time.sleep(2)
    # file.src_path = easygui.fileopenbox()
    # file.delete()

    '''RENAME FILE'''
    # print("Choose file to rename.")
    # time.sleep(2)
    # file.src_path = easygui.fileopenbox()
    # name = input("Enter new name: ")
    # time.sleep(2)
    # dest  = filedialog.askdirectory()
    # file.dest_path = os.path.join(dest, name)
    # print(file.dest_path)
    # file.rename(file.dest_path)

    '''MOVE FILE'''
    # print("Choose file to move.")
    # time.sleep(2)
    # file.src_path = easygui.fileopenbox()
    # print("Choose directory to move file to.")
    # time.sleep(2)
    # file.dest_path  = filedialog.askdirectory()
    # file.move()
    

    folder = Folders()
    '''COPY FOLDER'''
    # print("Choose folder to move.")
    # time.sleep(2)
    # folder.src_path = filedialog.askdirectory()
    # print("Choose destination directory.")
    # time.sleep(2)
    # folder.dest_path  = filedialog.askdirectory()
    # folder.copy()

    '''DELETE FOLDER'''
    # print("Choose folder to move.")
    # time.sleep(2)
    # folder.src_path = filedialog.askdirectory()
    # print("Choose destination directory.")
    # time.sleep(2)
    # # folder.dest_path  = filedialog.askdirectory()
    # folder.delete()

    '''MOVE FOLDER'''
    # print("Choose folder to move.")
    # time.sleep(2)
    # folder.src_path = filedialog.askdirectory()
    # print("Choose destination directory.")
    # time.sleep(2)
    # folder.dest_path  = filedialog.askdirectory()
    # folder.move()

    '''RENAME FOLDER'''
    # print("Choose folder to move.")
    # time.sleep(2)
    # folder.src_path = filedialog.askdirectory()
    # print("Choose destination directory.")
    # time.sleep(2)
    # dest  = simpledialog.askstring(title="User Input", prompt="Enter new folder name:")
    # temp = folder.src_path.split('/')
    # temp = temp[:-1]
    # temp.append(dest)
    # folder.dest_path = '/'.join(temp) 
    # print(folder.dest_path)
    # folder.rename()


    # print(folder.src_path)
    # print(file.dest_path)


    sys = System_Tasks()
    ''' SYSTEM INFO '''
    sys_info = sys.system_info()
    print(sys_info['System Name'])

    ''' Folder Info '''
    # print("Choose directory.")
    # time.sleep(2)
    # sys.src_path = filedialog.askdirectory()
    # dir_info = sys.folder_info()
    # dir_contents = sys.folder_contents()
    # display_folder_info(dir_info)

    ''' File Size '''
    # print("Choose directory.")
    # time.sleep(2)
    # sys.src_path = easygui.fileopenbox()
    # print(sys.file_size())

    ''' Find Files w/ Extension '''
    # print("Choose directory.")
    # time.sleep(2)
    # sys.src_path = filedialog.askdirectory()
    # sys.dest_path  = simpledialog.askstring(title="User Input", prompt="Enter file extension type to search (e.g. .txt, .zip, .png, .jpg, etc): ")
    # files_list = sys.find_files_ext()
    # format_file_list(files_list)

    ''' Find Files containing String '''
    # print("Choose directory.")
    # time.sleep(2)
    # sys.src_path = filedialog.askdirectory()
    # user_input  = simpledialog.askstring(title="User Input", prompt="Enter string matchcase for files: ")
    # sys.dest_path = f'*{user_input}*'
    # files_list = sys.find_files_contains()
    # format_file_list(files_list)  
    
    
    
main()