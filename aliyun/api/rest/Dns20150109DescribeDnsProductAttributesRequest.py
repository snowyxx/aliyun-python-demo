'''
Created by auto_sdk on 2015.12.03
'''
from aliyun.api.base import RestApi
class Dns20150109DescribeDnsProductAttributesRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.VersionCode = None

	def getapiname(self):
		return 'dns.aliyuncs.com.DescribeDnsProductAttributes.2015-01-09'
