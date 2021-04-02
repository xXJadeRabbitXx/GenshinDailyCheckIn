import datetime
import genshinstats
import time

genshinstats.set_cookie(account_id=YOUR_ACCOUNT_ID, cookie_token="YOUR_COOKIE_TOKEN")  # login

def daily_check_in():
    info = genshinstats.get_daily_reward_info()
    print('total rewards claimed:', info['total_sign_day'])

    # return true, if sign in successful; false otherwise
    if genshinstats.sign_in():
        print("Reward successfully claimed")
    else:
        print("Reward already claimed")
    return


if __name__ == '__main__':
    while True:
        print(datetime.datetime.now())
        daily_check_in()
        time.sleep(3600)
