#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import epd2in13bc
import requests, json
import time
from PIL import Image,ImageDraw,ImageFont
from datetime import datetime
import traceback

logging.basicConfig(level=logging.DEBUG)

#Prepare display
epd = epd2in13bc.EPD()
logging.info("Init and clear")
epd.init()
epd.Clear()

font12 = ImageFont.truetype('Font.ttc', 12)
font16 = ImageFont.truetype('Font.ttc', 16)
HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
drawblack = ImageDraw.Draw(HBlackimage)
drawry = ImageDraw.Draw(HRYimage)

def load_api_key():
    with open("config.json") as config_json:
        config_data = json.load(config_json)
        return config_data["api_key"]

def draw_weather(locale, temp, next_rain):
    margin_left = 4
    margin_top = 20
    datetime_str = time.strftime("%H:%M on %m/%d", time.localtime())

    drawblack.text((margin_left, margin_top + 0), f"Weather for {locale} @ {datetime_str}", font = font12, fill = 0)
    drawblack.text((margin_left, margin_top + 16), f"Temp: {temp}", font = font16, fill = 0)
    if next_rain:
        drawry.text((margin_left, margin_top + 36), f"Rain @ {next_rain.hour}:00 on {next_rain.month}/{next_rain.day}", font = font16, fill = 0)
    else:
        drawblack.text((4, margin_top + 36), f"No rain predicted in next 48 hrs", font = font16, fill = 0)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))

def fetch_weather(api_key, zip_code="10016"):
  
    base_url = "http://api.openweathermap.org/data/2.5/onecall"
    req_url = f"{base_url}?appid={api_key}&exclude=minutely&lat=40.746&lon=-73.978&units=imperial"
    response = requests.get(req_url) 
    raw_data = response.json()
    temp_F = raw_data["current"]["temp"]
    rounded_temp = round(temp_F, 0)
    hourly_data = raw_data["hourly"]
    hourly_will_rain = [x["dt"] for x in hourly_data if "rain" in x["weather"][0]["main"].lower()]
    next_rain = datetime.fromtimestamp(min(hourly_will_rain)) if len(hourly_will_rain) > 0 else None
    draw_weather(zip_code, rounded_temp, next_rain)

api_key = load_api_key()
fetch_weather(api_key)