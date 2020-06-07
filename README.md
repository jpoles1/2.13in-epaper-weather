This repo contains a python script which will pull in the weather from the OpenWeatherMap API and display it on a [2.13 in Waveshare e-paper HAT](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT) for the RasPi Zero/Zero W!

![E-paper Weather Station Demo](https://raw.githubusercontent.com/jpoles1/2.13in-epaper-weather/master/demo.jpg)

All you need to get started is an OpenWeatherMap API key and the appropriate hardware! Use the following steps to get set up:

1) Follow the [instructions on the Waveshare wiki](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT) (under Hardware/Software setup) to prepare the required pre-requisites for the e-paper display.

2) Clone this repo into your "home" directory (~/) or elsewhere (just be sure to change the path in the final step).

3) Create a `config.json` file with your API key using the following format: 

```
{
    "api_key": "your_key_here"
}
```

4) Add the following to the end of your crontab using `crontab -e` replacing the working directory following `cd` with wherever you've cloned this repo. You can change the update frequency from the 15 minutes set in the command below to whatever interval you desire:
```
*/15 * * * * cd /home/pi/2.13in-epaper-weather/ && /usr/bin/python3 weather.py > /tmp/epaper-weather.log 2>&1
```

5) Enjoy your new e-paper weather notification system! 