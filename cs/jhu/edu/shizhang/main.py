'''
Created on Dec 14, 2013

@author: shizhang
'''
import myHtmlPaser
import EdxCourseParser
import EdxParser
import LyndaSubParser
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


# # 
    conn = psycopg2.connect("dbname=iCollegeStation user=postgres")
    cur = conn.cursor()  
    
############################################################################################

#parse the edx data

############################################################################################
#     
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
#     
# 
# # #     cur.execute("SELECT * FROM site;")
#     for school in parser.getSchools():
#         cur.execute("INSERT INTO school (sid, schoolname, schoollink, schoolimg) VALUES (%s, %s, %s,%s)",(school.id, school.schoolname, school.schoollink, school.thumbnail))
#    # print cur.fetchall()
# 
# ############################################################################################
# 
# #parse the udacity data
# 
# ############################################################################################
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
    ## the procedure for lynda website 

    filehandle = urllib.urlopen("http://www.lynda.com/subject/all")
    parser = LyndaSubParser.LyndaSubParser() 
    parser.feed(filehandle.read())
    print parser.catname
    
#     uuids =[]
#     for cat in parser.catname:
#         id = uuid.uuid4()
#         print cur.execute("INSERT INTO station_category (id,catname) VALUES (%s,%s)",
#                         (id,cat))
#         uuids.append(id)
#     print uuids
    uuids = ['ec5662c2-7616-40a9-bf8f-afebd61f7e38', '8e44cf8e-a13a-4779-ba37-923a6f3cb0f6', 'b00074e9-8c87-41fd-a2dc-25d4f1800d6b', 'a6131ae3-e941-4983-9da9-6bc7cb3103c8', '26a7f0a1-b2cb-4aa6-8116-1bf3378e6f7b', 'f311392a-82de-443a-a1d6-bb8254bef6f0', 'a2cb3c54-2445-466b-884d-4001a3c599d2', '691e0a0d-e332-4259-8e97-c6ba850d271f', '45b3d78d-e560-4c08-b917-6007a8307d67', '784050c4-ca78-4dff-9958-2e3df651ea51', '55ec85c0-a665-4714-b333-548f548b2640', '7fec466e-9163-4b98-850a-09b2a1053457', 'c04baa87-dce2-4f77-8af8-aa6c227f9208', 'f283d4bd-6355-48d3-a6d4-0997013d0b7c', '6027f0e0-043d-49fa-ab50-62cc57d04740', 'ea8a5ff3-1e62-4f76-828f-14a6153742f9', '8ce238da-1f61-4a0d-b1f5-734ae6066363', 'a27670dd-206c-4459-a679-68da00b2057b', 'de8a30fe-2ced-4340-9f5c-393b35d73eaa', '08d7e58a-a8aa-43a0-a7b0-75f73e1c42cd', '7cc3a794-d740-46bd-a050-d8cb28187e46', 'da4e02f4-357c-4257-9165-60e59d91eb5d', '72d99e6c-40d4-482b-b272-65bfe270e00d', 'e702d6d1-3ea2-4b93-8397-0200868c641c', '39e56bc1-66f8-4b5f-a899-14bbac7d1029', '1d142700-8e2a-4149-ab36-500871d0d7b9', 'bd9c43c6-611c-4d33-885d-502b271c7a26', 'f51feb49-05bd-4491-ad6b-b377fe73ac95', '27fda1ac-5af5-4d6b-82af-92a583d1fd21', 'b2457d64-2e27-41ee-9e0b-45b4b6826e40', 'e6e83739-0e86-47c3-a8d7-9570ced3dc9a', 'f793dc57-e053-48f9-9989-dd70da4fe537', '61f99f91-9d90-477f-8632-942890a68faa', '76d6e3fb-a057-4667-b4bd-5fbdaa176485', 'd1898034-17f6-4a82-9055-0e9d95cbf7fd', '0d10aceb-568a-40b4-a292-a3b1a8fa5cbd', '7f6fd940-caa4-45d3-8b70-165daf8e4611', '3872c9b3-28bb-4a6f-ac13-40f42b01480c', '8f7f35ba-2990-4c08-98ee-f2af3d718f9a', 'fca8e12f-9bda-4093-b4ac-f8b7347f3974', 'e76b890a-9178-4fe1-80b5-461861834cae', '7a40e314-21fb-4d23-bace-c66408658806', '66fd8f0d-a6ca-4ddb-bc97-215fb0fe171e', '124d04eb-b3f6-4cd2-8a86-fbf19fc2babe', 'f142e7cd-c046-4765-9de7-b94118da002b', '8b14492b-18e1-4d3c-ac2c-4ed8b3d17624', '69a632ad-258b-435e-bef7-d93eee73181a', 'dee1adb0-2456-47a7-89d7-e05d2f516503', 'fa26a93a-fa9f-44dc-a70a-62380a695135', '497527a9-f46e-4b3b-b572-f5c1f5a2bbdf', '3ac18150-5ca2-479e-b7ef-d12d1734601b', 'ee0b7ab7-c938-46ba-9bf7-4e16682e03d5', 'f68c69ed-a438-48f4-aa99-c481f4d2fe63', '1edb8511-125b-4210-bf39-b9b490123f8c', 'b6a3e0ed-553a-4303-9d79-193b53659d72', 'e0076a40-900f-4aae-99c6-926cb9f3e52e', '50eb88bb-9a78-4eda-97df-5edc85f30227', '06e23cd4-741d-43f3-9de6-463ed4296d55', '914eff8f-7f47-4b96-bb70-0ae36264d0ae', 'bad74455-282d-4eb0-a999-4837c598750d', 'e4470808-4bfb-4968-8ccf-b27f7d8c8a4f', '79c47b55-2d17-477e-9bb4-31b8eab99047', 'ae9a136b-828d-46ea-ac95-f89cfae71176', '150c9f70-2933-481a-b794-2ef986ad65c4', 'ea89b421-1b99-4acf-8c64-0354bb40e49f', '85ce84e1-de21-4e1f-8041-21d0ac399cf3', '43dd5a44-4398-4462-8b8b-ea2b3d74a865', '0b57622b-1918-401a-9afe-1528b6044a27', 'e72d428d-a6ab-410b-85bb-64524c14af6d', 'b2a95e4c-adf0-47de-a993-e756fa4083e4', 'ef292355-539d-4c31-b9a3-8fa8bf8a03f6', '0c41a591-86d6-43ab-a931-e360a3aae2f0', '9215d992-0cfc-41bd-93a6-9a1e59b87566', 'b1a4ab07-aa0c-44cc-8625-2298629c04b0', 'bea4cbed-752f-4fc1-b170-31153e423caa', 'a33c9efd-434d-4fb6-9e3a-ca87b2a4526b', '1be1fb30-795e-4ba9-9c96-00974c912c7e', '70b3d10d-eea6-4553-980b-3a19732b8c94', 'af96e58f-0db0-41d6-abbe-c6be129f200e', '33caeb1f-629a-400a-8e31-946169aed7d3', 'be28d59e-33d6-42bf-bb74-331abcd6b5a6', '2839cb59-ec49-4de4-a6ed-8c99fa4db7fe', '691fffc6-28f6-4de5-a6a9-76bf0be8e122', '4a45451c-2a13-473e-a376-0acf09b37576', 'ed0fa230-f73c-4538-8d59-ef90e4ee1548', 'eacb7ea2-5e89-48ea-8256-4b29b897cff1', 'f65d51c6-5c8a-4ac2-851d-7eacc0df8dad', 'cb487c74-4ce5-4ae9-aeb6-71820f8b0669', 'ee67a371-cee4-4086-bd0e-3a0e0226b6ba', 'ba9d6aa8-6003-4b97-bd36-e3ca11001d67', '0f6eea8f-1160-4c91-aa7c-73577dfba7f0', 'a9bb22a3-528b-4f02-8939-aaaf982c29ef', '3452bbad-45f4-4369-a10c-d2514c7e484b', 'f89f2400-9332-4a2e-96ba-049ab0cfc432', '0f3be8cc-e43f-48b2-b709-ca38ef99dd11', '6a09f6a6-a8d9-4ea0-9136-31c5e28e9b5b', '9898ab86-b0bb-4c11-9656-4aef3c228e42', '100ef86f-54cf-496b-b7c4-60bef70617bf', '413dc1b4-aaf7-47ba-a3ad-2ae5336d75c2', '5a9fe5f0-f340-43eb-84c8-32b54a0b5f16', '1824d843-d6e4-438a-8d7c-0f7b24f85712', '27000052-a476-4f74-826c-d5e2afd23348', '857409f0-2db2-47f8-b4f7-34e5176568ce', 'ca8a477f-46dc-4c09-8e51-c5aa65453e91', 'a247b406-45eb-4532-ba5e-8330debbb52f', '89086ddf-7929-4b10-8d81-ff930fbea0e3', 'efcadd1a-cf4a-45f2-ab46-5e61c7ff3de6', 'f85d0a66-b92d-4743-b66c-28216fcd54c1', '57b688c4-b578-4e81-8d52-081e48da8f5c', '82f17406-08c7-40a6-a3c8-2496ccd952c5', 'ef1c6d5a-15be-464b-a711-2273710be9cc', 'f7d3637c-5528-43e8-962b-369aa436feb1', '2492f279-04e9-47e9-806a-53d35c13cb37', 'd3f23529-d1e4-40af-8cd4-4b83f051211b', '5018e7a9-a7f6-48eb-b7bc-c60515291430', 'bf86f8df-b7e0-4a0c-b3f1-778ebecda512', '4512785d-9428-44cc-a837-13078e9a32bf', '116e3a4b-51df-4501-9d2f-b13ad8827531', 'e1e2e8f8-eeb5-4a17-86ea-374f725ee7c9', '89a686c6-4198-46fc-ab44-e7243df95070', '4ff08234-54b6-40dd-a9df-b70e9bca3bd2', 'f8700594-1be3-469b-b01e-8f086f9e6181', '9eebfc38-08c0-418f-bf27-7dd4c5142c32', '9123589e-9cad-436b-a937-337429c74349', '643dcb01-a595-41d7-b558-a7938afc1e51', '18a459ef-aa7f-4b17-ab12-134c15a9320c', 'e0f64168-40f7-401c-8c28-e71663880a88', '5cc600fa-bc16-4043-807d-c3e1e1db344d', 'e94c6cc1-2f51-4143-a816-d6acf5e699f7', '47c86152-8a9a-4035-9b76-6b5ceaf37c6c', '10e425fd-b018-4524-98de-ad35c5a0d914', 'ac6543df-f1ed-4b1b-b808-26fda91f8d5b', 'e6e3f70b-83cc-4897-ae93-bf5fcc03a646', 'c2c7cdd8-c895-4be7-9d72-851d29da0989', 'f2a19985-4437-4030-8c10-bf368b2da278', '9fbbe976-9551-414f-87ca-819402d249a5', 'be6566ed-fce4-41a0-bef4-a6aba0638585', 'a4a79066-aadc-4003-9683-79c015156245', 'cce15533-1629-4374-a564-a28256f5e5d7', '0c381c52-6f13-40ef-83b8-ddf8f22b3dd8', '3237d662-9389-43fa-962c-ba58acc120dd', '33375f90-c578-46d9-a132-28f24857748d', '94e6dd48-9bd6-4925-be33-bb05e43700d5', 'eaff0809-0b95-49eb-97e5-fd6d5bca9980', '45e0a41c-4268-41e6-95b7-1f610de62e45', 'b4b38b98-311a-4cfc-b6c3-a6c746d21502', '8f5a683b-9823-48d1-ba79-ac5c83bdc63a', '05ff247b-73d2-4704-8a9c-ed6b1a50f78a', '47d8322b-3a30-4576-aab9-0e764dc97ec2', 'f032c280-cd20-44e0-be5f-21db66798d84', 'c4cd352f-a549-48cd-a38d-2b349c0e5473', '429d93b5-1d5b-4756-9ea3-1bc991929d74', '3b0181c7-388a-4204-9830-9aa689faea61', '177be6d7-5246-405f-b594-8eff006d141a', 'ad6ea124-8d7a-4272-90ec-471bf7469aef', '84e8b1c2-2dd1-4db1-a2ea-506361522280', '6e11bb3d-8751-4423-ac89-a4c0bd7e001c', '18b8ef69-37ec-4646-9159-27fb25608ac1', '6b272c50-5e65-4acf-a183-c544752ce526', 'ab645c40-74ef-43c6-ac2b-ce1ea45d7d63', 'b7ff184a-eef0-49cd-83c9-edc4dbcb288b', 'a3944350-b894-4c48-ad8b-ced36969e8ef', '6362a03a-e2d8-4608-828b-7219f4ceea4c', '6aaaa466-8c45-48c0-a977-dce2efe6c368', '856d766d-638b-4f71-ae8f-d583ce0de7fc', 'cd04691a-4aa4-40c7-8e51-4ece54695515', 'fd92d2fe-efc7-4f6e-a6bf-27b9d318d3b5', 'c03cacbc-e09e-4c3e-adae-d20b972956a1', '9d59c7c6-4804-4d4f-8f94-39794ea8823e', 'b7c9046a-d47a-44f3-bce1-4bdb88a19808', '5097ffbc-505c-4d72-ab5b-1e50ce64d79a', '7d04ab7d-9322-4abc-97e1-b90504f980fb', 'c248ff21-ec30-420e-a48b-9a8c5bd244d6', '3b642883-e955-47f6-99bf-e10f60c7a5b9', '484351b0-6b50-4bd3-bd4f-2c418a119699', '9e0dfb63-ce05-471e-a6ed-df2a6e085084', '2a9ef0a9-393c-4a38-8f0e-e281aa8888b6', '5e16364f-8e45-47ee-8c37-4f01637500ee', '788aac78-813f-4ebf-9911-f868d7fc1f92', '3c53ae7e-eca1-459f-a8d0-790d3638d3ba', 'b8b1a87c-0b94-4ef4-a6fe-a8ee8c61336f']
    cats = parser.getSchoolLinks()
    for i in range(0, len(cats)):
        handle = urllib.urlopen("http://www.lynda.com/"+cats[i])
        parser1 = LyndaSubParser.LyndaParser() 
        parser1.feed(handle.read())
        catid = uuids[i]
        for c in parser1.courses:
            #c.printc()
            c.uuid = uuid.uuid4()
            print c.uuid
            #c.printc()
            try:
                d = datetime.datetime.strptime(c.startdate, "%m/%d/%Y").date()
            except ValueError:
                d = datetime.date.today()
            print d
            cur.execute("INSERT INTO station_course (cid, siteid, title, subtitle, imglink, courselink, startTime, catid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                        (c.uuid, 2, c.title,c.subtitle, c.thumbnail,c.courselink, d, catid))
      


    
    conn.commit()
    cur.close()
    conn.close()
    
    