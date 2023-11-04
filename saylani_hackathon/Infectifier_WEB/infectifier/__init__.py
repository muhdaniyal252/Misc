from flask import Flask,render_template,url_for


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

from infectifier import routes