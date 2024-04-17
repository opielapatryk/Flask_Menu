from flask import Flask
from application.rest import dish
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

def create_app(config_name):

    app = Flask(__name__)
    CORS(app) 

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.register_blueprint(dish.blueprint)

    SWAGGER_URL=""
    API_URL="/static/swagger.json"  

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  
        API_URL,
        config={ 
            'app_name': "Restaurant API"
        },
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    return app
