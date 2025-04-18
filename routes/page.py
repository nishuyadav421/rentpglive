
from flask import render_template,jsonify


def init_page_routes(app):
    @app.route('/career')
    def career():
        return jsonify({
            'message': 'Career route hit successfully!'
        })
    

    @app.route('/about')
    def about():
        return jsonify({
            'message': 'About route hit successfully!'
        })

    @app.route('/contact')
    def contact():
        return jsonify({
            'message': 'Contact route hit successfully!'
        })

    @app.route('/terms')
    def terms():
        return jsonify({
            'message': 'Terms route hit successfully!'
        })

    @app.route('/privacy')
    def privacy():
        return jsonify({
            'message': 'Privacy route hit successfully!'
        })

    @app.route('/logout')
    def user_logout():
        return jsonify({
            'message': 'Logout route hit successfully!'
        })

    @app.route('/booking')
    def booking():
        return jsonify({
            'message': 'Booking route hit successfully!'
        })

    @app.route('/find-room')
    def find_room():
        return jsonify({
            'message': 'Find Room route hit successfully!'
        })

    @app.route('/room-analysis')
    def room_analysis():
        return jsonify({
            'message': 'Room Analysis route hit successfully!'
        })