#encoding=utf8
import web,sae
import sys,os
import MySQLdb

reload(sys)
abspath = os.path.dirname(__file__)
abspath += '/..'
sys.path.append(abspath)
sys.setdefaultencoding('utf-8')

from MySQL_API import SQL



class Admin:
    def __init__(self):
        '''session'''
        global session
        session = web.config._session
        

    def getIndexPage(self,pageType,pageindex):
        #pageType为页面类型0表示已发布，1表示未认证，2表示已认证。
        #返回顺序为（如果是在已发布页面，则有以下排序规则，不然则单纯按时间排序）
        #1.数组前面的是：进行中的活动（肯定未认证）；
        #2.再到活动已完成，未认证的活动；
        #3.最后才是活动已完成，已认证的活动；
        #pageindex表示页数，只返回5条，如果pageindex是1，那么就返回前五条，使用mysql的limited  a,b 来实现
        #a=pageindex*5-5 b=pageindex*5
        try:
            conn =  SQL.sacdb_init().getcon()
            cursor=conn.cursor()
            #下面写sql的查询语句
            #如果是update或insert要这么来：
            #cursor.execute("""insert into xxx (字段名,字段名,.....) values (%s,%s,...)""",(变量,变量,....))
            #cursor.execute("""update xxx set  字段=%s,字段=%s,... where ....""",(变量,变量,....))
            #最后要conn.commit()提交，select就不用
            #加油
            
            cursor.execute("""""")
        except MySQLdb.Error,e:
            errorinfo =  "admingip  Mysql Error %d: %s" % (e.args[0], e.args[1])
            return errorinfo
        except Exception as e:
            return 'admingip  '+str(e)
        finally:
            cursor.close()
            conn.close()
        

    

class admin_init:
    def __init__(self):
        '''session'''
        global session
        session = web.config._session

class index(admin_init):
    def __init__(self):
        admin_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'admin':
            return '''{"success":0}'''
        pageType = web.websafe(web.input().pageType)
        ret = admin().getIndexPage(pageType,1)
        
        except Exception as e:
            return "admin_index  "+str(e)

class indexpage(admin_init):
    def __init__(self):
        admin_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'admin':
            return '''{"success":0}'''
        pageType = web.websafe(web.input().pageType)
        page = web.websafe(web.input().page)
        ret = admin().getIndexPage(pageType,page)
        
        except Exception as e:
            return "admin_indexpage  "+str(e)

class releaseAc(admin_init):
    def __init__(self):
        admin_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'admin':
            return '''{"success":0}'''
        
        
        except Exception as e:
            return "releaseAc  "+str(e)


class changeAcIndex(admin_init):
    def __init__(self):
        admin_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'admin':
            return '''{"success":0}'''
        
        
        except Exception as e:
            return "changeAcIndex  "+str(e)


class checkAc(admin_init):
    def __init__(self):
        admin_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'admin':
            return '''{"success":0}'''
        
        
        
        
        except Exception as e:
            return "checkAc  "+str(e)

class confirmAcIndex(admin_init):
    def __init__(self):
        admin_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'admin':
            return '''{"success":0}'''
        
        
        
        
        except Exception as e:
            return "confirmAcIndex  "+str(e)


class confirmAc(admin_init):
    def __init__(self):
        admin_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'admin':
            return '''{"success":0}'''
        
        
        
        
        except Exception as e:
            return "confirmAc  "+str(e)