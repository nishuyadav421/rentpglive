from flask import render_template,jsonify
def init_page_routes(app):
    @app.route('/career')
    def career():
        return render_template('career.html')
    
    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    @app.route('/terms')
    def terms():
        return render_template('terms.html')
    
    @app.route('/privacy')
    def privacy():
        return render_template('privacy.html')

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

    @app.route('/profile')
    def profile():
        return render_template('profile.html')

    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/register')
    def register():
        return render_template('register.html')

    