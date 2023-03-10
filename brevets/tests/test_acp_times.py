"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
from acp_times import open_time, close_time
import arrow
import nose    # Testing framework
import logging
logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_brevet1():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
        60: (start_time.shift(hours=1, minutes=46), start_time),
        120: (start_time.shift(hours=3,minutes=32), start_time),
        175: (start_time.shift(hours=5,minutes=9), start_time),
        200: (start_time.shift(hours=5,minutes=53), start_time),
    }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        print("km:",km)
        print("checkpoint_open:",checkpoint_open)
        assert open_time(km, dist, start_time) == checkpoint_open
        #assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet2():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 1300
    checkpoints = {
        890: (start_time.shift(hours=29, minutes=9), start_time.shift(hours=65,minutes=23)),
    }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        print("km:",km)
        print("checkpoint_open:",checkpoint_open)
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet3():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 1000
    checkpoints = {
        0: (start_time, start_time.shift(hours=1)),
        20: (start_time, start_time.shift(hours=2)),
        60: (start_time, start_time.shift(hours=4)),
        120: (start_time, start_time.shift(hours=8)),
        175: (start_time, start_time.shift(hours=11,minutes=40)),
        550: (start_time, start_time.shift(hours=36,minutes=40)),
        600: (start_time, start_time.shift(hours=40)),
    }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        print("km:",km)
        print("checkpoint_open:",checkpoint_open)
        #assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet4():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 1300
    checkpoints = {
        0: (start_time, start_time.shift(hours=1)),
        20: (start_time.shift(minutes=35), start_time.shift(hours=2)),
        50: (start_time.shift(hours=1,minutes=28), start_time.shift(hours=3,minutes=30)),
        200: (start_time.shift(hours=5,minutes=53), start_time.shift(hours=13,minutes=20)),
        300: (start_time.shift(hours=9), start_time.shift(hours=20)),
        400: (start_time.shift(hours=12,minutes=8), start_time.shift(hours=24+2,minutes=40)),
        500: (start_time.shift(hours=15,minutes=28), start_time.shift(hours=24+9,minutes=20)),
        600: (start_time.shift(hours=18,minutes=48), start_time.shift(hours=24+16)),
        800: (start_time.shift(hours=24+1,minutes=57), start_time.shift(hours=48+9,minutes=30)),
        1000: (start_time.shift(hours=24+9,minutes=5), start_time.shift(hours=72+3))
    }

    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

def test_brevet5():
    start_time = arrow.get("2023-02-17 00:00", "YYYY-MM-DD HH:mm")
    dist = 200
    checkpoints = {
        200: (start_time, start_time.shift(hours=13,minutes=30)),
    }
    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        #assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close

    dist = 400
    checkpoints = {
        400: (start_time, start_time.shift(hours=15)),
    }
    for km, time_tuple in checkpoints.items():
        checkpoint_open, checkpoint_close = time_tuple
        #assert open_time(km, dist, start_time) == checkpoint_open
        assert close_time(km, dist, start_time) == checkpoint_close
