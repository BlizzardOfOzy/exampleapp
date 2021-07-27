# Example App

## Usage
To use, just run "vagrant up --provision". In 5-10 minutes, the application should be available locally at http://192.168.33.10:80. It just displays the contents of the mongodb database, and allows the user to submit new data to it.

A prometheus server is available on http://192.168.33.11:80. Default flask, mongodb, and kubernetes metrics are available.

I've included the app code and Dockerfile, however if you want to update the docker image you'll have to upload it to your own docker image repo and edit the "image" line of deployment.yaml to use it.

## Dependencies
* Vagrant
* Some VM software; Virtualbox recommended since that's what I've tested on