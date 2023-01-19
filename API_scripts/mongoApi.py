import pymongo  

#initiate MongoDB and asign it to a variable
mongo = pymongo.MongoClient("mongodb+srv://chanjiajin:S8438106%23c@cluster0.b2zj7en.mongodb.net/?retryWrites=true&w=majority")

#creating new project entry
#inserting (Title), (Abbreviation) and (Code) into {projects} db
#creating a new db using (Title)
def newProject(title, abbv, code):

    if title:
        #creating new db
        newDb = mongo[title]

        #inserting collections into new db
        details = newDb.details
        issues = newDb.issues
        flow = newDb.flow
        gantt = newDb.gantt
        docs = newDb.docs

        #inserting new project details for 
        #projects list table
        insertDoc = {
            "title": title,
            "abbv": abbv,
            "code": code
        }
        
        details.insert_one(insertDoc)


#for grabbing all projects and their details 
#for projects list table in proj_page
def fetchDetails():
    dbNames = mongo.list_database_names()
    projectsList = []

    for db in dbNames:
        if db != "users":
            collections = mongo[db]
            details = collections.details
            projectsList.append(details)
        else:
            pass
    
    return projectsList

#for finding project db and passing all data into it
def fetchProject(abbv):
    dbNames  =mongo.list_database_names()

    for db in dbNames:
        if dbNames != abbv:
            pass
        else:
            return mongo[db]


    