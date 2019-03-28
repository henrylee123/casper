# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         products
# Description:  
# Author:       henrylee
# Date:         19-3-28
#-------------------------------------------------------------------------------
import logging

from bson import ObjectId
from flask import jsonify, request
from flask_restplus import Resource
from api.restplus import api
from api.serializers import product

from database import db
from database.models import ProuctSchema

log = logging.getLogger(__name__)
ns = api.namespace('products', description='Operations related to customer product')
product_schema = ProuctSchema()
products_schema = ProuctSchema(many=True)


def create_product(data):
    user = data.get('user')
    user_input = data.get('user_input')
    output = data.get('output')
    # product = dict(user, user_input, output)
    product = dict(user=user, user_input=user_input, output=output)
    db.products.insert(product)

@ns.route('/')
class ProductCollection(Resource):

    def get(self):
        """
        :return:   list of products.
        """
        products = list(db.products.find())
        result = products_schema.dump(products)
        return jsonify({'prodcut': result.data})

    @api.expect(product)
    def post(self):
        """
        Create a new blog post
        """
        create_product(request.json)
        return None, 201


@ns.route('/<string:id>')
@api.response(404, 'Product not found')
class ProductItem(Resource):

    def get(self,id):
        """
        Returns one product
        """
        product = db.products.find_one({'_id': ObjectId(id)})
        result = product_schema.dump(product)
        return jsonify({'product': result.data})