'''
Created by auto_sdk on 2015.11.16
'''
from aliyun.api.base import RestApi
class Dns20150109ChangeDomainGroupRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DomainName = None
		self.GroupId = None

	def getapiname(self):
		return 'dns.aliyuncs.com.ChangeDomainGroup.2015-01-09'
