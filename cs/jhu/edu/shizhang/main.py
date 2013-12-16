'''
Created on Dec 14, 2013

@author: shizhang
'''
import myHtmlPaser
import EdxCourseParser
import EdxParser
import urllib

if __name__ == '__main__':
    # instantiate the parser and fed it some HTML
    '''
    read html file from the URL
    '''
#    filehandle = urllib.urlopen("https://www.udacity.com/courses")

    filehandle = urllib.urlopen("https://www.edx.org/school")
    '''
    parse the information for html file
    '''
#    rawfile = open("udacity.txt", 'w+')
#    parser = myHtmlPaser.MyHTMLParser(rawfile)
#    parser.feed(filehandle.read())
#    
#    print rawfile.read()
#   
    parser = EdxParser.EdxParser() 
#    corseparser = EdxCourseParser.EdxCourseParser()
    parser.feed(filehandle.read())
    for schoolcode in parser.getSchoolLinks():
        handler = urllib.urlopen("https://www.edx.org"+schoolcode)
        corseparser1 = EdxCourseParser.EdxCourseParser()
        corseparser1.feed(handler.read())
        handler = urllib.urlopen("https://www.edx.org"+schoolcode+"?page=1")
        corseparser2 = EdxCourseParser.EdxCourseParser()
        corseparser2.feed(handler.read())
        
    
    