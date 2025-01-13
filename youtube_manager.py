# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 19:23:24 2025

@author: vasug
"""

import json
import pyfiglet

def load_data():
    try:
        with open('youtube_file.txt','r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('youtube_file.txt','w') as file:
        json.dump(videos,file)

def list_all_videos(videos):
    print("\n")
    print("*"*70)
    print("\n")
    print('''\033[1;33m
   _   _ _  __   __        _        _          __   ___    _            
  /_\ | | | \ \ / /__ _  _| |_ _  _| |__  ___  \ \ / (_)__| |___ ___ ___
 / _ \| | |  \ V / _ \ || |  _| || | '_ \/ -_)  \ V /| / _` / -_) _ (_-<
/_/ \_\_|_|   |_|\___/\_,_|\__|\_,_|_.__/\___|   \_/ |_\__,_\___\___/__/
                                                                        
          \033[0m''')
    for index,video in enumerate(videos,start=1):
        text=pyfiglet.figlet_format((f"{index}.  {video['name']}  ,  Duration: {video['time']}"),font="short")
        print(text)
    

def add_video(videos):
    print("\n")
    print("*"*70)
    print("\n")
    name=input("Enter video name : ")
    time=input("Enter video time : ")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)

def update_video(videos):
    print("\n")
    print("*"*70)
    print("\n")
    list_all_videos(videos)
    index=int(input("Enter the video number to update : "))
    if 1<=index <= len(videos):
        name=input("Enter the new video name : ")
        time=input("Enter the new video time : ")
        
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("Invalid index selected")

def delete_video(videos):
    print("\n")
    print("*"*70)
    print("\n")
    list_all_videos(videos)
    index=int(input("Enter the video number to be deleted : "))
    if 1<=index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")
# main is the entry point
def main():

    videos=load_data()
    
    while True:
        print("\n")
        print("*"*70)
        print("\n")
        print(
            '''\033[1;31m
  __   __        _        _           __  __                             
 \ \ / /__ _  _| |_ _  _| |__  ___  |  \/  |__ _ _ _  __ _ __ _ ___ _ _ 
  \ V / _ \ || |  _| || | '_ \/ -_) | |\/| / _` | ' \/ _` / _` / -_) '_|
   |_|\___/\_,_|\__|\_,_|_.__/\___| |_|  |_\__,_|_||_\__,_\__, \___|_|  
                                                          |___/         
            \033[0m'''
            )
        print("\n")
        print("*"*70)
        print("\n")
        print("\033[1;36m1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube videos details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        
        choice = input("\n Enter your choice : ")
        
        #print(videos)
        
        match choice:
            case '1':
                list_all_videos(videos)
                
            case '2':
                add_video(videos)
                
            case '3':
                update_video(videos)
                
            case '4':
                delete_video(videos)
                
            case '5':
                break
            #default handling
            case _:
                print("Invalid Handling")

#
if __name__ == "__main__":
    main()
    
    
            
        