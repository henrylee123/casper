# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         restplus
# Description:  
# Author:       henrylee
# Date:         19-3-28
#-------------------------------------------------------------------------------

from flask_restplus import Api


api = Api(version='1.0',
          title='Caseper Api',
          description='Your friendly neighborhood ghostwriter',
          default='Casper',
          default_label='API information'
          )