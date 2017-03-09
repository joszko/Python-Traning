# script that blocks selected website during specified hours using the hosts file
# Mac/Linux: /etc/hosts
# Windows: C:\Windows\System32\drivers\etc\hosts
# Need to be run as administrator

import time
from datetime import datetime as dt

# hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
hosts_path = 'hosts'
redirect = '127.0.0.1'
website_list=['www.facebook.com','facebook.com' ]

while True:
    # making sure that the code will make changes during working hours
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23):
        print('Working Hours...')
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")

    else:
        print('Fun Hours')
        with open(hosts_path,'r+') as file:
            # file.readlines() will return a list with all the lines in the file
            content=file.readlines()
            # file.seek(0) places the pointer before the first character in file
            file.seek(0)
            for line in content:
                # With any() we see if any element is not false.
                if not any(website in line for website in website_list):
                    file.write(line)
                # file.truncate() removes all the characters after the pointer
                file.truncate()

    # time.sleep() makes the loop wait for some time until executing again
    time.sleep(5)