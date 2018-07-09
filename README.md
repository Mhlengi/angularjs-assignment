## [AngularJS Assignment]

## Requirements
- Python 3.6
- Postgresql 10.3

Please consult Google if you need to install any of the pre-requisites

## Installation
- Clone/Download the git repo - `git clone git@github.com:Kagiso-Future-Media/cms.git`.
- Create a Postgres database `angular_js_assigment` with user `postgres` and password `password`
- Navigate to a project folder('live_amp')
- Create virtual environment: virtualenv -p python3 venv
- Activate a virtual environment: . venv/bin/activate
- Install all the python dependencies `pip install -r requirements.txt`
- Run the database migrations `python manage.py migrate`
- Start the webserver `python manage.py runserver`
(*Please note everytime you pull from master you may need to run the migrations and install any new dependencies
- as per the above instructions*)

### Browser application tests
- Type the following URLs in your browser URL bar.
- Home Page :-> `http://localhost:8000/#/`
- About-Us Page :-> `http://localhost:8000/#/about`
- Add New Carousel :-> `http://localhost:8000/#/carousel`
- Additional Contact-Us Page :-> `http://localhost:8000/#/contact`
- Delete button is available to delete a carousel on home page.

### Running django tests
`python manage.py test`.
