# parse-web-python

The backend python applicaiton to parse web urls and fetch most of contents as texts.

## Getting Started

### Setup

```sh
# git clone
git clone git@github.com:kei49/parse-web-python.git
cd parse-web-python

# Prepare .env
cp .env.sample .env

# Use pipenv
pipenv shell

# Install dependencies
pipenv install
```

### Try Parsing Urls

```sh
# Parse some prepared urls by using an int argument
pipenv run main 0

# Try some custom url
pipenv run main https://github.com/kei49/parse-web-python

# Test some prepared urls
pipenv run test
```
