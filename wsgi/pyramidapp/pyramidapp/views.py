__author__ = 'irenebreck'

import pymongo
import sys
import os
# import json
# import bson

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.response import FileResponse

from pyramid_mailer.mailer import Mailer
from pyramid_mailer.message import Message
from pyramid_mailer.message import Attachment

# from bson import json_util

from bson.json_util import dumps
from mako.template import Template

#connnecto to the db on standard port
#connection = pymongo.MongoClient("mongodb://admin:manager@ds043378.mongolab.com:43378/velur")
#db         = connection.velur                # attach to db

#production database
connection = pymongo.MongoClient("mongodb://admin:manager@ds049288.mongolab.com:49288/cpserver")
db = connection.cpserver

profile_col = db.userprofile                 # specify the colllection
event_col = db.events

#current_event = 'Feb-22-2014-Saturday'
#current_event = 'Jun-02-2014-Saturday'

from pyramid.view import view_config

@view_config(route_name='UserProfile')
def UserProfileFormView(request):
    here = os.path.dirname(__file__)
    profile = os.path.join(here, 'static', 'UserProfile.html')
    return (FileResponse(profile))

@view_config(route_name='AddEvent')
def AddEventFormView(request):
    here = os.path.dirname(__file__)
    profile = os.path.join(here, 'static', 'AddEvent.html')
    return (FileResponse(profile))

@view_config(route_name='InfoDoc')
def getInfoDoc(request):
    here    = os.path.dirname(__file__)
    params  = request.params
    doc     = params['doc']
    docfile = os.path.join(here, 'static', doc)
    return (FileResponse(docfile))


@view_config(route_name='AttendEvent') #, renderer="./templates/attendance3.mako")
def getAttendance(request):
    param = request.params
    event_choice = param.get('event_choice')

    all_leads = profile_col.find({'events': event_choice},
                         {'_id': 0, 'fname': 1, 'lname': 1, 'email': 1, 'phonenumber': 1,
                          'agent_q':1, 'seminar_q':1, 'land_q':1, 'when':1, 'where':1})

    # all_leads   = col.find({})
    # data  = all_leads[:]
    # json_string = json.dumps(data, default=json_util.default)



    # data_string = [json.dumps(result, default=json_util.default, separators=(',', ':')) for result in all_leads]

    # this is helper function from bson

    #json_string = dumps(all_leads)

    #attendance_template = cptemplate.get_template('attendance.mako')
    #return attendance_template.render(data={"name":1})

    test_string = [lead for lead in all_leads]

    here = os.path.dirname(__file__)
    templatefile = os.path.join(here, 'templates', 'attendance.mako.save3')
    module_dir = os.path.join(here,'templates', 'mako_modules')

    mytemplate = Template(filename=templatefile, module_directory=module_dir)

    return(Response(mytemplate.render(guests=test_string, date=event_choice), content_type='text/html' ))

    #return({'guests': test_string})

    # return(Response(json_string, content_type="application/json"))

    #guest_list = [dict(guest) for guest in all_leads]
    #return {'guests': guest_list}

    #return {'rows': json_string}

@view_config(route_name='GetEvents') #, renderer="./templates/attendance3.mako")
def getEventData(request):
    param = request.params
    event_choice = param.get('event_choice')

    all_events = event_col.find({})
    # this is helper function from bson
    json_string = dumps(all_events)

    return(Response(json_string, content_type="application/json"))


@view_config(route_name='SaveEvent', renderer="templates/confirmed_save_event.pt")
def SaveEventDB(request):
   params = request.params
   eventname = params.get('eventname')
   event_date = params.get('event_date')
   event_discription = params.get('event_discription')

   # save to the DB
   event_col.insert({'eventname': eventname, 
                     'event_date':event_date, 
                     'event_discription':event_discription})

   # send email to notify the admin - time to reload the app
   return (request.params)
   

@view_config(route_name='SubmitUserProfile', renderer="templates/confirmed_data.pt")
def SubmitUserProfileView(request):
    params = request.params

    firstname = params.get('firstname')
    lastname = params.get('lastname')
    #      password  = params.get('password')
    email = params.get('email')
    phonenumber = params.get('phonenumber')

    # need to make sure if key/data exist. None (null) will be returned if not existed

    agent_q = params.get('agent_q')
    seminar_q = params.get('seminar_q')
    land_q = params.get('land_q')
    when = params.get('when')
    where = params.get('where')
    events = params.getall("event_choice")

    profile_col.insert({'fname': firstname,
                'lname': lastname,
                #                   'password': password,
                'email': email,
                'phonenumber': phonenumber,
                'events': events,
                'agent_q': agent_q,
                'seminar_q': seminar_q,
                'land_q': land_q,
                'when': when,
                'where': where
    })

    send_mail(request)
    # return Response('ok %(name)s!' % request.matchdict)
    return (request.params)


def send_mail(request):
    mailer = Mailer(host='smtp.gmail.com',
                    port=587, #???
                    username='celiapan.noreply@gmail.com',
                    password='1234test',
                    tls=True)

    if request.params.get('email') is not None:
        email = request.params['email']
    else:
        email = "the email does not exist"

    params = request.params
    event_choice = params.getall('event_choice')

    #current event is on Saturday
    event_time = " Meeting Time: " + event_choice[0]
    
    # if event_choice[0] == current_event:
    #    event_time += ", 01:00 PM - 05:00PM"
    # else:
    #    event_time += ", 10:00 AM - 02:00PM"

    send_topic = 'Welcome from Celia Pan'
    send_er = 'celiapan.noreply@gmail.com'
    send_to = [email]
    send_this = "Hi " + params.get('firstname')+ ',' + "\n     Thank you for signing up for the seminar.  \
The seminar will take place at:\n \
145 South Main Street Suite #145 \n \
Milpitas, CA 95035 \n"  + event_time + '\n\n' + \
"Please review the following documents: \n \
http://cpserver-velur.rhcloud.com/InfoDoc?doc=velur1.pdf \n \
http://cpserver-velur.rhcloud.com/InfoDoc?doc=velur2.pdf \n \
Please visit us at: www.celiapan-velur.com for more landbanking information."

    message = Message(subject=send_topic,
                      sender=send_er,
                      recipients=send_to,
                      body=send_this)

    # send attchments
    """
    here = os.path.dirname(__file__)
    att1 = os.path.join(here, 'static','velur1.pdf')
    attachment = Attachment(att1, "image/jpg",
                        open(att1, "rb"))
    message.attach(attachment)

    here = os.path.dirname(__file__)
    att2 = os.path.join(here, 'static','velur2.pdf')
    attachment = Attachment(att2, "image/jpg",
                        open(att2, "rb"))
    message.attach(attachment)
    """


    # mailer.send_immediately(message, fail_silently=False)
    mailer.send(message)
    return Response(email)


def view_root(context, request):
    return {'items': list(context), 'project': 'pyramidapp'}


def view_model(context, request):
    return {'item': context, 'project': 'pyramidapp'}
