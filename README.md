## Using Naive Bayes classifier and board game geek review data to design a model, and then using this model and flask to develop a website.
## The demo is deployed on Heroku and uses it as a server.[website link](https://flask-rating-prediction.herokuapp.com/predicted)

### static/dict_file.txt: The trained model of Naive Bayes classifier
### templates/flask.html: The front end of this demo
### Procfile: Let Heroku, when starting the Web, execute gunicorn run: app -log-file-. The following -log-file-parameter is to make the log only print to the standard output stdout, because Heroku does not provide us the function to write to the local disk.


