import datetime
import unittest.mock as mock
import pytest
import yaml
from times import compute_overlap_time, iss_passes, time_range



# for successful testing run pytest outside of week05-testing folder
with open("week05-testing/fixture.yaml", 'r') as yamlfile:
    fixture = yaml.safe_load(yamlfile)
    #print(fixture)

data_list = []
for i in range(0, len(fixture)):
    first_range = time_range(*list(fixture[i].values())[0]['time_range_1'])
    second_range = time_range(*list(fixture[i].values())[0]['time_range_2'])
    expected = [(start, stop) for start, stop in list(fixture[i].values())[0]['expected']]
    data_list.append((first_range,second_range,expected))

@pytest.mark.parametrize("first_range,second_range,expected", data_list)
def test_time_range_overlap(first_range,second_range,expected):
    assert compute_overlap_time(first_range,second_range) == expected

def test_negative_time_range():
    with pytest.raises(ValueError) as e:
        time_range("2010-01-12 10:00:00", "2010-01-12 09:30:00")
        assert e.match("end_time should be later than start_time")

class ISS_response:
    '''
    This class provides "hardcoded" return values to mock the calls to the online API.
    '''
    @property
    def status_code(self):
        return 200

    def json(self):
        '''
        mocks the bit from the json output we need from querying the API.
        '''
        now = datetime.datetime.now().timestamp()
        return {'message': 'success',          #this date time corresponds to Friday 13 November
                'request': {'altitude': 10.0, 'datetime':now, 'latitude': 23.141884, 'longitude': -82.356662, 'passes': 5},
                'response': [{'duration': 539, 'risetime': now + 88433},
                             {'duration': 629, 'risetime': now + 94095},
                             {'duration': 188, 'risetime': now + 99871},
                             {'duration': 256, 'risetime': now + 105676},
                             {'duration': 636, 'risetime': now + 111480}]}
def test_iss_passes():
    with mock.patch("requests.get", new=mock.MagicMock(return_value=ISS_response())) as mymock:
        iss_over_Havana = iss_passes(23.141884, -82.356662)
        mymock.assert_called_with("http://api.open-notify.org/iss-pass.json",
                                  params={
                                      "lat": 23.141884,
                                      "lon": -82.356662,
                                      "n": 5})
        assert len(iss_over_Havana) == 5
        # Create a range from yesterday to next week whether the overlap ranges are still 5
        yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
        next_week = datetime.datetime.now() + datetime.timedelta(days=7)
        large = time_range(f"{yesterday:%Y-%m-%d %H:%M:%S}", f"{next_week:%Y-%m-%d %H:%M:%S}")
        assert compute_overlap_time(large, iss_over_Havana) == iss_over_Havana
        