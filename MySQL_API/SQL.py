#encoding=utf8
import web
import MySQLdb,sys
reload(sys)
sys.setdefaultencoding('utf-8')


import sae.const

#sae.const.MYSQL_DB      # 数据库名
#sae.const.MYSQL_USER    # 用户名
#sae.const.MYSQL_PASS    # 密码
#sae.const.MYSQL_HOST    # 主库域名（可读写）
#sae.const.MYSQL_PORT    # 端口，类型为，请根据框架要求自行转换为int
#sae.const.MYSQL_HOST_S  # 从库域名（只读）
class sacdb_init:
	def __init__(self):
		"nothing"
	

	def getcon(self):
		try:
			connection = MySQLdb.connect(user=sae.const.MYSQL_USER,
                                         passwd=sae.const.MYSQL_PASS,
                                         host=sae.const.MYSQL_HOST,
                                         port=int(sae.const.MYSQL_PORT),
                                         db=sae.const.MYSQL_DB,
                                         charset="utf8"
                                         )
			#cursor = connection.cursor()
			return connection
		except Exception as e:return e