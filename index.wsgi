#encoding=utf8
import os,sys

import sae
import web
app_root = os.path.dirname(__file__)
import os 
from login import login
from logout import logout
home='' 
os.environ["SCRIPT_NAME"] = home 
os.environ["REAL_SCRIPT_NAME"] = home
web.config.debug = True
#session settings
web.config.session_parameters['cookie_name'] = 'Mr.E_session_id'
web.config.session_parameters['cookie_domain'] = None
web.config.session_parameters['timeout'] = 0.5 * 60 * 60 * 3
web.config.session_parameters['ignore_expiry'] = True
web.config.session_parameters['ignore_change_ip'] = False
web.config.session_parameters['secret_key'] = 'HiTxqFuKsckU7sg0A0J'
web.config.session_parameters['expired_message'] = 'Session expired'

urls = (
    '/', 'Hello',
    '/(.*.html)', 'StaticFile',
    '/login',login.login,
    '/logout',logout.logout
    #'/register',register.regiter


    #'/stuIndex',stu.index
    #'/stuIndexPage',stu.indexpage
    #'/stuParticipate',stu.participate
    #'/stuHome',stu.home
    #'/stuHomePage',stu.homepage

    #'/adminIndex',admin.index
    #'/adminIndexPage',admin.indexpage
    #'/releaseAc',admin.releaseAc
    #'/changeAcIndex',admin.changeAcIndex
    #'/changeAc',admin.changeAc
    #'/checkAc',admin.checkAc
    #'/confirmAcIndex',admin.confirmAcIndex
    #'/confirmAc',admin.confirmAc
)
class Hello:
    def GET(self):
        return app_root+"askdj9asd990huj"

class StaticFile:
    def GET(self, file):
        web.seeother('/static/'+file); 


app = web.application(urls, globals(), autoreload = False)
db = web.database(dbn='mysql', host=sae.const.MYSQL_HOST,port=int(sae.const.MYSQL_PORT),user=sae.const.MYSQL_USER, pw=sae.const.MYSQL_PASS, db=sae.const.MYSQL_DB) 
store = web.session.DBStore(db, 'sessions') 

session = web.session.Session(app, store,
    initializer={
            'ID'        :   '',
            'login'     :   False,
            'username'  :   '',
            'usertype'  :   '',
            'ehour'     :   0
        }
    ) 
web.config._session = session

app = app.wsgifunc()
application = sae.create_wsgi_app(app)
