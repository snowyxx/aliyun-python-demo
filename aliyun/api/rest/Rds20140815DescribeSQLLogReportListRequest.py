'''
Created by auto_sdk on 2015.08.07
'''
from aliyun.api.base import RestApi
class Rds20140815DescribeSQLLogReportListRequest(RestApi):
	def __init__(self,domain='rds.aliyuncs.com',port=80):
		RestApi.__init__(self,domain, port)
		self.DBInstanceId = None
		self.EndTime = None
		self.Page = None
		self.PageNumbers = None
		self.StartTime = None

	def getapiname(self):
		return 'rds.aliyuncs.com.DescribeSQLLogReportList.2014-08-15'
