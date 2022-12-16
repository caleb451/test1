# Import necessary packages and functions
from flask import Flask, render_template

# Create our web application
app = Flask(__name__)

# Create our routes
@app.route('/git_update', methods=['POST'])
def git_update():
	repo = git.Repo('./portfolio_final')
	origin = repo.remotes.origin
	repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
	origin.pull()
	return '', 200

@app.route('/')
def home():
	return render_template('index.html')
