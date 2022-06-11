import time
import datetime


def play_time(streaming_history,
              start_date: time.struct_time = None,
              end_date: time.struct_time = None) -> datetime.timedelta:
    if start_date is None:
        start_date = time.gmtime(0)
    if end_date is None:
        end_date = time.gmtime()

    total_ms = 0
    for i in streaming_history:
        stamp = time.strptime(i['endTime'], '%Y-%m-%d %H:%M')
        if start_date <= stamp <= end_date:
            total_ms += i['msPlayed']

    return datetime.timedelta(milliseconds=total_ms)


def history_range(streaming_history) -> tuple[time.struct_time, time.struct_time]:
    start = time.strptime(streaming_history[0]['endTime'], '%Y-%m-%d %H:%M')
    end = time.strptime(streaming_history[-1]['endTime'], '%Y-%m-%d %H:%M')

    return start, end
