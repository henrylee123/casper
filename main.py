# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         main.py
# Description:  
# Author:       henrylee
# Date:         19-3-28
#-------------------------------------------------------------------------------

from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the brower URL
    localhost:500/
    :return:   the rendered template 'home.html'
    """
    return render_template('home.html')

# If we're runing in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='localhost', port=1111, debug=True)
