'''
Created by auto_sdk on 2015.11.10
'''
from aliyun.api.base import RestApi
class Rds20140815DeleteDBInstanceRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DeleteDBInstance.2014-08-15'