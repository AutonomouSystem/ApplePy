#/usr/bin/env python

from __future__ import print_function

import subprocess
import os

class AppleScript():
    
    """ Scripts to supplement AppleScript usage within Python """
    
    def __init__(self):
        self.pie = ''
        self.scpts = ''
        self.filename = ''
        self.res = ''
        
    
    def snake_hug(self, *args):
        """ 
        Wrap up AppleScript commands by line for osascript execution
        
        To use, pass in AppleScript lines by line, "line1", "line2", "line3", etc.        
        
        """
        
        base = ['osascript', '-e']
        
        commands = list()
        
        for cmds in args[:]:            
            commands.append(cmds)
            commands.append('-e')
            
        
        if commands[-1] == '-e':
            del commands[-1]
            base.extend(commands)
        else:
            base.extend(commands)              
        
        #return base
        self.pie = base
        
    
    def scpt_build(self):
        """ 
        Open AppleScript in plaintext - Return list(scpt) 
        Note, .scpt is compiled AppleScript
        Use osadecompile -> plaintext
        e.g. $ osadecompile file.scpt >> ~/Path/file.txt    
    
        TO-DO:
        -Only execute on plaintext
        -Add osadecompile
    
        """
        pass   
      
      
    def cute(self):
        """ 
        Execute AppleScript
        
        TO-DO:
        - Add argument for call/output
        - Add default argument
        
        """
        if bool(self.pie):         
            #subprocess.call(self.pie, shell=False)
            self.res = subprocess.check_output(self.pie, universal_newlines=False).strip('\n')
        
    def result(self):
        return self.res 
      
      
if __name__ == "__main__":
    mommas = AppleScript()
    mommas.snake_hug('display dialog "Hi there... testing 1.. 2.. 3?" with icon stop buttons {"Less than 2", "Less than 3", "More than 0"}') # AS code
    mommas.cute() 
    print(mommas.res)
