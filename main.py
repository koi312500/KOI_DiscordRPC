import rpc
from pypresence import Presence
import time
from time import mktime

print("KOI#4182's Discord Rich Presence Python.")

client_id = '865396378837975072'
start_time = mktime(time.localtime())
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) 

print("Program will ask forever. If you want to keep your rpc state, please don't input anything.")
while 1:
    detatils_now = str(input("Please input you RPC's details : "))
    state_now = str(input("Please input you RPC's state : "))
    timestamps_change = str(input("Do you want to change you timestamps to now? (Input 'y' to change. Other char == None.) : "))
    if str(timestamps_change) == 'y':
        start_time = mktime(time.localtime())
    activity = {
            "state": state_now,  # anything you like
            "details": detatils_now,  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "코이를 낚는 낚시꾼 코이!",  # anything you like
                "small_image": "koi3125_profile-512",  # must match the image key
                "large_text": "코이는 코이에요!",  # anything you like
                "large_image": "koi3125_profile2"  # must match the image key
            },
            "buttons": [{"label": "Join to KOI's server.", "url": "https://discord.gg/sX2K7eGdzT"}, {"label": "KOI's solved.ac!", "url": "https://solved.ac/profile/koi312500"}]
        }
    rpc_obj.set_activity(activity)
    
from pypresence import Presence
