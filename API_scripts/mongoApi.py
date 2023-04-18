import pymongo

#initiate MongoDB and asign it to a variable
mongo = pymongo.MongoClient(
  "mongodb+srv://chanjiajin:S8438106%23c@cluster0.b2zj7en.mongodb.net/?retryWrites=true&w=majority"
)


#for adding user into the db
def addUser(name, dept, discipline, email, password, company):
  db = mongo["user"]
  users = db["users"]

  insertDoc = {
    "name": name,
    "dept": dept,
    "company": company,
    "discipline": discipline,
    "email": email,
    "password": password
  }

  users.insert_one(insertDoc)

#for validating login details
def verUser(email, password, check, statement):
  #access users collection
  user = mongo["user"]
  users = user["users"]

  #to extract all emails registered
  items = users.find({}, {"_id":0})

  #to append the items into a mutable and recognisable array
  itemList = []
  for i in items:
    itemList.append(i)

  #to check if email exists in the list
  emailList = []
  for e in itemList:
    emailList.append(e["email"])

  if email in emailList:
    for x in itemList:
      emailCheck = x["email"]

      if emailCheck == email:
        truePass = x["password"]

        if truePass == password:
          statement = "Logging in"
          check = True
          return statement, check
        else:
          statement = "Wrong login credentials or account does not exist."
          check = False
          return statement, check
      else:
        pass
  else:
    statement = "Wrong login credentials or account does not exist."
    check = False
    return statement, check


  





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
      #returns a collection if iterable 
      #documents instead of an object
      info = details.find({}, {"_id": 0})

      #to loop over the returned cursor from find()
      #and put them in a dictionary
      #a cursor is the collection of the documents
      #returned from the cursor method find()
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
def newTask(abbv, task, start, end):
  db = mongo[abbv]

  insertDoc = {"task": task, "start": start, "end": end}

  gantt = db["gantt"]
  gantt.insert_one(insertDoc)


#to fetch all tasks to display in gantt chart
#function will be used in both proj_details and proj_settings
def fetchTasks(abbv):
  db = mongo[abbv]
  gantt = db["gantt"]
  tasks = []

  #to extract all information from the colllection
  #minus the _id
  items = gantt.find({}, {"_id":0})

  #to loop over the returned cursor,
  #append each document element into a list
  #and append the list into tasks
  for item in items:
    taskDets = []
    for i in item:
      taskDets.append(i)
      
    tasks.append(taskDets)
  
  return tasks


#To update database of any changes done to the gantt chart
#All data to be updated regardless of how many changes there are
#This update will work everytime the settings stack widget is changed
def updateGantt(abbv, update):
  db = mongo[abbv]
  gantt = db["gantt"]

  #to extract old values from the colllection
  #minus the _id
  old = []
  items = gantt.find({}, {"_id":0})
  
  for i in items:
    old.append(i)

  #to replace old values with new ones
  for old in old:
    for new in update:
      value = {"$set": new}
      gantt.update_one(old, value)


def fetchMembers(abbv):
  db = mongo[abbv]
  members = db["members"]

  projMembers = []

  membersList = members.find({},{"_id": 0})

  for member in membersList:
    for i in member:
      name = i["name"]
      dept = i["dept"]
      disc = i["discipline"]
      email = i["email"]
      membersDets = [name,dept,disc,email]
      projMembers.append(membersDets)
  
  return projMembers


#for fetching list of users
def fetchUsers(abbv):
  db = mongo[abbv]
  members = db["members"]
  users = []

  #to extract all information from the colllection
  #minus the _id
  people = members.find({}, {"_id":0})

  #to loop over the returned cursor,
  #append each document element into a list
  #and append the list into tasks
  for person in people:
    user = []
    for i in person:
      user.append(i)

    users.append(user)
  
  return users
