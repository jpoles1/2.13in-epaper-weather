sudo su
echo "*/1 * * * * /usr/bin/python3 $(pwd)/weather.py > /tmp/epaper-weather.log 2>&1" > /etc/cron.d/weather
service crond restart
exit
