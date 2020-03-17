#!/usr/bin/python

import time, datetime
import RPi.GPIO as GPIO
import argparse
import telepot
from telepot.loop import MessageLoop

light_bl = 11
green = 5 
yellow = 6 
white = 13
red = 19
blue = 26


def parse_args():
    parser = argparse.ArgumentParser(description='PythonBot for LED control.')
    return parser.parse_args()

def slipt(word):
    return [char for char in word]

def dec_to_bin(x):
    return str(bin(x)[2:])

def turn_on_led(index):
    led_list = [light_bl, green, yellow, white, red, blue]
    GPIO.output(led_list[index], True) 

def turn_off_led():
    GPIO.output(white, 0)
    GPIO.output(yellow, 0)
    GPIO.output(red, 0)
    GPIO.output(blue, 0)
    GPIO.output(green, 0)
    GPIO.output(light_bl, 0)

def get_time():
    now = time.time()
    seconds = int(now % 60 ) 
    binary_result =  slipt(dec_to_bin(int(seconds))) 
    print "Time in seconds: ", seconds
    print "Time in seconds (binary): ", dec_to_bin(int(seconds))
    #print binary_result[::-1] #inverting the list to have the LSB first
    index = 0
    for item in binary_result[::-1]:
        if item == '1':
            turn_on_led(index)
        index += 1
    time.sleep(0.5)
    turn_off_led()


def setup():
    now = datetime.datetime.now()
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)


    #LED Blue
    GPIO.setup(blue, GPIO.OUT)
    GPIO.output(blue, 0) #Off initially

    #LED Red
    GPIO.setup(red, GPIO.OUT)
    GPIO.output(red, 0) #Off initially


    #LED White
    GPIO.setup(white, GPIO.OUT)
    GPIO.output(white, 0) #Off initially


    #LED Yellow
    GPIO.setup(yellow, GPIO.OUT)
    GPIO.output(yellow, 0) #Off initially


    #LED Green
    GPIO.setup(green, GPIO.OUT)
    GPIO.output(green, 0) #Off initially

    #LED Light_bl
    GPIO.setup(light_bl, GPIO.OUT)
    GPIO.output(light_bl, 0) #Off initially



def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Received. %s' %command

    if 'on' in command:
        message = "Turned on "
        if 'white' in command:
            message = message + "white"
            GPIO.output(white, 1) 
        if 'yellow' in command:
            message = message + "yellow"
            GPIO.output(yellow, 1) 
        if 'red' in command:
            message = message + "red"
            GPIO.output(red, 1) 
        if 'blue' in command:
            message = message + "blue"
            GPIO.output(blue, 1) 
        if 'green' in command:
            message = message + "green"
            GPIO.output(green, 1)
        if 'light_bl' in command:
            message = message + "light_blue"
            GPIO.output(light_bl, 1)
        if 'all' in command:
            message = message + "all "
            GPIO.output(white, 1)
            GPIO.output(yellow, 1)
            GPIO.output(red, 1)
            GPIO.output(blue, 1)
            GPIO.output(green, 1)
            GPIO.output(light_bl, 1)
        message = message + "lights "        
        telegram_bot.sendMessage(chat_id, message) 

    if 'off' in command:
        message = "Turned off "
        if 'white' in command:
            message = message + "white"
            GPIO.output(white, 0) 
        if 'yellow' in command:
            message = message + "yellow"
            GPIO.output(yellow, 0) 
        if 'red' in command:
            message = message + "red"
            GPIO.output(red, 0) 
        if 'blue' in command:
            message = message + "blue"
            GPIO.output(blue, 0) 
        if 'green' in command:
            message = message + "green"
            GPIO.output(green, 0)
        if 'light_bl' in command:
            message = message + "light_blue"
            GPIO.output(light_bl, 0) 
        if 'all' in command:
            message = message + "all"
            GPIO.output(white, 0)
            GPIO.output(yellow, 0)
            GPIO.output(red, 0)
            GPIO.output(blue, 0)
            GPIO.output(green, 0)
            GPIO.output(light_bl, 0)
        message = message + "lights "        
        telegram_bot.sendMessage(chat_id, message) 

    if command == '/time':
        get_time()
        message = "Returned time in seconds"
        telegram_bot.sendMessage(chat_id, message)

    if command == '/counter':
        start_time = time.time()
        for i in range(60):
            print "tick"
            get_time()
            time.sleep(1.0 - ((time.time() - start_time) % 1 ))
        message = "Counter started. 60 seconds."
        telegram_bot.sendMessage(chat_id, message)


def main():
    print "=================================" 
    print "Version 1.0"
    print "Send comments, suggestions, improvements to aaadam94@gmail.com"
    print "================================="
    print "Available LED colors: blue, red, white, yellow, green, light_bl \n" 
    args=parse_args()
    setup()
    print(telegram_bot.getMe())
    MessageLoop(telegram_bot, action).run_as_thread()
    print "Up and Running ..."

    while 1:
        time.sleep(10)



if __name__ == "__main__":
    telegram_bot = telepot.Bot('TELEPOT_BOT_ID')
    main()



