# -*- encoding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 9
_modified_time = 1380692472.153455
_enable_loop = True
_template_filename = 'templates/attendance.mako.save3'
_template_uri = 'templates/attendance.mako.save3'
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
        __M_writer(u' : </h1>\n<br>\n\n<table width="500" border="0">\n')
        # SOURCE LINE 14
        for row in guests:
            # SOURCE LINE 15
            __M_writer(u'        ')
            __M_writer(unicode(makerow(row)))
            __M_writer(u'\n')
        # SOURCE LINE 17
        __M_writer(u'</table>\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_makerow(context,row):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n    ')
        # SOURCE LINE 20
        fname = row['fname'] 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 21
        lname = row['lname'] 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 22
        email = row['email'] 
        
        __M_writer(u'\n    ')
        # SOURCE LINE 23
        phone = row['phonenumber'] 
        
        __M_writer(u'\n        <td>')
        # SOURCE LINE 24
        __M_writer(unicode(fname))
        __M_writer(u'</td>')
        # SOURCE LINE 25
        __M_writer(u'        <td>')
        __M_writer(unicode(lname))
        __M_writer(u'</td>')
        # SOURCE LINE 26
        __M_writer(u'        <td>')
        __M_writer(unicode(email))
        __M_writer(u'</td>')
        # SOURCE LINE 27
        __M_writer(u'        <td>')
        __M_writer(unicode(phone))
        __M_writer(u'</td>')
        # SOURCE LINE 28
        __M_writer(u'    </tr>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


