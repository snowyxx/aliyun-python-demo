'''
Created by auto_sdk on 2015.05.29
'''
from aliyun.api.base import RestApi
class Mts20140618CancelJobRequest(RestApi):
	def __init__(self,domain='mts.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.JobId = None

	def getapiname(self):
		return 'mts.aliyuncs.com.CancelJob.2014-06-18'
