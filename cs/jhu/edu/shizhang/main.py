'''
Created on Dec 14, 2013

@author: shizhang
'''
import myHtmlPaser
import EdxCourseParser
import EdxParser
import urllib
import psycopg2, psycopg2.extras
import uuid
import datetime
if __name__ == '__main__':
    psycopg2.extras.register_uuid()
    # instantiate the parser and fed it some HTML
    '''
    read html file from the URL
    '''
#   filehandle = urllib.urlopen("https://www.udacity.com/courses")

    filehandle = urllib.urlopen("https://www.edx.org/school")
    '''
    parse the information for html file
    '''
#    rawfile = open("udacity.txt", 'w+')
#    parser = myHtmlPaser.MyHTMLParser(rawfile)
#    parser.feed(filehandle.read())
#    
#    print rawfile.read()
# # 
    conn = psycopg2.connect("dbname=iCollegeStation user=postgres")
    cur = conn.cursor()  
    
############################################################################################

#parse the edx data

############################################################################################
    
#     parser = EdxParser.EdxParser() 
# # #    corseparser = EdxCourseParser.EdxCourseParser()
#     parser.feed(filehandle.read())
#     
#     
#     for school in parser.getSchools():
#         #school.printschool()
# #     for schoolcode in parser.getSchoolLinks():
#         handler = urllib.urlopen("http://"+school.schoollink)
#         corseparser1 = EdxCourseParser.EdxCourseParser()
#         corseparser1.feed(handler.read())
#         for c in corseparser1.courses:
#             #c.printc()
#             c.uuid = uuid.uuid4()
#             print c.uuid
#             try:
#                 d = datetime.datetime.strptime(c.startdate, "%d %b %Y").date()
#             except ValueError:
#                 d = datetime.date.today()
#                 
#             print d
#             print cur.execute("INSERT INTO course (cid, siteid, title, subtitle, imglink, courselink, sid, lecturer, startTime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#                         (c.uuid, 1, c.title,c.subtitle, c.thumbnail,c.courselink, school.id,c.instructor, d))
#         
#         
#         handler = urllib.urlopen("http://"+school.schoollink+"?page=1")
#         corseparser2 = EdxCourseParser.EdxCourseParser()
#         corseparser2.feed(handler.read())
#         for c in corseparser2.courses:
#             #c.printc()
#             c.uuid = uuid.uuid4()
#             print c.uuid
#             try:
#                 d = datetime.datetime.strptime(c.startdate, "%d %b %Y").date()
#             except ValueError:
#                 d = datetime.date.today()
#             cur.execute("INSERT INTO course (cid, siteid, title, subtitle, imglink, courselink, sid, lecturer, startTime) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
#                         (c.uuid, 1, c.title,c.subtitle, c.thumbnail,c.courselink, school.id,c.instructor, d))
    

# #     cur.execute("SELECT * FROM site;")
#     for school in parser.getSchools():
#         cur.execute("INSERT INTO school (sid, schoolname, schoollink, schoolimg) VALUES (%s, %s, %s,%s)",(school.id, school.schoolname, school.schoollink, school.thumbnail))
#     print cur.fetchall()

############################################################################################

#parse the udacity data

############################################################################################
#     filehandle = urllib.urlopen("https://www.udacity.com/courses")
#     parser = myHtmlPaser.MyHTMLParser()
#     parser.feed(filehandle.read())
# 
#     courses = parser.getCourses()
#     cats = parser.getCats()
#     print cats
#     for cat in cats.keys():
#         print cur.execute("INSERT INTO category (catid,catname) VALUES (%s,%s)",
#                         (cats[cat],cat))
#          
#     for c in courses:
#         print cur.execute("INSERT INTO course (cid, siteid, title, subtitle, imglink, courselink, intro, catid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
#                         (c.uuid, 3, c.title,c.subtitle, c.thumbnail,c.courselink, c.info, cats[c.cat]))

############################################################################################

#parse the lynda data

############################################################################################         
    conn.commit()
    cur.close()
    conn.close()
    
    
    