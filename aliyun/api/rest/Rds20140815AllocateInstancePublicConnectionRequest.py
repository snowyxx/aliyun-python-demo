'''
Created by auto_sdk on 2015.08.04
'''
from aliyun.api.base import RestApi
class Rds20140815AllocateInstancePublicConnectionRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.ConnectionStringPrefix = None
		self.DBInstanceId = None
		self.Port = None

	def getapiname(self):
		return 'rds.aliyuncs.com.AllocateInstancePublicConnection.2014-08-15'
