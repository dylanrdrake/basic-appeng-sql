**About**

This is a template for a Flask app for Google Cloud Platform's Appengine.  I wanted to create a boiler plate, reusable template to reuse for web app projects. I wanted it to be ready to go with everything it needs for accessing Cloud SQL and authenticating with Oauth2.



**Install**

Run git clone https://github.com/dylanrdrake/basic-appeng-sql



**Setup**

Make sure you have the Google Cloud SDK installed.

Make sure you have pip2.7 installed (pip3 will install the wrong version of urllib2). Then in the project's root directory run pip2.7 install -t lib/ -r requirements.txt

Edit the env_config.py file by filling in all of the database variables of you Cloud SQL instance. (Make sure to add this file in your .gitignore so that you don't upload any sensitive passwords to a public github repositor)



**Run locally**

To run locally, navigate to the root directory of the project and enter the command dev_appserver.py ./
Then use a browser to navigate to the local host specified in the output and click on the instance link to use your app.


**Deploy**

gcloud app deploy app.yaml
