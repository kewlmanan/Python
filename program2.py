#! /usr/bin/python

if __name__=="__main__":

    x=raw_input("Enter the sentence\n")
    x.rstrip('\n')
    
    # Calculate lengths of words after splitting the input string 
    # and generate the o/p string along with it 
    
    result=''
    for item in x.split(' '):
        result=result+str(len(item))+' '
    
    print result
