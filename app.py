from venv import create
from petfax import create_app

app = create_app()

"""
    route stuff
"""
# @app.route('/test', methods=('GET', 'POST'))
# def test_route():
#     #if request.method
#     return ''

# @app.route('/fruit/<name>')
# def fruit(name):
#     return name

# @app.route('/user/<int:userId>')
# def show(userId):
#     return userId