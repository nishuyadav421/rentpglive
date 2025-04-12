from flask import jsonify,request

def init_user_routes(app):
    @app.route('/api/v1/user/login', methods=['POST'])
    def user_login():
        email = request.form.get('email', '')
        password = request.form.get('password', '')

        # Example response
        return jsonify({
            'email': email,
            'password': password,
            'message': 'Login route hit successfully!'
        })


    @app.route('/api/v1/user/register', methods=['POST'])
    def user_register():
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        mobile=request.form.get('mobile', '')
        name=request.form.get('name', '')
        address=request.form.get('address', '')
        # Example response
        return jsonify({
            'email': email,
            'password': password,
            'mobile': mobile,
            'name': name,
            'address': address,
            'message': 'Register route hit successfully!'
        })


    @app.route('/api/v2/user/register', methods=['POST','GET'])
    def user_registers():
        email = request.form.get('email', '')
        password = request.form.get('password', '')
        mobile=request.form.get('mobile', '')
        name=request.form.get('name', '')
        address=request.form.get('address', '')
        # Example response
        return jsonify({
            'email': email,
            'password': password,
            'mobile': mobile,
            'name': name,
            'address': address,
            'message': 'Register route hit successfully!'
        })