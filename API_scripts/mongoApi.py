import pymongo

#initiate MongoDB and asign it to a variable
mongo = pymongo.MongoClient("mongodb+srv://chanjiajin:S8438106%23c@cluster0.b2zj7en.mongodb.net/?retryWrites=true&w=majority")

#Creating new project database and colections
def newProject(title, abbv, code, creator):
    db = mongo['{}'.format(title)]

    #creating details collection and adding in details documents
    details = db.details
    proj_details = [{
        "title": title,
        "abbreviation": abbv,
        "code": code
    }]
    details.insert_many(proj_details)

    #creating members collection and putting in proj admin
    members = db.members
    members.insert_one({
        "name": "{}".format(creator.name),
        "roles": ["admin"],
        "dept": "{}".format(creator.dept),
        "email": "{}".format(creator.email)
    })

    #creating other collections
    issues = db.issues
    flow = db.flow
    gantt = db.gantt
    docs = db.docs

    