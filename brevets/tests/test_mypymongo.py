"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging
from mypymongo import brevet_insert, brevet_fetch
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)
#write one test that inserts dist, maybe 2 brevets, begin time,
#then fetches

def test_p5():
    start = '2023-01-01T00:00';
    brevet_dist_km = '1000';
    controllist = [
    {'km': '200', 'open': '2023-03:09T02:56', 'close': '2023-03-09T06:40'},
    {'km': '200', 'open': '2023-03:09T02:56', 'close': '2023-03-09T06:40'},
    {'km': '', 'open': '', 'close': ''}, {'km': '', 'open': '', 'close': ''},
    {'km': '', 'open': '', 'close': ''}, {'km': '', 'open': '', 'close': ''},
    {'km': '', 'open': '', 'close': ''}, {'km': '', 'open': '', 'close': ''},
    {'km': '', 'open': '', 'close': ''}, {'km': '', 'open': '', 'close': ''},
    {'km': '', 'open': '', 'close': ''}, {'km': '', 'open': '', 'close': ''},
    {'km': '', 'open': '', 'close': ''}, {'km': '', 'open': '', 'close': ''},
    {'km': '', 'open': '', 'close': ''}, {'km': '', 'open': '', 'close': ''},
    {'km': '', 'open': '', 'close': ''}, {'km': '', 'open': '', 'close': ''},
    ]

    testcase = {'start': start,
    'brevet_dist_km': brevet_dist_km,
    'controllist': controllist}
    brevet_insert(**testcase)
    x = brevet_fetch()
    assert x == testcase, f"failure: {testcase} does not equal {x}"
