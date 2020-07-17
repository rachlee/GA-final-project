#####
# Author: Rachel Lee
# Assignment: Final Project
# Date: 7/23/2020
#####

# import libraries 
import os
import subprocess
import shutil

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
        self.__src_path = str(src) + '\\'

    # Get File's destination path attribute
    def __get_dest_path(self):
        return self.__dest_path
    
    # Set File's destination path attribute
    def __set_dest_path(self, dest):
        self.__dest_path = str(dest) + '\\'

    src_path = property(fget=__get_src_path, fset=__set_src_path)
    dest_path = property(fget=__get_dest_path, fset=__set_dest_path)

    # Copy file(s)
    def copy(self):
        pass

    # Move file(s)
    def move(self):
        pass
    
    # Remove file(s)
    def remove(self):
        pass

    # Delete file(s)
    def delete(self):
        pass



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
        self.__src_path = str(src) + '\\'

    # Get Folder's destination path attribute
    def __get_dest_path(self):
        return self.__dest_path
    
    # Set Folder's destination path attribute
    def __set_dest_path(self, dest):
        self.__dest_path = str(dest) + '\\'

    src_path = property(fget=__get_src_path, fset=__set_src_path)
    dest_path = property(fget=__get_dest_path, fset=__set_dest_path)

    # Copy folder(s)
    def copy(self):
        pass

    # Move folder(s)
    def move(self):
        pass
    
    # Remove folder(S)
    def remove(self):
        pass

    # Delete folder(s)
    def delete(self):
        pass

class System_Tasks:
    pass



# Run Python System Automation Tool
def main():

    test_file = Files()
    test_file.src_path = r"C:\Users\file" #raw string; can also use "C:\\Users"
    print(test_file.src_path)

    test_folder = Folders()
    test_folder.src_path = r"C:\Users\folder" #raw string; can also use "C:\\Users"
    print(test_folder.src_path)
    
main()