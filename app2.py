# Raspberry Pi 3 GPIO Pins Status And Control Using Flask Web Server and Python

import RPi.GPIO as GPIO
import time
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
ledRed = 13
ledYellow= 19
ledGreen= 26
ledSts = 0
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledYellow,GPIO.OUT)
GPIO.setup(ledGreen, GPIO.OUT)
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledYellow, GPIO.LOW)
GPIO.output(ledGreen, GPIO.LOW)
@app.route('/')
def index():
    ledSts = GPIO.input(led)
    templateData = { 'led':ledSts}
    return render_template('index.html', **templateData)
@app.route('/<deviceName>/<action>')
def do(deviceName, action):
    deviceName = 0
    if action == "on":
        ledSts = 1
        
        GPIO.output(ledGreen, GPIO.HIGH)
        time.sleep(3)
        
        GPIO.output(ledGreen, GPIO.LOW)
        GPIO.output(ledYellow, GPIO.HIGH)
        time.sleep(1)
        
        GPIO.output(ledYellow, GPIO.LOW)
        GPIO.output(ledRed, GPIO.HIGH)
        time.sleep(4)
        
    if action == "off":
        GPIO.output(ledRed, GPIO.LOW)
        GPIO.output(ledYellow, GPIO.LOW)
        GPIO.output(ledGreen, GPIO.LOW)
        ledSts = 0
        
    templateData = { 'led' : ledSts }
    return render_template('index.html', **templateData )
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True)
