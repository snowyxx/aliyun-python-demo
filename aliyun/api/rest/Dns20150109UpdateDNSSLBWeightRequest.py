'''
Created by auto_sdk on 2015.11.16
'''
from aliyun.api.base import RestApi
class Dns20150109UpdateDNSSLBWeightRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.RecordId = None
		self.Weight = None

	def getapiname(self):
		return 'dns.aliyuncs.com.UpdateDNSSLBWeight.2015-01-09'
