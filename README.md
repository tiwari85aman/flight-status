# flight-status
PIP package to get status of flight pnr status and other details [Supports multiple Indian Airlines]

# How to Install
To install this pip package run the following command.

`pip install flight-status`

# Supported Airlines
- Indigo
- Spice Jet

# Usage

- Create an object of class `Airlines` with particular aviation company.

Example:

``aviation = Airlines(aviation="indigo")``

- Use available functions to get respective details.

### Get PNR status:

- define a `config` dict with the required parameters

| Airline  | Config  |
| ------------ | ------------ |
|  Indigo  | `{ "booking_reference": "XXX",    "email_lastname": "XXX"}` |
|  SpiceJet  |  `{ "booking_reference": "XXX",    "email_lastname": "XXX"}` |


`` aviation.get_pnr_status(parameters=config)``