#!/usr/bin/python3
import sys
import fileinput
import re

# Input from user

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

inpFileName = str(sys.argv[1])

# Opening selected file

try:
    file_stream = open(inpFileName)
    pass
except:
    print("The file does not exist.")
    exit(13)
    pass
finally:
    file_stream.close()
    pass

# Updating the file

def edit_file(file_name, search_text, replace_to_text):
    # Transforming Regex
    search_text = search_text.replace("-", ".")
    search_text = search_text.replace("*", ".*")

    # Operation
    with open(file_name, "r") as file_input:
        with open("file_name.txt", "w") as output: 
            for line in file_input:
                words = line.split()
                for word in words:
                    matches = re.findall(search_text, word)
                    for match in matches:
                        if(match in words):
                            # DO WORK
                            line = line.replace(match, replace_to_text)
                        pass
                    pass
                output.write(line)        
    
    print("The word ", search_text, " succesfully updated to ", replace_to_text,)
    pass

# Deleting Operation

def delete_text_in_file(file_name, search_text):
    # Transforming Regex
    search_text = search_text.replace("-", ".")
    search_text = search_text.replace("*", ".*")

    #Operation
    with open(file_name, "r") as file_input:
        with open("file_name.txt", "w") as output: 
            for line in file_input:
                words = line.split()
                for word in words:
                    matches = re.findall(search_text, word)
                    for match in matches:
                        if(match in words):
                            # DO WORK
                            line = line.replace(match, '')
                        pass
                    pass
                output.write(line)           
    
    print(search_text, " Deletion succesful.")
    pass

def print_file(file_name):
    file_stream = open(inpFileName)
    Lines = file_stream.readlines()
    count = 0
    # Striping the newline character
    for line in Lines:
        count += 1
        print("Line{}: {}".format(count, line.strip()))
        pass
    pass

def count_text_in_file(file_name, search_text):
    file_stream = open(inpFileName)
    Lines = file_stream.readlines()
    count = 0
    # Transforming Regex
    search_text = search_text.replace("-", ".")
    search_text = search_text.replace("*", ".*")

    # Striping the newline character
    for line in Lines:
        words = line.split()
        for word in words:
            matches = re.findall(search_text, word)
            for match in matches:
                if(match in words):
                    # DO WORK
                    count += 1
                pass
            pass
        pass
    print(count, " found.")
    return count

# Main Cycle

while(True):
    user_selection = str(input("Please enter your command: "))
    if(user_selection == "q"):
        exit(0)
        pass

    out = user_selection.split(" ")

    if(len(out) == 2):
        # Finding or Deleting
        if(out[0] == 'F'):
            # TO DO
            adet = count_text_in_file(inpFileName, out[1])
            pass
        elif(out[0] == 'D'):
            delete_text_in_file(inpFileName, out[1])
            pass
        pass
    elif (len(out) == 3):
        # Replacing
        if(out[0] == 'R'):
            edit_file(inpFileName, out[1], out[2])
            pass
        pass
    else:
        print("The command does not exist.")
        pass

    pass
