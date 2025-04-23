from flask import render_template
def init_admin_routes(app):
    @app.route('/admin')
    def admin():
        return render_template('admin.html')

    @app.route('/admin/login')
    def admin_login():
        return render_template('admin_login.html')