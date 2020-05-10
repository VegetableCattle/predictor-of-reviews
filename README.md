## Using Naive Bayes classifier and board game geek review data to design a model, and then using this model and flask to develop a website.
## The demo is deployed on Heroku and uses it as a server.[website link](https://flask-rating-prediction.herokuapp.com/predicted)

**static/dict_file.txt**: The trained model of Naive Bayes classifier
**templates/flask.html**: The front end of this demo
**Procfile**: Let Heroku, when starting the Web, execute gunicorn run: app -log-file-. The following -log-file-parameter is to make the log only print to the standard output stdout, because Heroku does not provide us the function to write to the local disk.
**app.json**: Some introductions about this website
**requirements.txt**: Some libraries and their versions required for the demo to run on Heroku.
**run.py**: flask back end code

Download following libraries:

```
pip install flask
pip install numpy
```

Deploy the demo on Heroku:

```
mkdir /home/heroku/predictor-of-reviews     # Create local code working directory
cd /home/heroku/predictor-of-reviews        # Switch to the local code working directory
git init                                    # Create a local code base
heroku git:remote -a predictor-of-reviews   # Connect to the remote Heroku flask-bjhee code base
```
Push local git repository to Heroku remote repository:
```
git add .
git commit -m "Initialize Project"
git push heroku master 

```
See website deployment effect:
```
heroku open
```
