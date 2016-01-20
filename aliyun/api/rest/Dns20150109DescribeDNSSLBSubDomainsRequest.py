'''
Created by auto_sdk on 2015.11.16
'''
from aliyun.api.base import RestApi
class Dns20150109DescribeDNSSLBSubDomainsRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DomainName = None
		self.PageNumber = None
		self.PageSize = None

	def getapiname(self):
		return 'dns.aliyuncs.com.DescribeDNSSLBSubDomains.2015-01-09'
