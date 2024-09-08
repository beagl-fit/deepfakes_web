# README
This program is a part of David Novak's bachelor's thesis concerning raising awareness of deepfakes

It is a web application made using **Python (flask)**, **HTML**, **JS**, **CSS**, and **Bootstrap**

The application will use the default flask development server which should not be used for an official deployment

### Contents of the web
* a journey about deepfakes and deepfake attacks
* a playground where users can experience 'simplified creation of deepfakes' and test their deepfakes knowledge
  * I do not own the rights to the images used and therefore even the deepfakes created out of them
* test I used for realizing an experiment to find out whether this application helped users
  * this part is commented out and not a default component of the web

## Running the application
To run this web application:
* navigate to the web directory (*some/path/* **deepfakes_web**)
* create and activate virtual environment (optional)
* install python requirements from **requirements.txt** file
* run the application
  * if your Python installation is missing other python modules, add these to the requirements file

The commands to run after navigating to the web directory might be:
* `chmod -R a+rX .`
* `python3 -m venv env`
* `source env/bin/activate`
* `pip install -r requirements.txt`
* `flask run`