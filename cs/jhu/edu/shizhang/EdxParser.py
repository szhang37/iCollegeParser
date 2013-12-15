'''
Created on Dec 14, 2013

@author: shizhang
'''
from HTMLParser import HTMLParser
import re
# create a subclass and override the handler methods
class EdxParser(HTMLParser):

    
    def __init__(self):
        HTMLParser.__init__(self)
        self.rawfile = open('edxschool.txt', 'w+')
        self.isUseful = False
        self.schoolLink = []; 
        
    def handle_starttag(self, tag, attrs):
        if tag =="div" and attrs[0][0] == 'class' and re.match('item-list' , attrs[0][1]):
            #print "Encountered a start tag:", tag
            self.isUseful = True;
        if self.isUseful == True:
            if tag == "span" :
                self.parseSpan(attrs);
            elif tag == "a" :
                if attrs[0][0] == 'href':
                    self.schoolLink.append(attrs[0][1]);
                    self.rawfile.write("school link: "+ attrs[0][1]+"\n")
                    #print attrs[0][1]
            elif tag == "img" :
                    self.rawfile.write("school thumbnail: "+ attrs[1][1]+"\n")
                    self.rawfile.write("school name: "+ attrs[5][1]+"\n")
                
    
    def handle_endtag(self, tag):
        if tag == "div" and self.isUseful == True:
            self.isUseful = False;
    def handle_data(self, data):
        pass
    def getSchoolLinks(self):
        return self.schoolLink;
     
            
        
            

