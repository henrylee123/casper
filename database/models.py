# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         models
# Description:  
# Author:       henrylee
# Date:         19-3-28
#-------------------------------------------------------------------------------
from bson import ObjectId
from marshmallow import Schema, fields


Schema.TYPE_MAPPING[ObjectId] = fields.String


class ProuctSchema(Schema):
    user = fields.Int()
    user_input = fields.Str()
    output = fields.Str()