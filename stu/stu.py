#encoding=utf8
import web,sae
import sys,os
import MySQLdb
import json

reload(sys)
abspath = os.path.dirname(__file__)
abspath += '/..'
sys.path.append(abspath)
sys.setdefaultencoding('utf-8')

from MySQL_API import SQL



class Stu:
    def __init__(self):
        '''session'''
        global session
        session = web.config._session
        

    def getIndexPage(self,pageType,pageindex):
        #pageType为页面类型0表示首页，1表示未开始，2表示进行中，3表示热门,热门就按照报名人数来就好了
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
        except MySQLdb.Error,e:
            errorinfo =  "stugip  Mysql Error %d: %s" % (e.args[0], e.args[1])
            return errorinfo
        except Exception as e:
            return 'stugip  '+str(e)
        finally:
            cursor.close()
            conn.close()
        
class stu_init:
    def __init__(self):
        '''session'''
        global session
        session = web.config._session

        
        
#stuName：学生姓名；
##pageCnt：活动拥有的页码数量；
##list[i][‘AcId’]:活动i的id；
##list[i][‘imgSrc’]:活动i的图片的源地址；
##list[i][‘dateTime’]:活动i的进行时间；
##list[i][‘AcName’]：活动i的名称；
##list[i][‘AcOrg’]:活动i的举办单位；
##list[i][‘AcPlace’]：活动i的举办地点；
##list[i][‘AcNum’]：活动i的可容纳报名人数；
##list[i][‘AcNumRest’]:活动i的剩余空位；
##list[i][‘AcHour’]:活动i的公益时长；
class index(stu_init):
    def __init__(self):
        stu_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'student':
            return '''{"success":0}'''
        pageType = web.websafe(web.input().pageType)
        #ret = Stu().getIndexPage(pageType,1)
        if pageType == 0:                                           #0表示平常的排序
            try:
                conn =  SQL.sacdb_init().getcon()
                cursor=conn.cursor()
                sql = "SELECT * FROM activitylist WHERE state=%s ORDER BY posttime DSC"
                param=(0)
                cursor.execute(sql, param)
                data = cursor.fetchall()
                postdata = {"sucess": 1, "stuName": session.username, "pageCnt": (len(data) + 4) / 5, "list": []}
                for i in range(0, postdata["pageCnt"]):
                    postdata["list"].append({"AcId": data[i]["ID"], "imgSrc":data[i]["filepath"], "dateTime": data[i]["starttime"], "AcName": data[i]["name"], "AcOrg": data[i]["authorname"], "AcPlace": data[i]["location"], "AcNum": data[i]["maxnum"], "AcNumRest": data[i]["maxnum"] - data[i]["paticipatenum"], "AcHour": data[i]["ehour"]})

                return str(postdata);
            except MySQLdb.Error,e:
                errorinfo =  "index  Mysql Error %d: %s" % (e.args[0], e.args[1])
                return errorinfo
            except Exception as e:
                return 'index  '+str(e)
            finally:
                cursor.close()
                conn.close()
        elif pageType == 1:                                              #1表示未开始的活动
            try:
                conn =  SQL.sacdb_init().getcon()
                cursor=conn.cursor()
                sql = "SELECT * FROM activitylist WHERE state=%s and statetime > %s ORDER BY posttime DSC LIMIT 0, 5"
                param = (0, datetime.datetime.now())
                cursor.execute(sql, param)
                data = cursor.fetchall()
                postdata = {"sucess": 1, "stuName": session.username, "pageCnt": (len(data) + 4) / 5, "list": []}
                for i in range(0, postdata["pageCnt"]):
                    postdata["list"].append({"AcId": data[i]["ID"], "imgSrc":data[i]["filepath"], "dateTime": data[i]["starttime"], "AcName": data[i]["name"], "AcOrg": data[i]["authorname"], "AcPlace": data[i]["location"], "AcNum": data[i]["maxnum"], "AcNumRest": data[i]["maxnum"] - data[i]["paticipatenum"], "AcHour": data[i]["ehour"]})

                return str(postdata);
            except MySQLdb.Error,e:
                errorinfo =  "index  Mysql Error %d: %s" % (e.args[0], e.args[1])
                return errorinfo
            except Exception as e:
                return 'index  '+str(e)
            finally:
                cursor.close()
                conn.close()
        elif pageType == 2:                         #当pageType为3的时候代表至今尚未结束的活动
            try:
                conn =  SQL.sacdb_init().getcon()
                cursor=conn.cursor()
                sql = "SELECT * FROM activitylist WHERE state=%s and statetime < %s ORDER BY posttime DSC LIMIT 0, 5"
                param = (0, datetime.datetime.now())
                cursor.execute(sql, param)
                data = cursor.fetchall()
                postdata = {"sucess": 1, "stuName": session.username, "pageCnt": (len(data) + 4) / 5, "list": []}
                for i in range(0, postdata["pageCnt"]):
                    postdata["list"].append({"AcId": data[i]["ID"], "imgSrc":data[i]["filepath"], "dateTime": data[i]["starttime"], "AcName": data[i]["name"], "AcOrg": data[i]["authorname"], "AcPlace": data[i]["location"], "AcNum": data[i]["maxnum"], "AcNumRest": data[i]["maxnum"] - data[i]["paticipatenum"], "AcHour": data[i]["ehour"]})

                return str(postdata);
            except MySQLdb.Error,e:
                errorinfo =  "index  Mysql Error %d: %s" % (e.args[0], e.args[1])
                return errorinfo
            except Exception as e:
                return 'index  '+str(e)
            finally:
                cursor.close()
                conn.close()
        elif pageType == 3:                     #当pageType为3的时候代表至今热门的活动
            try:
                conn =  SQL.sacdb_init().getcon()
                cursor=conn.cursor()
                sql = "SELECT * FROM activitylist WHERE state=%s ORDER BY posttime DSC, paticipatenum DSC LIMIT 0, 5"
                param = (0)
                cursor.execute(sql, param)
                data = cursor.fetchall()
                postdata = {"sucess": 1, "stuName": session.username, "pageCnt": (len(data) + 4) / 5, "list": []}
                for i in range(0, postdata["pageCnt"]):
                    postdata["list"].append({"AcId": data[i]["ID"], "imgSrc":data[i]["filepath"], "dateTime": data[i]["starttime"], "AcName": data[i]["name"], "AcOrg": data[i]["authorname"], "AcPlace": data[i]["location"], "AcNum": data[i]["maxnum"], "AcNumRest": data[i]["maxnum"] - data[i]["paticipatenum"], "AcHour": data[i]["ehour"]})

                return str(postdata);
            except MySQLdb.Error,e:
                errorinfo =  "index  Mysql Error %d: %s" % (e.args[0], e.args[1])
                return errorinfo
            except Exception as e:
                return 'index  '+str(e)
            finally:
                cursor.close()
                conn.close()
