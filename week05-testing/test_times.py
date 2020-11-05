from times import time_range, compute_overlap_time
import pytest

""" def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large,short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_ranges_not_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    short = time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00", 2, 60)
    result = compute_overlap_time(large,short)
    expected = []
    assert result == expected

def test_ranges_with_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",8)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00", 2)
    result = compute_overlap_time(large,short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:45:00'),('2010-01-12 10:45:00', '2010-01-12 11:00:00')]
    assert result == expected

def test_ranges_start_end(): 
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00")
    result = compute_overlap_time(large,short)
    expected = []
    assert result == expected """

def test_time_goes_backwards(): # this is the negative test
    with pytest.raises(ValueError):
        time_range("2010-01-12 10:15:00","2010-01-12 10:00:00")

@pytest.mark.parametrize("test_input,expected",[('compute_overlap_time(time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00"),time_range("2010-01-12 11:30:00", "2010-01-12 12:00:00"))',[])
                                               ,('compute_overlap_time(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00",8),time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00",2))',[('2010-01-12 10:30:00', '2010-01-12 10:45:00'), ('2010-01-12 10:45:00', '2010-01-12 11:00:00')])
                                               ,('compute_overlap_time(time_range("2010-01-12 10:00:00", "2010-01-12 10:30:00"),time_range("2010-01-12 10:30:00", "2010-01-12 11:00:00"))',[])
                                               ,('compute_overlap_time(time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60))',[('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')])
                                               ]) # the last row is a valid one.
def test_eval(test_input,expected):
    assert eval(test_input) == expected