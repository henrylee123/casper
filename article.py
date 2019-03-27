# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         article.py
# Description:  
# Author:       henrylee
# Date:         19-3-28
#-------------------------------------------------------------------------------
import bson
from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
ARTICLE = {
    str(bson.ObjectId()): {
        "title": "Best Markering Content",
        "fname": "Doug",
        "lname": "Farrnell",
        "body": "Initiative shared unit of analysis change-makers inspiring",
        "timestamp": get_timestamp()
    },
    str(bson.ObjectId()): {
        "title": "Worst Markering Content",
        "fname": "Kent",
        "lname": "Brockman",
        "body": "Incubator strengthening infrastructure or uplift empathetic",
        "timestamp": get_timestamp()
    },
    str(bson.ObjectId()): {
        "title": "Mediocre Markering Content",
        "fname": "Bunny",
        "lname": "Easter",
        "body": "Youth initiative youth, progress correlation unprecedented",
        "timestamp": get_timestamp()
    },
}

# Create a handler for our read (GET) articles
def read():
    """
    This function responds to a request for /api/articles
    with the complete lists of articles

    :return:        sorted list of articles
    """
    return [ARTICLE[key] for key in sorted(ARTICLE.keys())]
if __name__ == '__main__':
    pass