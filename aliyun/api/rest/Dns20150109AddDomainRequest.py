'''
Created by auto_sdk on 2015.11.16
'''
from aliyun.api.base import RestApi
class Dns20150109AddDomainRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Desc = None
		self.DomainName = None
		self.GroupId = None

	def getapiname(self):
		return 'dns.aliyuncs.com.AddDomain.2015-01-09'
