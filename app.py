# import necessary libraries
from flask import Flask, request, render_template
import wikipedia
import requests
import logging


#logger config
logger = logging.getLogger(__name__)
logging.basicConfig(filename="wiki.log",filemode='a', level = logging.DEBUG, format = f"%(asctime)s %(levelname)s %(message)s")

URL= "https://en.wikipedia.org/w/api.php"

requests.get(URL, verify=False)

app = Flask(__name__)

# create Landing Page
@app.route('/', methods=['GET', 'POST'])
def home():
	try:
		#checks if there is no input in search, then loads the landing page
		if not request.args.get('q'):
			app.logger.info("No data in query, wiki.html has loaded")
			return render_template('wiki.html')
		#gets input from the search string, formats it into a json, lists all possible matches links 
		data = requests.get(URL,params={'action': 'query', 'format': 'json', 'list': 'search', 'srsearch': request.args.get('q')})
		#loads the results page and displays data collected
		return render_template('results.html', data= data.json(),q = request.args.get('q'))
	except Exception as e:
		app.logger.exception("issues loading the data {}".format(e))
		return render_template('results.html')



if __name__ == '__main__':
	app.run(debug=True)
