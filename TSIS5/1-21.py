def file_read(fname):
        txt = open(fname)
        print(txt.read())

file_read('test.txt')



a_file = open("file_name.txt")

number_of_lines = 3

for i in range(number_of_lines):

    line = a_file.readline()
    print(line)




def Appendtext(fname):
        with open(fname,'a+') as f:
                    f.write('appending line 1, ')
                    f.write('appending line 2. ')
            f.close()
# y=open('file1.txt')
# print(y.read())
Appendtext('file1.txt')

x= open('file1.txt')
print(x.read())



a_file = open("example.txt", "r")
lines = a_file.readlines()
last_lines = lines[-5:]

print(last_lines)
a_file.close()



def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                content_list = f.readlines()
                print(content_list)

file_read('test.txt')



def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')


def file_read(fname):
        content_array = []
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                for line in f:
                        content_array.append(line)
                print(content_array)

file_read('test.txt')


def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))


def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("test.txt"))


from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))



def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of a plain file: ",file_size("test.txt"))



color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open('abc.txt')
print(content.read())


from shutil import copyfile
copyfile('test.py', 'abc.py')



with open('abc.txt') as fh1, open('test.txt') as fh2:
    for line1, line2 in zip(fh1, fh2):
        print(line1+line2)



import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('test.txt'))



f = open('abc.txt','r')
print(f.closed)
f.close()
print(f.closed)



def remove_newlines(fname):
    flist = open(fname).readlines()
    return [s.rstrip('\n') for s in flist]

print(remove_newlines("test.txt"))



def count_words(filepath):
       with open(filepath) as f:
         data = f.read()
       data.replace(",", " ")
       return len(data.split(" "))
print(count_words("words.txt"))


import glob
char_list = []
files_list = glob.glob("*.txt")
for file_elem in files_list:
   with open(file_elem, "r") as f:
       char_list.append(f.read())
print(char_list)


import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)



import string
def letters_file_line(n):
   with open("words1.txt", "w") as f:
       alphabet = string.ascii_uppercase
       letters = [alphabet[i:i + n] + "\n" for i in range(0, len(alphabet), n)]
       f.writelines(letters)
letters_file_line(3)