# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         serializers
# Description:  
# Author:       henrylee
# Date:         19-3-28
#-------------------------------------------------------------------------------

from flask_restplus import fields
from api.restplus import api


product = api.model('product', {
    'user': fields.Integer(required=True, description='User id'),
    'user_input': fields.String(required=True, description='User supplied input'),
    'output': fields.String(required=True, description='Content generation'),
    'pub_date': fields.DateTime,
}
)