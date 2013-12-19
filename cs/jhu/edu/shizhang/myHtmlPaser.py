'''
Created on Dec 14, 2013

@author: shizhang
'''
from HTMLParser import HTMLParser
import EdxCourseParser
import re
import uuid
# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

    
    def __init__(self):
        HTMLParser.__init__(self)
        #self.rawfile = rawfile
        self.isUseful = False
    
        self.tagMap = ["crs-li-title","crs-li-sub","crs-li-tags-category","crs-li-text"]
        self.currentTag = ""
        self.courses = []
        self.category = {}
        
    def handle_starttag(self, tag, attrs):
        if tag =="li" and attrs[0][0] == 'data-ng-show' and re.match('isCourseShown*' , attrs[0][1]):
            #print "Encountered a start tag:", tag
            self.isUseful = True
            self.courses.append(EdxCourseParser.Course())
        if self.isUseful == True:
            if tag == "span" :
                self.parseSpan(attrs);
            elif tag == "a" :
                if attrs[0][0] == 'href':
                    #self.rawfile.write("course link: "+ attrs[0][1]+"\n")
                    c = self.courses.pop()
                    c.setlink("http://www.udacity.com"+attrs[0][1])
                    c.uuid = uuid.uuid4()
                    self.courses.append(c)
                    #print attrs[0][1]
            elif tag == "img" :
                    #self.rawfile.write("thumbnail: "+ attrs[0][1]+"\n")
                    #self.rawfile.write("course id: "+ attrs[1][1]+"\n")
                    c = self.courses.pop()
                    c.setthumbnail("http:"+attrs[0][1])
                    self.courses.append(c)
    
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
            #self.rawfile.write(self.currentTag +": "+data+"\n")
            if self.currentTag == self.tagMap[0]:
                c = self.courses.pop()
                c.settitle(data)
                self.courses.append(c)
            elif self.currentTag == self.tagMap[1]:
                c = self.courses.pop()
                c.setsub(data)
                self.courses.append(c)
            elif self.currentTag == self.tagMap[2]:
                if not self.category.has_key(data):
                    self.category[data] = uuid.uuid4()
                c = self.courses.pop()
                c.cat = data
                self.courses.append(c)
            elif self.currentTag == self.tagMap[3]:
                c = self.courses.pop()
                c.setinfo(data)
                self.courses.append(c)
    def parseSpan(self, attrs) :
        
        if attrs[0][0] == "class" :
            for t in self.tagMap :
                if attrs[0][1] == t :
                    self.currentTag = t
            if attrs[0][1] == 'new-course-tag':
                self.currentTag = ''
     
    def getCourses(self):
        return self.courses
    def getCats(self):
        return self.category        

