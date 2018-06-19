
# coding: utf-8

# In[1]:


import requests
import datetime
right_now = datetime.datetime.now()
date_string = right_now.strftime("%Y-%M")


# In[2]:


response = requests.get('https://api.darksky.net/forecast/XXX/40.730610, -73.935242?units=si')
data = response.json()
NYC = 'https://api.darksky.net/forecast/XXX/40.730610, -73.935242?units=si'


# In[3]:


data['currently']


# In[4]:


NYC_daily_forecast = data['daily']['data'][0]
NYC_daily_forecast


# In[5]:


temp_feeling = NYC_daily_forecast['temperatureHigh']
if NYC_daily_forecast['temperatureHigh'] > 80:
    temp_feeling == 'hot'
elif NYC_daily_forecast['temperatureHigh'] > 93:
    temp_feeling == 'super hot'
else:
    temp_feeling = 'humid and warm. Your favorite aka a NYC summer day, you know,'

print("Right now it is", data['currently']['temperature'], "degrees out and", data['currently']['summary']+". Today will be", temp_feeling, "with a high of", NYC_daily_forecast['temperatureHigh'], "and a low of", NYC_daily_forecast['temperatureLow'],".")
if NYC_daily_forecast['precipProbability'] > 0.6:
    print("Bring your umbrella!")


# In[6]:


response = requests.post(
        "https://api.mailgun.net/v3/DOMAINNAME/messages",
        auth=("api", "XXXX"),
        data={"from": "Weathery <mailgun@DOMAINNAME>",
              "to": ["USERMAIL"],
              "subject": "Good morning, Ninja: 8AM Weather forecast" +right_now.strftime("%B-%d-%Y"),
              "text": "Testing some Mailgun awesomness!"})
response.text
