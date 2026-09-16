from datetime import datetime, timedelta
import json
def add_week_to_dates(dates: list[str]) -> list[str]:
    output_dates = []
    for date in dates:
        date_obj = datetime.strptime(date, '%Y.%m.%d')
        new_date_obj = date_obj + timedelta(days=7)
        output_dates.append(new_date_obj.strftime('%B %#d, %Y'))
    return output_dates

print(add_week_to_dates(["2022.12.31", "2023.1.7"]))


def event_durations(json_str):
    events = json.loads(json_str)
    durations = []
    for event in events:
        start_date = datetime.strptime(event['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(event['end_date'], '%Y-%m-%d')
        duration = (end_date - start_date).days
        durations.append(duration)
    return durations








def test_add_week_to_dates():
    assert add_week_to_dates(["2022.12.31", "2023.1.7"]) == ["January 7, 2023", "January 14, 2023"]
    assert add_week_to_dates([]) == []

def test_event_durations():
    json_str1 = ('[{"name": "Event 1", "start_date": "2022-01-01", "end_date": "2022-01-05"},'
                ' {"name": "Event 2", "start_date": "2022-02-15", "end_date": "2022-02-18"},'
                ' {"name": "Event 3", "start_date": "2022-03-10", "end_date": "2022-03-20"}]')
    assert event_durations(json_str1) ==[4, 3, 10]