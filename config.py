# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         config
# Description:  
# Author:       henrylee
# Date:         19-3-28
#-------------------------------------------------------------------------------
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client.casper

if __name__ == '__main__':
    pass