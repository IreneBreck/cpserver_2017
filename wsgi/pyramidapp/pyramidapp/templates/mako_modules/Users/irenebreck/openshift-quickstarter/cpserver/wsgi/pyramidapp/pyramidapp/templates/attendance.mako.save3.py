# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1392799493.310001
_enable_loop = True
_template_filename = '/Users/irenebreck/openshift-quickstarter/cpserver/wsgi/pyramidapp/pyramidapp/templates/attendance.mako.save3'
_template_uri = '/Users/irenebreck/openshift-quickstarter/cpserver/wsgi/pyramidapp/pyramidapp/templates/attendance.mako.save3'
_source_encoding = 'ascii'
_exports = ['makerow']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        date = context.get('date', UNDEFINED)
        guests = context.get('guests', UNDEFINED)
        def makerow(row):
            return render_makerow(context._locals(__M_locals),row)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!doctype html>\n<html>\n\n<head>\n<title>Attendance</title>\n</head>\n\n<body>\n\n<h1>Sign up for ')
        # SOURCE LINE 10
        __M_writer(unicode(date))
        __M_writer(u' : </h1>\n<br>\n\n<table width="500" border="1">\n    <tr>\n        <td>fname</td>')
        # SOURCE LINE 16
        __M_writer(u'        <td>lname</td>')
        # SOURCE LINE 17
        __M_writer(u'        <td>email</td>')
        # SOURCE LINE 18
        __M_writer(u'        <td>phone</td>')
        # SOURCE LINE 19
        __M_writer(u'        <td>are you an agent?</td>')
        # SOURCE LINE 20
        __M_writer(u'        <td>attend our seminar?</td>')
        # SOURCE LINE 21
        __M_writer(u'        <td>invest on land</td>')
        # SOURCE LINE 22
        __M_writer(u'        <td>when</td>')
        # SOURCE LINE 23
        __M_writer(u'        <td>where</td>\n    </tr>\n')
        # SOURCE LINE 25
        for row in guests:
            # SOURCE LINE 26
            __M_writer(u'        ')
            __M_writer(unicode(makerow(row)))
            __M_writer(u'\n')
        # SOURCE LINE 28
        __M_writer(u'</table>\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_makerow(context,row):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\n  <tr>\n    ')
        # SOURCE LINE 32
        fname = row['fname'] 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 33
        lname = row['lname'] 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 34
        email = row['email'] 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 35
        phone = row['phonenumber']   
        
        __M_writer(u'\n    ')
        # SOURCE LINE 36
        agent_q   = row['agent_q']   
        
        __M_writer(u'\n    ')
        # SOURCE LINE 37
        seminar_q = row['seminar_q'] 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 38
        land_q    = row['land_q']    
        
        __M_writer(u'\n    ')
        # SOURCE LINE 39
        when      = row['when']      
        
        __M_writer(u'\n    ')
        # SOURCE LINE 40
        where     = row['where']     
        
        __M_writer(u'\n        <td>')
        # SOURCE LINE 41
        __M_writer(unicode(fname))
        __M_writer(u'</td>')
        # SOURCE LINE 42
        __M_writer(u'        <td>')
        __M_writer(unicode(lname))
        __M_writer(u'</td>')
        # SOURCE LINE 43
        __M_writer(u'        <td>')
        __M_writer(unicode(email))
        __M_writer(u'</td>')
        # SOURCE LINE 44
        __M_writer(u'        <td>')
        __M_writer(unicode(phone))
        __M_writer(u'</td>')
        # SOURCE LINE 45
        __M_writer(u'        <td>')
        __M_writer(unicode(agent_q))
        __M_writer(u'</td>')
        # SOURCE LINE 46
        __M_writer(u'        <td>')
        __M_writer(unicode(seminar_q))
        __M_writer(u'</td>')
        # SOURCE LINE 47
        __M_writer(u'        <td>')
        __M_writer(unicode(land_q))
        __M_writer(u'</td>')
        # SOURCE LINE 48
        __M_writer(u'        <td>')
        __M_writer(unicode(when))
        __M_writer(u'</td>')
        # SOURCE LINE 49
        __M_writer(u'        <td>')
        __M_writer(unicode(where))
        __M_writer(u'</td>\n  </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


