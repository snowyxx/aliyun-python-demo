'''
Created by auto_sdk on 2015.06.10
'''
from aliyun.api.base import RestApi
class Dns20150109UpdateBatchDomainRecordsRequest(RestApi):
	def __init__(self,domain='dns.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.Records = None

	def getapiname(self):
		return 'dns.aliyuncs.com.UpdateBatchDomainRecords.2015-01-09'
