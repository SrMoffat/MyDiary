[![Build Status](https://travis-ci.org/SrMoffat/MyDiary.svg?branch=non-persistent-endpoints)](https://travis-ci.org/SrMoffat/MyDiary)
[![Coverage Status](https://coveralls.io/repos/github/SrMoffat/MyDiary/badge.svg?branch=non-persistent-endpoints)](https://coveralls.io/github/SrMoffat/MyDiary?branch=non-persistent-endpoints)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1035762f60c44fc4a83ed5900b7eeecd)](https://www.codacy.com/app/SrMoffat/MyDiary?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SrMoffat/MyDiary&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/f981ab50b5790bf90bab/maintainability)](https://codeclimate.com/github/SrMoffat/MyDiary/maintainability)

# MyDiary
MyDiary is an online journal where users can pen down their thoughts and feelings.

## Github Pages
The UI templates can be tested on [github pages](https://srmoffat.github.io/MyDiary/UI/index.html)

## Non-persistent endpoints
The non-persistent endpoints where *no database has been used, only ADTs.* are [here](https://github.com/SrMoffat/MyDiary/tree/non-persistent-endpoints)

### Non-persistent version
Try out the non-persistent endpoints on [Heroku](https://mydiary-moff.herokuapp.com/)

## Persistent endpoints
The persistent endpoints where *a POSTGRESQL database has been used* are [here](https://github.com/SrMoffat/MyDiary/tree/ft2-delete-entry)

## Features
1. Users can create an account and log in.
2. Users can view all entries to their diary.
3. Users can view the contents of a diary entry.
4. Users can add an entry.
5. Users can modify an entry.

## Getting Started
1. **Clone repository** `git clone https://github.com/SrMoffat/MyDiary.git`
2. **Navigate to directory** `cd MyDiary`
3. **Create virtual environment** `virtualenv venv`
4. **Activate environment (Ubuntu)** `source/venv/bin/activate`
4. **Activate environment (Windows)** `cd venv/scripts/activate`
4. **Set .env variables** `see "example_env"`
5. **Install dependencies** `pip install -r requirements.txt`
6. **Run app** `python manage.py run`
7. **Open postman/curl**
8. **Navigate to endpoints** e.g. `POST http://127.0.0.1:5000/api/v2/entries` to *ADD* an entry

### Prerequisites

1. [Python](https://www.python.org/downloads/release/python-370/)
2. [Flask](http://flask.pocoo.org/docs/1.0/)
3. [Postresql](https://www.postgresql.org/docs/10/static/index.html)

## Tools
1. [Virtualenv]()
2. [Pytest](https://docs.pytest.org/en/latest/contents.html)
3. [Postman](https://www.getpostman.com/)

## Running the tests
**Run this command:** ```pytest```
**With coverage** ```pytest --cov```

## Contributing

Please feel free to fork the repository and contribute on [Github](https://github.com/SrMoffat/MyDiary)

## Versioning

The REST API uses ordinal number versioning with the first being `v1` without persistence and `v2` with a database

## Authors

* **Ngige Gitau** - *All the work* - [Github](https://github.com/SrMoffat/MyDiary)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who unblocked me during the bootcamp 
* Special thanks to Andela for the opportunity
* Special thanks to Joan Awinja Ingari and Gideon Gitau for the correspondence 




