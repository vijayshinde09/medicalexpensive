from insurance.exception import InsuranceException
from insurance.logger import logging
import os,sys


def test_logging_exception():

    try:
        logging.info("test start")

        result=3/0
        print(result)
        logging.info("test end")
    except Exception as e:
        logging.debug(str(e))
        raise InsuranceException(sys,e)


if __name__=="__main__":
    try:
        test_logging_exception()
    except Exception as e:
        print(e)
