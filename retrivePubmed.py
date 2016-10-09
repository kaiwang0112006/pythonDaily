# -*- coding: utf-8 -*- 
import Bio
from Bio import Entrez
import optparse
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def getOptions():
    parser = optparse.OptionParser('python *.py [option]"')
    parser.add_option('--input',dest='input',help='input file of sideeffect', default='')
    parser.add_option('--drug',dest='drug',help='output druglist', default='drugout.txt')
    parser.add_option('--query',dest='query',help='output query result', default='queryout.txt')

    
    #parser.add_option('--lag',dest='lag',type="int",help='lag value (default 2)',default=2)

    options, args = parser.parse_args()

    if (options.input=='') :
        parser.print_help()
        print ''
        print 'You forgot to provide input file!'
        print 'Current options are:'
        print options
        sys.exit(1)
    return options


def main():
    options = getOptions()
    filein = options.input
    filedrug = options.drug
    filequery = options.query
    
    fin = open(filein)
    drugout = open(filedrug,'w')
    drugout.write('drug\tside effect\tCount\tqueryID\n')
    
    queryout = open(filequery,'w') 
    queryout.write('queryID\tDOI\tTitle\tSource\tPmcRefCount\tIssue\tSO\tISSN\tVolume\tFullJournalName\tRecordStatus\tESSN\tELocationID\tPages\tPubStatus\tAuthorList\tEPubDate\tPubDate\tNlmUniqueID\tId\n')
    
    queryID = 1
    for eachline in fin:
        line = eachline.split('\t')
        drug = line[3]
        sider = line[4]
        Entrez.email = "wangkai0112006@163.com"
        termWord = "%s AND %s" % (drug, sider)
        pubmedHandle = Entrez.esearch(db="pubmed",term=termWord)
        pubmedRecord = Entrez.read(pubmedHandle)
        Count = pubmedRecord['Count']
        drugout.write('%s\t%s\t%s\t%s\n' % (drug, sider, Count, str(queryID)))
        IdList = pubmedRecord['IdList']
        if IdList!=[]:
            Entrez.email = "wangkai0112006@163.com"
            ContentHandle = Entrez.esummary(db="pubmed", id=",".join(IdList))
            ContentRecords = Entrez.parse(ContentHandle)
            for record in ContentRecords:
                doi = "%s" % (record['DOI'] if record.has_key('DOI') else '')
                title = "%s" % (record['Title'] if record.has_key('Title') else '')
                source = "%s" % (record['Source'] if record.has_key('Source') else '')
                PmcRefCount = "%s" % (record['PmcRefCount'] if record.has_key('PmcRefCount') else '')
                Issue = "%s" % (record['Issue'] if record.has_key('Issue') else '')
                so = "%s" % (record['SO'] if record.has_key('SO') else '')
                ISSN = "%s" % (record['ISSN'] if record.has_key('ISSN') else '')
                Volume = "%s" % (record['Volume'] if record.has_key('Volume') else '')
                FullJournalName = "%s" % (record['FullJournalName'] if record.has_key('FullJournalName') else '')
                RecordStatus = "%s" % (record['RecordStatus'] if record.has_key('RecordStatus') else '')
                ESSN = "%s" % (record['ESSN'] if record.has_key('ESSN') else '')
                ELocationID = "%s" % (record['ELocationID'] if record.has_key('ELocationID') else '')
                Pages = "%s" % (record['Pages'] if record.has_key('Pages') else '')
                PubStatus = "%s" % (record['PubStatus'] if record.has_key('PubStatus') else '')
                AuthorList = "%s" % (",".join(record['AuthorList']) if record.has_key('AuthorList') else '')
                EPubDate = "%s" % (record['EPubDate'] if record.has_key('EPubDate') else '')
                PubDate = "%s" % (record['PubDate'] if record.has_key('PubDate') else '')
                NlmUniqueID = "%s" % (record['NlmUniqueID'] if record.has_key('NlmUniqueID') else '')
                rid = "%s" % (record['Id'] if record.has_key('Id') else '')
                rline = ''
                
                for item in [str(queryID),doi,title,source,PmcRefCount,Issue,so,ISSN,Volume,FullJournalName,RecordStatus,ESSN,ELocationID,Pages,PubStatus,AuthorList,EPubDate,PubDate,NlmUniqueID,rid]:
                    rline = rline + str(item) + '\t'
                rline = rline[:-1] + '\n'
                queryout.write(rline)


        queryID += 1
    fin.close()
    drugout.close()
    
if __name__ == "__main__":
    main()
            
'''
        {'DOI': '10.1016/S1081-1206(10)60976-3', 'Title': 'Contact dermatitis to levobun
olol eyedrops superimposed on IgE-mediated rhinoconjunctivitis.', 'Source': 'Ann
 Allergy Asthma Immunol', 'PmcRefCount': 0, 'Issue': '6', 'SO': '2006 Dec;97(6):
817-8', 'ISSN': '1081-1206', 'Volume': '97', 'FullJournalName': 'Annals of aller
gy, asthma & immunology : official publication of the American College of Allerg
y, Asthma, & Immunology', 'RecordStatus': 'PubMed - indexed for MEDLINE', 'ESSN'
: '1534-4436', 'ELocationID': '', 'Pages': '817-8', 'PubStatus': 'ppublish', 'Au
thorList': ['Blumetti B', 'Brodell RT', 'Helms SE', 'Brodell LP', 'Bredle DL'],
'EPubDate': '', 'PubDate': '2006 Dec', 'NlmUniqueID': '9503580', 'LastAuthor': '
Bredle DL', 'ArticleIds': {'pii': 'S1081-1206(10)60976-3', 'medline': [], 'pubme
d': ['17201244'], 'eid': '17201244', 'rid': '17201244', 'doi': '10.1016/S1081-12
06(10)60976-3'}, u'Item': [], 'History': {'medline': ['2007/01/17 09:00'], 'pubm
ed': ['2007/01/05 09:00'], 'entrez': '2007/01/05 09:00'}, 'LangList': ['English'
], 'HasAbstract': 0, 'References': [], 'PubTypeList': ['Letter'], u'Id': '172012
44'}
'''      