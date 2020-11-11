import pytest
import yaml
from times import compute_overlap_time, time_range

with open("fixture.yaml", 'r') as yamlfile:
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