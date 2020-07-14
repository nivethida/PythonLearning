# -*- coding: utf-8 -*-

import os

class fileReader():
    
    def __init__(self):
        self.size = ''
        self.modification_time = ''
        self.f = ''
        self.root_path = './'
        self.num_lines=0
        
        
    def connect(self, filename):
        self.f = open(self.root_path+filename, "r")
        
    def getSize(self, filename):
        self.size = os.stat(self.root_path+filename).st.size
        
        
        
        
        
        