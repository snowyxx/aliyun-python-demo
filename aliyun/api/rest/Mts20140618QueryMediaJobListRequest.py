'''
Created by auto_sdk on 2015.05.29
'''
from aliyun.api.base import RestApi
class Mts20140618QueryMediaJobListRequest(RestApi):
	def __init__(self,domain='mts.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.MediaJobIds = None

	def getapiname(self):
		return 'mts.aliyuncs.com.QueryMediaJobList.2014-06-18'
