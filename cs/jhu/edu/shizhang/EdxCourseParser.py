'''
Created on Dec 14, 2013

@author: shizhang
'''
from HTMLParser import HTMLParser
import re
# create a subclass and override the handler methods
class EdxCourseParser(HTMLParser):

    
    def __init__(self):
        HTMLParser.__init__(self)
        self.rawfile = open('edxschool.txt', 'w+')
        self.left = False
        self.right = False
        self.tagMap = ["title course-title","name","subtitle course-subtitle copy-detail","strong","img"]
        self.current = -1
        self.courses = []
        self.strong = 0
    def handle_starttag(self, tag, attrs):
        if tag =="div" and attrs :
            if attrs[0][0] == 'class' and re.match('col-left-courses column-left views-fieldset' , attrs[0][1]):
            #print "Encountered a start tag:", tag
                
                self.left = True    
                self.right = False

            elif attrs[0][0] == 'class' and re.match('col-right-courses column-right views-fieldset' , attrs[0][1]):
            #print "Encountered a start tag:", tag
                self.left = False    
                self.right = True
                
        if self.left == True:
            if tag == "h2" and attrs[0][0] == 'class' and attrs[0][1] == 'title course-title' :
                self.current = 0
            elif tag == "a" :
                if attrs[0][0] == 'href' and re.match('https://www.edx.org/course/*' , attrs[0][1]) :
                    self.current = 1
                    #print "school link: "+ attrs[0][1]
                    c = self.courses.pop()
                    c.setlink(attrs[0][1])
                    self.courses.append(c)
                    #print attrs[0][1]
            elif tag =="div" and attrs[0][0] == 'class' and re.match('subtitle course-subtitle copy-detail' , attrs[0][1]): 
                self.current = 2
            elif tag == "strong":
                self.strong+=1
                self.current = 3
            
                    
        if self.right == True:
            if tag == "img" and attrs[0][0] == 'class' and attrs[0][1] == 'image-style-none' :
                #print attrs[1][1]
                self.courses.append(Course())
                c = self.courses.pop()
                c.setthumbnail(attrs[1][1])
                self.courses.append(c)
                
                self.strong = 0
                
    
    def handle_endtag(self, tag):
        if self.left == True:
            self.current = -1
    
    def handle_data(self, data):
        if self.current != -1:
            if self.current == 1:
                c = self.courses.pop()
                c.settitle(data)
                self.courses.append(c)
            elif self.current ==2 :
                c = self.courses.pop()
                c.setsub(data)
                self.courses.append(c)
            elif self.current ==3 :
                if self.strong ==2 :
                    c = self.courses.pop()
                    c.setstart(data)
                    self.courses.append(c)
                elif self.strong ==3 :
                    c = self.courses.pop()
                    c.setinstructor(data)
                    self.courses.append(c)
            
                
            
class Course:
    def __init__(self):
        self.thumbnail = ""
        self.courselink = ""
        self.title = ""
        self.subtitle =""
        self.startdate = ""
        self.instructor = ""
        self.uuid = ""
        self.info = ""
        self.cat = ""
        
    def setthumbnail(self, thumb):
        self.thumbnail = thumb
    def setlink(self, link):
        self.courselink = link
    def settitle(self,t):
        self.title = t
    def setinfo(self,i):
        self.info = i
    def setsub(self, sub):
        self.subtitle = sub.replace("\n"," ")
    def setstart(self, start):
        self.startdate = start
    def setinstructor(self, instructor):
        self.instructor = instructor
    def printc(self):
        print "clink:"+self.courselink
        print "lecturer:"+self.instructor
        print "startdate:"+self.startdate
        print "title:"+self.title
        print "sub:"+self.subtitle
        print "imglink:"+self.thumbnail    
        print "info:"+self.info
        print "cat:"+self.cat
        
     
            
        
            

