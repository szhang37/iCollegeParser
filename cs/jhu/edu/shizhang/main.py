'''
Created on Dec 14, 2013

@author: shizhang
'''
import myHtmlPaser
import EdxCourseParser
import EdxParser
import LyndaSubParser
import urllib

if __name__ == '__main__':
    # instantiate the parser and fed it some HTML
    '''
    read html file from the URL
    '''
#    filehandle = urllib.urlopen("https://www.udacity.com/courses")

    
    '''
    parse the information for html file
    '''
#    rawfile = open("udacity.txt", 'w+')
#    parser = myHtmlPaser.MyHTMLParser(rawfile)
#    parser.feed(filehandle.read())
#    
#    print rawfile.read()

## the procedure for edx website 

#    filehandle = urllib.urlopen("https://www.edx.org/school")
#    parser = EdxParser.EdxParser() 
#
#    parser.feed(filehandle.read())
#    for schoolcode in parser.getSchoolLinks():
#        handler = urllib.urlopen("https://www.edx.org"+schoolcode)
#        corseparser1 = EdxCourseParser.EdxCourseParser()
#        corseparser1.feed(handler.read())
#        handler = urllib.urlopen("https://www.edx.org"+schoolcode+"?page=1")
#        corseparser2 = EdxCourseParser.EdxCourseParser()
#        corseparser2.feed(handler.read())


## the procedure for lynda website 

    filehandle = urllib.urlopen("http://www.lynda.com/subject/all")
    parser = LyndaSubParser.LyndaSubParser() 
    parser.feed(filehandle.read())
    
    for schoolcode in parser.getSchoolLinks():
        handle = urllib.urlopen("http://www.lynda.com/"+schoolcode)
        parser1 = LyndaSubParser.LyndaParser() 
        parser1.feed(handle.read())