'''
Created by auto_sdk on 2015.04.03
'''
from aliyun.api.base import RestApi
class Mkvstore20150301DescribeMonitorItemsRequest(RestApi):
	def __init__(self,domain='m-kvstore.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'm-kvstore.aliyuncs.com.DescribeMonitorItems.2015-03-01'
