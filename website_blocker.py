import time 
from datetime import datetime as dt 

hosts_path = r"C:\Users\Udeshya Dixit\Videos\hosts"

redirect = "127.0.0.1"

website_list = ["www.facebook.com","facebook.com"] 

    
  
while True: 
    if dt(dt.now().year, dt.now().month, dt.now().day,8)  < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,16): 
        print("Working hours...") 
        a=open(hosts_path, 'r+')
        content = a.read() 
        for website in website_list: 
            if website in content: 
                pass
            else: 
                a.write(redirect + " " + website + "\n") 
    else:
        b=open(hosts_path, 'r+') 
        content=b.readlines() 
        for line in content: 
            if not any(website in line for website in website_list): 
                b.write(line) 
  
            # removing hostnmes from host file 
            b.truncate() 
  
        print("Fun hours...") 
    time.sleep(5)