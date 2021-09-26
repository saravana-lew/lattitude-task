# lattitude find max profit for a stock sales

This project contains source code and supporting files to find a max price out of a sales. 

## Functionality Delivered
* Validates inputs
* finds max profit between a possible low and high price out of stock price list


## Modules
It includes the following files and folders:

functions - Code for the application and common files.

tests - Unit tests for the functions' application code and Mock data files for unit test.

## Config files
dev.vars => for deploying on dev environment
main.vars => for deploying on main/prod environment

### Configuration
| Key                  | Description                                                                                     |
| -------------------- | ----------------------------------------------------------------------------------------------- |
| LOGLEVEL             | Level at which log statements are written. Possible values - DEBUG, INFO,WARNING,ERROR,CRITICAL |


## Function
| Function Name                   | Description                                                                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| get_stock_price            | Find maximum profit from the stock price list                                                                                          |


## Configure virtual environment
Configure local python virtual environment and install development dependencies

```bash
python3 -m venv venv
. venv/bin/activate
make install-dev
```

## Test Cases
Execute test case using below commands
```
 python -m unittest discover -s ./tests/unit/ -p '*.py'
```