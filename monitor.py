#!/usr/bin/env python
# coding: utf-8

import aliyun.api

aliyun.setDefaultAppInfo('N********q', 'P*******H')


def getDomainList():
    domainList = []
    domains = aliyun.api.rest.Dns20150109DescribeDomainsRequest()
    domains_dirc = domains.getResponse()
    for domain in domains_dirc[u'Domains'][u'Domain']:
        domainName = domain[u'DomainName']
        domainList.append(domainName)
    return domainList


def getDomainDetails(domains):
    domainList = []
    domainWhois = aliyun.api.rest.Dns20150109DescribeDomainWhoisInfoRequest()
    for domain in domains:
        domainDirc = {}

        domainName = domain
        domainWhois.DomainName = domainName
        domainWhois_dirc = domainWhois.getResponse()
        domainUser = domainWhois_dirc[u'RegistrantName']
        domainMail = domainWhois_dirc[u'RegistrantEmail']
        domainOU = domainWhois_dirc[u'Registrar']
        domainExpDate = domainWhois_dirc[u'ExpirationDate']
        domainRegDate = domainWhois_dirc[u'RegistrationDate']

        domainDirc['domainName'] = domainName
        domainDirc['domainUser'] = domainUser
        domainDirc['domainMail'] = domainMail
        domainDirc['domainOU'] = domainOU
        domainDirc['domainExpDate'] = domainExpDate
        domainDirc['domainRegDate'] = domainRegDate

        domainList.append(domainDirc)

    return domainList


def getDomainRecords(domains):
    domainRecordsList = []
    domainRecords = aliyun.api.rest.Dns20150109DescribeDomainRecordsRequest()
    for domain in domains:
        domainRecords.DomainName = domain
        domainRecordsResp = domainRecords.getResponse()
        for dRecord in domainRecordsResp[u'DomainRecords'][u'Record']:
            dRecordDict = {}
            dRecordName = dRecord[u'DomainName']
            dRecordRR = dRecord[u'RR']
            dRecordType = dRecord[u'Type']
            dRecordValue = dRecord[u'Value']
            dRecordLine = dRecord[u'Line']
            dRecordTTL = dRecord[u'TTL']
            dRecordStatus = dRecord[u'Status']
            dRecordLocked = dRecord[u'Locked']

            dRecordDict['RecordName'] = dRecordName
            dRecordDict['RecordRR'] = dRecordRR
            dRecordDict['RecordType'] = dRecordType
            dRecordDict['RecordValue'] = dRecordValue
            dRecordDict['RecordLine'] = dRecordLine
            dRecordDict['RecordTTL'] = str(dRecordTTL)
            dRecordDict['RecordStatus'] = dRecordStatus
            dRecordDict['RecordLocked'] = str(dRecordLocked)

            domainRecordsList.append(dRecordDict)

    return domainRecordsList


def wapperOutput(name, list):
    print '<--table ' + name + ' starts-->'
    keys = list[0].keys()
    print ('|').join(keys)
    for d in list:
        print '|'.join(d.values())
    print '<--table ' + name + ' ends-->'
if __name__ == '__main__':
    domains = getDomainList()
    domainList = getDomainDetails(domains)
    recordsList = getDomainRecords(domains)

    wapperOutput('Domain details', domainList)
    wapperOutput('Domain records', recordsList)
