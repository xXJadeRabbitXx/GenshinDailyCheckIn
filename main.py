import datetime
import genshinstats
import time
import requests

genshinstats.set_cookie(account_id="<account id as int>", cookie_token="<cookie token as string>")  # login

def daily_check_in():
    info = genshinstats.get_daily_reward_info()
    print('total rewards claimed:', info[1])

    # return true, if sign in successful; false otherwise
    if genshinstats.claim_daily_reward():
        print("Reward successfully claimed")
    else:
        print("Reward already claimed")
    return


if __name__ == '__main__':
    while True:
        print(datetime.datetime.now())

        try:
            daily_check_in()
            time.sleep(3600)
        except requests.ConnectionError:
            print("Problem with Connection, retrying ...")

