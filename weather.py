#!/usr/bin/python
# -*- coding:utf-8 -*-
import logging
import epd2in13bc
import requests, json
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

#Prepare display
epd = epd2in13bc.EPD()
logging.info("Init and clear")
epd.init()
epd.Clear()

font20 = ImageFont.truetype('Font.ttc', 20)
font18 = ImageFont.truetype('Font.ttc', 18)
drawblack = ImageDraw.Draw(HBlackimage)

def load_api_key():
    with open("config.json") as config_json:
        config_data = json.load(config_json)
        return config_data["api_key"]

def draw_temp():
    
def fetch_weather(api_key, zip_code="10016"):
  
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
    # Give city name     
    req_url = base_url + "appid=" + api_key + "&zip=" + zip_code 
    
    # get method of requests module 
    # return response object 
    response = requests.get(req_url) 
    
    # json method of response object  
    # convert json format data into 
    # python format data 
    raw_data = response.json()
    print(raw_data)
    temp_K = raw_data["main"]["temp"]
    temp_F = (temp_K - 273.15) * 9/5 + 32
    print(temp_F)
    drawblack.text((10, 0), f"Temperature: {temp_F}", font = font20, fill = 0)

api_key = load_api_key()
fetch_weather(api_key)

"""
try:
    logging.info("epd2in13bc Demo")

    epd = epd2in13bc.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()
    time.sleep(1)

    # Drawing on the image
    logging.info("Drawing")
    font20 = ImageFont.truetype('Font.ttc', 20)
    font18 = ImageFont.truetype('Font.ttc', 18)

    # Drawing on the Horizontal image
    logging.info("1.Drawing on the Horizontal image...")
    HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)
    drawblack.text((10, 0), 'hello world', font = font20, fill = 0)
    drawblack.text((10, 20), '2.13inch e-Paper bc', font = font20, fill = 0)
    drawblack.text((120, 0), u'微雪电子', font = font20, fill = 0)
    drawblack.line((20, 50, 70, 100), fill = 0)
    drawblack.line((70, 50, 20, 100), fill = 0)
    drawblack.rectangle((20, 50, 70, 100), outline = 0)
    drawry.line((165, 50, 165, 100), fill = 0)
    drawry.line((140, 75, 190, 75), fill = 0)
    drawry.arc((140, 50, 190, 100), 0, 360, fill = 0)
    drawry.rectangle((80, 50, 130, 100), fill = 0)
    drawry.chord((85, 55, 125, 95), 0, 360, fill =1)
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    time.sleep(2)

    # Drawing on the Vertical image
    logging.info("2.Drawing on the Vertical image...")
    LBlackimage = Image.new('1', (epd.width, epd.height), 255)  # 126*298
    LRYimage = Image.new('1', (epd.width, epd.height), 255)  # 126*298
    drawblack = ImageDraw.Draw(LBlackimage)
    drawry = ImageDraw.Draw(LRYimage)

    drawblack.text((2, 0), 'hello world', font = font18, fill = 0)
    drawblack.text((2, 20), '2.13 epd b', font = font18, fill = 0)
    drawblack.text((20, 50), u'微雪电子', font = font18, fill = 0)
    drawblack.line((10, 90, 60, 140), fill = 0)
    drawblack.line((60, 90, 10, 140), fill = 0)
    drawblack.rectangle((10, 90, 60, 140), outline = 0)
    drawry.rectangle((10, 150, 60, 200), fill = 0)
    drawry.arc((15, 95, 55, 135), 0, 360, fill = 0)
    drawry.chord((15, 155, 55, 195), 0, 360, fill =1)
    epd.display(epd.getbuffer(LBlackimage), epd.getbuffer(LRYimage))
    time.sleep(2)

    logging.info("Clear...")
    epd.init()
    epd.Clear()

    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13bc.epdconfig.module_exit()
    exit()
"""