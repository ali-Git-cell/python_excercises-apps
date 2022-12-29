'''
Maitaining a register of members on a .txt document. Every month this file is updated the by removing the members who are not active.
Given the file currentMem, each member with a 'no' in their Active column is removed. 
track of each of the removed members is kept and appended to the exMem file. The original format of the files is preserved. 
'''

'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members
    
    This function removes all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''
def cleanFiles(currentMem,exMem):
    with open(currentMem,'r+') as writeFile: 
        with open(exMem,'a+') as appendFile:
            #getting the data
            writeFile.seek(0)
            members = writeFile.readlines()
            #removing header
            header = members[0]
            members.pop(0)
                
            inactive = [member for member in members if ('no' in member)]
            '''
           below is alternative for the above 

            for member in members:
            if 'no' in member:
                inactive.append(member)
            '''
            #to the beginning of the write file
            writeFile.seek(0) 
            writeFile.write(header)
            for member in members:
                if (member in inactive):
                    appendFile.write(member)
                else:
                    writeFile.write(member)      
            writeFile.truncate()

# The code below is to view the files.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg,exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg,'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())
    
with open(exReg,'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
                
