[![HitCount](http://hits.dwyl.io/ro6ley/PyShortener.svg)](http://hits.dwyl.io/ro6ley/PyShortener)

# PyShortener! 

This repository contains the code for this [blogpost]().

## Getting Started

### Prerequisites

Kindly ensure you have the following installed on your machine:

- [ ] [Python 3](https://realpython.com/installing-python/)
- [ ] [Pipenv](https://pipenv.readthedocs.io/en/latest/#install-pipenv-today) or VirtualEnv
- [ ] Git
- [ ] An IDE or Editor of your choice

### Running the Application

1. Clone the repository
```
$ git clone https://github.com/ro6ley/PyShortener.git
```

2. Check into the cloned repository
```
$ cd PyShortener
```

3. If you are using Pipenv, setup the virtual environment and start it as follows:
```
$ virtualenv --python=python3 env --no-site-packages
$ source env/bin/activate
```

4. Install the requirements
```
$ pip install -r requirements.txt
```

4. Run the script
```
$ python pyshortener.py -h
```

5. Shorten a URL
```
$ python pyshortener.py --url google.com
```

## Contribution

Please feel free to raise issues using this [template](./.github/ISSUE_TEMPLATE.md) and I'll get back to you.

You can also fork the repository, make changes and submit a Pull Request using this [template](./.github/PULL_REQUEST_TEMPLATE.md).