#返回与index一样，只是代表不同的页面的东西
#
class indexpage(stu_init):
    def __init__(self):
        stu_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'student':
            return '''{"success":0}'''
        pageType = web.websafe(web.input().pageType)
        page = web.websafe(web.input().page)
        #ret = Stu().getIndexPage(pageType,page)
        
        if pageType == 0:
            try:
                conn =  SQL.sacdb_init().getcon()
                cursor=conn.cursor()
                sql = "SELECT * FROM activitylist WHERE state=%s ORDER BY posttime DSC LIMIT %s, %s"
                param=(0, page * 5 - 5, page * 5)
                cursor.execute(sql, param)
                data = cursor.fetchall()
                postdata = {"sucess": 1 , "list": []}
                for i in range(0, postdata["pageCnt"]):
                    postdata["list"].append({"AcId": data[i]["ID"], "imgSrc":data[i]["filepath"], "dateTime": data[i]["starttime"], "AcName": data[i]["name"], "AcOrg": data[i]["authorname"], "AcPlace": data[i]["location"], "AcNum": data[i]["maxnum"], "AcNumRest": data[i]["maxnum"] - data[i]["paticipatenum"], "AcHour": data[i]["ehour"]})

                return str(postdata);
            except MySQLdb.Error,e:
                errorinfo =  "indexpage  Mysql Error %d: %s" % (e.args[0], e.args[1])
                return errorinfo
            except Exception as e:
                return 'indexpage  '+str(e)
            finally:
                cursor.close()
                conn.close()
        elif pageType == 1:#1表示未开始的活动
            try:
                conn =  SQL.sacdb_init().getcon()
                cursor=conn.cursor()
                sql = "SELECT * FROM activitylist WHERE state=%s and statetime > %s ORDER BY posttime DSC LIMIT %s, %s"
                param = (0, datetime.datetime.now(), page * 5 - 5, page * 5)
                cursor.execute(sql, param)
                data = cursor.fetchall()
                postdata = {"sucess": 1 , "list": []}
                for i in range(0, postdata["pageCnt"]):
                    postdata["list"].append({"AcId": data[i]["ID"], "imgSrc":data[i]["filepath"], "dateTime": data[i]["starttime"], "AcName": data[i]["name"], "AcOrg": data[i]["authorname"], "AcPlace": data[i]["location"], "AcNum": data[i]["maxnum"], "AcNumRest": data[i]["maxnum"] - data[i]["paticipatenum"], "AcHour": data[i]["ehour"]})

                return str(postdata);
            except MySQLdb.Error,e:
                errorinfo =  "indexpage  Mysql Error %d: %s" % (e.args[0], e.args[1])
                return errorinfo
            except Exception as e:
                return 'indexpage  '+str(e)
            finally:
                cursor.close()
                conn.close()
        elif pageType == 2:
            try:
                conn =  SQL.sacdb_init().getcon()
                cursor=conn.cursor()
                sql = "SELECT * FROM activitylist WHERE state=%s and statetime < %s ORDER BY posttime DSC LIMIT %s, %s"
                param = (0, datetime.datetime.now(), page * 5 - 5, page * 5)
                cursor.execute(sql, param)
                data = cursor.fetchall()
                postdata = {"sucess": 1 , "list": []}
                for i in range(0, postdata["pageCnt"]):
                    postdata["list"].append({"AcId": data[i]["ID"], "imgSrc":data[i]["filepath"], "dateTime": data[i]["starttime"], "AcName": data[i]["name"], "AcOrg": data[i]["authorname"], "AcPlace": data[i]["location"], "AcNum": data[i]["maxnum"], "AcNumRest": data[i]["maxnum"] - data[i]["paticipatenum"], "AcHour": data[i]["ehour"]})

                return str(postdata);
            except MySQLdb.Error,e:
                errorinfo =  "indexpage  Mysql Error %d: %s" % (e.args[0], e.args[1])
                return errorinfo
            except Exception as e:
                return 'indexpage  '+str(e)
            finally:
                cursor.close()
                conn.close()
        elif pageType == 3:
            try:
                conn =  SQL.sacdb_init().getcon()
                cursor=conn.cursor()
                sql = "SELECT * FROM activitylist WHERE state=%s ORDER BY posttime DSC, paticipatenum DSC LIMIT %s, %s"
                param = (0, page * 5 - 5, page * 5)
                cursor.execute(sql, param)
                data = cursor.fetchall()
                postdata = {"sucess": 1 , "list": []}
                for i in range(0, postdata["pageCnt"]):
                    postdata["list"].append({"AcId": data[i]["ID"], "imgSrc":data[i]["filepath"], "dateTime": data[i]["starttime"], "AcName": data[i]["name"], "AcOrg": data[i]["authorname"], "AcPlace": data[i]["location"], "AcNum": data[i]["maxnum"], "AcNumRest": data[i]["maxnum"] - data[i]["paticipatenum"], "AcHour": data[i]["ehour"]})

                return str(postdata);
            except MySQLdb.Error,e:
                errorinfo =  "indexpage  Mysql Error %d: %s" % (e.args[0], e.args[1])
                return errorinfo
            except Exception as e:
                return 'indexpage  '+str(e)
            finally:
                cursor.close()
                conn.close()

