'''
Created by auto_sdk on 2014.10.21
'''
from aliyun.api.base import RestApi
class Rds20130528RestoreDBInstanceRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.BackupId = None
		self.DBInstanceId = None

	def getapiname(self):
		return 'rds.aliyuncs.com.RestoreDBInstance.2013-05-28'
