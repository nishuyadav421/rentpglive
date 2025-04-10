from flask import jsonify

def init_user_routes(app):
    @app.route('/login')
    def login():
        return jsonify({
            "massage":"I am here to help on the backend problem "
        })