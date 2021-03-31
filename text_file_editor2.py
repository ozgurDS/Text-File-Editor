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
    file_stream = open(inpFileName,encoding='utf8')
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
    final_text =""
    with open(file_name, "r",encoding='utf8') as file_input:
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
                final_text += line
    file_input.close()
    with open(file_name, "w",encoding='utf8') as final_file:
        final_file.write(final_text)
        pass
    final_file.close()
    
    print("The word ", search_text, " succesfully updated to ", replace_to_text,)
    pass

# Deleting Operation

def delete_text_in_file(file_name, search_text):
    # Transforming Regex
    search_text = search_text.replace("-", ".")
    search_text = search_text.replace("*", ".*")

    #Operation
    final_text = ""
    with open(file_name, "r",encoding='utf8') as file_input:
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
            final_text += line
            pass
        pass
    file_input.close()
    # open file for writing final text
    with open(file_name, "w",encoding='utf8') as final_file:
        final_file.write(final_text)
        pass
    final_file.close()
    
    print(search_text, " Deletion succesful.")
    pass

def count_text_in_file(file_name, search_text):
    file_stream = open(inpFileName,'r',encoding='utf8')
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
    file_stream.close()
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