#返回success=1表示成功，否则失败
class participate(stu_init):
    def __init__(self):
        stu_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'student':
            return '''{"success":0}'''
        Acid = web.websafe(web.input().Acid)
        try:
            conn =  SQL.sacdb_init().getcon()
            cursor=conn.cursor()
            sql = "insert into participate(StudentID, ActivityID, AuthenticationStatus) values(%s,%s,%s)"
            param=(session.ID, Acid, 0)
            cursor.execute(sql, param)
            data = cursor.fetchall()
            return '''{"success":1}'''
        except MySQLdb.Error,e:
            errorinfo =  "stu_participate  Mysql Error %d: %s" % (e.args[0], e.args[1])
            return errorinfo
        except Exception as e:
            return 'stu_participate  '+str(e)
        finally:
            cursor.close()
            conn.close()
        
    


class home(stu_init):
    def __init__(self):
        stu_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'student':
            return '''{"success":0}'''
        
        try:
            conn =  SQL.sacdb_init().getcon()
            cursor=conn.cursor()
            sql = "SELECT * FROM participate WHERE StudentID=%s ORDER BY participatetime DSC"
            
            cursor.execute(sql, param)
            data = cursor.fetchall()
            
            postdata = {"sucess": 1,  "pageCnt": (len(data) + 4) / 5, "list": []}
            for i in range(0, 5):
                sql = "SELECT * FROM activitylist WHERE ID=%s"
                param=(data[i]["StudentID"])
                cursor.execute(sql, param)
                actdata = cursor.fetchone()
                postdata["list"].append({"AcId": data[i]["StudentID"], "AcComState": actdata["status"], "AcAuthenState": data[i]["AuthenticationStatus"], "imgSrc":actdata["filepath"], "dateTime": actdata["starttime"], "AcName": actdata["name"], "AcOrg": actdata["authorname"], "AcPlace": actdata["location"], "AcNum": actdata["maxnum"], "AcNumRest": actdata["maxnum"] - actdata["paticipatenum"], "AcHour": actdata["ehour"]})
        return str(postdata);
        
        except MySQLdb.Error,e:
            errorinfo =  "stuhome  Mysql Error %d: %s" % (e.args[0], e.args[1])
            return errorinfo
        except Exception as e:
            return 'stuhome  '+str(e)
        finally:
            cursor.close()
            conn.close()


