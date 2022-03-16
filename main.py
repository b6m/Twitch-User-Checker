from pystyle import Anime, Colorate, Colors, Center , System, Write
from colorama import Fore
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# banner = f"""   {Fore.LIGHTBLACK_EX}             ╔═════════════════════════════════════════════════════════════════════╗
#                 {Fore.LIGHTWHITE_EX}║   ┌┬┐┬ ┬┬┌┬┐┌─┐┬ ┬  ┬ ┬┌─┐┌─┐┬─┐ ┌┐┌┌─┐┌┬┐┌─┐  ┌─┐┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐║
#                 {Fore.LIGHTBLACK_EX}║    │ ││││ │ │  ├─┤  │ │└─┐├┤ ├┬┘ │││├─┤│││├┤   │  ├─┤├┤ │  ├┴┐├┤ ├┬┘║
#                 {Fore.LIGHTWHITE_EX}║    ┴ └┴┘┴ ┴ └─┘┴ ┴  └─┘└─┘└─┘┴└─ ┘└┘┴ ┴┴ ┴└─┘  └─┘┴ ┴└─┘└─┘┴ ┴└─┘┴└─║
#                 {Fore.LIGHTBLACK_EX}╚═════════════════════════════════════════════════════════════════════╝  
#                 {Fore.LIGHTWHITE_EX}    ║               M{Fore.LIGHTBLACK_EX}a{Fore.LIGHTWHITE_EX}d{Fore.LIGHTBLACK_EX}e{Fore.LIGHTWHITE_EX} B{Fore.LIGHTBLACK_EX}y{Fore.LIGHTWHITE_EX} r{Fore.LIGHTBLACK_EX}i{Fore.LIGHTWHITE_EX}p{Fore.LIGHTBLACK_EX}#{Fore.LIGHTWHITE_EX}1{Fore.LIGHTBLACK_EX}1{Fore.LIGHTWHITE_EX}1{Fore.LIGHTBLACK_EX}5{Fore.LIGHTWHITE_EX}                        ║
#                 {Fore.LIGHTBLACK_EX}    ║               Put Webhook In config.json              ║
#                 {Fore.LIGHTWHITE_EX}    ╚═══════════════════════════════════════════════════════╝ 
banner = f"""                ╔═════════════════════════════════════════════════════════════════════╗
                ║ ┌┬┐┬ ┬┬┌┬┐┌─┐┬ ┬  ┬ ┬┌─┐┌─┐┬─┐ ┌┐┌┌─┐┌┬┐┌─┐  ┌─┐┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐  ║
                ║  │ ││││ │ │  ├─┤  │ │└─┐├┤ ├┬┘ │││├─┤│││├┤   │  ├─┤├┤ │  ├┴┐├┤ ├┬┘  ║
                ║  ┴ └┴┘┴ ┴ └─┘┴ ┴  └─┘└─┘└─┘┴└─ ┘└┘┴ ┴┴ ┴└─┘  └─┘┴ ┴└─┘└─┘┴ ┴└─┘┴└─  ║
                ╚═════════════════════════════════════════════════════════════════════╝  
                    ║               Made By Rip                             ║
                    ║               Put Webhook In config.json              ║
                    ╚═══════════════════════════════════════════════════════╝ 
                """

print(Colorate.Horizontal(Colors.blue_to_purple, banner))

import requests, colorama, random
import os
from os import system
from colorama import Fore, init
import json
import threading
import time
import scraper
init(convert=True)


with open('config.json') as f:
    config = json.load(f)

Webhook = config.get('Webhook')

def send(user, x):
    data = {
    "content" : f"{user} **__Is Now Available__ | Checked: {x} Amount Of Users**!",
    "username" : "rip",
    "avatar_url" : "https://i.pinimg.com/564x/37/37/4a/37374a5f27b2814cbdc6c9d8d76a9f1a.jpg"
    }
    requests.post(Webhook, json=data)


proxies = open("./proxies.txt").read().splitlines()

def Check():
    x = 0
    y = 0
    z = 0
    while True:
        user = ''.join((random.choice('abcdefghijklmnopqrstuvwxyz1234567890')) for x in range(4))
        url = f"https://m.twitch.tv/{user}"
        head = {
		'Host': 'm.twitch.tv',
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "rip#1115",
        "Accept-Language": "en-us",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://m.twitch.tv/service-worker.js",
        'Connection': 'keep-alive'
        }
        lmao = requests.Session()
        re = lmao.get(url, headers=head, proxies={"http": 'http://' + random.choice(proxies)})
        if re.status_code == 404:
            if len(user) >= 4:
                x += 1
                y += 1
                print(f"[{Fore.GREEN}+{Fore.RESET}] {Fore.LIGHTBLACK_EX}Available >> {user} | Checked: {x} {Fore.RESET}")
                send(user, x)
        elif re.status_code == 200 or 204:
            x += 1
            z += 1
            print(f"[{Fore.RED}-{Fore.RESET}] {Fore.LIGHTWHITE_EX}Taken >> {user} | Checked: {x} {Fore.RESET} ")


if __name__ == "__main__":
    from scraper import scrape
    scrape()
    time.sleep(2.5)
    for i in range(10):
        threading.Thread(target=Check()).start
