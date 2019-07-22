
# Running Locally

- cd /Users/preston/parscore6
- python /Applications/google-cloud-sdk/bin/dev_appserver.py app.yaml

# Deploying

- At a command prompt, login as yourself: `gcloud auth login`

- `gcloud config set account 'preston.rohner@gmail.com'`

- `gcloud app deploy ./app.yaml --project parscore6-hrd`

# Misc

- Attempted to run the tests on 7/22/19 and got this error:  `No module named django.utils.simplejson`

- There used to be the Google App Engine Launcher for the Mac and I used that.  It went away a few years ago.