class homepage(stu_init):
    def __init__(self):
        stu_init.__init__(self)
       
    def POST(self):
        if session.login == False or session.usertype != 'student':
            return '''{"success":0}'''
        
        page = web.websafe(web.input().page)
        
        try:
            conn =  SQL.sacdb_init().getcon()
            cursor=conn.cursor()
            sql = "SELECT * FROM participate WHERE StudentID=%s ORDER BY participatetime DSC LIMIT page*5-5, page*5"
            
            cursor.execute(sql, param)
            data = cursor.fetchall()
            
            postdata = {"sucess": 1, "list": []}
            for i in range(0, 5):
                sql = "SELECT * FROM activitylist WHERE ID=%s"
                param=(data[i]["StudentID"])
                cursor.execute(sql, param)
                actdata = cursor.fetchone()
                postdata["list"].append({"AcId": data[i]["StudentID"], "AcComState": actdata["status"], "AcAuthenState": data[i]["AuthenticationStatus"], "imgSrc":actdata["filepath"], "dateTime": actdata["starttime"], "AcName": actdata["name"], "AcOrg": actdata["authorname"], "AcPlace": actdata["location"], "AcNum": actdata["maxnum"], "AcNumRest": actdata["maxnum"] - actdata["paticipatenum"], "AcHour": actdata["ehour"]})
        return str(postdata);
        
        except MySQLdb.Error,e:
            errorinfo =  "stu_homepage  Mysql Error %d: %s" % (e.args[0], e.args[1])
            return errorinfo
        except Exception as e:
            return 'stu_homepage  '+str(e)
        finally:
            cursor.close()
            conn.close()
    