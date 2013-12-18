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
        self.schools = []; 
        
    def handle_starttag(self, tag, attrs):
        if tag =="div" and attrs[0][0] == 'class' and re.match('item-list' , attrs[0][1]):
            #print "Encountered a start tag:", tag
            self.isUseful = True;
            
            
        if self.isUseful == True:
            if tag == "span" :
                self.parseSpan(attrs);
            elif tag == "a" :
                if attrs[0][0] == 'href':
                    self.schools.append(EdxParser.School())
                    school = self.schools.pop()
                    school.setlink("www.edx.org"+attrs[0][1]);
                    id = attrs[0][1].replace("/school/", "")
                    school.setid(id)
                    self.schools.append(school)
                    self.rawfile.write("school link: "+ attrs[0][1]+"\n")
                    #print attrs[0][1]
            elif tag == "img" :
                    school = self.schools.pop()
                    school.setthumbnail(attrs[1][1])
                    school.setname(attrs[5][1])
                    self.schools.append(school)
                    self.rawfile.write("school thumbnail: "+ attrs[1][1]+"\n")
                    self.rawfile.write("school name: "+ attrs[5][1]+"\n")
                
    
    def handle_endtag(self, tag):
        if tag == "div" and self.isUseful == True:
            self.isUseful = False;
    def handle_data(self, data):
        pass
    def getSchools(self):
        return self.schools
     
    class School:
        def __init__(self):
            self.id = ""
            self.schoolname = ""
            self.schoollink = ""
            self.thumbnail = ""
        
        def setid(self, schoolid): 
            self.id = schoolid
        def setname(self, schoolname):
            self.schoolname = schoolname
        def setlink(self, schoollink):
            self.schoollink = schoollink
        def setthumbnail(self, thumbnail):
            self.thumbnail = thumbnail
        def getid(self): 
            return self.id 
        def getname(self):
            return self.schoolname
        def getlink(self):
            return self.schoollink 
        def getthumbnail(self):
            return self.thumbnail
        def printschool(self):
            print self.id
            print self.schoolname
            print self.schoollink
            print self.thumbnail
            
            
        
            

