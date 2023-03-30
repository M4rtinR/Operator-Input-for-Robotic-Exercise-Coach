import time
from datetime import datetime
import requests

# Send ready signal
# Wait for response
# Loop however many times was in response
# Enter to start
# Enter to stop
# Calculate time
# Calculate performance
# Send time and performance but don't wait for response

def main():
    output = {
        "start": True
    }

    # Send post request to Pepper
    post_address = "http://192.168.1.207:5000/cue"
    r = requests.post(post_address, json=output)

    while not(r.status_code == 200):
       time.sleep(1)

    reps = r.json().get("reps")
    set_count = r.json().get("set")
    print("set_count = " + str(set_count))

    input("Press enter to start")
    start_time = datetime.now()
    for x in list(range(1, reps+1)):  # Will go up to and including no. of reps.
        input("Press enter to stop")
        finish_time = datetime.now()

        rep_time = finish_time - start_time

        rep_time_delta = rep_time.total_seconds()
        print("rep_time = " + str(rep_time_delta))

        # Compare time to target time and update performance
        target_time = 1.0
        diff_from_target = target_time - rep_time_delta
        '''performance = 0
        if 0.5 < diff_from_target:
            performance = 1
        elif diff_from_target > -0.5:
            performance = 2'''

        rep_data = {
            "rep": x,
            "score": rep_time_delta
        }
        r = requests.post(post_address, json=rep_data)

        while not (r.status_code == 200):
            time.sleep(0.01)

        print('set = ' + str(r.json().get('set')))
        if not(r.json().get('set') == set_count):
            break

        start_time = finish_time

    r = None
    main()

if __name__ == '__main__':
    main()
