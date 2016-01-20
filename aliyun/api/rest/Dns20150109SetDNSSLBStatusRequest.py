'''
Created by auto_sdk on 2015.11.16
'''
from aliyun.api.base import RestApi
class Dns20150109SetDNSSLBStatusRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Open = None
		self.SubDomain = None

	def getapiname(self):
		return 'dns.aliyuncs.com.SetDNSSLBStatus.2015-01-09'
