#!/bin/python

__author__ = 'Francisco Guzman'

import csv
import collections 
import sys
import hyposet

from hyposet import CQAHypData, CQAQHypSet,HypSetGroup





def parseCQA(file_str):

    with open(file_str,'r') as csvfile:
        #QID,
        #QCATEGORY,
        #QDATE,
        #QUSERID,
        #QTYPE,
        #QGOLD_YN,
        #QSUBJECT,
        #QBODY,
        #CID,
        #CUSERID,
        #CGOLD,
        #CGOLD_YN,
        #CSUBJECT,
        #CBODY
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')

        data= HypSetGroup()
        for row in reader:
            question=CQAHypData(row['QID'],row['QSUBJECT'],row['QBODY'])
            hyp= CQAHypData(row['CID'],row['CSUBJECT'],row['CBODY'],row['CGOLD'],question)
            data.addItem(question,hyp)
            

        return data



if __name__ == '__main__':
   
    if len(sys.argv) <2:

      data= parseCQA("sampledata/CQA-QL-train+dev.xml.full.csv")
      data.dumpTextToFile("sampledata/CQA-QL-train+dev.xml.full.csv.id+txt")
    elif len(sys.argv) <3:
      data=parseCQA(sys.argv[1])
      data.dumpTextToFile(sys.argv[1]+".txt")
    else:
      data=parseCQA(sys.argv[1])
      data.dumpTextToFile(sys.argv[2])

