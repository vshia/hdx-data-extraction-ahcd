# NAMCS-NHAMCS-data-extraction
------
Extract and process NAMCS and NHMCS patient case data.
  - # NAMCS
    The National Ambulatory Medical Care Survey (NAMCS) is a national survey designed to meet the need for objective, reliable information about the provision and use of ambulatory medical care services in the United States. Findings are based on a sample of visits to nonfederally employed office-based physicians who are primarily engaged in direct patient care.
  - # NHAMCS
    The National Hospital Ambulatory Medical Care Survey (NHAMCS) is designed to collect data on the utilization and provision of ambulatory care services in hospital emergency and outpatient departments, and in ambulatory surgery centers

# Code Structure
--------
>   namcs serves as base directory
  * data  - contains all public NAMCS data and dataset for all years
  * general
    - namcs_extractor.py - download and extract public NAMCS data
    -  namcs_converter.py - process and convert NAMCS data in human readable format
* helpers - various methods for manipulating dataset and it's details
* mappers
    - helpers - methods to translate raw data from dataset to human readable format
    - years - year wise NAMCS details like fields, their position in dataset, length etc.
* namcs - contains configurable parameters and constants
* scripts
    - controllers - provide common entry point for execution
    - validation - validation of dataset and parameters provided while invoking script controllers
* utils - contains useful decorators, context managers etc.

### Installation
-----
Currently supported python version 3.6.x,
To check python version
```sh
python --version
```
Ensure pip, setuptools, and wheel are up to date
```sh
python -m pip install --upgrade pip setuptools wheel
```
If you have local copy of this repo and want to install directly from it.
```sh
pip install ${PATH_FOR_NAMCS-NHAMCS-data-extraction_REPO}
```
Similarly you can execute setup file
```sh
python3 ${PATH_FOR_NAMCS-NHAMCS-data-extraction_REPO}/setup.py install
```
for example:
```sh
pip install /var/tmp/NAMCS-NHAMCS-data-extraction/
```
and
for example:
```sh
python3 /var/tmp/NAMCS-NHAMCS-data-extraction/setup.py install
```
You can also use pip directly for Installation.
```sh
pip install namcs
```
-----
### Usage
-----
```sh
>>> import namcs
>>> from namcs.scripts.controllers import NAMCSController
```
### Uninstall
-----
To uninstall you can use either
```sh
easy_install -m namcs
```
or
```sh
pip uninstall namcs
```
### TODO
-----
- Support for all years
    - supported years are 1973, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1985, 1989, 1990, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015
 - Support for more fields
    - supported fields are
        - date_of_visit
        - date_of_birth
        - year_of_visit
        - year_of_birth
        - month_of_visit
        - month_of_birth
        - patient_age
        - gender
        - physician_diagnosis
 ---
License
----
To be discussed.