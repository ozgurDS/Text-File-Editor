
# Text File Editor

## About

This project aiming to create a file editor for manipulating the words in a text based file. The program has 3 main functions: finding, replacing and deleting the words as the user pleases.

## Getting Started

You will need `Python 3` with the necessary modules installed to run the program. These modules are: `sys`, `fileinput` and `re` libraries.

## Starting the Program

Open your terminal and simply locate the folder of the program. Then, simply call the program with python and enter the text file you need to modify as the parameter. 

Example: `python3 text-file-editor.py text.txt` We run the text-editor code with the given file text.txt.

Once you started the program, you can do as many operations as you want before closing it.

## Commands and Usage  

The program has 3 main commands: F command for finding the count of the  word, R command for replacing and D command for deleting. For example: If we run `F apple` command, the program returns the count of the word apple in the file. If we run `R apple banana` command, the program replaces all the apples with banana. If we run `D apple` command, the program deletes all the apples from the file. 

The program also has 2 special expressions `-` and `*` where `-` stands for any character and `*` stands for zero or any number of characters. For example, when we run `F -il-` command, the program can return a 4 character word starting and anding with any character and "il" in the middle, such as will, bill, file etc. If we run `F *il*` command instead, the program can return any word that has "il" in it such as ill, drill, ilusion etc. 

The 2 expressions can be combined for the specific operations. For example the command `F -il*` will return us the number of the words those starts with any character but the "il" must take place in second to third character in the word, but the word could end any number of characters, so program can return bill, pillars, nile etc.

You can also use the expression `-` more than 2 times. For example, running `F --il-----` command can return billards.

## Closing the Program

After finishing, simply run command `q` to close the program. The operations you committed will be saved automatically.


## License

Özgür HACIMUSTAFAOĞLU
Copyright (c) 2021
Licensed under the [MIT license](LICENSE).
