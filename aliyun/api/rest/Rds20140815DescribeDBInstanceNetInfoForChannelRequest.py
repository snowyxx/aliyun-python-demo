'''
Created by auto_sdk on 2015.03.25
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeDBInstanceNetInfoForChannelRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None
		self.Flag = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeDBInstanceNetInfoForChannel.2014-08-15'
