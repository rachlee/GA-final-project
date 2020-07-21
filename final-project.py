#####
# Author: Rachel Lee
# Assignment: Final Project
# Date: 7/23/2020
#####

# import libraries 
import os
import subprocess
import shutil
import easygui
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from tkinter import simpledialog



from distutils.dir_util import copy_tree

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
        shutil.copy2(self.__src_path, self.__dest_path)

    # Move file(s)
    def move(self):
        shutil.move(self.__src_path, self.__dest_path)
    
    # Rename file(s)
    def rename(self, name):
        os.rename(self.__src_path, name)

    # Delete file(s)
    def delete(self):
        os.remove(self.__src_path)



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
        copy_tree(self.__src_path, self.__dest_path)

    # Move folder(s)
    def move(self):
        shutil.move(self.__src_path, self.__dest_path)
    
    # Rename folder(S)
    def rename(self):
        pass

    # Delete folder(s)
    def delete(self):
        shutil.rmtree(self.__src_path)

class System_Tasks:

    def __init__(self):
        pass 
    
    def system_info(self):
        pass

    def find_files_ext(self):
        # find files that contains extension (i.e. .zip, .pdf. .png, .txt etc)
        pass

    def find_files_contains(self):
        # find files that contain 'string'
        pass

    def folder_info(self):
        # get list of files in folder and folder sizae
        pass

    def file_size(self):
        pass



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

    '''COPY FILE'''
    file = Files()
    # print("Choose file to copy.")
    # file.src_path = easygui.fileopenbox()
    # print("Choose destination path. ")
    # file.dest_path = filedialog.askdirectory()

    # file.copy()
    '''DELETE FILE'''
    # print("Choose file to delete.")
    # file.src_path = easygui.fileopenbox()
    # file.delete()

    '''RENAME FILE'''
    # print("Choose file to rename.")
    # file.src_path = easygui.fileopenbox()
    # name = input("Enter new name: ")
    # dest  = filedialog.askdirectory()
    # file.dest_path = os.path.join(dest, name)
    # print(file.dest_path)
    # file.rename(file.dest_path)

    '''MOVE FILE'''
    # print("Choose file to move.")
    # file.src_path = easygui.fileopenbox()
    # print("Choose directory to move file to.")
    # file.dest_path  = filedialog.askdirectory()
    # file.move()
    

    folder = Folders()
    '''COPY FOLDER'''
    # print("Choose folder to move.")
    # folder.src_path = filedialog.askdirectory()
    # print("Choose destination directory.")
    # folder.dest_path  = filedialog.askdirectory()
    # folder.copy()

    '''DELETE FOLDER'''
    # print("Choose folder to move.")
    # folder.src_path = filedialog.askdirectory()
    # print("Choose destination directory.")
    # # folder.dest_path  = filedialog.askdirectory()
    # folder.delete()

    '''MOVE FOLDER'''
    # print("Choose folder to move.")
    # folder.src_path = filedialog.askdirectory()
    # print("Choose destination directory.")
    # folder.dest_path  = filedialog.askdirectory()
    # folder.move()

    '''RENAME FOLDER'''
    # print("Choose folder to move.")
    # folder.src_path = filedialog.askdirectory()
    # print("Choose destination directory.")
    # dest  = simpledialog.askstring(title="User Input", prompt="Enter new folder name:")
    # temp = folder.src_path.split('/')
    # temp = temp[:-1]
    # temp.append(dest)
    # folder.dest_path = '/'.join(temp) 
    # print(folder.dest_path)
    # os.rename(folder.src_path, folder.dest_path)




    print(folder.src_path)
    # print(file.dest_path)
    
main()