'''
Created on Dec 14, 2013

@author: shizhang
'''
from HTMLParser import HTMLParser
import re
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    
    def __init__(self, rawfile):
        HTMLParser.__init__(self)
        self.rawfile = rawfile
        self.isUseful = False
    
        self.tagMap = ["crs-li-title","crs-li-sub","crs-li-tags-category","crs-li-text"]
        self.currentTag = ""
        
    def handle_starttag(self, tag, attrs):
        if tag =="li" and attrs[0][0] == 'data-ng-show' and re.match('isCourseShown*' , attrs[0][1]):
            #print "Encountered a start tag:", tag
            self.isUseful = True;
        if self.isUseful == True:
            if tag == "span" :
                self.parseSpan(attrs);
            elif tag == "a" :
                if attrs[0][0] == 'href':
                    self.rawfile.write("course link: "+ attrs[0][1]+"\n")
                    #print attrs[0][1]
            elif tag == "img" :
                    self.rawfile.write("thumbnail: "+ attrs[0][1]+"\n")
                    self.rawfile.write("course id: "+ attrs[1][1]+"\n")
                
    
    def handle_endtag(self, tag):
        if tag =="li" and self.isUseful == True :
            #print "Encountered some end  :", tag
            self.isUseful = False
        
        if tag =="span" and self.isUseful == True :
            #print "Encountered some end  :", tag
            self.currentTag = ""
            #self.isUseful = False
    
    def handle_data(self, data):
        if self.isUseful == True and self.currentTag != "":
            #print self.currentTag
            #print "Encountered some data  :", data
            #data = data.replace("\n", "")
            
            #data = data.replace("                                ", "")
            self.rawfile.write(self.currentTag +": "+data+"\n")
    
    def parseSpan(self, attrs) :
        
        if attrs[0][0] == "class" :
            for t in self.tagMap :
                if attrs[0][1] == t :
                    self.currentTag = t  
     
            
        
            

