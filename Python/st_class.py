#! /usr/bin/env python

import os
import sys

class Stack:
    def __init__(self, len):
		self.top=-1
		self.size=len
		self.array=[]
		print " Stack created"
    def overflow_check(self):
        if ( self.top == (self.size-1)):
	    	print " Stack Overflow "
	       	sys.exit()
    def underflow_check(self):
        if ( self.top == -1 ):
             print "Stack Underflow" 
             sys.exit()
    def push(self, x):
		self.overflow_check()
		self.array.append(x)
		self.top += 1
                print x
                print "pushed \n"
    def pop(self):
        self.underflow_check()
        x=self.array.pop()
        self.top -= 1
        print x 
        print " popped \n "

    def listall(self):
        print " The elements in the list are :"
      	for i in self.array:
            print i
            print " "

if __name__ == "__main__":
    NewStack = Stack(3)
    NewStack.push(3)
    NewStack.push(4)
    NewStack.listall()
    NewStack.pop()
    NewStack.listall()
	
