import os
import pathlib
import sys

from os import listdir
from os.path import isfile, join

def display_lines(path,number_of_lines):
    list_line=[]
    with open(path,'r') as f:
        for i in range(number_of_lines):
            line=f.readline()
            list_line.append(line)
            #print('line number '+str(i+1)+': '+line)
    return list_line

def compare_lines(list1,list2):
    for i in range(len(list1)):
        if list1[i]!=list2[i]:
            bool=False
            print('line number: '+str(i+1))
            print(list1[i])
            print(list2[i])
           # break
        else:
            bool=True
    return bool

  


def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles  


#Gives current directory
basepath=os.getcwd()
print("Path: "+basepath)
sub_elem=str(basepath)+'\\'+'MGP_StimeFabbisogno1'
print(sub_elem)

elem=os.listdir(sub_elem)

count=0
files_xml=[]
for e in elem:
    if e.endswith('.xml'):
        files_xml.append(e)
        count+=1
    
print('Num xml files:'+str(count))

#print(files_xml)
    
num_lines=10

basepath=sub_elem

# for i in files_xml:
#     index = files_xml.index(i)
#     print('File a:'+i)
#     pathfile1=str(basepath)+"\\"+i
#     #print(pathfile1)
#     list1=display_lines(pathfile1,num_lines)
    
#     for j in range(index+1,len(files_xml)):
#         #print("\t"+str(j))
#         elemj = files_xml[j]
#         print("\t"+'File b:'+elemj)
#         pathfile2=str(basepath)+"\\"+elemj
#     # print(pathfile2)
#         list2=display_lines(pathfile2,num_lines)
#         bool=compare_lines(list1,list2)
#         if bool==False:
#             print("\t"+str(bool))
#     print('******')





# Save a reference to the original standard output  
original_stdout = sys.stdout 

#Write the result in document.txt
with open('result.txt', 'w') as f:
    sys.stdout = f # Change the standard output to the file we created. 
    for i in files_xml:
        index = files_xml.index(i)
        print('File a:'+i)
        pathfile1=str(basepath)+"\\"+i
        #print(pathfile1)
        list1=display_lines(pathfile1,num_lines)
        
        for j in range(index+1,len(files_xml)):
            #print("\t"+str(j))
            elemj = files_xml[j]
            print("\t"+'File b:'+elemj)
            pathfile2=str(basepath)+"\\"+elemj
        # print(pathfile2)
            list2=display_lines(pathfile2,num_lines)
            bool=compare_lines(list1,list2)
            if bool==False:
                print("\t"+str(bool))

        print('******')
    sys.stdout = original_stdout # Reset the standard output to its original value






# pathfile1=str(basepath)+"\\"+files_xml[1]
# print(pathfile1)
# num_lines=27
# list1=display_lines(pathfile1,num_lines)
# print('******')
# pathfile2=str(basepath)+"\\"+files_xml[4]
# print(pathfile2)
# list2=display_lines(pathfile2,num_lines)

# print(compare_lines(list1,list2))









# dirName =basepath
# # Get the list of all files in directory tree at given path
# listOfFiles = getListOfFiles(dirName)

# for e in listOfFiles:
#     print(e)
#     print('\n')

# print('Number of elements: ',str(len(listOfFiles))) #5.679 file



    
