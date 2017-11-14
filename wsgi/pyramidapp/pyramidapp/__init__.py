import os

from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from pyramidapp.models import appmaker

def main(global_config, **settings):
    """ This function returns a WSGI application.
    """
    # OpenShift Settings
    
    """ if os.environ.get('OPENSHIFT_DB_URL'):
          settings['sqlalchemy.url'] = \
                '%(OPENSHIFT_DB_URL)s%(OPENSHIFT_APP_NAME)s' % os.environ
    #engine = engine_from_config(settings, 'sqlalchemy.')
    #get_root = appmaker(engine)
    #config = Configurator(settings=settings, root_factory=get_root)
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'pyramidapp:static')

    """
    config.add_view('pyramidapp.views.view_root',
                    context='pyramidapp.models.MyApp',
                    renderer="templates/root.pt")
    config.add_view('pyramidapp.views.view_model',
                    context='pyramidapp.models.MyModel',
                    renderer="templates/model.pt")
    """

    config.add_route('UserProfile', '/UserProfile/{name}')
    config.add_route('SubmitUserProfile', '/SubmitUserProfile/{name}')
    config.add_route('AttendEvent', '/AttendEvent')
    config.add_route('AddEvent','/AddEvent')
    config.add_route('GetEvents','/GetEvents/{name}')
    config.add_route('SaveEvent','/SaveEvent/{name}')
    config.add_route('InfoDoc', '/InfoDoc')

    config.scan()


    return config.make_wsgi_app()


