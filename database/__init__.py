# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         __init__.py
# Description:  
# Author:       henrylee
# Date:         19-3-28
#-------------------------------------------------------------------------------
from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017/')
db = client.casper