import time
import traceback

from filemgr import load_zipped_data
from stats import history_range, play_time

if __name__ == '__main__':
    try:
        print('Loading data... \n')
        DATA = load_zipped_data()
        start, end = history_range(DATA.streaming_history)

        temp_start = input('Starting date (empty for earliest, otherwise in the form of <yyyy-mm-dd HH:MM>): \n -> ')
        temp_end = input('End date (empty for latest, otherwise in the form of <yyyy-mm-dd HH:MM>): \n -> ')

        start = start if temp_start == '' else temp_start
        end = end if temp_end == '' else temp_end

        total_time = play_time(DATA.streaming_history, start, end)

        print(f'Total Play Time \n'
              f'from [{time.strftime("%Y-%m-%d %H:%M", start)}] to [{time.strftime("%Y-%m-%d %H:%M", end)}]:')
        print(total_time)
        print(f'or {int(total_time.total_seconds() / 60)} minutes')
    except Exception:
        traceback.print_exc()

    input('\nPress Enter to Exit.')
