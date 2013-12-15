'''
Created on Dec 14, 2013

@author: shizhang
'''
import myHtmlPaser
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
    parser.feed(filehandle.read())
    print parser.getSchoolLinks();
    