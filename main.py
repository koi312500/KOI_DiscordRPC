import rpc
import time
from time import mktime

print("KOI#4182's Discord Rich Presence Python.")

client_id = '865396378837975072'
start_time = mktime(time.localtime())
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) 

assets = {
    "small_text": "현재 공부중입니다...",  # anything you like
    "small_image": "koi3125_profile2",  # must match the image key
    "large_text": "공부중.....",  # anything you like
    "large_image": "studylogo"  # must match the image key
}

print("Program will ask forever. If you want to keep your rpc state, please don't input anything.")

while 1:
    detatils_now = str(input("Please input you RPC's details : "))
    state_now = str(input("Please input you RPC's state : "))
    timestamps_change = str(input("Do you want to change your timestamps to now? Input 'y' to change. : "))
    activity_change = str(input("Do you want to change your activity now? Input 'y' to change. : "))

    if timestamps_change == 'y':
        start_time = mktime(time.localtime())

    if activity_change == 'y':
        small_text = str(input("Small Text : "))
        small_image_name = str(input("Small image name : "))
        print(small_image_name)
        large_text = str(input("Large Text : "))
        large_image_name = str(input("Large image name : "))

    activity = {
            "state": state_now,  # anything you like
            "details": detatils_now,  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": assets,
            "buttons": [{"label": "코이의 서버에요!", "url": "https://discord.gg/mcBjTMMxN6"}, {"label": "코이의 사이트", "url": "https://koi3125.xyz"}]
        }
    rpc_obj.set_activity(activity)
