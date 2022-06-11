import time
import traceback

from filemgr import load_zipped_data
from stats import history_range, play_time, play_counts

if __name__ == '__main__':
    try:
        print('Loading data... \n')
        DATA = load_zipped_data()
        start, end = history_range(DATA.streaming_history)

        temp_start = input('Starting date (empty for earliest, otherwise in the form of <yyyy-mm-dd HH:MM>): \n -> ')
        temp_end = input('End date (empty for latest, otherwise in the form of <yyyy-mm-dd HH:MM>): \n -> ')
        print('\n')

        start = start if temp_start == '' else temp_start
        end = end if temp_end == '' else temp_end

        print(f' ===> Statistics from [{time.strftime("%Y-%m-%d %H:%M", start)}] to [{time.strftime("%Y-%m-%d %H:%M", end)}]: \n')

        total_time = play_time(DATA.streaming_history, start, end)

        print(f'Total Play Time:')
        print(f'{total_time!s}  or {int(total_time.total_seconds() / 60)} minutes')
        print('\n')

        play_counts = play_counts(DATA.streaming_history)

        print('Top Played Tracks:')
        for i, k, v in zip(range(1, 21), play_counts.keys(), play_counts.values()):
            print(f'#{i:2} - {v:4} : {k}')
        print('\n')

    except Exception:
        traceback.print_exc()

    input('\nPress Enter to Exit.')
