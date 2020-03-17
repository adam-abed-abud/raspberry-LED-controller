# Controlling LEDs with a Raspberry Pi

**Technology:** Python, TelegramAPI, electronics, DIY


#### Contolling, blinking, having fun with some LEDs


 - Author: **Adam Abed Abud**
 - Last update: November, 2019



#### What you will need
-- Raspberry Pi (any version), mouse, keyboard, monitor
-- Red, blue, green, yellow, white LEDs
-- Solderless breadboard for prototyping
-- 5 x 330 ohm Resistors
-- Some male to female jumper wires


#### Build the circuit (pictures taken from instructables.com)
Build a circuit like the one shown in the figure below:
![alt text](https://cdn.instructables.com/FTZ/I92N/J4YFNJLI/FTZI92NJ4YFNJLI.LARGE.jpg?auto=webp&fit=bounds)

For reference here is a figure representing all the GPIO pins for the raspberry pi.

![alt text](https://cdn.instructables.com/FFW/AXYJ/J4OFLGTE/FFWAXYJJ4OFLGTE.LARGE.jpg?auto=webp&height=1024&fit=bounds
)

#### Usage

Start the bot application. 

```sh
python LLED_bot.py 
```

#### Example usage

You can test the system by trying on your telegram application the following commands:

/turn_on_led [COLOR] 
/turn_off_led [COLOR]

COLOR can be any of the following "green", "yellow", "white", "red", "blue" or "all" for all the LEDs together 

/counter 
This is used to start the 60 second stopwatch in binary LEDs

--- 
License
----

**Free Software!** 
For the benefit of everyone.











