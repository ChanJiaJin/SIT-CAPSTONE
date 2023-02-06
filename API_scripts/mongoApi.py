import pymongo

#initiate MongoDB and asign it to a variable
mongo = pymongo.MongoClient(
  "mongodb+srv://chanjiajin:S8438106%23c@cluster0.b2zj7en.mongodb.net/?retryWrites=true&w=majority"
)


#creating new project entry
#inserting (Title), (Abbreviation) and (Code) into {projects} db
#creating a new db using (Title)
def newProject(title, abbv, code):

  if title:
    #creating new db
    newDb = mongo[title]

    #inserting collections into new db
    details = newDb.details
    information = newDb.information
    issues = newDb.issues
    flow = newDb.flow
    gantt = newDb.gantt
    docs = newDb.docs

    #inserting new project details for
    #projects list table
    insertDoc = {"title": title, "abbv": abbv, "code": code}

    details.insert_one(insertDoc)


#for grabbing all projects and their details
#for projects list table in proj_page
def fetchDetails():
  dbNames = mongo.list_database_names()
  projectsList = []

  #looping over all db
  for db in dbNames:

    #to remove db without details collection
    if db != "users" and db != "admin" and db != "local":

      #access collection
      details = mongo[db]["details"]

      #to find all info and exclude _id
      info = details.find({}, {"_id": 0})

      #to loop over the returned cursor from find()
      #and put them in a dictionary
      for i in info:
        title = i["title"]
        abbv = i["abbv"]
        code = i["code"]
        projDetails = [title, abbv, code]
        #append dictionary to array
        projectsList.append(projDetails)
    else:
      pass

  return projectsList


#for finding project db and passing all data into it
def fetchProject(abbv):
  dbNames = mongo.list_database_names()

  for db in dbNames:
    if dbNames != abbv:
      pass
    else:
      return mongo[db]


#for adding in gantt chart items
def addTask(title, task, start, end):
  db = mongo[title]

  insertDoc = {"task": task, "start": start, "end": end}

  gantt = db["gantt"]
  gantt.insert_one(insertDoc)


#to fetch all tasks to display in gantt chart
#function will be used in both proj_details and proj_settings
def fetchTasks(title):
  db = mongo[title]
  gantt = db["gantt"]
  tasks = []

  for i in gantt:
    tasks.append(i)

  return tasks


#To update database of any changes done to the gantt chart
#All data to be updated regardless of how many changes there are
#This update will work everytime the settings stack widget is changed
def updateGantt(title, update):
  db = mongo[title]
  gantt = db["gantt"]

  #to extract old values
  old = []
  for i in gantt:
    old.append(i)

  #to replace old values with new ones
  for old in old:
    for new in update:
      value = {"$set": new}
      gantt.update_one(old, value)


#for adding user into the db
def fetchMembers(title, name, dept, discipline, email):
  db = mongo[title]
  members = db["members"]

  insertDoc = {
    "name": name,
    "dept": dept,
    "discipline": discipline,
    "email": email
  }

  members.insert_one(insertDoc)


#for fetching list of users
def fetchUsers(title):
  db = mongo[title]
  members = db["members"]
