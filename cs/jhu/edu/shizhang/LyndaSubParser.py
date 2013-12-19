'''
Created on Dec 16, 2013

@author: shizhang
'''
from HTMLParser import HTMLParser
import re
from EdxCourseParser import Course
# create a subclass and override the handler methods
class LyndaSubParser(HTMLParser):

    
    def __init__(self):
        HTMLParser.__init__(self)
        #self.rawfile = open('edxschool.txt', 'w+')
        self.isUseful = False
        self.schoolLink = []; 
        self.catname = []
        self.isname = False
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
        if tag == "span" and self.isUseful == True:
            self.isname = True
        if tag == "a" and self.isUseful == True:
            self.isname = False
    def handle_data(self, data):
        if self.isUseful ==True and self.isname == True:
            #print data
            self.catname.append(data.upper())
            #pass
    def getSchoolLinks(self):
        return self.schoolLink;


class LyndaParser(HTMLParser):
       
    def __init__(self):
        
        HTMLParser.__init__(self)
        #self.rawfile = open('edxschool.txt', 'w+')
        self.current = -1
        self.schoolLink = [];
        self.courses = []
    def handle_starttag(self, tag, attrs):
        if tag =="div" and attrs:
            if attrs[0][0] == 'class' and re.match('course-name' , attrs[0][1]):
                self.current = 0

            if attrs[0][0] == 'class' and re.match('thumb' , attrs[0][1]):
                self.current = 1
                self.courses.append(Course())

            if attrs[0][0] == 'class' and re.match('course-date' , attrs[0][1]):
                self.current = 2
                
        if self.current == 0:
            if tag == "a" :
                if attrs[0][0] == 'href':
                    print "http://www.lynda.com"+attrs[0][1]
                    co = self.courses.pop()
                    co.courselink ="http://www.lynda.com"+attrs[0][1]
                    self.courses.append(co)
            
        elif self.current == 1:
            if tag == "a" :
                if attrs[3][0] == 'title':
                    print attrs[3][1] 
                    co = self.courses.pop()
                    co.subtitle =attrs[3][1]
                    self.courses.append(co)
            elif tag == "img" :
                if attrs[0][0] == 'src':
                    print attrs[0][1]
                    co = self.courses.pop()
                    co.thumbnail =attrs[0][1]
                    self.courses.append(co)
                                
    def handle_data(self, data):
        if self.current ==0:
            print "0:"+data 
            co = self.courses.pop()
            co.title =data
            self.courses.append(co)
        if self.current == 2:
            print "2:"+data.strip()
            co = self.courses.pop()
            co.startdate =data.strip()
            self.courses.append(co)
            
            
    def handle_endtag(self, tag):
        if tag == "div" and self.current!= -1:
            self.current = -1;
#             print "end"
    
