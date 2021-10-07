#!/usr/bin/python
# Orignial Author : Alireza Rezaei (@Ali-Xoerex)

import os
import sys
import sqlite3

def setup():
    filelist = os.listdir()
    if not "words.db" in filelist: #Database does not exist
        print("Database do not exists, Creating Database...")
        db = sqlite3.connect('words.db')
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS Words (Word TEXT NOT NULL UNIQUE)")
        db.commit()
        print("Database & Table successfully created!")
        cursor.execute("INSERT INTO Words VALUES('{}')".format("Apple")) #Adding at least one word
        db.commit()
        db.close()

def Quit():
    print("Bye")
    sys.exit(0)

def ShowDB():
    db = sqlite3.connect('words.db')
    cursor = db.cursor()
    counter = 0
    try:
        for row in cursor.execute("SELECT Word FROM WORDS"):
            print(row[0])
            counter += 1
    except sqlite3.OperationalError as err:
        print("Error Occured while accessing database:",err,end=" ")
    db.close()
    print("Total Words: {}".format(counter))    

def AddDB():
    db = sqlite3.connect('words.db')
    cursor = db.cursor()
    counter = 0
    print("Type in new words, write EOF when finished")
    while True:
        entry = input(" >>> ")
        if entry == "EOF":
            break
        cursor.execute("SELECT Word FROM WORDS WHERE Word='{}'".format(entry))
        if cursor.fetchone():
            print("Word already in database!")
            continue
        else:
            cursor.execute("INSERT INTO Words VALUES ('{}')".format(entry))
            db.commit()
            counter += 1
    print("Successfully added {} word(s)".format(counter))   
    db.close()     

def RemoveDB():
    db = sqlite3.connect('words.db')
    cursor = db.cursor()
    counter = 0
    print("Type in words you wish to remove, write EOF when finished")
    while True:
        entry = input(" >>> ")
        if entry == "EOF":
            break
        cursor.execute("SELECT Word FROM WORDS WHERE Word='{}'".format(entry))
        if not cursor.fetchone():
            print("Word not in database!")
            continue
        else:
            cursor.execute("DELETE FROM Words WHERE Word='{}'".format(entry))
            db.commit()
            counter += 1
    print("Successfully removed {} word(s)".format(counter))   
    db.close()    

def Help():
    print("""
        exit : Exits the program
        show : Shows all words in database
        add : Add new words to database
        remove : Delete unwanted words from database
        help : Minimal Manpage of all commands
    """)    

cmd_to_func = {
    "exit" : Quit,
    "show" : ShowDB,
    "add" : AddDB,
    "remove" : RemoveDB,
    "help": Help
}

def main():
    setup()
    while True:
        command = input("Hangman>> ")
        if command not in cmd_to_func:
            print("Invalid command! use \"help\" to see all commands")
            continue
        cmd_to_func[command]()    

if __name__ == "__main__":
    main()