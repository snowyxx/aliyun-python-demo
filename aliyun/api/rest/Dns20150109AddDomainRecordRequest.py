'''
Created by auto_sdk on 2015.09.18
'''
from aliyun.api.base import RestApi
class Dns20150109AddDomainRecordRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DomainName = None
		self.Line = None
		self.Priority = None
		self.RR = None
		self.TTL = None
		self.Type = None
		self.Value = None

	def getapiname(self):
		return 'dns.aliyuncs.com.AddDomainRecord.2015-01-09'
