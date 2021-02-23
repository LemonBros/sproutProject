from flask_login import logout_user
from flask import url_for

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))