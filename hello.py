# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 14:20:36 2019

@author: mosta
"""

#def introduction(name, event, nattended):
#    """ Provides an introduction to attendant. """
#    
#    template = "Hello %s, welcome to %s! This is your %dth time attending."
#    
#    statement = template % (name, event, nattended)
#    
#    return statement

#def introduction_format(name, event, nattended):
#    """ Provides an introduction to attendant. """
#    template = "Hello {}, welcome to {}! This is your {}th time attending."
#    
#    statement = template.format (name, event, nattended)

def introduction_format(name, event, nattended):
    """ Provides an introduction to attendant using string concatenation. """
    statement = "Hello" + name + ", welcome to " + event + "! This is your " + str(nattended)    
 # return statement   
    return statement
name = input ("What is your name? ")
event = input ("What event are you attending? ")
ntimes= input("How many times have you attended? ")

statement = introduction(name, event, int(ntimes))

print (statement)