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

Then install the nltk packages:
- `python -m nltk.downloader all`

If you want to boot the api in your local computer, add exec permissions to boot.sh file using `chmod +x sys/boot.sh`. Also, make sure you have a local postgres db booted up. For mac users there's a utility app that will make your life easier: http://postgresapp.com/

Once you have installed postgres, create the tables using the commands on the sql file `schema.sql` and then create the user and give it permissions on the db and tables:
- `CREATE USER api with PASSWORD '';`
- `GRANT ALL ON analyses TO api;`
- `GRANT ALL ON data_sources TO api;`
- `GRANT USAGE, SELECT ON SEQUENCE analyses_analysis_id_seq TO api;`

Then boot api issuing from root folder `./sys/boot.sh`.

If you want to run the test suite, install pytest as a ***global*** pip dependency with `pip install pytest`. Then do go to project root folder and do `sys/test.sh`

If you want the api to run against a remote postgres db, create an `application.json` with the same contents of `reference.json` and override values.

Project Structure
----------------------

    |_ README.md
    |_ LICENSE
    |_ .travis.yml [10]
    |_ .gitignore
    |_ pytest.ini [8]
    |_ requirements.txt [9]
    |_ metadata/
        |_ ...
    |_ schema/
        |_ ...
    |_ env/ [1]
        |_ ...
    |_ src/ [2]
        |_ ...
        |_ init.py [3]
        |_ config/ [11]
            |_ reference.json=20
        |_ tests/ [4]
            |_ pytest_*
    |_ sys/ [5]
        |_ boot.sh [6]
        |_ test.sh [7]
        |_ ...

[1] - This is the environment folder. Previously called flask, env is preferred as it describes better what this folder is about. Flask has nothing to do, apart that is one dependency installed in the virtual environment, but there are many others. This folder is ignored by git, so it needs to be set up locally as explained in README.md
<br>[2] - src folder, where the source code of this project lives. Before it was called backend
<br>[3] - init script that will instantiate the different modules and will boot up the api to the port and host defined in the config module.
<br>[4] - tests folder. This folder contains the tests that the test suite will run. All files must start with name `pytest_` in order for pytest to recognise them. Each file must declare a `Pytest_` class and each individual test case function must start with name `pytest_`. This was custom defined in [8] so that we only run our test suite.
<br>[5] - this folder contains the bash scripts to perform tasks like testing or booting the api.
<br>[6] - this script checks that the env folder is present and executes init.py with the right python binary.
<br>[7] - this script exports the right `PYTHONPATH` for pytest to work properly, downloads all the nltk dependencies and runs py.test to test all files that start with `pytest_`. This file is used by <a href="https://travis-ci.org/Xarxa6/hackathon">Travis CI</a> but it can be run locally as well, just give exec permissions with `chmod +x sys/test.sh` and run it.
<br>[8] - where the custom pytest configuration is defined.
<br>[9] - file passed to pip to install all the listed dependencies. This is needed by <a href="https://travis-ci.org/Xarxa6/hackathon">Travis CI</a> to setup the env in their server but it’s also more convenient for us to run in our local envs rather than installing one by one manually.
<br>[10] - <a href="https://travis-ci.org/Xarxa6/hackathon">Travis CI</a> configuration
<br>[11] - this folder contains the configuration files. Note that the config module will try to first use an application.json and if it can’t find it, this module will default to `reference.json`. You can provide your own `application.json` with your configuration as git ignores all application.json
