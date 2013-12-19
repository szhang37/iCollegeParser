'''
Created on Dec 16, 2013

@author: shizhang
'''
from HTMLParser import HTMLParser
import re
# create a subclass and override the handler methods
class LyndaSubParser(HTMLParser):

    
    def __init__(self):
        HTMLParser.__init__(self)
        #self.rawfile = open('edxschool.txt', 'w+')
        self.isUseful = False
        self.schoolLink = []; 
        
    def handle_starttag(self, tag, attrs):
        if tag =="div" and attrs:
            if attrs[0][0] == 'class' and re.match('software-name' , attrs[0][1]):
            #print "Encountered a start tag:", tag
                self.isUseful = True;
        if self.isUseful == True:
            if tag == "a" :
                if attrs[0][0] == 'href':
                    self.schoolLink.append(attrs[0][1]);
                    #print "school link: "+ attrs[0][1]
                
    
    def handle_endtag(self, tag):
        if tag == "div" and self.isUseful == True:
            self.isUseful = False
    def handle_data(self, data):
        if self.isUseful ==True:
            print data
    def getSchoolLinks(self):
        return self.schoolLink;


class LyndaParser(HTMLParser):
       
    def __init__(self):
        
        HTMLParser.__init__(self)
        #self.rawfile = open('edxschool.txt', 'w+')
        self.current = -1
        self.schoolLink = [];
        
    def handle_starttag(self, tag, attrs):
        if tag =="div" and attrs:
            if attrs[0][0] == 'class' and re.match('course-name' , attrs[0][1]):
                self.current = 0

            if attrs[0][0] == 'class' and re.match('thumb' , attrs[0][1]):
                self.current = 1

            if attrs[0][0] == 'class' and re.match('course-date' , attrs[0][1]):
                self.current = 2
                
        if self.current == 0:
            if tag == "a" :
                if attrs[0][0] == 'href':
                    print attrs[0][1] 
            
        elif self.current == 1:
            if tag == "a" :
                if attrs[3][0] == 'title':
                    print attrs[3][1] 
            elif tag == "img" :
                if attrs[0][0] == 'src':
                    print attrs[0][1]
                                
    def handle_data(self, data):
        if self.current ==0 or self.current == 2:
            print data
            
            
    def handle_endtag(self, tag):
        if tag == "div" and self.current!= -1:
            self.current = -1;
    
