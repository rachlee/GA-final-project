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
import psutil
import platform
from datetime import datetime
import time




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

    def find_files_ext(self):
        # find files that contains extension (i.e. .zip, .pdf. .png, .txt etc)
        pass

    def find_files_contains(self):
        # find files that contain 'string'
        pass

    # Method to return list of files and subdirectories and dict of file/folder creation_date, modified_date, size
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

        return dir_items, items

    # Method to return size of file
    def file_size(self):
        return os.stat(self.__src_path).st_size

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

def system_menu():
    print("=========================================================")
    print("==========          System Tasks Menu          ==========")
    print("=========================================================")
    print("")
    

# Run Python System Automation Tool
def main():

    # test_file = Files()
    # test_file.src_path = r"C:\Users\file" #raw string; can also use "C:\\Users"
    # print(test_file.src_path)

    # test_folder = Folders()
    # test_folder.src_path = r"C:\Users\folder" #raw string; can also use "C:\\Users"
    # print(test_folder.src_path)

    # subprocess.Popen(r'explorer /select,"C:\\Users\\rachl\\Documents\\TEST"')
    
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
    # os.rename(folder.src_path, folder.dest_path)



    # print(folder.src_path)
    # print(file.dest_path)


    sys = System_Tasks()
    ''' SYSTEM INFO '''
    sys_info = sys.system_info()
    print(sys_info['System Name'])

    ''' Folder Info '''
    print("Choose directory.")
    time.sleep(2)
    sys.src_path = filedialog.askdirectory()
    print(sys.folder_info())

    ''' File Size '''
    print("Choose directory.")
    time.sleep(2)
    sys.src_path = easygui.fileopenbox()
    print(sys.file_size())
    
    
    
main()