from datetime import timedelta

from time import gmtime, struct_time

from filemgr.types import History


def play_time(streaming_history: list[History],
              start_date: struct_time = gmtime(0),
              end_date: struct_time = gmtime()) -> timedelta:
    """
    calculates total listening time between (optionally) specified time ranges
    no start/end time specified will use the earliest/latest dates in history
    """
    total_time = timedelta()
    for i in streaming_history:
        if start_date <= i['endTime'] <= end_date:
            total_time += i['msPlayed']

    return total_time


def history_range(streaming_history: list[History]) -> tuple[struct_time, struct_time]:
    """
    find the time range the streaming history covers;
    returns tuple of the earliest and latest dates
    """
    return streaming_history[0]['endTime'], streaming_history[-1]['endTime']


def play_counts(streaming_history: list[History]) -> dict[History, int]:
    """
    Generates dictionary with unique artist-track-name keys and number of times played as values

    :return: descending sorted dictionary by play count
    """
    result = {}
    for i in streaming_history:
        key = f"{i['artistName']} - {i['trackName']}"
        if key not in result:
            result[key] = 0
        result[key] += 1

    sort = {k: result[k] for k in sorted(result, key=result.get, reverse=True)}

    return sort
