'''
Created by auto_sdk on 2015.12.03
'''
from aliyun.api.base import RestApi
class Dns20150109ChangeDomainOfDnsProductRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.InstanceId = None
		self.NewDomain = None

	def getapiname(self):
		return 'dns.aliyuncs.com.ChangeDomainOfDnsProduct.2015-01-09'
