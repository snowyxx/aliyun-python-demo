'''
Created by auto_sdk on 2015.11.16
'''
from aliyun.api.base import RestApi
class Dns20150109UpdateDomainGroupRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.GroupId = None
		self.GroupName = None

	def getapiname(self):
		return 'dns.aliyuncs.com.UpdateDomainGroup.2015-01-09'
