from flask import Flask
from routes.main import init_main_routes
from routes.user import init_user_routes
from routes.page import init_page_routes
from routes.admin import init_admin_routes

app = Flask(__name__)
init_main_routes(app)
init_user_routes(app)
init_page_routes(app)
init_admin_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
