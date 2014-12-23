Xarxa6 Hackathon  [![Build Status](https://travis-ci.org/Xarxa6/hackathon.svg?branch=master)](https://travis-ci.org/Xarxa6/hackathon) [![Gitter](https://badges.gitter.im/Join Chat.svg)](https://gitter.im/Xarxa6/hackathon?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
=================

Project Setup
------------------------
Make sure you have Python 2.7.x installed on your local computer. Check version issuing `python --version`

Clone repo
`git clone git@github.com:Xarxa6/hackathon.git`

If you don't have your local environment setup with `pip` and `virtualenv`:
- Follow instructions on how to install pip for your OS here: https://pip.pypa.io/en/latest/installing.html
- Install `virtualenv` with `pip install virtualenv`

Open project root folder and do `virtualenv env`

Then use the `pip` in the virtual environment to install required dependencies:
- `source env/bin/activate`
- `pip install -r requirements.txt`

If you want to boot the api in your local computer, add exec permissions to boot.sh file using `chmod +x sys/boot.sh`. Also, make sure you have a local postgres db booted up. For mac users there's a utility app that will make your life easier: http://postgresapp.com/ See `src/config/reference.json` to know what username and password to create.

Then boot api issuing from root folder `./sys/boot.sh`.

If you want to run the test suite, install pytest as a ***global*** pip dependency with `pip install pytest`. Then do go to project root folder and do `sys/test.sh`

If you want the api to run against a remote postgres db, create an `application.json` with the same contents of `reference.json` and override values.
