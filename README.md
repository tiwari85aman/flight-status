# flight-status
PIP package to get status of flight pnr status and other details [Supports multiple Indian Airlines]

## Architecture
!["architecture"](/docs/images/architecture.png)

# How to Install
To install this pip package run the following command.

`pip install flight-status`

# Supported Airlines
- Indigo
- Spice Jet


## Prerequisites
- Chrome webdriver is required for the package to work.
- webdriver execuatable is passed as parameter to the package.
- Download chrome webdriver supported for your installed chrome version. 

Download Link: https://chromedriver.chromium.org/downloads

## Usage
- Create an object of class `Airlines` with particular aviation company.

params:
- avaiation : Aviation company name
- config : webdriver config

Example:

``driver_config = {"webdriver": "chrome", "executable": "/path/to/executable"}``

``aviation = Airlines(aviation="indigo", config=driver_config)``

- Use available functions to get respective details.

### Get PNR status:

- define a `config` dict with the required parameters

| Airline  | Config  |
| ------------ | ------------ |
|  Indigo  | `{ "booking_reference": "XXX",    "email_lastname": "XXX"}` |
|  SpiceJet  |  `{ "booking_reference": "XXX",    "email_lastname": "XXX"}` |


`` aviation.get_pnr_status(parameters=config)``
