'''
Created by auto_sdk on 2014.08.19
'''
from aliyun.api.base import RestApi
class Ecs20140526DescribeSecurityGroupsRequest(RestApi):
	def __init__(self,domain='ecs.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.PageNumber = None
		self.PageSize = None
		self.RegionId = None
		self.VpcId = None

	def getapiname(self):
		return 'ecs.aliyuncs.com.DescribeSecurityGroups.2014-05-26'
