## WHO Global Health Observatory Data Collector

[HDX](https://data.hdx.rwlabs.org/) collector for [WHO Global Health Observatory Data](http://apps.who.int/gho/data/node.main.132?lang=en).

## Introduction

hdxscraper-who operates in the following way:

- Downloads `Global Health Observatory Data` json data
- Groups the rows by indicator
- Dynamically creates a separate database table for each group

With hdxscraper-who, you can

- Save WHO Data to an external database
- Create CKAN datasets with externally generated CSV files
- Update resources previously uploaded to CKAN with new metadata

[View the live data](https://data.hdx.rwlabs.org/organization/world-health-organization)

## Requirements

hdxscraper-who has been tested on the following configuration:

- MacOS X 10.9.5
- Python 2.7.10

hdxscraper-who requires the following in order to run properly:

- [Python >= 2.7](http://www.python.org/download) (MacOS X comes with python pre-installed)

## Setup

*local*

(You are using a [virtualenv](http://www.virtualenv.org/en/latest/index.html), right?)

    git clone https://github.com/reubano/hdxscraper-who.git
    pip install -r requirements.txt
    manage setup

*ScraperWiki Box*

    rm -rf tool
    git clone https://github.com/reubano/hdxscraper-who.git tool
    cd tool
    make setup

## Usage

*local*

    manage run

*ScraperWiki Box*

    source venv/bin/activate
    screen manage -m Scraper run

Now press `Ctrl-a d`. The results will be stored in the file `scraperwiki.sqlite`.

*view all available commands*

    manage

## Upload tables to [HDX](http://data.hdx.rwlabs.org/)/[CKAN](http://ckan.org/)

*upload to production site*

    manage upload

*upload to staging site*

    manage upload -s

## Update tables on [HDX](http://data.hdx.rwlabs.org/)/[CKAN](http://ckan.org/) with new metadata

*update dataset on production site*

    manage update

*update dataset on staging site*

    manage update -s

## Update ScraperWiki box with new code

    cd tool
    make update
    source venv/bin/activate
    screen manage -m Scraper run
    # Now press `Ctrl-a d`

## Configuration

hdxscraper-who will use the following [Environment Variables](http://www.cyberciti.biz/faq/set-environment-variable-linux/) if set:

Environment Variable|Description
--------------------|-----------
CKAN_API_KEY|Your CKAN API Key
CKAN_PROD_URL|Your CKAN instance remote production url
CKAN_REMOTE_URL|Your CKAN instance remote staging url
CKAN_USER_AGENT|Your user agent

## Creating a new collector

If you would like to create collector or scraper from scratch, check out [cookiecutter-collector](https://github.com/reubano/cookiecutter-collector).

    pip install cookiecutter
    cookiecutter https://github.com/reubano/cookiecutter-collector.git

## Contributing

### Code

1. fork
2. commit
3. submit PR
4. ???
5. PROFIT!!!

### Document

- improve this readme
- add comments to confusing parts of the code
- write a "Getting Started" guide
- write additional deployment instructions ([Heroku](http://heroku.com/), [AWS](http://aws.amazon.com/), [Digital Ocean](http://digitalocean.com/), [GAE](https://appengine.google.com/))

### QA

1. follow this guide and see if everything works as expected
2. if something doesn't work, please submit an issue

## License

hdxscraper-who is distributed under the [MIT License](http://opensource.org/licenses/MIT).
