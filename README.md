# AI-Robotic-Workshop

Making a moving robot eye with Arduino (eye and eyelid movement)
07/18/1401
Approximate reading time is 4 minutes

Contents [show]
In this project, we are going to make a smart eye with Arduino. This project is simple and requires a few servo motors. The complicated part of the story is making the eye components, which is very easy thanks to the existence of 3D printers. All 3D files and project codes are included and you can make the necessary changes if needed.
Video display
00:00
00:09
Required parts
The list of parts required for the smart eye is very short because all the hard work is done by the 3D printer and we only need a few bolts and nuts.
• 6* six SG90 servo motors
• M2, M3 and M4 bolts
• Arduino UNO
Connections of the 3D model of the eye
At the beginning of this project you need to print all the 3D models. After printing, sand some parts that should be smooth. Then we can start assembling the parts. If the printing process was done correctly, you should see these parts:

Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Pico board training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
As you can see in the picture below, 5 servo motors are connected to Servo_Block.

Then we connect the Servo_Block to the Main_Base, the result of which is something like the image below. We have also used four M3 screws with a thickness of 12 mm to make the base of the device.

Next, we attach the Eye-Adaptor to the Fork for both eyes. After doing this, we connect Eye-Holder with Eye-Adaptor and Three-point_Connector to Fork. After doing all this process, the result will be something like the image below.

After doing this, we attach the sixth and last servo to the Sub_Base and then attach the Sub_Base to the Main_Base with screws. We have also connected X-Arm and Y-Arm with screws.

Now we attach the lid fasteners to the lid and use M3 screws to hold the lids on both sides.

If you've done everything correctly, you'll end up with something like the image above, where you can see that we've attached the eyelids to the eyelid connector and screwed them to the servo arms. After doing this, we can move on to the coding process.
If you have any questions about this article, ask in the comments section
Schematic of the moving eye circuit of the robot with Arduino
The schematic of Arduino board connections with servo motors is shown in the picture below. As you can see, it is very simple and understandable. You can use Arduino Ono instead of Arduino Nano.
Suggested article: How to make Arduino Uno board with ATmega328 microcontroller
As we said before, the hardware connections are very simple. We use six Arduino pins to control six servo motors. If we take a quick look at the Arduino specifications, we can see that the Arduino has six PWM pins, and we use all of those pins to control all six of our servo motors.
Get the required parts from the Ironex parts store.
Arduino code to control the robot eye
The Arduino code of the robot eye is very simple and understandable. To make this code work, we will use Arduino's Servo.h library. We start our code by including the required libraries and defining all the instances needed to control all six servo motors.
#include <Servo.h>
Servo top_left_eyelid;
Servo bottom_left_eyelid;
Servo top_right_eyelid;
Servo bottom_right_eyelid;
Servo Yarm;
Servo Xarm;
Then we have the setup() function. In the setup function, we have declared which part of the eye is connected to which Arduino pin. This is very useful because we can unplug all the connectors and plug it back in exactly as it was.
 top_left_eyelid.attach(10);
 bottom_left_eyelid.attach(11);
 top_right_eyelid.attach(5);
 bottom_right_eyelid.attach(6);
 Yarm.attach(9);
 Xarm.attach(3);
Next we initialize the serial monitor for debugging and call some functions to keep the eye open and centered and add some delay.
 Serial.begin(9600);
 open_eye();
 eye_ball_centert();
 delay(2000);
Next we have the loop() function, but before explaining the loo[ function, we will explain a few more important functions that are necessary to understand the content inside the loop function. These functions are the most important functions and with these we want to move the eyeball. First, we have the open_eye() function. If you look at the hardware, you have to move one servo clockwise and one counterclockwise, we do this for the right and left eyelid.
void open_eye() {
 top_left_eyelid.write(55);
 bottom_left_eyelid.write(36);
 top_right_eyelid.write(2);
 bottom_right_eyelid.write(160);
}
Then we have the close_eye() function. In the close_eye function, we will do exactly the same function as open_eye, but in reverse.
void close_eye() {
 top_left_eyelid.write(2);
 bottom_left_eyelid.write(120);
 top_right_eyelid.write(46);
 bottom_right_eyelid.write(55);
}
Then we have look_up() and look_down() functions. If you look at the hardware, the movement of the Y arm moves the eyeball up and down.
void look_up() {
 Yarm.write(132);
}
void look_down() {
 Yarm.write(45);
}
In the next step, we have the function eye_ball_left() and eye_ball_right(), which is the same function as up and down, with the difference that it moves the eyeball in the horizontal direction.
void eye_ball_left() {
 Xarm.write(50);
}
void eye_ball_right() {
 Xarm.write(130);
}
Then we have the synchronous_close() function, by calling this function the eye will be closed and opened once.
void synchronous_close() {
 close_eye();
 delay(420);
 open_eye();
 delay(222);
}
Then we have the random_close() function that randomly opens and closes the eye. This creates an interesting effect.
void random_close() {
 close_eye();
 delay(random(220, 880));
 open_eye();
 delay(random(220, 880));
}
Then we have the random_movement() function. In this function, we have used Arduino's random() function inside the delay function so that the eye moves randomly.
void random_movement() {
 Xarm.write(60);
 delay(random(250, 340));
 Yarm.write(80);
 delay(random(250, 340));
 Xarm.write(120);
 delay(random(250, 340));
 Yarm.write(140);
 Xarm.write(60);
 delay(random(250, 340));
 Yarm.write(80);
 delay(random(250, 340));
 Xarm.write(120);
 delay(random(250, 340));
 Yarm.write(140);
 eye_ball_centert();
 delay(300);
 synchronous_close();
 random_close();
}
Now we explain the loop function which is the main function of Arduino. In this function, we move the eye to the left, right, and center, then up and down, and then we blink. We do this a few times and make a random move. And finally we have two for loops. There are for loops as an example of how to achieve smooth motion or moving the eyeball.
void loop() {
 eye_ball_left();
 delay(680);
 eye_ball_right();
 delay(680);
 eye_ball_centert();
 delay(450);
 synchronous_close();
 eye_ball_centert();
 delay(450);
 look_up();
 delay(400);
 look_down();
 delay(400);
 eye_ball_centert();
 delay(300);
 random_close();
 delay(450);
 look_up();
 delay(400);
 look_down();
 delay(400);
 random_movement();
 delay(400);
 eye_ball_centert();
 delay(300);
 top_left_eyelid.write(2);
 bottom_left_eyelid.write(120);
 delay(200);
 top_left_eyelid.write(55);
 bottom_left_eyelid.write(36);
 delay(200);
 open_eye();
 delay(500);
 for (int i = 60; i < 120; i++)
 {
 Xarm.write(i);
 Yarm.write(i - 5);
 delay(10);
 }
 eye_ball_centert();
 delay(400);
 synchronous_close();
 for (int i = 120; i > 60; i--) {
 Xarm.write(i);
 Yarm.write(i - 5);
 delay(10);
 }
}
This marks the end of the code section.
Airnex/Arduino training/making a bluetooth robot with Arduino (car control with mobile phone)
Teaching Arduino Arduino projects
Making a bluetooth robot with Arduino (car control with mobile phone)
02/10/1401
Approximate study time 7

Making the Arduino bluetooth robot chassis
The robot chassis is the base and the main part of the robot that holds all the circuits of the robot. Therefore, we will use PVC boards to build a reliable and strong chassis. These boards are strong while being light.
Cut the pieces with the given dimensions:
• Rectangular piece 10.5 x 13.5 cm (2 pieces)
• 7.5 x 2.3 cm strips (2 pieces)
• 11.5 x 2.3 cm strip (2 pieces)
• 4.3 x 2.3 cm (1 piece)
• 10.5 x 3.5 cm (2 pieces)
It will end up looking like this:
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Pico board training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store

Connecting motors: Now all four motors are connected in pairs and each pair is connected in parallel. That is, the right engine is connected to the left engine.
Connecting the motor to the motor driver: Since we are using the L298N module, we have 2 terminals on both sides to connect the motors. Just connect the motors to the driver as the polarity and direction can be controlled using the input pins connected to the Arduino. We will discuss this in the next steps.
We have made other robotics projects before, if you want to make something different and easier, you can check out our other projects linked below.
• Boat control with Arduino
• Arduino disinfecting robot
• Arduino smart vacuum cleaner robot
• Arduino Wi-Fi controlled robot
Arduino bluetooth car circuit
The complete circuit of the Arduino bluetooth car is shown below. This circuit is made of generic components and can be obtained from any online or local store.

Required parts
• Arduino UNO
• Bluetooth module HC05
• L298N motor driver
• NeoPixel LED (if needed)
• 18650 lithium ion battery with protection circuit
• BO engines with wheels * 4
• Perforated board * 2
• DC female jack
Get the required parts from the Ironex parts store.
The operation of this circuit is very simple and understandable. First, we have an Arduino that works as the brain of the circuit. Then we have the Bluetooth module. The Bluetooth module is connected to pin 13 and 10 of Arduino which we use as software serial communication pins. Next, we'll use pins 11,12,8, and 7 to connect our WS2812B RGB LEDs. Finally, we use pins 9, 6, 5, and 4 to connect the L298N motor driver IC that drives our four motors.
Suggested article: Relay control with sensor data connected to Arduino
Arduino L298N
3 IN1
If you have any questions about this article, ask in the comments section
9 IN2
5 IN3
6 IN4
VIN +5V
GND GND
Arduino HC05
10 Tx
11 Rx
+5V VCC
GND GND
Arduino NeoPixel
8 Left LED
7 Right LED
12 Front LED Data
13 Back LED Data
Arduino code for bluetooth controlled robot
The Arduino code and Bluetooth based robot is a bit complicated, so we will split the whole code into three separate files so that we can understand it better.
arduino_bluetooth_bot_main:
As we all know bluetooth module uses serial communication to communicate with arduino and since arduino has only one serial or TX port and RX port, we need to use arduino's SoftwareSerial.h library to communicate with bluetooth module. So in the void setup() function we configure the hardware serial with 9600 baud for debugging and we configure the software serial with 38400 baud for Bluetooth communication. Then by sending the AT command to the Bluetooth module, we check whether the Bluetooth module is working or not. If the Bluetooth module returns the OK message, everything is fine. Once this is done, we call the LED_setup() function to set up the neopixel LEDs, which we will discuss later.
#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX
void setup() {
 // Serial communication
 Serial.begin(9600);
 mySerial.begin(38400);
 while (!Serial) {
 ; // Wait for the serial connection to be established
 }
 Serial.println("Sending AT...");
 mySerial.write("AT");
 if (mySerial.available()>0) {
 Serial.write(mySerial.read());
 }
 Serial.println("loop begins");
 LED_setup();
}
Next, we need to initialize three variables, the first variable is called rcd and is a character variable that holds the data received from the bluetooth module. In the next step, we define a spd variable of integer type that holds the car's speed data. Then we have a time_now variable of long type that we will use to store the time data. We check the rcd variable that is being received and execute an if condition based on it. We continue this process for all RGB LEDs and robot movements.
void loop() { // run over and over
 if (mySerial.available()) {
 rcd = mySerial.read();
 Serial.write(rcd);
 }
 unsigned long time_now = 0;
 if (rcd == 'O')
 {
 R_LED(1);
 L_LED(1);
 F_LED(1);
 B_LED(1);
 }
 if (rcd == 'o')
 {
 R_LED(0);
 L_LED(0);
 F_LED(0);
 B_LED(0);
 }
 if (rcd == 'X')
 { L_LED(1);
 }
 if (rcd == 'x')
 {
 L_LED(0);
 }
 if (rcd == 'P')
 {
 R_LED(1);
 }
 if (rcd == 'p')
 { R_LED(0);
 }
 if (rcd == 'W')
 { F_LED(1);
 }
 if (rcd == 'w')
 { F_LED(0);
 }
 if (rcd == 'U')
 { B_LED(1);
 }
 if

 Inside the LED controller file, we have set, declared and defined the pins to which the neopixel LEDs are connected. We have used the Adafruit_NeoPixel library to control the neopixels.
#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h>
#endif
#define F_LED_PIN 12 //Front LED
#define F_LED_PIXEL 6
#define B_LED_PIN 13 //Back LED
#define B_LED_PIXEL 6
#define R_LED_PIN 7 //Right LED
#define R_LED_PIXEL 1
#define L_LED_PIN 8 //Left LED
#define L_LED_PIXEL 1
Adafruit_NeoPixel F_LED_STRIP(F_LED_PIXEL, F_LED_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel B_LED_STRIP(B_LED_PIXEL, B_LED_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel R_LED_STRIP(R_LED_PIXEL, R_LED_PIN, NEO_GRB + NEO_KHZ800);
Adafruit_NeoPixel L_LED_STRIP(L_LED_PIXEL, L_LED_PIN, NEO_GRB + NEO_KHZ800);
Then inside this file, we have LED_setup() function. Inside this function, we've initialized all the neopixel LEDs and turned them off with the default function provided by Adafruit so that the neopixels don't accidentally turn on at the beginning of the code.
void LED_setup()
{
 #if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
 clock_prescale_set(clock_div_1);
#endif
 F_LED_STRIP.begin();
 B_LED_STRIP.begin();
 R_LED_STRIP.begin();
 L_LED_STRIP.begin();
 R_LED_STRIP.clear();
 L_LED_STRIP.clear();
 F_LED_STRIP.clear();
 B_LED_STRIP.clear();
}
Next, we have four more functions that control all the LEDs. These functions are connected to the robot and are called R_LED, L_LED, F_LED, B_LED respectively.
void R_LED(int a)
{
 if(a==1)
 {
 R_LED_STRIP.clear();
 R_LED_STRIP.setPixelColor(0, R_LED_STRIP.Color(0, 255, 255));
 R_LED_STRIP.show(); // Send the updated pixel colors to the hardware.
 }
 else {
 R_LED_STRIP.clear();
 R_LED_STRIP.show();
 }
}
void L_LED(int a)
{
 if(a==1)
 {
 L_LED_STRIP.clear();
 L_LED_STRIP.setPixelColor(0, L_LED_STRIP.Color(0, 255, 255));
 L_LED_STRIP.show(); // Send the updated pixel colors to the hardware.
 }
 otherwise
 {
 L_LED_STRIP.clear();
 L_LED_STRIP.show();
 }
}
void F_LED(int a)
{
 if(a==1)
 {
 F_LED_STRIP.clear();
 F_LED_STRIP.setPixelColor(0, F_LED_STRIP.Color(255, 255, 255));
 F_LED_STRIP.setPixelColor(1, F_LED_STRIP.Color(0, 0, 50));
 F_LED_STRIP.setPixelColor(2, F_LED_STRIP.Color(0, 0, 50));
 F_LED_STRIP.setPixelColor(3, F_LED_STRIP.Color(0, 0, 50));
 F_LED_STRIP.setPixelColor(4, F_LED_STRIP.Color(0, 0, 50));
 F_LED_STRIP.setPixelColor(5, F_LED_STRIP.Color(255, 255, 255));
 F_LED_STRIP.show(); // Send the updated pixel colors to the hardware.
 }
 else if(a==0)
 {
 F_LED_STRIP.clear();
 F_LED_STRIP.show();
 }
}
void B_LED(int a)
{
 if(a==1)
 {
 B_LED_STRIP.clear();
 B_LED_STRIP.setPixelColor(0, B_LED_STRIP.Color(255, 0, 0));
 B_LED_STRIP.setPixelColor(1, B_LED_STRIP.Color(0, 50, 0));
 B_LED_STRIP.setPixelColor(2, B_LED_STRIP.Color(0, 50, 0));
 B_LED_STRIP.setPixelColor(3, B_LED_STRIP.Color(0, 50, 0));
 B_LED_STRIP.setPixelColor(4, B_LED_STRIP.Color(0, 50, 0));
 B_LED_STRIP.setPixelColor(5, B_LED_STRIP.Color(255, 0, 0));
 B_LED_STRIP.show(); // Send the updated pixel colors to the hardware.
 }
 else if(a==0)
 {
 B_LED_STRIP.clear();
 B_LED_STRIP.show();
 }
}
Movements:
In this particular file, we have defined functions to control the movement of the robot. In the function shown below, we have used the analogWrite(5, spd) function and passed the pin and the speed value so that it can generate a PWM signal. After that, we control a motor driver IC and it drives the motor.
void Forward()
{
 analogWrite(5, spd);
 digitalWrite(6, 0);
 analogWrite(9, spd);
 digitalWrite(3, 0);
 // delay(50);
}
void Backward()
{
 digitalWrite(5, 0);
 analogWrite(6, spd);
 digitalWrite(9, 0);
 analogWrite(3, spd);
}
void Stop()
{
 analogWrite(5, 0);
 digitalWrite(6, 0);
 analogWrite(9, 0);
 digitalWrite(3, 0);
}
void FdRight()
{
 analogWrite(5, spd);
 digitalWrite(6, 0);
 digitalWrite(9, 0);
 analogWrite(3, 0);
}
void BkRight()
{
 analogWrite(5, 0);
 digitalWrite(6, 0);
 digitalWrite(9, 0);
 analogWrite(3, spd);
}
void SharpRight()
{
 analogWrite(5, spd);
 digitalWrite(6, 0);
 digitalWrite(9, 0);
 analogWrite(3, spd);
}
void SharpLeft()
{
 digitalWrite(5, 0);
 analogWrite(6, spd);
 analogWrite(9, spd);
 digitalWrite(3, 0);
}
void BkLeft()
{
 digitalWrite(5, 0);
 analogWrite(6, spd);
 analogWrite(9, 0);
 digitalWrite(3, 0);
}
void FdLeft()
{
 digitalWrite(5, 0);
 analogWrite(6, 0);
 analogWrite(9, spd);
 digitalWrite(3, 0);
}

Making an Android application for a Bluetooth robot
It is very easy to make an Android application with application builders. First, we design the user interface. We have used MIT software to build this Android software. In the image below, you can see the graphic appearance of this program.

In the logical part, there is not much. We use the standard App Inventor methods to connect to the HC-05 Bluetooth and once the connection is made, we only send specific commands to move the robot and control the robot's LEDs. The aia file for the Android application is placed at the bottom of the page, which you can download and edit as you wish. The screenshot of the logical part is given below.
Suggested article: Teaching how to make a melody with an Arduino board

We are finishing our project based on arduino, android and bluetooth controlled robot car. I hope you enjoyed reading this article and learned something useful. Now it's time to make it yourself. If you have any questions, you can use our forum to contact us.
Teaching Arduino Arduino projects
Floor cleaning robot with Arduino (smart vacuum cleaner)
05/13/1400
Approximate reading time is 6 minutes

Contents [show]
In today's world, we are all busy with work and do not have enough time to properly clean the house. The solution is very simple, you just need to buy a home vacuum cleaner robot that cleans your house by itself. But these robots have a high cost and this can be a negative point. Today, we are designing a smart robot vacuum cleaner based on Arduino, which will easily clean the floor of your house and will cost very little. We had already made an Arduino vacuum cleaner robot, but that robot had a large volume and weight and was not very convenient. The robot we design in this tutorial has ultrasonic sensors and infrared proximity sensors. The ultrasonic sensor gives the robot the ability not to hit obstacles and the proximity sensor helps the robot to recognize the stairs and not fall.
Video display
00:00
00:45
Schematic circuit of floor cleaning robot with Arduino
We have three ultrasonic sensors that detect obstacles. These three sensors are the important part of our project and we connect them to Arduino. We also connect the VCC of the IR module to 5V. We use a 7.4V battery, to convert it to 5V, an LM7805 voltage regulator is used.

Required parts
• Arduino Pro Mini
• 3 * HC-SR04 ultrasonic module
• L293D motor driver
• 2 * 5V motor
• Switch
• LM7805 voltage regulator
• 7.4 V lithium ion battery
• Infrared module
• Conventional portable vacuum cleaner
Get the required parts from the Ironex parts store.
Ordinary portable vacuum cleaner!
In the parts requirement section, we talked about portable vacuum cleaners. The foldable vacuum cleaner that you can see below is a small and energy-efficient vacuum cleaner that we embed in the robot. These types of vacuum cleaners have good facilities and because they are cheap, they can easily start our work.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Pico board training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store

To detect obstacles, we use HC-SR04 ultrasonic distance sensor. The work is very simple, first, the transmitter module sends out an ultrasonic wave that travels through the air, hits an obstacle and bounces back, and the receiver receives that wave. By calculating the time with Arduino, we can determine the distance. Read the Arduino distance meter article for more information.
 How the ultrasonic sensor works
Infrared proximity sensor for stair detection
An infrared sensor is used to detect the presence of foam. If the robot falls down the stairs, it may be damaged. We use an infrared proximity sensor to detect stairs.
Suggested article: RGB LED color control project with mobile and Arduino (IoT)

Building a circuit for an Arduino floor cleaning robot
In order to make the circuit stronger and more stylish, we solder the required parts on a perforated board.

Building a housing for a smart vacuum cleaner robot
Making the enclosure is completely tasteful and you can design an enclosure or box for your robot in any way you want. In your case, you should consider a place for the ultrasonic and proximity sensor. The following pictures will help you in making this container.


Arduino-based floor cleaning robot code
The complete code of the project is placed at the end of the page in the downloadable file. In this code, we do not use any additional library. Here we explain the important parts of the code.
At the beginning of the code, we define variables for required pins such as Echo and Trig pins of ultrasonic sensors. Note that 1 is the left sensor, 2 is the front sensor, and 3 is the right sensor.
If you have any questions about this article, ask in the comments section
const int trigPin1 = 3;
const int echoPin1 = 5;
const int trigPin2 = 6;
const int echoPin2 =9;
const int trigPin3 = 10;
const int echoPin3 = 11;
int irpin = 2;
Then we define variables for distance, all of which are variables of type (int) and we used (long) for duration. Again, we have three of each.
 long duration1;
 long duration2;
 long duration3;
int distanceleft;
int distancefront;
int distanceright;
int a=0;
In Setup we need to define all pins as input or output using pinModes() function. To send ultrasonic waves from the module, we need to enable the Trig pin, that is, all the Trig pins must be defined as OUTPUT. And to receive Echo, we need to read the status of Echo pins, so all Echo pins must be defined as INPUT. We also activate the serial monitor for troubleshooting. To read the status of the infrared module, we have defined the irpin pin as an input.
pinMode(trigPin1, OUTPUT);
pinMode(trigPin2, OUTPUT);
pinMode(trigPin3, OUTPUT);
pinMode(echoPin1, INPUT);
pinMode(echoPin2, INPUT);
pinMode(echoPin3, INPUT);
 pinMode(irpin, INPUT);
And these digital pins are defined as OUTPUT for motor driver input.
pinMode(4, OUTPUT);
pinMode(7, OUTPUT);
pinMode(8, OUTPUT);
pinMode(12, OUTPUT);
In the void loop we have three sections for three sensors. All the parts work the same but each one is for different sensors. In this section, we read the obstacle distance from each sensor and store it in the defined int variable. To read the distance, we first need to make sure that the Trig pins are on, for this we need to set the Trig pin to LOW for 2 µs. Now, to generate the ultrasonic wave, we need to turn the Trig pin HIGH for 10 µs. With this, the ultrasonic wave is sent, and by using the pulseIn() function, we can read the sending and receiving time and store this value in the "duration" variable. This function has 2 parameters, the first one is the name of the Echo pin and you can write HIGH or LOW for the parameter. HIGH means that the pulseIn() function starts counting and stops counting when the pin goes HIGH, and LOW means the function starts counting and stops counting when the pin goes LOW. This function shows the length of the ultrasonic pulse in microseconds. To calculate the distance, we multiply the time by 0.034. (the speed of sound in air is 340 m/s) and we divide it by 2 because the distance obtained is the round trip distance of the wave.
digitalWrite(trigPin1, LOW);
delayMicroseconds(2);
digitalWrite(trigPin1, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);
duration1 = pulseIn(echoPin1, HIGH);
distanceleft = duration1 * 0.034 / 2;
After calculating the distance of the sensors to the obstacles, we can control the motors using the if command, thus controlling the movement of the robot. This is very simple. We consider the distance to approach the obstacle and change the path as 15. We change the path of the robot with conditions. And the other two distances are large (this means that there are no obstacles in front of its sensors) Using the digitalWrite function, we can direct the motors to the right. Then we check the status of the IR sensor. If the robot is on the ground, the value of the IR pin will be LOW and if not, the value will be HIGH. Then we store that value in the int s variable. We are going to control the robot according to this situation.

This part of the code is used to move the robot forward and backward:
if(s==HIGH)
 {
 digitalWrite(4, LOW);
 digitalWrite(7, HIGH);
 digitalWrite(8, LOW);
 digitalWrite(12, HIGH);
 delay(1000);
 a=1;
 }
After detecting the absence of floor, the robot does not move forward. Instead, it moves to the left, so we can avoid the problem.
if ((a==0)&&(s==LOW)&&(distanceleft <= 15 && distancefront > 15 && distanceright <= 15) || (a==0)&&(s==LOW)&&(distanceleft > 15 && distancefront > 15 && distanceright > 15))
This part of the code is used to move the robot to the right:
 digitalWrite(4, HIGH);
 digitalWrite(7, LOW);
 digitalWrite(8, HIGH);
 digitalWrite(12, LOW);
If the robot detects that there is no floor, the value changes to 1 and the robot moves to the left. After left rotation, the value of 'a' changes from 1 to 0.
 if ((a==1) &&(s==LOW) ||(s==LOW) && (distanceleft <= 15 && distancefront <= 15 && distanceright > 15) || (s== LOW) && (distanceleft <= 15 && distancefront <= 15 && distanceright > 15) || (distanceleft <= 15 && distanceright > 15) || (distanceleft <= 15 && distanceright > 15))
 {
 digitalWrite(4, HIGH);
 digitalWrite(7, LOW);
 digitalWrite(8, LOW);
 digitalWrite(12, HIGH);
 delay(100);
 a=0;
 }
This part of the code is used to move the robot to the left:
if ((s==LOW)&&(distanceleft > 15 && distancefront <= 15 && distanceright <= 15) ||(s==LOW)&& (distanceleft > 15 && distancefront > 15 && distanceright <= 15) ||( s==LOW)&& (distanceleft > 15 && distancefront <= 15 && distanceright > 15) )
 {
 digitalWrite(4, LOW);
 digitalWrite(7, HIGH);
 digitalWrite(8, HIGH);
 digitalWrite(12, LOW);
 }

Technology
Types of robots (investigation of types of robots and their use)
1399/12/05
Approximate reading time is 4 minutes

Contents [show]
It is not easy to define what a robot is and to categorize robots. Each robot has its own unique features and in general the size, shape and capabilities of different robots are very different. Many robots have different features. In this article, we have divided the robots into 15 groups.
Aerospace robots

The group of air and space robots is very wide. This group includes all flying robots and robots that are sent to space. Like the Mars rover robots and humanoid robots that were sent to the International Space Station.
Consumer robots

Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Pico board training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
Consumer bots are robots that you can buy and use for entertainment or to help you do things. As an example, we can mention dog robots and... For example, surface cleaning robots help you clean the house. View the surface cleaning robot with Arduino.
Rescue robots

These robots perform dangerous tasks such as searching for survivors in emergency situations. For example, after the 2011 earthquake and tsunami in Japan, Packbots were used to assess damage at the Fukushima Daiichi nuclear power plant. Check out the Rescue Robot with a Raspberry Pi Camera.
Drones and quadcopters

Drones and quadcopters are also called drones. Drones are produced in different sizes and have high autonomy. Examples include DJI's popular Phantom series and Parrot's Anafi, as well as military systems such as the Global Hawk, which are used for long-range surveillance. I suggest you see the article on what is a quadcopter and the article on making a quadcopter.
Robots with educational application

This broad range of next-generation robotics is intended for use at home or in classrooms. These robots can be used for training in the circuit or at home and have a large operating range.

Fun robots

These robots are created to create an emotional reaction and to create laughter or a feeling of surprise and amazement. Among them are the robot comedian RoboThespian, Disney park robots such as Navi Shaman and robots with the ability to play music such as Partner.
Artificial limbs

Robotic exoskeletons can be used to physically rehabilitate and enable the paralyzed patient to walk again. Some of them have industrial or military applications due to their mobility, endurance or capacity to carry heavy loads.
If you have any questions about this article, ask in the comments section
Suggested article: Trigonometric mathematical functions in MATLAB (E Matlab, cosine, etc.)
Humanoid robots

When most people think of robots, they actually think of humanoid robots. Examples of humanoid robots include Honda's Asimo, which has a mechanical appearance, and the Geminoid series, which are designed to look like people. View the humanoid robot with Arduino.
Industrial robots

An industrial robot consists of a manipulative arm designed to perform repetitive tasks. Unimate, for example, is the granddaddy of all factory robots. This category includes systems such as Amazon warehouse robots and collaborative factory robots that can work alongside human workers. See how to make a robotic arm with Arduino.
Medical robots

Medical and health robots include systems such as da Vinci surgical robot and bionic prostheses as well as robotic exoskeletons. A system that might fit into this category but is not a robot is Watson, IBM's question-answering supercomputer that has been used in healthcare applications.
Military and security robots

Military robots include ground systems such as Endeavor Robotics' PackBot, which is used in Iraq and Afghanistan to search for improvised explosive devices, and BigDog, which is designed to help soldiers carry heavy equipment. Security robots include autonomous mobile systems such as Cobalt.
Using robots for research applications

The vast majority of today's robots are born in universities and corporate research laboratories. Although these robots can perform useful tasks, their main purpose is to help researchers conduct research. So although some bots may be described with other categories, they can also be called research bots.
Self-driving cars

Many robots can go to different places without the need of human control. Today, with the increase in the number of self-driving cars, it is more likely that you will see a car on the street that goes around without the need for driver control.
Remote presence robot

Telepresence bots allow you to be in a place without actually going there. You log into a robot via the internet and drive it, see around and talk to people. Workers can use it to collaborate with engineers, and doctors can use it to examine patients.
Underwater robots

The favorite place of these robots is in the water. They range from deep-sea vessels like the Aquanaut, diving humanoids like the Ocean One, and bio-inspired systems like the ACM-R5H snake robot.
What is Airnex/technology/humanoid robot? Review of humanoid robots
Technology
What is a humanoid robot? Review of humanoid robots
2019/11/24
Approximate study time 8 minutes

Time waits for nothing. Apparently, this case also shows the same with the speed of updating technology these days. Moore's Law has already been broken. Because always, technological advancements taken from science fiction and action movies are made to implement fictional tools in reality. On October 26, 2017, a female robot named "Sofia" with advanced capabilities was granted the citizenship of Saudi Arabia. Who would have thought it would be possible one day when C-3PO in the "Star Wars" franchise was one of the first and most memorable humanoid robot characters in the movies.
c
Personal home assistants:
Combining the Internet of Things with these robots creates a personal home assistant that manages electricity, light, sound, and temperature in the home using a home automation system.
virtual reality:
Combining virtual reality with these robots and programming them to replicate our movements will give you a copy of yourself that will come in handy in a fire, flood, experiment, or other dangerous situation where human life is at stake. We can find various applications of these futuristic robots but let's talk about the most important application. One thing that will be very useful for people in need: the artificial limb.
Suggested article: What is the Internet of Things? Getting to know the application of IoT Internet of Things

The topic of artificial organs:
One of the main reasons for prostheses is that they look like real body parts. It can be used to transplant or replace a part of the body that connects to the body's nervous system. A person without a hand after the elbow can arrange a hand for himself to connect to the nerves under the arm near the shoulder. Each nervous and stretching movement of the inner part of the arm gives a unique signal to the brain.
This signal will correspond to a specific hand movement. The modular prosthetic limb recognizes the muscle pattern and the movement in the hand is performed accordingly. Let's not forget that each of these will happen in real time. Just by stimulating a thought, you can move the hand just like your own hand. It will change the way certain people live. This technology will be useful for people who have had an accident and lost a limb or other part of their body.
Also, the best technology available today has more than 100 sensors in its sole, which provides real sensory capabilities of touch on the surface of artificial arms and legs, which provides sensory innervation and good feeling.
The advancements of these humanoid robots are not endless. Major innovations and developments of this technology happen every day in this field. Numerous applications from industry until now in daily life continue the trend of these neutral materials and lead them upwards.
In the near future, robots will replace many jobs. This issue is being discussed all over the world. The idea of ​​"basic income for all" was introduced as one of the options while maintaining stagnation and unemployment. Governments of several countries have resisted and expressed their thoughts on banning artificial intelligence, while some governments were interested in the applications of humanoid robots and their replacement for jobs.
The importance of these products can be easily seen by increasing the issues, merits and demerits discussed in homes. There is one thing for sure, and that is that with a combination of the best artificial intelligence and the best in the physical structure of the circuit, a product can be known that will take over the world very quickly with any limitations. The development of this kind of humanoid robots has already started, because we can see the robot Sophia as an excellent example of artificial intelligence with a full human physical structure.
What is a robotic arm? Full introduction of industrial arms
11/06/2019
Approximate reading time is 4 minutes

Contents [show]
Industrial arms or robotic arms are machines used to handle or control materials without making direct contact. Basically, it is used to control radioactive or biologically dangerous objects that are difficult for a person to control. But now they are used in many industries to do things like lifting heavy objects, continuous welding with high precision, etc. Apart from industries, they are also used as surgical tools in hospitals. Today, doctors widely use robotic arms in their operations.
Before I tell you about the types of industrial arms, I want to talk about joints.
A joint has two references. The first one is the usual fixed frame of reference. The second reference frame is not fixed and moves relative to the first reference frame depending on the joint position (or joint value) that defines its configuration.
Here we will discuss two joints that are used in the construction of various types of industrial arms.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
1. Rotary joint robotic arm
They have one degree of freedom and describe rotational motions (1 degree of freedom) between bodies. Their configuration is defined by a value that indicates the amount of rotation around the z-axis of their first reference frame.
You can see here the rotational joint between the two bodies. Here the follower can rotate around its base.

2. Prism joint robotic arm
Prismatic joints have one degree of freedom and are used to describe translational motions between bodies. Their configuration is defined by a value that shows the amount of transfer in the Z axis of their first reference frame.
You can see here different prism joints in one system.

Different types of robotic arms
Different types of industrial arms are used in industries according to the needs. Some of them are as follows:
Robot Cartesian coordinates
In this industrial robot, its main 3 axes have prismatic joints or they move linearly between each other. Cartesian robots are very suitable for glue distribution, for example, in the automotive industry. The main advantage of Cartesians is that they are able to move in several linear directions. Also, they are able to draw a straight line and their planning is easy. The disadvantages of the Cartesian robot are that they take up a lot of space because most of the space of this robot is unusable.
Suggested article: conversion

PUMA robot
PUMA (Programmable Universal Machine for Assembly or Programmable Universal Arm) is the most common industrial robot used in assembly, welding and university laboratories. This robot is more similar to the human arm than the SCARA robot and has much more flexibility than it, but this also reduces its accuracy. Therefore, they are used in tasks that require less precision, such as assembly, welding, and moving objects. This robot has three rotational joints, but not all joints are parallel, the second joint from the base is perpendicular to the other joints (orthogonal mode). ) are This makes PUMA compatible in all three axes X, Y and Z. Its disadvantage is low accuracy, so it cannot be used in sensitive applications and applications that require high accuracy.

Polar robots
They are sometimes considered spherical robots. These are stationary robot arms with spherical or near-spherical casings that can be positioned in a polar coordinate system. They are more complex than Cartesian and SCARA robots, but their control solution is less complex. These robots have two rotary joints and one prismatic joint to create an almost spherical working space. Its main applications are in the production line and pick-and-place robot operations.
Suggested article: Teaching image processing with OpenCV in Python and doing an example (#1)

In terms of wrist design, it has two configurations.
Pitch-Yaw-Roll (XYZ) is like a human arm and Roll-Pitch-Roll is like a spherical wrist. The spherical wrist is more popular than others because it is mechanically simpler to implement. It shows special settings that can be detected and thus avoided when working with the robot. The balance between the simplicity of robust solutions and the existence of unique configurations is suitable for the design of the spherical wrist, and this is the reason for its success.
Teaching Arduino Arduino projects
Automatic disinfecting robot with infrared lamp and Arduino
10/09/2019
Approximate reading time is 5 minutes

Contents [show]
These days, due to the spread of the corona virus, the lives and livelihoods of many people have changed. The only way to minimize the spread is to maintain social distance and follow hygiene protocols. Also, these days the need to disinfect the environment has increased and we cannot do this continuously. In this Arduino project, we want to solve this problem by making a disinfectant robot. The robot we build in this project uses UV lamps to emit ultraviolet rays and destroy viruses. Also, this robot is fully automatic and has an obstacle avoidance system. That is, when you turn it on, it will rotate in the house and emit radiation to objects, and as a result, the disinfection process will be completely automatic.
As mentioned, our robot has ultraviolet LEDs. It has been discovered that viruses, bacteria and pathogens are inactivated by exposure to ultraviolet (UV) light. This light destroys the genetic material in pathogenic agents. Viruses like covid-19 (coronavirus) can survive on surfaces for a long time. Irradiating ultraviolet rays on them will make them inactive.
Video display
00:00
00:45
See the rest of the projects related to Corona:
• Non-contact thermometer with Raspberry Pi (send email with image)
• Elevator control with hand movement with Arduino board (without contact)
• Making a non-contact thermometer with Arduino (for Corona and recording in Excel)
• Cheap corona thermometer project with Arduino and DS18B20 sensor
• Corona thermometer project with Android mobile and Arduino (image recording and Excel output)
Disinfectant robot circuit with Arduino
The image of the circuit may seem complicated at first, but it is very simple. We have three ultrasonic sensors that detect obstacles. We connect the Ground and VCC legs of the ultrasonic sensors to the Ground and 5V of the Arduino. The Trig and Echo pins of the sensors are connected to the shown pins of the Arduino. We use the L293D motor driver to control the motors. Ultraviolet LEDs are also always on, so they are directly connected to the power supply with a 330 ohm resistor. We use a 7.4V battery to power the robot and a 7805 regulator to convert it to 5V.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store

Required parts
The parts used in the robot are very common and you will easily find them in different stores.
• Arduino Pro Mini board
• HC-SR04 ultrasonic module (three pieces)
• L293D motor driver
• 5 volt motors
• Ultraviolet LEDs (eight numbers)
• 7805 voltage regulator
• 7.4 V lithium ion battery
• 330 ohm resistance (ten pieces)
Suggested article: Measuring capacitor capacity with Arduino (making a capacitor meter)
Get the required parts from the Ironex parts store.
Making a housing for an Arduino-based disinfectant robot
The following pictures will help you to make the robot housing. You can create the container according to the available materials, your creativity and your needs. The best option is to use sheets. Cut the housing as in the pictures and put the LEDs and the ultrasonic module in them.


Arduino code for surface disinfection robot with ultraviolet light
The complete code of the project is placed at the bottom of the page. Here we check the important parts of the code. We do not use a special library to understand the information received from ultrasonic sensors. At the beginning of the code, we determine which Arduino pins Trig and Echo are connected to. In this project, we have three echo bases and three trigger bases. Note that 1 means the left sensor, 2 the front sensor and 3 the right sensor.
const int trigPin1 = 3;
const int echoPin1 = 5;
const int trigPin2 = 6;
const int echoPin2 =9;
const int trigPin3 = 10;
const int echoPin3 = 11;
Then we defined int type variables for the distance and chose the (long) type for the duration. Again, we have three of each. I suggest you to see the article on variable types in Arduino.
long duration1;
 long duration2;
 long duration3;
int distanceleft;
int distancefront;
int distanceright;
In the void setup section, we must define the type of Arduino pins that are connected to the sensors. For Trig pins, we should consider the output type and for Echo pins, we should consider the input type. Also, we start the serial communication with the rate of 9600.
pinMode(trigPin1, OUTPUT);
pinMode(trigPin2, OUTPUT);
pinMode(trigPin3, OUTPUT);
pinMode(echoPin1, INPUT);
pinMode(echoPin2, INPUT);
pinMode(echoPin3, INPUT);
Serial.begin(9600);
Also, the pins connected to the motor driver are completely defined as outputs.
pinMode(4, OUTPUT);
pinMode(7, OUTPUT);
pinMode(8, OUTPUT);
pinMode(12, OUTPUT);
In void loo[, we have three sections for three sensors. All parts work the same but each part works for different sensors. In each section, we first set the Trig base High for 10 microseconds and then use the pulsein() command to obtain the duration of the ultrasonic wave going back and forth to the objects. Using a simple formula and the speed of sound in air, which is 340 meters per second, we calculate the round trip distance. Since we need the distance, we divide the dilution and return distance by 2. Finally, we store the distance of each sensor from the objects in front of it in the corresponding variable.
If you have any questions about this article, ask in the comments section
digitalWrite(trigPin1, LOW);
delayMicroseconds(2);
digitalWrite(trigPin1, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin1, LOW);
duration1 = pulseIn(echoPin1, HIGH);
distanceleft = duration1 * 0.034 / 2;
Serial.print("Distance1: ");
Serial.println(distanceleft);
After knowing the distance of each sensor from the obstacle, we control the motors with the if command. It is very simple. We considered the threshold distance to be 15 cm. You can change this value. Using this condition, for example, when the left sensor is less than 15 cm away from the obstacle, it moves to the right.
if ((distanceleft <= 15 && distancefront <= 15 && distanceright > 15) || (distanceleft <= 15 && distancefront > 15 && distanceright > 15))
Below we have explained the code used to move the left, right and front motor separately.
Suggested article: delayMicroseconds command in Arduino (delay microseconds)
This part of the code is used to move the robot to the right:
 digitalWrite(4, HIGH);
 digitalWrite(7, LOW);
 digitalWrite(8, HIGH);
 digitalWrite(12, LOW);
This part of the code is used to move the robot to the left:
 if ((distanceleft > 15 && distancefront <= 15 && distanceright <= 15) || (distanceleft > 15 && distancefront > 15 && distanceright <= 15) || (distanceleft > 15 && distancefront <= 15 && distanceright > 15) )
 digitalWrite(4, LOW);
digitalWrite(7, HIGH);
digitalWrite(8, HIGH);
digitalWrite(12, LOW);
This part of the code is used to move the robot directly:
 if ((distanceleft <= 15 && distancefront > 15 && distanceright <= 15) || (distanceleft > 15 && distancefront > 15 && distanceright > 15))
 {
 digitalWrite(4, HIGH);
 digitalWrite(7, LOW);
 digitalWrite(8, HIGH);
 digitalWrite(12, LOW);
 }

Items in the file: full source
Airnex/Raspberry Pi training/Car robot control project with Android mobile and Raspberry Pi
Raspberry Pi tutorial, Raspberry Pi project
Car robot control project with Android mobile and Raspberry Pi
04/28/2019
Approximate reading time is 6 minutes

Contents [show]
hello We prepared the car robot control project with Android and Raspberry Pi.
Making a control robot with Android Bluetooth and Raspberry Pi
Raspberry Pi is very popular for IoT projects due to its ability to seamlessly communicate wirelessly over the Internet. Raspberry Pi 3 has Wi-Fi and Bluetooth, and Bluetooth is a very popular wireless communication protocol. In this Raspberry Pi project, we want to control a robot using Raspberry Pi and Bluetooth

Now open the bl Bluetoothctl program with the following command:
sudo bluetoothctl
You can check all the instructions of the Bluetooth app by typing "help". Then we must enter the following commands in the specified order:
[bluetooth]# power on
[bluetooth]# agent on
[bluetooth]# discoverable on
[bluetooth]# pairable on
[bluetooth]# scan on
After sending the last command, "scan on", you will see your Bluetooth device (mobile phone) in the list. Make sure your mobile phone's Bluetooth is turned on and visible to nearby devices. Then copy the MAC address of your device and pair it using the given command:
pair <address of your phone>
Then you will be asked for a password for this terminal, then type the password there and hit enter. Then enter the same password on your mobile phone. Congratulations, your Android phone is now successfully paired with Raspberry Pi.

As mentioned earlier, you can use the desktop interface to pair a mobile phone. After installing Blueman, you will see a Bluetooth icon on the right side of the Raspberry Pi desktop as shown below, which you can use to pair your mobile phone with the Raspberry Pi easily.

Choosing a toy car:
In this project, we have used a toy car. This car has two DC motors in the front and rear. The front engine is used to steer the car in the sense of turning left or right (like the real steering feature of the car). And the rear engine is used to drive the car in the backward and forward directions. You can use any toy car that has two DC motors to turn the front and back wheels.
Robot control project circuit with Android and Raspberry Pi
In this car control project, we have used L293D motor driver to control the motors. The power bank is used to provide the required power for the motors and Raspberry Pi board. Note that the power bank may limit your speed due to its heavy weight, so you can also use regular or lithium batteries. The image below shows all the connections of this project.
Get the required parts from the Ironex parts store.

Note: Do not apply more than 5V to the Raspberry Pi.
Remote car control with BlueTerm Android app
Now after pairing the mobile phone, we need to install an Android app to communicate with the Raspberry Pi using the Bluetooth serial adapter. Here we installed the BlueTerm program. Download BlueTerm software
You can also use any other Bluetooth terminal program that supports RFCOMM communication.
After downloading and installing the BlueTerm application, run the Python code given at the bottom of the page and select the paired Raspberry Pi device from the BlueTerm application.

After successful connection, you will see the message connected: raspberrypi at the top of the software.
Suggested article: Analog to digital tutorial on Raspberry Pi with Python

Now you can just enter the following commands in the BlueTerm program to make the car move in the desired direction. Press "q" to exit the program. You can also use the Google Voice typing keyboard to control this car using your Voice.
Commands:
• F – Move forward
• B – Move backwards
• S – Stop
• L – move forward left
• R – move forward right
• A – move to the rear left
• P – Move right back
• Q – Exit

Source robot controlled by Android and Raspberry Pi
Python program to control Raspberry Pi GPIO pins with Android app is very simple. We just need to learn a little about the code for Bluetooth RFCOMM communications. First, we need to import the bluetooth socket library, which allows us to control bluetooth with python language. We have installed the library in the previous section. The complete code of the project is placed at the end of the page in the downloadable file. Here we explain some parts of the code.
Then we include the header files and define the pins for the motor, which are LOW by default.
import bluetooth
import time
import RPi.GPIO as GPIO

m11=18
m12=23
m21=24
m22=25
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(m11, GPIO.OUT)
GPIO.setup(m12, GPIO.OUT)
GPIO.setup(m21, GPIO.OUT)
GPIO.setup(m22, GPIO.OUT)
GPIO.output(m11, 0)
GPIO.output(m12, 0)
GPIO.output(m21, 0)
GPIO.output(m22, 0)
The code responsible for Bluetooth communication is below:
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
port = 1
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print "Accepted connection from ", address
Here we can understand them linearly:
server_socket = bl Bluetooth.BluetoothSocket: Create socket for Bluetooth RFCOMM communication.
server_socket.listen (1): The server accepts a connection once.
client_socket, address = server_socket.accept(): The server accepts the connection request and assigns the MAC address to the address variable.
data = client_socket.recv(1024): Receives data through client_socket and assigns it to variable data. A maximum of 1024 characters can be received at the same time.
After this, we have created some functions that are responsible for moving the car in the desired direction:
def left_side_forward (), def Right_side_forward (), def def (), def left_side_reverse (), def Right_side_reverse (), def reverse () def stop ( )
These functions are called in order when we enter L, R, F, A, P, B, S in the Android application and the robot moves accordingly.
data=""
while 1:
 data= client_socket.recv(1024)
 print "Received: %s" % data
 if (data == "F"):
 forward()
 elif (data == "L"):
 left_side_forward()
 elif (data == "R"):
 right_side_forward()
 elif (data == "B"):
 reverse()
 elif (data == "A"):
 left_side_reverse()
 elif (data == "P"):
 right_side_reverse()
 elif data == "S":
 stop()
 elif (data == "Q"):
 print("Quit")
 break
client_socket.close()
server_socket.close()
Items in the file: complete source, schematic
Airnex/Raspberry Pi training/Building a ball tracking robot with Raspberry Pi and Processing
Raspberry Pi tutorial, Raspberry Pi project
Building a ball tracking robot with Raspberry Pi and Processing
04/28/2019
Approximate reading time is 6 minutes

Contents [show]
hello We prepared the construction of the ball tracking robot with Raspberry Pi and Processing.
Object tracking robot project with Raspberry Pi
The field of robotics, artificial intelligence and machine learning is rapidly evolving, which will surely change the way humans live in the near future. Robots are thought to communicate and interact with the real world through sensors and machine learning processing. Image recognition and processing is one of the common parts in robotics, where robots understand objects by seeing the real world through cameras and sensors. In this Raspberry Pi project, we use the power of Raspberry Pi to build a robot. This robot can track the ball. Just like robots playing football.
OpenCV is a very popular and open source tool used for image processing, but in this tutorial to keep the project simple, we will use Processing IDE.
The following video will help you understand how this project works.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
Video display
00:00
00:59
Install Processing on Raspberry Pi
We will use the processing environment to program the Raspberry Pi. That is, we do not use Python in this project. So follow the steps below:
Step 1: Connect your Raspberry Pi to your monitor, keyboard and mouse and turn it on.
Step 2: Make sure the Pi is connected to an active internet connection as we are downloading a few items.
Step 3: Click on Processing ARM, to load the Raspberry Pi Processing IDE. The download will be in the form of a ZIP file.
Step 4: After downloading, extract the files into your ZIP folder in your desired directory. I extracted it to the desktop.
Step 5: Now open the extracted folder and click on the file called Processing. It should look like the window that opens like the image below.

Step 6: This is the environment where we will type our codes. For people who are familiar with Arduino, working with this software is very simple because they are very similar to each other.
Step 7: To work with the ball we need two libraries to be installed. Click Sketch -> Import Library -> Add Library. The following box will open.

Step 8: Use the text box on the top left to search for Raspberry Pi and hit enter, your search result should look something like this.
If you have any questions about this article, ask in the comments section
Suggested article: Raspberry Pi and Python image and e-mail home security system project

Step 9: Search for “GL Video” and “Hardware I/O” libraries and click install to install it. Be sure to install both libraries.
Step 10: Depending on your internet, the installation will take a few minutes.
Ball tracking robot project circuit with Raspberry Pi
The circuit schematic of the ball tracking robot project with Raspberry pi is shown in the image below.

As you can see, this circuit consists of a PI camera, a motor driver module and a pair of motors connected to the Raspberry pi. The complete circuit is powered by a power bank. As the details of the pins are not mentioned in the Raspberry Pi image, we need to check the pins using the image below.

To drive the motors, we need four pins (A, B, A, B). These four pins are connected from GPIO14, 4, 17 and 18 respectively. The orange and white wires together form a motor connection. So we have two similar pairs for two engines.
As shown in the picture, the motors are connected to the L293D motor driver module, and the driver module is powered by a power bank. Make sure the GND of the power bank is connected to the GND of the Raspberry Pi, only then will your connection work.
Required parts
1. Raspberry Pi board
2. Camera module with ribbon cable
3. L293D motor driver
4. Power bank or any portable power source
Get the required parts from the Ironex parts store.
Note: Having a screen is required when programming the Raspberry Pi because only then can you view the camera footage.
Ball tracking project code with Raspberry Pi
The complete Processing program of this project is provided at the end of this page. Here we explain some parts of the code.
The concept of the program is very simple. Although the purpose of this project is to track the ball, we don't really intend to do that. We just want to identify the ball using its color. As we all know, movies are nothing but successive frames of images. So we take pictures successively and compare its pixels with the color of the ball. If they match, we can say that we have found the ball. Using this information, you can find the position of the ball. According to the received information, if the match is on the right side of the image, we move the robot to the right, and the same for other directions.
As always we start by importing the two libraries we downloaded. This can be done by the following two lines. The hardware I/O library is used to access the GPIO pins of the PI directly from the Processing environment, and the glvideo library is used to access the Raspberry Pi camera module.
import processing.io.*;
import gohai.glvideo.*;
Inside the setup void (), we set the output pins for the motor control and also receive the video from the pi camera and resize it into a window of size 320 * 240.
void setup() {
 size(320, 240, P2D);
 video = new GLCapture(this);
 video.start();
 trackColor = color(255, 0, 0);
 GPIO.pinMode(4, GPIO.OUTPUT);
 GPIO.pinMode(14, GPIO.OUTPUT);
 GPIO.pinMode(17, GPIO.OUTPUT);
 GPIO.pinMode(18, GPIO.OUTPUT);
}
void draw() is like an infinite loop. The code inside this loop will be executed until the program terminates. If the camera source is available, we read the video that comes out of it.
void draw() {
 background(0);
 if (video.available()) {
 video.read();
 }}
Then we start dividing the video frame into pixels. Each pixel has some red, green and blue color. These values ​​are stored in variables r1, g1 and b1
 for (int x = 0; x < video.width; x ++ ) {
 for (int y = 0; y < video.height; y ++ ) {
 int loc = x + y*video.width;
 // Current color
 color currentColor = video.pixels[loc];
 float r1 = red(currentColor);
 float g1 = green(currentColor);
 float b1 = blue(currentColor);
To detect the color of the ball first, we have to click on the color. After clicking, the color of the ball is stored in a variable called trackColour.
void mousePressed() {
 // Save color where the mouse is clicked in trackColor variable
 int loc = mouseX + mouseY*video.width;
 trackColor = video.pixels[loc];
}
Once we have the preset color and the current color, we need to compare them. This comparison is done using the dist function. This function checks how close the current color is to the preset color.
float d = dist(r1, g1, b1, r2, g2, b2);
If the color similarity is greater than a certain range, we assume that we have found the ball. Then we store the location of that pixel in the closestX and closestY variables to find the location of the ball.
if (d < worldRecord) {
 worldRecord = d;
 closestX = x;
 closestY = y;
 }
We also draw an ellipse around the found color to indicate that the color has been found.
if (worldRecord < 10) {
 // Draw a circle at the tracked pixel
 fill(trackColor);
 strokeWeight(4.0);
 stroke(0);
 ellipse(closestX, closestY, 16, 16);
 println(closestX,closestY);
Finally, we can compare the position of the nearest X and the nearest Y and adjust the engines so that the color reaches the center of the page. The following code is used to rotate the robot to the right because it is determined that the X color position is on the left side of the screen (<140)
 if (closestX<140)
 {
 GPIO.digitalWrite(4, GPIO.HIGH);
 GPIO.digitalWrite(14, GPIO.HIG
The router robot is able to track the line with the help of an infrared sensor. This sensor has IR transmitter and IR receiver. The infrared transmitter transmits the light and the receiver (Photodiode) waits for the transmitted light to be reflected and returned. Not all surfaces reflect IR light, only a white surface can fully reflect them, and a black surface will completely absorb them as shown in the figure below.

In this Raspberry pi project, we use two IR sensors to check whether the robot is moving on the line or not. These motors need high current. Hence we use a motor driver module like L293D.
Each infrared sensor is placed on one side of the line. If neither sensor detects a black line, the Raspberry Pi commands both motors to run.

If the left sensor is on the black line, the robot moves to the left. This means that the right engine turns off and only the left engine moves.

If the right sensor is placed on the black line, the robot will turn to the right. It means that the left engine turns off and only the right engine moves.

If both sensors are on the black line, the robot will stop.

Line following robot circuit with Raspberry Pi
The circuit diagram of the project is shown in the picture below.

As you can see, the circuit includes two infrared sensors and a pair of motors connected to the Raspberry Pi. We have fed the circuit using a power bank, you can use your favorite method.

If you have any questions about this article, ask in the comments section
Suggested article: Threaded programming with two cores on Raspberry Pi Pico
As shown in the picture, the top left corner PI pin is the +5V pin, we use this +5V pin to power the IR sensors. Then we connect the GND pins to the GND of the IR sensor and the motor driver module using the black wire.
To drive the motors, we need four pins (A, B, A, B). These four pins are connected in GPIO 14, 4, 17 and 18 respectively. The orange and white wires together form a motor connection. So we have two similar pairs for two engines.
As shown in the picture, the motors are connected to the L293D motor driver module, and the driver module is powered by a power bank. Make sure the GND of the power bank is connected to the GND of the Raspberry Pi, only then your connection will work.
Required parts
1. Raspberry Pi 3 or any other model
2. IR infrared sensor - two numbers
3. DC Gear motor – two numbers
4. L293D motor driver
Get the required parts from the Ironex parts store.
Raspberry Pi Black Line Follower Robot Programming
When you're done with assembly and connections, your robot should look something like this.

Now it's time to program our robot. The complete code of the project is placed at the bottom of the page. Here we explain some parts of the code.
We want to import the GPIO file from the library. The following code allows us to program the GPIO pins of the Raspberry Pi board. Also, as in the previous part of the tutorial, we change the name of GPIO to IO. And every time we want to refer to the GPIO pins, we use the word IO.
import RPi.GPIO as IO
Sometimes, the GPIO pins we are trying to use may perform other functions. In this case, we will receive warnings when running the program. The following command tells PI to ignore the warnings and continue with the program.
IO.setwarnings(False)
We can enter Raspberry Pi GPIO pins or its pin number or GPIO number. For example, pin 35 on the Raspberry pi board is the same as GPIO pin 19. So we can introduce it with 19 or 35.
IO.setmode (IO.BCM)
We set 6 pins as input and output pins. The first two pins are the input pins for reading the values ​​of the infrared sensor. The next four are the output pins that control the right and rear motors.
IO.setup(2,IO.IN) #GPIO 2 -> left infrared sensor
IO.setup(3,IO.IN) #GPIO 3 -> Right IR sensor

IO.setup(4,IO.OUT) #GPIO 4 -> terminal A of the right motor
IO.setup(14,IO.OUT) #GPIO 14 -> terminal B of the right motor

IO.setup(17,IO.OUT) #GPIO 17 -> Terminal A of left motor
IO.setup(18,IO.OUT) #GPIO 18 -> terminal B of left motor
The infrared sensor shows the value True if you sense the white surface, and as mentioned above, when both sensors are true and detect the white surface, the robot moves forward.
 if(IO.input(2)==True and IO.input(3)==True): #any sensor on the white surface
 IO.output(4,True) #1A+
 IO.output(14,False) #1B-

 IO.output(17,True) #2A+
 IO.output(18,False) #2B-
If a sensor is on the black line, the line following robot must move on the opposite side. That is, if the right sensor is on the black line, the robot moves to the left.
elif(IO.input(2)==False and IO.input(3)==True): #rotate right
 IO.output(4,True) #1A+
 IO.output(14,True) #1B-

 IO.output(17,True) #2A+
 IO.output(18,False) #2B-
elif(IO.input(2)==True and IO.input(3)==False): #rotate left
 IO.output(4,True) #1A+
 IO.output(14,False) #1B-

 IO.output(17,True) #2A+
 IO.output(18,True) #2B-
If both sensors are on the same black line, both motors are disabled and the robot stops. This state often occurs at the end of the path.

It often happens at the end of the path.
 else: #success bot
 IO.output(4,True) #1A+
 IO.output(14,True) #1B-

 IO.output(17,True) #2A+
 IO.output(18,True) #2B-
Load the Python code on your Raspberry Pi board and run it. All you have to do is make a path using, for example, black electrical tape on a white surface. It is not necessary for the background surface to be completely white, but the farther it is from black, the better.
Suggested article: LED control training with Raspberry Pi and Python (blinking LED)
Items in the file: complete circuit schematic, complete source
Internet of things training, Raspberry Pi project training, Raspberry Pi projects, Internet of things
Building a rescue robot with a camera with Raspberry Pi
04/23/2019
Approximate reading time is 5 minutes

Contents [show]
hello We prepared the project of building and controlling a car robot with a camera with Internet and Raspberry Pi.
Designing a rescue robot with Raspberry Pi and viewing the image on the Internet
In this Raspberry Pi project, we are going to build a robotic car that is controlled through the Internet and has a webcam to send images. This robot can be a useful and cheap security and espionage tool. This project can be included in the category of Internet of Things projects because we control it through the Internet and receive the images. This project can be used as a rescue robot during fire and earthquake.
Video display
00:00
01:30

This robot has a webcam through which you can receive live video and the interesting thing is that you can control and move the robot through an internet browser. Since the robot can be controlled through an internet browser, it means it can be controlled both through a laptop and through a mobile phone. We create an HTML web page that has links to move forward, move backward, move right, and move left. By clicking on any link, the robot will be directed to the desired path. We have used Motion to receive video directly from the camera and Flask to send commands from the web page to the Raspberry Pi with Python.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
The performance video of the project is placed at the bottom of the page.
Install and configure Motion to receive video from Raspberry Pi
Motion is an open source software developed for Linux. The package detects motion and starts recording video from it. By installing “Motion” on your Raspberry Pi, you can magically turn your Raspberry Pi into a security camera. This package is used to receive live video, make Timelapse videos, take snapshots, etc. Motion captures and saves video whenever it detects motion or any disturbance in the field of view. By entering the Raspberry Pi IP address along with the port, you can view the live video in the web browser.
Here you need to run just a few commands. Before that, check that your Raspberry Pi is connected to the internet. Use LAN or Wi-Fi and follow the steps below:
Step 1: First run the following command to update Raspbian system on Raspberry Pi:
sudo apt-get update
Step 2: Then install the “Motion” library using the following command:
sudo apt-get install motion
Step 3: Now set Daemon Motion to Yes in file: /etc/default/motion, so that it always runs. Editing is done with the following command.
sudo nano /etc/default/motion

Then save the file by pressing “CTRL + X”, then “Y” and Enter.
Suggested article: Controlling home appliances with Android mobile and ESP32 Bluetooth board
Step 4: Now we need to set the permission on the Target Directory (/var/lib/motion/), where the motion, video recordings and image files are stored. We need to set "Motion" as the owner of this directory by issuing the following command:
sudo chown motion:motion /var/lib/motion/
This permission is required otherwise you will receive an error when checking the status of the Motion service.
You can check the status of the service using this command: sudo service motion status
If you have any questions about this article, ask in the comments section
Step 5: Now the job is almost done. We just need to set a config option in the Motion configuration file (/etc/motion/motion.conf) which is stream_localhost to Off. We need to turn this off, otherwise the video will not be viewed on the network. Edit the config file of the Motion package with “nano” and turn it off as shown below:
sudo nano /etc/motion/motion.conf

Now you need to restart the Motion package using the following command:
sudo /etc/init.d/motion restart
Now we are done in this part. Just enter the Raspberry Pi's IP and enter port 5010 at the end to see the image. such as:
192.168.43.199:5010
If the Raspberry Pi board version used is before 3, you need a Wi-Fi dongle for this project.
Setting up Flask on Raspberry Pi
Here we create a web server using Flask that provides a way to send commands from the web page to the Raspberry Pi. Flask allows us to run Python scripts through a web page. We can send data from Raspberry pi to web browser

Here you can enter the IP address on which the video will be played on the web page using the img src tag. Change the IP address according to the Raspberry Pi but keep the port the same.
<img src="http://192.168.43.199:8081" /> <!--Enter Raspberry Pi IP Address-->
You should enter this code in an editor like Notepad and then save it with .html extension. Then according to your Python script folder, place it in the /templates folder. Be sure to do this step because otherwise the project will not work.
Suggested article: ESP32 programming with Micropython
You can check the IP address of your Raspberry Pi using the ifconfig command:
ifconfig
Rescue robot project circuit with Raspberry Pi
The picture below shows the circuit diagram of this project.
Get the required parts from the Ironex parts store.

Use the type of wheels and chassis related to you and available items. We have used a power bank to power the circuit. You just need to connect some wires to the DC motors and L293D motor driver module.

As mentioned, open the IP address of your Raspberry Pi along with port 5010. Then you will see the web page which has four links to move the robot and on the left side of the page you will see the live image received from the robot.
Items in the file: complete source, complete schematic
Teaching Arduino Arduino projects
Construction and control of robotic arm with Arduino and servo motor
04/23/2019
Approximate reading time is 6 minutes

Contents [show]
hello We prepared the construction and control of the robotic arm with Arduino and servo motor.
Learning how to design robot arms with Arduino
In this Arduino project, we are going to build a robotic arm based on Arduino Uno. Here we design the arm using cardboard and you can use ready-made or 3D printed arms. The complete steps of designing the robot arm are explained below. In this project, we use the Arduino board to control the servo motors that are connected to the arm parts. We can also use this project as a robotic crane. This project is very suitable for beginners who want to learn how to make a simple robot at low cost. Also here you will learn how servo motors work.
Our robotic arm is controlled by four potentiometers connected to Arduino. Each potentiometer is used to control a servo motor. You can easily move different parts of the robot by turning these potentiometers. With a little practice and finesse, you can easily pick up and move objects. We have used small servo motors for this tutorial. You can use this project for heavy operations, but you should choose stronger servo motors.
The following video will help you understand how this project works.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
Video display
00:00
00:58
What is a servo motor?
Servo motor is a combination of DCT motor, position control system and gears. Servos have many uses in the modern world and that is why they are available in various shapes and sizes. In this tutorial, we will use the SG90 servo motor, which is one of the most popular and cheapest servos. SG90 is a 180 degree servo. Therefore, with this servo, we can set the axes from 0 to 180 degrees.

A servo motor generally has three wires, one for positive voltage, one for GND, and one for position adjustment. The red wire is connected to power, the brown wire is connected to gnd, and the yellow (or white) wire is connected to the input signal.
In a servo, we have a control system that takes the PWM signal from the signal pin. It decodes the signal and gets the duty cycle from it. After that, it compares this ratio with predefined position values. If there is a difference in the values, it adjusts the servo position accordingly. So the axis position of the servo motor is based on the PWM duty cycle on the signal pin.
If you are not familiar with duty cycle and PWM, see the opposite tutorial: Tutorial on setting up PWM with Arduino
PWM signal frequency is different based on the type of servo motor. For SG90, PWM signal frequency is about 50Hz. To find out the operating frequency of your servo, check the datasheet of the corresponding model. After selecting the frequency, another important point here is the DUTY RATIO of the PWM signal.
The table below shows the servo position for a specific duty cycle. By choosing the right value, you can place the servo at any angle. For example, for 45º, the duty ratio should be 5 or 5%.
Duty cycle position
0 degree 2.5
90 degrees 7.5
180 degrees 12.5
Making a robotic arm with cardboard
Choose a flat and hard surface as the base of the arm. Place a servo motor in the middle and secure it in place with glue. Make sure the servo can fully rotate 180 degrees as shown below.

Place a small piece of cardboard on top of the first servo and then glue the second motor servo onto this board and secure it in place. The servo rotation should match the diagram.

If you have any questions about this article, ask in the comments section
Take some cardboard and cut it into 11 x 3 cm pieces. Make sure your cardboard is sturdy and not soft. Cut a rectangular hole at one end (0.8cm from the bottom) just enough to accommodate another servo motor, and firmly fit the servo gear at the other end with screws or glue. Then put the third cedar in the first hole.

Now cut another piece of cardboard with the lengths shown in the figure below and glue another rib at the bottom of this piece.

Now, as shown in the picture, glue the fourth and last piece on the edge of the second piece.

By doing this, the two pieces look connected.

Then connect it to the first servo so that it looks something like the picture below.

For the hook, cut two more cardboards 1cmx7cm and 4cmx5cm. As shown in the figure, glue them together and glue the final rib on the same edge.

Attach this piece to the top of the arm. The construction of the robotic arm is finished.

Robotic arm project circuit with Arduino
The circuit connections of the robotic arm with Arduino are shown below.

The voltage received from the potentiometers has high noise, so we have used resistors for this purpose. The voltage received from the potentiometers is then fed to the analog to digital channels in Arduino. We use four ADC channels of Arduino for this purpose.
Required parts
1. Arduino Uno board
2. 1000uF capacitor – four numbers
3. 100nF capacitor – four numbers
4. Servo motor SG 90 - four pieces
5. 10 kilo ohm potentiometer - four numbers
6. Power supply (5v)
Suggested article: Setting up a pulse sensor with Arduino (Pulse Sensor heartbeat)
Get the required parts from the Ironex parts store.
Robotic arm code with Arduino
Arduino has six analog to digital channels. As mentioned, we use four ADC channels to control the robotic arm. The analog to digital Arduino Uno has 10-bit precision. Therefore, the analog value of 0-5 volts is converted to a digital value of 0-1023. That is, approximately 4.9 millivolts per unit. The complete code of the project is placed at the end of the page in the downloadable file. Here we explain some parts of the code.
Now, in order for the UNO to be able to convert the analog signal into a digital signal, we must use the ADC channel of the Arduino UNO channel with the help of the following functions:
1. analogRead(pin);
2. analogReference();
3. analogReadResolution(bits);
Arduino ADC channels have a default reference value of 5V. This means that we can give a maximum input voltage of 5V to the ADC conversion on each input channel. Since some sensors provide voltages of 0-2.5V, so with a 5V reference, we get less accuracy, so we have an instruction that enables us to change this reference value. Therefore, we use "analogReference()" to change the reference value.
If you need Bichner's explanation, see Analog to Digital on Arduino.
By default we get the maximum ADC resolution which is 10 bits, this resolution can be changed using the directive (“analogReadResolution(bits);”).
In the robotic arm circuit, we default this reference voltage, so we can read the value from the ADC channel with analogRead(pin); let's read Here, pin indicates the pin where the analog signal is received. We want to read the analog value from pin A0, so we have to write:
int SENSORVALUE0 = analogRead(A0);
Now let's talk about the servo motor, Arduino Uno has a feature that enables us to control the position of the servo by providing a degree value. If we want the servo to be at 30 degrees. Call the library (Servo.h). This library makes the work very easy.
#include <Servo.h>
servo servo0;
servo0.attach(3);
servo0.write(degrees);
Now, we have SG90 servo position from 0-180 and ADC values ​​from 0-1023. We will use a special function that automatically matches both values.
sensorvalue0 = map(sensorvalue0, 0, 1023, 0, 180);
This statement automatically synchronizes both values ​​and stores the result in "servovalue0". This is how we use Arduino servo to control our motors in the Arduino robotic arm project.
Project performance video
As mentioned, four potentiometers are provided to the user, and by turning each potentiometer, we give a variable voltage in the analog channel to the digital Arduino. By turning these potentiometers, you can easily move the robotic arm and pick up and place objects.
Items in the file: complete source, complete schematic
Teaching Arduino Arduino projects
Robot control with mobile gyroscope sensor and Arduino
22/04/2013
Approximate reading time is 5 minutes

Contents [show]
hello We prepared the robot control project with mobile gyroscope sensor and Arduino.
Learning how to control a robot with an Android mobile gyroscope and Arduino
In this Arduino project, we are going to control the car robot through the gyroscope sensor of our mobile phone, and you will be able to control the robot just by tilting the phone. We will also use Arduino and RemoteXY program for this robot. The RemoteXY app is used to establish a connection between the smartphone and the Arduino board to control the robot. We will add a joystick in this app so that the robot can be controlled by the joystick as well as by tilting the phone. This project works with both IOS and Android.
The G sensor or G-Sensor is basically the accelerometer sensor of the smartphone, which is used to find the screen display direction. The accelerometer obtains the Z, Y and X directions. Accelerometers are now very accurate and sensitive. In this project, our robot moves according to the direction we have tilted the phone. For example, when we place the phone in the forward slope, the robot moves forward and it is the same for the other four directions. This project is like controlling the car in the games, with the difference that instead of controlling the car inside the Android mobile phone, the car robot made by us is controlled. The performance video of this project is placed at the bottom of the page.
The following video shows you how the project works:
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
Video display
00:00
00:50
Robot control with RemoteXY Android software
To create a user interface to control the car robot using the RemoteXY application, you should go to the following link: Creating an Android user interface with RemoteXY
The web page will appear as follows:
Then, from the left side of the screen, remove the switch button and joystick and place it in the mobile phone. This button turns on the light on pin 13, which is connected internally on the Arduino, and moves the robot's joystick. The web page will look like this after placing the switch and joystick.

Then we need to add the G sensor enable/disable button along with the joystick so that we can move the car robot by tilting the phone left, right, up and down. Using that button we can enable and disable the G sensor, when the G sensor is disabled the car can be controlled by moving the Joystick. So to put the G sensor enable/disable button, click on the joystick you placed on the mobile and there will be a section on the left side, at the end there is an option to put the G sensor button near the joystick , so place the G sensor button anywhere you like. The web page will then appear as below.
Suggested article: Setting up the water level detection module with Arduino

After that, click on the "Get source code" button and save it to your computer. Install the library related to this software, which is placed in the download file at the bottom of the page. You also need to download the Android app. Download Remote XY Android software
Robot control circuit with mobile gyroscope and Arduino
The image below shows the schematic circuit of the car robot control project with a gyroscope sensor.

First of all, we will connect the L298N motor controller to the Arduino. Connect the ENA and ENB pins of the motor controller to Arduino pins 12 and 11 respectively. These two pins are for PWM control of the motor. Using these pins, the speed of the car can be increased or decreased. Then connect IN1, IN2, IN3 and IN4 to pins 10, 9, 8 and 7 of Arduino board respectively. These pins cause the motors to rotate in both directions (clockwise and counterclockwise).
If you have any questions about this article, ask in the comments section

To power the motor, connect the positive and negative of the battery to the 12V and GND of the motor driver. Then connect 5V and GND from the motor driver to GND and Vin of Arduino.
Then we will connect the HC-06 Bluetooth module to the Arduino. If you have HC-05 it will work too. Then connect the Bluetooth module's TX pin to Arduino pin 2 and RX pin to Arduino pin 3. Also, to learn more about using bluetooth with arduino, check out bluetooth controlled toy car using arduino.
Required parts
1. Arduino UNO board
2. L298N motor driver module
3. Bluetooth module HC-06 or HC-05
Get the required parts from the Ironex parts store.
Robot control code with gyroscope and virtual joystick and Arduino
The complete code of the project is placed at the end of the page in the downloadable file. Here we check some parts of the code.
First of all, we call the serial communication and RemoteXY libraries. The RemoteXY library will help us set up the program with Arduino, through which we will control the robot car. After that we have defined the pins for the bluetooth module, TX from bluetooth module is connected to pin 2 of Arduino and RX from bluetooth module is connected to pin 3 of Arduino.
#define REMOTEXY_MODE__SOFTWARESERIAL
#include <SoftwareSerial.h> //Call the serial communication library
#include <RemoteXY.h> //call remotexy library

/* RemoteXY connection settings */
#define REMOTEXY_SERIAL_RX 2 //set RX pin
#define REMOTEXY_SERIAL_TX 3 //set TX pin
#define REMOTEXY_SERIAL_SPEED 9600 //Set baudrate to 9600
The following code increases or decreases the speed of the motor. When the joystick is in the center, the speed will be zero, and when it is in the forward direction, the speed will increase from zero to 100. And in the opposite direction, the movement speed decreases from 0 to -100.
 if (motor_speed>100) motor_speed=100;
 if (motor_speed<-100) motor_speed=-100;
 if (motor_speed>0) {
 digitalWrite(pointer[0], HIGH);
 digitalWrite(pointer[1], LOW);
 analogWrite(pointer[2], motor_speed*2.55);
 }
 else if (motor_speed<0) {
 digitalWrite(pointer[0], LOW);
 digitalWrite(pointer[1], HIGH);
 analogWrite(pointer[2], (-motor_speed)*2.55);
 }
 else {
 digitalWrite(pointer[0], LOW);
 digitalWrite(pointer[1], LOW);
 analogWrite(pointer[2], 0);
 }
In the code below, we have defined a function that will be called whenever we move the joystick in the program. When we turn on the switch in the program, pin 13 of the Arduino, which is connected to the LED, becomes 1.
void loop()
{
 RemoteXY_Handler();
 digitalWrite (ledpin, (RemoteXY.switch_1==0)?LOW:HIGH);
 Speed ​​(first_motor, RemoteXY.joystick_1_y - RemoteXY.joystick_1_x);
 Speed ​​(second_motor, RemoteXY.joystick_1_y + RemoteXY.joystick_1_x);
}
How to run and project performance video
Add the RemoteXY library to the Arduino libraries and load the code into the Arduino IDE. Then install the app on your mobile phone and then turn on Bluetooth. The user interface of the program will appear like this.
Then go to Bluetooth and turn it on. After turning it on, it will show you Bluetooth devices. Select your HC-06 bluetooth module from there, from there you can control the Robot Car.

This is how we can use the accelerometer sensor in our mobile phone to move the robot.
Items in the file: Arduino source, project schematic
Smart robot vacuum cleaner project with Arduino and ultrasonic
04/17/2019
Approximate reading time is 3 minutes

Contents [show]
hello We have prepared the smart robot vacuum cleaner project with Arduino and ultrasonic.
Teaching how to make a home cleaning robot with Arduino
In this Arduino project, we will build a vacuum cleaner robot that will help us keep our home and workplace clean and tidy. This four-wheeled robot can intelligently avoid hitting obstacles and walls. This idea was inspired by the famous Robot Roomba vacuum cleaner, shown in the image below.
Video display
00:00
00:59
Smart vacuum cleaner robot circuit with Arduino
In the picture below, you can see the circuit diagram of this project. This circuit is simple and its description is given below.

Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
Choosing a microcontroller is a very important task, because this controller will act as the brain of your robot. Most of these projects are made with Arduino and Raspberry Pi. In this project, we use an Arduino Uno board.
As you can see in the pictures below, we have installed an ultrasonic sensor in the front and two IR sensors on both sides of the robot.
The ultrasonic sensor consists of two circles, one of which is used to send the signal and the other to receive the radiation. The duration of transfer and return is calculated by the microcontroller. Now, since the time and speed of sound are known, the distance can be calculated with the following formulas.
Distance = time x speed of sound / 2
The value is divided by 2 because at first the round trip distance is calculated and by dividing by two only the distance of sending the wave is calculated.

Many motors are used in the field of robotics, the most used of which are stepper and servo motors. Since this project does not have any complex actuators, we will use a simple PMDC motor. Our battery is bulky and heavy, so we use four motors to drive the robot, all four motors are the same.
The most difficult task when building a robot is to prepare the chassis of our robot. The problem is in the availability of tools and materials. You can use acrylic, wood or 3D printed parts.
Choosing the battery capacity should be the last part of our work because it depends solely on your chassis and motors. Here our battery should drive the vacuum cleaner which we need around 3-5A. Therefore, we will need a heavy battery. Here we use SLAB 12V 20Ah SLAB, but you can power this robot and its motors any way you want.
I suggest you see the surface cleaning robot project with Arduino.
If you have any questions about this article, ask in the comments section
Suggested article: How to make a reminder project with Arduino?
Required parts
1. Wooden sheets for chassis
2. Infrared sensor
3. Ultrasonic sensor
4. Vacuum cleaner with DC current
5. Arduino Uno
6. 12 volt 20 amp battery
7. Motor driver IC (L293D)
Get the required parts from the Ironex parts store.
DC vacuum cleaner
Because our robot works on 12V 20Ah DC system. Our vacuum cleaner must be a 12V DC vacuum cleaner.

Motor driver (L293D)
The motor driver is an intermediary module between the Arduino and the motor. The use of the motor driver is because the Arduino microcontroller will not be able to supply the current required by the motor and can only supply 40 mA, hence drawing more current than Arduino causes it to be permanently damaged. We will use the L293D Motor Driver IC which is capable of supplying up to 1A, so this driver receives the information from the Arduino and drives the motor according to the commands.
Robot and motor driver test
The complete code of the project is placed at the end of the page in the downloadable file. It is recommended to test your motor driver and robot motor with the following code before connecting the sensors.
void setup()
{
Serial.begin(9600);
pinMode(9,OUTPUT);
pinMode(10, OUTPUT);
pinMode(11,OUTPUT);
pinMode(12,OUTPUT);
}

void loop()
{
delay(1000);
Serial.print("forward");
digitalWrite(9,HIGH);
digitalWrite(10,LOW);
digitalWrite(11,HIGH);
digitalWrite(12,LOW);
delay(500);
Serial.print("backward");
digitalWrite(9,LOW);
digitalWrite(10,HIGH);
digitalWrite(11,LOW);
digitalWrite(12,HIGH);
}
If everything works well, you can connect the sensors and the Arduino as shown in the circuit schematic and upload the complete code to the Arduino.
Items in the file: complete source, schematics
Preventing the robot from hitting obstacles with Raspberry Pi and Python
04/11/2019
Approximate reading time is 5 minutes

Contents [show]
hello We prepared the project of the robot not hitting obstacles with Raspberry Pi, Python and Ultrasonic.
Learning how to build a smart obstacle detection robot with Raspberry Pi
In this Raspberry Pi project, we are building an automatic robot that moves independently of external controllers such as joysticks, etc. This robot stops in its path every time it approaches an obstacle and goes back and chooses another path. Raspberry Pi and DC motor + ultrasonic sensor are used in this project.
Finally, we make a robot that can move freely and change its path whenever it sees an obstacle.
Video display
00:00
00:50
We have many projects about robots, which you can see in the topic section.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
We also made this project with Arduino and PIC:
• Arduino robot project, the robot does not hit the obstacle
• Project to prevent the robot from colliding with the PIC barrier
Description of the ultrasonic sensor HC-SR04
We need to have a general information about the ultrasonic sensor. We know that sound vibrations cannot penetrate through solids. So when a sound source causes a vibration, that vibration travels through the air at a speed of 220 meters per second. As we said, these vibrations cannot penetrate through solids, that is, when they hit a surface like a wall, they return to the sensor at the same speed, this technique is called ECHO.
 Arduino ultrasonic project
The HC-SR04 ultrasonic sensor provides an output signal proportional to the distance based on the echo. The sensor here generates a sound vibration within the range of the sensor, and after sending a vibration, it waits for the sound to return.
The transmitter emits an ultrasonic wave at a frequency of 40 Hz, this wave passes through the air and returns when it senses an object. The return waves are observed by the receiver. Now we know that the time required for the reflection and return of this wave is taken and the speed of the ultrasonic wave is 3400 cm/s. Using this information and the following formula, you can calculate the distance [distance = wave speed * time]
How does the robot detect obstacles?
When the robot turns on and starts working, the Raspberry Pi measures the distance of the objects in front of it using the ultrasonic sensor module and stores it in a variable. The RPi then compares this value with predefined values ​​and accordingly decides to move the robot left, right, forward or backward.
Suggested article: Connecting ESP8266 module to Raspberry Pi Pico
In this project, we have chosen the dangerous distance in Raspberry Pi to be 15 cm. Whenever the robot is less than 15 cm away from any object, the Raspberry Pi will stop the robot and move backward, then turn it left or right. Now before moving forward again, the Raspberry Pi will check again if there is an obstacle within 15 cm to the right or left, if there is, the robot will stop again and go back, if not After changing the direction, it continues on its way.
The ultrasonic sensor sends sound waves continuously and if it receives its reflection in a short period of time, it knows that it is close to the obstacle and should stop. Raspberry Pi checks the time between sending and receiving the message and then calculates the distance. The speed of sound is about 340 meters per second. Therefore, the distance can be calculated using the following formula.
Distance = (time / 2) * speed of sound
The speed of sound is approximately 340 meters per second.
We calculate the distance in centimeters as follows:
 pulse_start = time.time()
 while GPIO.input(ECHO)==1:
 GPIO.output(led, False)
 pulse_end = time.time()
 pulse_duration = pulse_end - pulse_start
 distance = pulse_duration * 17150
 distance = round(distance,2)
 avgDistance=avgDistance+distance
where pulse_duration is the time between sending and receiving the ultrasonic signal.
Schematic of the robot not hitting the Raspberry Pi obstacle
The circuit of the project to avoid the robot hitting the obstacle is very simple. As you can see in the picture below, an ultrasonic module is connected to GPIO pins 17 and 27 of Raspberry Pi. L293D motor driver is used to control motors and its pins 2, 7, 10 and 15 are connected to GPIO pins 12, 16, 20, 21 of Raspberry Pi. In this project, we have used two DC motors to drive the robot. One motor is connected to output pins 6 and 3 of the motor driver and the other to pins 11 and 14 of the motor driver.
If you have any questions about this article, ask in the comments section

Required parts
1. Raspberry pie
2. HC-SR04 ultrasonic sensor module
3. ROBOT chassis with full screw
4. DC motor
5. Motor driver L293D
6. 1 kilo ohm resistance
7. 100 nanofarad capacitor
Get the required parts from the Ironex parts store.
amendment
In the circuit above, use the voltage divider circuit as below to connect the ultrasonic to the Raspberry Pi. Because otherwise, the ultrasonic will supply 5 volts to the Raspberry Pi, and the Raspberry Pi can only tolerate 3.3 volts. So, otherwise, your win will be damaged.

Programming the robot to avoid obstacles with Python
We are using Python language for the program here. The complete code of the project is placed at the end of the page in the downloadable file. Here we check some parts of the code.
The programming part of this project plays a very important role in performing all operations. First of all, we call the required libraries. We create variables and define pins for the ultrasonic sensor, motor and components.
import RPi.GPIO as GPIO // Library of GPIO pins
import time // Delay library

# Import time library
GPIO.setwarnings(False) // Suppress warnings
GPIO.setmode(GPIO.BCM)

TRIG = 17 // Ultrasonic trigger pin
ECHO = 27 // Ultrasonic echo pin
... .....
.... .....
Then we create some functions named def forward(), def back(), def left(), def right() which are used to move the robot.
Then in the program, we activate the ultrasonic sensor and measure the time between sending and receiving the wave and then measure the distance.
i=0
 avgDistance=0
 for i in range(5):
 GPIO.output(TRIG, False)
 time.sleep(0.1)

 GPIO.output(TRIG, True)
 time.sleep(0.00001)
 GPIO.output(TRIG, False)

 while GPIO.input(ECHO)==0:
 GPIO.output(led, False)
 pulse_start = time.time()

 while GPIO.input(ECHO)==1:
 GPIO.output(led, False)
 pulse_end = time.time()
 pulse_duration = pulse_end - pulse_start

 distance = pulse_duration * 17150
 distance = round(distance,2)
 avgDistance=avgDistance+distance
Finally, we write the code that determines if the robot is less than 15 cm away from the obstacles, it will stop and go back.
 if avgDistance < 15: // If the distance was less than 15
 count=count+1 // A number is added to the count variable
 stop() // stop
 time.sleep(1)
 back() // Go back
 time.sleep(1.5)
 if (count%3 ==1) & (flag==0):
 right() // facing right
 flag=1
 else: // if there is an obstacle on the right side
 left() // facing left
 flag=0
 time.sleep(1.5)
 stop() // stop
 time.sleep(1)
 else: // If there were no obstacles
 forward() // Forward
 flag=0
Items in the file: complete source, complete schematic
Arduino training, Internet of Things training, Esp projects, Arduino projects
Robot control with Wi-Fi via Android with Arduino and Esp8266
04/09/2019
Approximate reading time is 4 minutes

Contents [show]
hello We prepared the control of the robot with Wi-Fi through Android with Arduino and Esp8266.
Setting up a controlled robot with mobile Wifi and Arduino
There are different types of robots. Toy car robots to advanced industrial robots. In this Arduino project, we want to launch a Wi-Fi controlled robot using Arduino board and Blynk software. This robot calls with any Android smartphone with Wi-Fi. We have used Blink software to control the robot. Blynk is a very Arduino compatible program. This software can be easily downloaded from Play Store.
How this project works is very simple. We put the joystick in the Android software and just move it. For example, if we want to direct the robot to the right, we only need to pull the joystick to the right. In the same way, we can move the robot in different directions.
The Blynk app sends values ​​from two axes to the Arduino via Wi-Fi. Arduino receives the values, compares them with predefined values ​​and moves the robot accordingly in the desired direction.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
The video below is short, but it will help you understand how this project works.
Video display
00:00
00:14
At the end of this tutorial, we will build a robot that can move in different directions. The performance video of this robot is placed at the bottom of the page.
We also have other projects in this field:
• Face recognition robot and face tracker with Arduino and Processing
• Humanoid robot project with Arduino (learning how to make a two-legged robot with Arduino)
• Teaching how to make a self-balancing robot with Arduino (self-balancing robot project with Arduino)
Blynk application configuration steps
First, download it from Google Play and install it on your Android mobile phone. Download Blynk
After installation, you need to create an account. You can do this through Gmail connected to your phone. Then, in the Create New Project section, select the name of the project you want and the Node MCU board. Then select Wi-Fi from the Connection Type drop-down list and click Create. An Auth Token will be generated and sent to the email address you entered. Enter this Auth Token Code in the Arduino code below.
char auth[] = "caa17a11c0124d4083d0eaa995f45917";
Then click the Create button in the Blynk app.
Now select the Joystick widget, click Joystick, Configure Joystick.
Suggested article: ADXL345 accelerometer setup with Arduino

Then press the Play button at the top of the screen.
Schematic of the robot control circuit with Android Wi-Fi with Arduino
The schematic of the Wi-Fi robot control project is shown in the image below.
An L293D driver IC is used to control DC motors. The input pins of the motor driver IC are directly connected to pins 8, 9, 10 and 11 of the Arduino. And DC motors are connected in its output pins. Here we have used 9V battery to drive DC motors.
Required parts
1. Arduino UNO board
2. ESP8266 Wi-Fi module
3. Motor driver L293D
4. DC motor
5. Robot chassis plus wheels
Get the required parts from the Ironex parts store.
Description of the robot control code with Wifi
This program is ready in Arduino IDE. We just need to download the Blynk library for Arduino. And after making some changes, you can build your own Wi-Fi controlled robot. The complete code of the project is placed at the end of the article. Here we explain the important parts of the code.
First, we put all the libraries needed to run this code in the Arduino IDE, and then we put the Auth Token received from the Blynk program in the code. So we define the Wi-Fi serial pin.
If you have a problem in this part, see the tutorial on installing the library in Arduino.
#define BLYNK_PRINT Serial // Comment this out to disable prints and save space
#include <ESP8266_SoftSer.h>
#include <BlynkSimpleShieldEsp8266_SoftSer.h>

// Set ESP8266 Serial object
#include <SoftwareSerial.h>
SoftwareSerial EspSerial(2, 3); // RX, TX

ESP8266 wifi(EspSerial);

char auth[] = "caa17a11c0124d4083d0eaa995f45917";
Then we define the output pins (8,910,11) for the motors and write some direction functions for the robot movement. void forward(), void backward(), void right() and void left()
After this, in the setup function, we configure all the required devices such as motor pins, start the serial communication, enter the Wi-Fi username and password.
void setup()
{
 Serial.begin(9600); // Serial communication rate
 delay(10);
 EspSerial.begin(9600); // Wi-Fi module connection rate
 delay(10);

 Blynk.begin(auth, wifi, "username", "password"); //Your Wi-Fi name and password
 pinMode(m11, OUTPUT); // Set motor pins
 pinMode(m12, OUTPUT);
 pinMode(m21, OUTPUT);
 pinMode(m22, OUTPUT);
}
Here we define a number of conditions that the motors will be activated according to the values ​​sent by the joystick module. The activation of the motors are placed in the motion functions that we introduced, such as Backward().
BLYNK_WRITE(V1)
{
 int x = param[0].asInt();
 int y = param[1].asInt();
 if(y>220) // If the joystick value was greater than 220
 forward(); // Move forward
 else if(y<35) // If the joystick value was less than 35
 backward(); // Move backward
 else if(x>220) // If the joystick value was greater than 220
 right(); // Move to Rasa
 else if(x<35) // If the joystick value was less than 35
 left(); // Move left
 else // if none
 stop(); // Stop the robot
}
Finally, we need to run the blynk function in a loop, so that the system starts working.
void loop()
{
 blynk.run();
}
Items in the file: source code, project schematic
Airnex/Arduino training/Building a dancing and walking robot control with Android and Arduino
Teaching Arduino Arduino projects
Making a dancing and walking robot controlled by Android and Arduino
04/03/2019
Approximate reading time is 4 minutes

Contents [show]
hello We prepared the construction of a dancing and walking robot with Arduino (control with Android - Bluetooth).
Human walking robot project with Arduino
We prepared an Arduino project with which we will make a small robot that can walk and dance. The purpose of this tutorial is how to build small robots for fun with Arduino and also how to program a servo motor (What is a servo motor?). At the end of this tutorial, you will be able to build a robot that can dance, walk and its actions can be controlled through your Android phone. Also, you can easily manipulate this program to program other movements for this robot.
Video display
00:00
00:55
If you use a 3D printer in this project, your work will be much more beautiful. If you don't have access to a 3D printer, you can give your design online to be printed and sent to you, and you can also make the body of this robot using cardboard. As you can see in the picture, this robot needs few electronic parts. The project performance video is placed at the bottom of the page.
3D printing of the robot body
3D printing is an amazing tool that can be of great help in building prototype projects or testing mechanical designs. In this project, the robot body shown above is completely 3D printed. You can download the 3D printing STL files at the bottom of the page. Upload these files to your 3D printing software such as Cura and print them directly. We use a software called Cura to print STL files. Below are the settings I used to print the material, you can use the same or change them based on your printer.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store

After printing, your 3D parts will look like something below.
The circuit of the dancing robot project with Android and Arduino
Connecting the dancing robot hardware is very simple. The complete schematic is shown in the image below. (Hip = hip, Ankel = ankle)

We have used a punched board to make the connections. Make sure your circuit also fits inside the robot head.
Required parts
1. Arduino Nano
2. Servo motor SG90 - four pieces
3. Bluetooth module HC-05 / HC-06
Get the required parts from the Ironex parts store.
Robot assembly
After the hardware and 3D printed parts are ready, we can assemble this robot. Before fixing the motor, be sure to place the motors in the following angles so that the program will work flawlessly.
Suggested article: randomSeed command in Arduino (randomization of random numbers)
Engine Number Engine Location Engine Mode
1 left hip 110
2 right hips 100
4 left ankle 90
5 maps of the right foot 80
These angles can be adjusted using the program provided at the end of the tutorial. After making the connections, just upload the above program to your Arduino and type the following in the serial monitor (note: Baud rate is 57600).
1, 100, 110
2,90,100
4,80,90
If you have any questions about this article, ask in the comments section
5,70,80
Your serial monitor should look something like this after placing all your engines.

After setting the motors at the respective angles, mount them as shown below.

Walking robot code with Android and Arduino
Programming the dancing robot is the most interesting and fun part in this tutorial. Here we explain the important parts of the code. You can download the complete code at the end of the article.
This program is able to control the functions of the robot through serial monitor or bluetooth. You can also control each motor individually using the serial monitor.
The following codes determine which servo motor is connected to which Arduino pin board.
 servo1.attach(3);
 servo2.attach(5);
 servo4.attach(9);
 servo5.attach(10);
As we said, the operation of the robot is controlled by serial monitor and bluetooth. Here we determine the Bluetooth and serial communication rate.
Bot_BT.begin(9600); //start the Bluetooth communication at 9600 baud rate

Serial.begin(57600);
For example, if we want to move motor number 1, which is the left buttock motor, from its default position of 110 degrees to 60 degrees. We can simply write "1,110,60" in Arduino serial monitor and press enter key. This will help you to perform complex movements with the robot.
This is where functions are called based on values ​​received from the serial or bluetooth monitor. As shown in the code, the gmotor variable will have the value of the serial monitor and BluetoothData will have the value received from the Bluetooth device.
All functions are defined inside the “Bot_Functions” page. You can open it up and see what's actually happening inside each function.
Android application with Processing software
Processing Android software is used to build the Android application. If you want to make changes in the program, the processing file is included in the download file that you can edit. If you do not need to edit, you can use the APK file that is included in the download file.
Note: Your Bluetooth module must be named HC-06, otherwise the app will no longer be able to connect to your Bluetooth module.
After installing the app, you can pair the bluetooth module with your phone and then launch the app. You should see something like the image below.

If you want to make the program more attractive or connect to a Bluetooth device with a name other than Hc-06, you need to edit the processing code.
Working with a robot controlled by an Android phone
Once your hardware, Android app, and Arduino are ready, it's time to play with the robot. You can control the robot using the buttons in the program or directly from the serial monitor using the following commands as shown in the image below.
Suggested article: Setting up a pulse sensor with Arduino (Pulse Sensor heartbeat)

Each command makes the robot perform some strange tasks and you can also on adding more actions based on your creativity.
This robot can also be powered by a 12V adapter or by using a 9V battery. This battery can be easily placed under the board and can also be covered with the robot head.
Items in the file: Arduino source, project schematic, Android app, processing code, 3D printing file
Teaching Arduino Arduino projects
Face recognition and face tracking robot with Arduino and Processing
Face recognition robot project with Arduino
Have you ever wanted to create a face recognition project without using other programming such as OpenCV, Visual Basic #C, etc.? In this Arduino project, we will make a face tracking robotic arm by mixing the power of Arduino and Android. The advantage of this project is that you don't need to buy a camera module and this is done with the phone camera. Also, the Arduino does not need to be connected to the computer. Also, we use a Bluetooth module to connect Android and Arduino. The Android application used in this project was produced using Android Processing. You can download this program at the bottom of the page.
The following video will help you understand how this project works.
Video display
00:00
00:30
At the end of this tutorial, you have a robot that can track your face and follow it. You can use these markets to record your videos. Because our robot moves so that your face is exactly in the middle of the screen. All our efforts have been to make this project work as simply as possible. Anyone with minimal knowledge of hardware or coding can start this project.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
I suggest you to see the humanoid robot project with Arduino.
At the end of the article, you can see the project performance video and the complete description of the project code.
3D printing of parts (optional)
To tilt the mobile phone, we need some mechanical structures like a mobile holder and some servo brackets. You can use a cardboard to make it, but we used a 3D printer.

3D printing is an amazing tool that can help in building and testing projects with mechanical designs. If you have access to a 3D printer, you can use the 3D printing files at the end of the article and print your parts. We use a software called Cura to print STL files. Below are the settings we used to print the material, you can use the same or change them based on your printer.

After printing all the required materials, you can secure them in position using screws and some glue. After the assembly is finished, your parts should look something like the image below.
Suggested article: isLowerCase command in Arduino (lower case check)

Face tracking robot circuit with Arduino
The circuit of the face tracking project with Arduino and smartphone is shown in the image below.

As seen in the circuit schematic, our circuit has 2 servo motors. One is to move the phone left and right and the other is to adjust the tilt of the mobile phone. The movement direction of the servo motor is controlled by Arduino Nano. Motion information is also provided to Arduino by Hc 05 Bluetooth module. The whole circuit is powered by a 9V battery. This circuit can be easily connected on the board.
If you have any questions about this article, ask in the comments section
Required parts
1. Arduino Nano
2. SG90 servo motor - two pieces
3. Bluetooth module HC-05 / HC-06
4. 9 volt battery
Get the required parts from the Ironex parts store.
Face recognition android application settings
As we said before, the main brain of this project is the Android application. This Android application is developed using Android Processing. You can directly install this app on your mobile phone and launch it by following the steps below.
1. Download the APK file at the bottom of the page.
2. Turn on the circuit.
3. In the phone settings, search for the Bluetooth self-module with the name "HC-05". (If you renamed your module, rename it back to HC-05.)
4. Connect to your Bluetooth module. If prompted, try 000 and 1234.
5. You should see the image of your camera on the screen and also see the words Connected to: HC-05 at the top of the screen.
6. Jerk your camera, you should see a green square on the face in front of the camera.

You can take this Arduino face tracking project to the next level by bringing so many improvements that you don't need to code your own Android app. Creating an android app may seem difficult but trust me with the help of processing you can learn it in no time. The complete processing code used to build this program can be uploaded here. You can improve with your creativity. To learn more about processing, check out the following projects:
Face tracking project code with Arduino
The Android app recognizes the face and its position on the screen. It then decides which direction the servos should move based on the position of the face. Then this information is sent to Arduino to move the servos.
The Arduino program for this project is relatively simple, we just need to control the path of the two servo motors based on the values ​​received from the bluetooth module. You can get the complete code at the end of this tutorial. Here we explain some important lines of Arduino code.
In the following code, serial connection is established with pin D12 as RX and D11 as TX. Therefore, pin D12 should be connected to TX of Bluetooth module and pin D11 to RX of Bluetooth module.
SoftwareSerial cam_BT(12, 11); // RX, TX
Then we start the Bluetooth module with a baud rate of 9600. Make sure the module is also running at the same baud rate. Otherwise, change it.
cam_BT.begin(9600); //9600 baud rate
cam_BT.println("Ready to take commands");
In the following line, we tell Arduino to read the information obtained from the phone. Also, this data is stored in the "BluetoothData" variable.
if (cam_BT.available()) //Command to read received information
 {
BluetoothData=cam_BT.read();
Serial.print("Incoming from BT:");
Serial.println(BluetoothData);
}
Based on the data received from Bluetooth, the direction of the motor is controlled. To turn a motor to the left, 2 numbers are subtracted from the previous value of the motor. If you need your robot to move faster, change this value.
if (BluetoothData==49) //rotate left
{pos1+=2; servo1.write(pos1);}

if (BluetoothData==50) //rotate right
{pos1-=2; servo1.write(pos1);}

if (BluetoothData==51) //rotate up
{pos2-=2; servo2.write(pos2);}

if (BluetoothData==52) //rotate down
{pos2+=2; servo2.write(pos2);}
After preparing the circuit and uploading the program to Arduino, open the software. The program automatically connects to the Bluetooth module named Hc-05 and waits for it to find a face and identify it. Then you can put your face or a photo of a face in front of the camera to recognize it. Then you can move or move the photo to see how the robot follows the face.
Suggested article: Teaching DC motor speed control with potentiometer and Arduino
Items in the file: complete source, project schematic, Android software
Teaching Arduino Arduino projects
Humanoid robot project with Arduino (making two-legged robot)
03/31/2019
Approximate reading time is 5 minutes

Contents [show]
hello We have prepared the humanoid robot project with Arduino (training to make a two-legged robot with Arduino).
Learning how to make a human robot with Arduino
I have always been interested in robots. Robots that imitate human behavior are very attractive. My interest led me to try to put a humanoid bot on the site. The robot we build in this project can walk and run. In this Arduino project, we will get to know how to make a two-legged robot.
You can watch the following video to fully understand the construction of this robot.
Video display
00:00
00:38
The main goal in this tutorial is to make our robot strong enough to not be damaged by running and long walks. Our secondary goal is to design a biped body for this project. This design has been made and you can easily download it from the end of the article and have your body elegantly using 3D printers. The performance video of the project is placed at the end of the article.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store

The steps of making a humanoid robot with Arduino:
1. Design process
2. Printing of designed parts
3. Required parts
4. Connecting servo motors
5. Making connections between parts
6. Assembling the legs of the robot
7. PCB design (optional)
8. Assembling the body
9. Basic settings of the code
10. Description of knee movements (optional)
11. Upload the complete project code
1: Design process
We have designed the required parts of this robot and you can download it for free at the end of the article. First, we designed servo motors and legs. The legs are designed in such a way that they have shafts on both sides of the engine to create stability and strength.

This design is done with the aim of compressing the robot and making maximum use of the torque provided by the servo motors. If you do not have access to a 3D printer in your city, you can easily order 3D printing online.
2: Print the designed parts

The parts required for this project must be custom designed, so a 3D printer is used to print them. Printing is done in 40% infill mode and 2 parameters, 0.4mm nozzle and 0.1mm layer height with PLA and your desired color. You can see the list of designs in the download file. You should print several copies of the following parts:
• bearing link x 2
• Servo horn link x 2
Foot link x 2
• bridge x 1
• electronics mount x 1
• electronics spacer x 8 (optional)
Servo horn space x 12 (optional)
3: Required parts

Here is a list of all the parts needed to build a humanoid robot with Arduino. All the parts are available and you can easily find them.
1. Arduino Uno board
2. Towerpro MG995 servo motor – six pieces
3. MPU6050 accelerometer (optional)
4. Ultrasonic sensor (optional)
5. Skate bearing (8x22x7mm)
6. M4 bolt
Suggested article: Comprehensive L293D training with Arduino board (motor direction and speed control)
Get the required parts from the Ironex parts store.
 Towerpro MG995 servo motor
4: Connecting servo motors

Then we need to connect the servo motors to the robot. After printing all the parts, you can start adjusting the servo and servo brackets. First apply pressure to the bearing of the knee support. The fit must be strictly observed. It is recommended to slightly widen the inner surface of the holes. Then pass the M4 screw through the hole and tighten it with a nut. The images of how to connect the knee and leg parts and the complete design of the robot are placed in the downloadable file at the end of the page.
If you have any questions about this article, ask in the comments section
5: Connecting the parts

After the brackets are assembled, start the connections. To make the bearing bond, once again gently ream the inner surface of the bores for the bearing and then press the bearing into the bore on both sides. How to connect the parts together can be fully seen using the images in the download file.
6: Assembling the legs of the robot

After connecting the parts and brackets, you can also connect them together to make the robot's legs. First, start by connecting the thigh and knee servos. Then connect the leg to the knee. It may be difficult but it is worth it. Pay attention to the pictures to fully understand how to connect.
7: PCB design (optional)

This step is optional. To do the wiring, we decided to make our custom PCB using board pins and header pins. The PCB contains ports that directly connect the servo motor wires. It also has a port for the external power supply needed to power the servo motors. A jumper wire connection is used for USB communication and external power for Arduino. Mount the Arduino and PCB using 3D printed screws and spacers.
Note: Be sure to remove the jumper wires before connecting the Arduino via USB. Failure to do so may damage the Arduino. If you decide not to use a PCB, make the servo connections as below.

Connecting servos to Arduino
1. Left thigh to pin 9
2. Right thigh to pin 8
3. Left knee to pin 7
4. Right knee to pin 6
5. Left foot to pin 5
6. Right foot to pin 4
Use normal male and female wires to connect the PCB to the Arduino using the information above.
8: Assembling the body

After connecting the legs, connect all the parts together to make the robot body completely. Use M4 bolts and nuts to make the connections. How to connect is fully explained in the download file at the bottom of the page.
9: Basic settings of the code

that servo motors do not need to be perfectly aligned to remain relatively parallel. This is why the "center position" of each servo motor must be manually adjusted to match the legs. To achieve this, remove the servo horns from each servo and run the setup.ino blueprint (in the download file). . Open the constants.h file in the file and change the servo deflection values ​​(lines 1-6) so that the legs are perfectly aligned and smooth. Play with the values ​​and get an idea of ​​what is needed in your case. Change the values ​​and manipulate the servo motors to stay perfectly parallel.
Suggested article: Downloading Arduino software for Android
Refer to the images for guidance.
10: Upload the complete project code

Before programming the Arduino, minor changes must be made to the file. The deviation values ​​obtained in the previous section should be entered in the project code.
Note: If you have used the designs provided in this tutorial, you do not need to change anything. If you changed things and did not proceed according to this tutorial, you must make minor changes in the Arduino code. L1 is the fixed distance between the axis of the thigh and the axis of the knee. L2 is the distance between the axis of the knee and the axis of the ankle. Therefore, if you use your own design, be sure to change these items.
After uploading the given code and turning on the robot, the robot moves forward in a simple way. You can change the way the robot moves according to your taste and add other features to it.
Items in the file: complete source, required images
Surface cleaning robot with Arduino (cleaning and cleaning robot)
20/03/2013
Approximate reading time is 2 minutes
Floor cleaning robot project with Arduino
Floor cleaners are nothing new, but they all share one problem. All of them are very expensive. In this Arduino project, we will make an automatic home cleaning robot that requires little money. Using an ultrasonic sensor, this robot can detect obstacles and objects in front of it and does not hit them and cleans the floor of the house. Our cleaning robot has a small brush attached to it to clean the floor.
Watching the video below will help you understand this project.
Video display
00:00
00:28
Required parts
1. Arduino Uno board
2. Ultrasonic sensor HC-SR04
3. Arduino motor driver shield
4. Power supply for supplying electricity to motors (battery, power bank or...)
5. A brush
6. Scrub pad
Get the required parts from the Ironex parts store.
How do ultrasonic sensors work?
We need to have a general information about the ultrasonic sensor. We know that sound vibrations cannot penetrate through solids. So when a sound source causes a vibration, that vibration travels through the air at a speed of 220 meters per second. As we said, these vibrations cannot penetrate through solids, that is, when they hit a surface like a wall, they return to the sensor at the same speed, this technique is called ECHO.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store

The HC-SR04 ultrasonic sensor provides an output signal proportional to the distance based on the echo. The sensor here generates a sound vibration within the range of the sensor, and after sending a vibration, it waits for the sound to return.
The transmitter emits an ultrasonic wave at a frequency of 40 Hz, this wave passes through the air and returns when it senses an object. The return waves are observed by the receiver. Now we know that the time required for the reflection and return of this wave is taken and the speed of the ultrasonic wave is 3400 cm/s. Using this information and the following formula, you can calculate the distance [distance = wave speed * time]
I suggest you also see the smart vacuum cleaner robot project with Arduino and ultrasonic.
Assembling floor cleaning robot parts

Mount the Arduino on the chassis. Make sure there are no short circuits if your chassis is made of metal. Secure the motors to the wheel and chassis using screws. Place the brush and scrub pad in front of the chassis.
Suggested article: Servo motor control project with Arduino internet and ESP8266 Wi-Fi module
Schematic circuit of the cleaning robot project
The circuit of this home cleaning robot is very simple. As you can see below, the ultrasonic sensor is connected to the Arduino and put the motor driver shield on the Arduino board. The link to download the schematic and the complete code of the project is placed at the bottom of the page.

The ultrasonic trigger pin is connected to pin 12 on Arduino, the echo pin is connected to pin 13, the voltage pin is connected to 5V pin and the GND pin is connected to GND pin. The Echo pin and the Trigger pin allow the Arduino Uno to communicate with the sensor.
The motor shield must have at least 2 outputs and they must be connected to your 2 motors. Typically, these outputs are labeled “M1” and “M2” or “Motor 1” and “Motor 2”. Connect your battery and power bank to the motor shield and Arduino respectively.
Items in the file: complete circuit schematic, complete source
Making a firefighter robot with Arduino (fire extinguishing)
03/16/2019
Approximate reading time is 2 minutes

Contents [show]
hello We have prepared the construction of a firefighter robot with Arduino (a complete tutorial on how to put out a fire with an Arduino robot).
Complete tutorial on designing a firefighter robot with Arduino
With the advancement of technology, especially in robotics, replacing humans with robots is very suitable for fighting fire. This improves the efficiency of firefighters and also reduces risk. In this Arduino project, we will build a firefighter robot that automatically senses the fire, goes near the fire and activates the water pump to pour water on the fire. This is a very simple robot that teaches us the basic concept of robotics. Once you understand the basics you will be able to build more advanced robots.
You can see the complete work of this robot in the video below. The maximum distance that our robot can detect a fire depends on the size of the fire. You can also use the potentiometer on top of the modules to control the sensitivity of the robot. We have used a power bank, you can also use a 12 volt battery.
Video display
00:00
00:40
Required parts
1. Arduino Uno board
2. Fire/flame sensor – three numbers
3. Servo motor SG90
4. L293D motor driver module
5. DC water pump
How does the firefighter robot work?
The main brain of this project is Arduino Uno, we use the fire sensor module (flame sensor) which is explained below to detect the fire.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
Flame detection sensor YG1006
Flame and fire detection sensor is designed to detect and respond to flame and fire. The response to the fire is up to you and it can be turning on a lamp or an alarm or nothing
Get help from your creativity to make your own water source! For me it is like this:
I used a small aluminum (drinking) can that you can put the pump in and pour water into. Then put it on a servo motor so you can control the direction of the water.

We simply place the container on top of the motor and activate the pump inside to pump the water out through the pipe. Then we can use the servo motor to rotate the whole container and control the direction of water spraying.
Items in the file: complete circuit schematic, complete source
AVR training, AVR project
Robot router project with AVR microcontroller (line follower)
02/26/2019
Approximate reading time is 3 minutes

Contents [show]
hello We prepared the line-following robot with AVR and Atmel Studio (complete tutorial on how to make a router robot).
Learning how to build a router robot with AVR
In this AVR project we will build a robot (line follower) with Atmel Studio compiler. Building a robot is a sweet topic in electronics. One of the most common robots for beginners is the black (or white) line following robot. In this tutorial, we will make a robot that follows the line drawn on the surface. See the circuit performance video at the bottom of the page!
In these robots, infrared sensors or IR sensors are used to identify lines. IR sensors are good at detecting black or white lines. Although you can use more advanced sensors to have the ability to detect other colors as well.
Video display
00:00
00:24
Today, pathfinder robots are widely used in manufacturing, medical, household, etc. industries. And these robots can be developed that can do other things besides routing.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
We also made this project with Arduino board and PIC microcontroller and we use a little of the descriptions of those projects. You can see:
• Arduino router line following robot project
• Complete training on making a line following machine (PIC router robot project)
How the line following machine works
In this part, we will get to know the different parts and how the router robot works.
Infrared sensor section
 IR infrared sensor
The router robot is able to track the line with the help of an infrared sensor. This sensor has IR transmitter and IR receiver. The infrared transmitter transmits the light and the receiver (Photodiode) waits for the transmitted light to be reflected and returned. Not all surfaces reflect IR light, only a white surface can fully reflect them, and a black surface will completely absorb them as shown in the figure below.



In this line following robot, we used IR transmitters and receiver. IR modules are based on infrared and are used to send and receive light. According to the image above, when infrared rays shine on a white surface, the surface reflects it towards the infrared receiver. And when it shines on the black surface, that ray is absorbed by the black surface and nothing happens!
To manage this robot, we used AVR ATmega16 microcontroller. The driver part includes a drive motor and 2 DC motors. Because the microcontroller cannot provide enough voltage to the motors, we use the motor drive to provide enough voltage and current for the motors.
How to work with a line follower project with Atmel Studio
Working with this robot is very interesting, this robot senses the black line using sensors and sends the signal to the microcontroller, and then the Microcontroller informs the motors of the movement!
Suggested article: clock and date project with AVR microcontroller and seven segment
In this project, as we said, we use 2 sensors, one on the right and one on the left. When the two left and right sensors sense the white surface, the robot moves forward.
 AVR router robot tutorial
If the left sensor is placed on the black surface, the robot moves to the left.
If you have any questions about this article, ask in the comments section

If the right sensor is placed on the black line, the robot will turn to the right.
If both sensors are on the black line, the robot will stop!
 Stop the line follower robot
You can compare the above images with the table below to understand better:
Input, output, robot movement
Left sensor. Right sensor. Left engine. Right engine
LS RS LM1 LM2 RM1 RM2
0 0 0 0 0 0 Stop the robot
0 1 1 0 0 0 Turn right
1 0 0 0 1 0 Turn left
1 1 1 0 1 0 Moving forward
Parts required for the project
1. DC motor gear - two numbers
2. IR infrared sensor - two numbers
3. L293D module
4. Power bank
5. Atmega16 microcontroller
6. Crystal oscillator 16Mhz
7. 100nF capacitor – two numbers
8. Capacitor 22pF – two numbers
9. Button
Get the required parts from the Ironex parts store.
Items in the file: complete schematic, complete source
Building a self-balancing robot with Arduino (self-balancing robot project)
2019/02/10
Approximate reading time is 3 minutes

Contents [show]
hello We have prepared the training for making a self-balancing robot with Arduino (self-balancing robot project with Arduino). Watch the circuit performance video!
Learning how to build a balance robot with Arduino
In this Arduino project, we use a DC motor and an accelerometer to balance a self-balancing robot. You have seen examples of these robots in electric scooters. We make the robot so that even if we push it, the robot will maintain its balance and we can control it to go forward and backward. The performance video of this robot is placed at the end of the article.
Video display
00:00
00:37
Description of the self-balancing robot project with Arduino

The concept of project work is simple. We need to check whether the robot is leaning back or forward using the accelerometer sensor. If it leans back, we turn the wheels in the backward direction, and if it leans forward, we turn the wheels in the forward direction. We will explain the project part by part at your service.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
Controller: The controller we use in this project is Arduino UNO. Because it is very simple to use. You can also use Arduino Nano or Arduino mini. But I recommend you to use UNO because we can program it directly without any external hardware.
Motors: The best motor that you can use for your balanced robot is undoubtedly the stepper motor. But to keep the project simple, we use DC gear motor. Yes, having a stepper motor is not mandatory. The balancing robot also works well with these common yellow DC gear motors that are available.
Motor driver: We have used L298N motor driver to control the Gear DC motor.
Wheel: Be careful in choosing the right wheel! The wheels you choose should have the right amount of grip and the right amount of sliding.
Accelerometer and gyroscope: The best choice of accelerometer and gyroscope for this robot will be the MPU6050 sensor. So don't try to start this project with a normal accelerometer like ADXL345 or something like that! You will definitely not get an answer.
Battery: We need a battery that is as light as possible and its working voltage should be more than 5V so that we can power the Arduino directly without any booster module. So the ideal choice for us would be a 7.4V lithium battery.
Chassis: You have to be very careful to make the right chassis. You can make the chassis with cardboard, wood, plastic or anything else. Try to ensure that your chassis is strong enough and does not shake when the robot is maintaining its balance. We have included the 3D files for the design of this robot's body in the download file, and if you have access to 3D printers, you can use these files.
The list of required parts for the robot project with Arduino
• Arduino Uno board
• DC gearbox motor – two
• L298N driver motor
• MPU6050 accelerometer sensor – download library + specifications of MPU6050 sensor
• 7.4 V lithium battery
Suggested article: light detection and photocell setup with Arduino (device switch with LDR)
Get the required parts from the Ironex parts store.
Description of the project circuit

The complete schematic of the project is included in the download file. The connection of this robot is very simple. We just need to connect the MPU6050 gyro sensor to the Arduino and the motors to the motor driver module. The circuit is powered by a 7.4V lithium ion battery. The driver module and Arduino are powered directly through the +12 pin and Vin. The regulator on the Arduino Uno board converts the 7.4V battery input to 5V, and the microcontroller and accelerometer sensor get power from it. DC motors can work in the voltage range of 5 to 12 volts. In the table below, for your convenience, we have specified how to connect the pins of the accelerometer sensor and motor driver with Arduino.
Pins of Arduino pin parts
MPU6050 sensor
Vcc +5V
Ground Gnd
SCL A5
SDA A4
INT D2
L298N driver motor
IN1 D6
IN2 D9
IN3 D10
IN4 D11
The MPU6050 communicates with the Arduino via the I2C protocol, so we use Arduino pins A4 and A5. DC motors are connected to pins D6, D9, D10 and D11. We need to connect them to the PWM pins because we can control the speed of the DC motor.
Items in the file: Schematic, Hex file, Arduino file, 3D print file and...
Teaching Arduino Arduino projects
Arduino robot control with joystick (speed, distance and angle display)
02/03/2019
time
hello We have prepared a project to build a robot with Arduino and display the speed, distance traveled and angle. You can see the circuit performance video at the bottom of the page!
Learning how to make a robot with Arduino
These days, robots use various technologies such as GPS, RF, accelerometer, gyroscope, etc. to provide many possibilities. In this arduino project we will use LM393 speed sensor to measure some critical parameters like speed, distance and angle of movement of the robot using Arduino microcontroller. Arduino is the most popular choice among those interested in building robots, from line-following robots to more complex robots.
Video display
00:00
00:39
We build a small robot that is powered by a lithium battery and controlled using a joystick. During the movement time, we can measure the speed, distance traveled and the angle of the robot and display them in real time on the character LCD screen connected to Arduino.
Parts required for the project
1. Arduino Nano board
2. Character LCD
3. Motor driver L298N
4. Joystick
5. Lithium battery 2000mA 7.4V
6. DC motor – two numbers
7. Speed ​​sensor LM393 (or H206)
Get the required parts from the Ironex parts store.
Speed ​​sensor module LM393 – H206
Before I start explaining the code and circuit, let me introduce you to the LM393 speed sensor module. The H206 speed sensor has an infrared sensor and an LM393 voltage comparator. Because LM393 plays an important role in this sensor, this sensor is offered both under the name of speed sensor H206 and under the name of speed sensor H206.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store

The infrared sensor is equipped with an IR lamp and a phototransistor. The Grid screen consists of slots, this screen is placed between the infrared sensor so that the sensor can sense the grid screen slots. Each gap in the grid plate activates the IR sensor when passing through the gap. The activation of the infrared sensor, i.e. sensing the gaps in the Grid plate, are then converted into voltage signals using a comparator. Comparator IC LM393 has three pins, two of which are used to power the module and one output pin to count the number of actuators.
How to connect speedometer sensor LM393 H206
Installing this type of sensor is a bit difficult. It can be mounted only on engines that have shafts protruding from both sides. One side of the shaft is attached to the wheel while the other side is used to install the Grid plate as shown in the image below.
Suggested article: isPrintable command in Arduino (printability check)

Since the wheel and the plate are connected to the same shaft, both rotate at the same speed, and therefore the speed of the wheel can be measured by measuring the speed of the plate. Make sure that the slots of the grid screen pass through the infrared sensor, only then the sensor will be able to count the number of slots passed.
The grid shown above has 20 grid slots. This means that the sensor will find 20 gaps for a full rotation of the wheel. By counting the number of gaps detected by the sensor we can calculate the distance traveled by the wheel, similarly by measuring how fast the sensor finds gaps we can determine the speed of the wheel. In this car robot, we will install this sensor on both wheels and hence we can also find the angle of the robot.
Joystick robot project circuit with Arduino

The complete schematic file of this project is included in the download file. Our car robot uses Arduino Nano as its brain. Also, DC motors are driven by the L298N H-Bridge motor driver module. We use JoyStick to control the speed and direction of the robot. We use two H206 sensors to measure speed, distance and angle. The measured values ​​are displayed by a 2*16 character LCD. We use a potentiometer to adjust the LCD contrast. We also use the resistor to adjust the input current to the LCD backlight.

The circuit is powered by a 7.5V lithium battery. This 7.4V is connected to the 12V pin of the driver module. The 7805 voltage regulator converts 7.4V to +5V, which is used to power the Arduino Nano board, character LCD, sensors and joystick.
The motors are controlled by digital pins 8, 9, 10 and 11 of Arduino. Since the speed of the motors must also be controlled, we must connect the PWM signals to the + terminal of the motor. Pins 9 and 10 of Arduino are able to generate PWM wave. The X and Y values ​​of the joystick are read using analog pins A2 and A3, respectively.
If you have any questions about this article, ask in the comments section
How to calculate speed by H206 sensor
After installing the sensor, make sure that the grid plate and the motor rotate at the same speed. If you only want to measure speed and distance, you can use a sensor.
When the screen rotates, the sensor senses the gap and sends a signal to the microcontroller, and with the next gap, another signal is sent. Using the time interval traveled between two gaps, we can calculate the speed.
In Arduino we can easily calculate the speed using the millis() function. When the first interrupt occurs we can store the millis() value in a dummy variable (as in the code below) and then when the second interrupt occurs we can calculate the millis() value by subtracting the pevtime value.
Time taken = current time – previous time
timetaken = millis()-pevtime; // Spent time
After calculating the elapsed time, we can easily calculate the rpm using the following formulas, dividing 1000 by the elapsed time gives us RPS and multiplying by 60 to convert RPS to RPM (revolutions per minute).
rpm=(1000/timetaken)*60;
After calculating the revolutions per minute, the speed (v) of the vehicle can be calculated using the following formulas, provided that we know the radius of the wheel.
v = 2π × RPS × wheel radius
>>>> v = wheel radius * rpm * 0.104
Note that the above formula is for calculating the speed in meters per second, if you want it to be calculated in kilometers per hour, replace 0.0104 with 0.376.
Suggested article: Temperature and humidity measurement project with Arduino
The mesh screen has 20 slits, and therefore, to measure the time between two slits, the microcontroller bears a lot of extra load. Since there are two breaks for each speed measurement (one at the start and one at the end of the gap) we will make a total of 40 breaks for the wheel to make a full revolution. So we wait for 40 interrupts before calculating the wheel speed. The code of this section is shown below:
if(rotation>=40)
{
 timetaken = millis()-pevtime; // time spent ms
 rpm=(1000/timetaken)*60; //Formula for calculating rpm
 pevtime = millis();
 rotation=0;
}
The disadvantage of this method is that, the speed value does not go to zero because the microcontroller is always waiting for one rotation to calculate the rpm value. This bug can be fixed by adding a simple code that monitors the time interval between two breaks and if it is more than normal, we can set the rpm and speed to zero. In the code below, we have used the dtime variable to check the time difference, and if it is greater than 500 milliseconds, the value of speed and rpm will be zero.
if(millis()-dtime>500)
{
 rpm = v = 0; // Set the speed and revolutions per minute to zero
 dtime=millis();
}
Teaching how to calculate distance by LM393 sensor
We already know that the arduino will sense 40 interrupts when the rotation is complete. So for every rotation by the wheel, it is obvious that the distance traveled by the wheel is equal to the circumference of the wheel. Since we already know the radius of the wheel, we can get the distance using the following formula. (Distance = distance)
Distance = 2πr * number of wheels
distance = (2*3.141*wheel radius) * (left_intr/40)
How to calculate angle by LM393 sensor
As I said before, if you don't want to get the angle, using only one H206 sensor is enough.
There are many ways to determine the angle of the robot. Accelerometer and gyroscope are usually used to determine these values. But using the H206 sensor in both wheels is a cheaper method. In this way, we know how many revolutions each wheel has made. The figure below shows how to calculate the angle.

When the robot is turned on, the angle it is in is assumed to be 0 degrees. From there, it turns to the left, the angle increases in the negative, and if it turns to the right, the angle increases in the positive. To understand, draw the range from -90 to +90 as shown. In such an arrangement, since both wheels have the same diameter, if any of the wheels make a complete rotation, the robot will rotate at an angle of 90 degrees.
For example, if the left wheel makes a complete turn (80 breaks) and the robot turns 90 degrees to the left, and similarly if the right wheel makes a complete turn (80 breaks), the robot turns -90 degrees to the left. It turns right. Now we know that if the arduino detects 80 breaks in a wheel, the bot has turned 90 degrees, and based on which wheel it has turned, we can tell whether the bot has turned positive (right) or negative (left). Therefore, the left and right angles can be calculated using the following formulas.
int angle_left = (left_intr % 360) * (90/80) ;
int angle_right = (right_intr % 360) * (90/80) ;
Once we have calculated both the left and right angles, we can get the angle the robot is facing by subtracting the left angle from the right angle. (angle = angle)
angle = angle_right - angle_left;
Description of project code in Arduino software
In this part of the code, we define the pins that we said in the circuit description section:
#define LM_pos 9 // left motor
#define LM_neg 8 // left motor
#define RM_pos 10 // Right motor
#define RM_neg 11 // Right motor
#define joyX A2
#define joyY A3
In this part of the code, you must enter the radius of the wheel you are using in centimeters:
float radius_of_wheel = 0.033; //For further measurements
Items in the file: Schematic, Hex file, Arduino file, etc.
PIC training, PIC project
PIC microcontroller obstacle avoidance robot project
01/28/2019
Approximate reading time is 3 minutes

Contents [show]
hello We have prepared the project of preventing the robot from colliding with the PIC obstacle (complete training for making a robot with an ultrasonic sensor). Action movie
We must have general information about the ultrasonic sensor. We know that sound vibrations cannot penetrate through solids. So when a sound source causes a vibration, that vibration travels through the air at a speed of 220 meters per second. As we said, these vibrations cannot penetrate through solids, that is, when they hit a surface like a wall, they return to the sensor at the same speed, this technique is called ECHO.
Suggested article: odometer and odometer with PIC and Hall effect sensor

The "HC-SR04" ultrasonic sensor provides an output signal proportional to the distance based on the echo. The sensor here generates a sound vibration within the range of the sensor, and after sending a vibration, it waits for the sound to return.
 How the ultrasonic sensor works
The circuit of the project of the robot not to collide with the obstacle with PIC

The circuit consists of an ultrasonic sensor, two IR sensors and a pair of DC motor gears along with a motor driver module. The motor driver module used in this project is L293D.

We will need a motor driver because the output pin of the PIC microcontroller cannot provide enough power to drive the motor. As you can see in the schematic, this module is powered directly from the power supply (5V). This module has four pins (two for each motor) that are connected to the PIC to control the direction of the motors. You can download the complete schematic from the bottom of the page. You can use a power bank like me or use a 9 or 12 volt battery and use a 7805 regulator to adjust the current to 5 volts.
Parts required for the project
1. PIC16F877A microcontroller (PIC16F877A datasheet)
2. Infrared sensor - 2 pcs
3. Ultrasonic sensor HC-SR04
4. Gear DC motor – 2 pcs
5. L293D drive motor
6. Power bank or 12 volt power supply with 7805 regulator
Get the required parts from the Ironex parts store.
Items in the file: complete source file, complete schematic and...
Airnex/PIC training/Routing robot training with PIC microcontroller
PIC training, PIC project
Teaching how to build a router robot with a PIC microcontroller
01/28/2019
Approximate reading time is 3 minutes

Contents [show]
hello We have prepared a complete tutorial on making a line following machine (PIC router robot project). Watch the circuit performance video!
PIC router robot project
The line following machine is a simple yet attractive robot for most students. In this tutorial we will learn how a router robot works and how we can build it using PIC16F877A microcontroller. The PIC16F877A is a multipurpose microcontroller that has 40 pins. If you are interested in robotics, then you must be familiar with the name "routing robot". This robot is able to follow a line using a pair of infrared sensors and a motor.
Video display
00:00
00:45
See also:
• Router robot project with Arduino
• Line following robot with AVR
How the line following machine works
Infrared sensor section
 IR infrared sensor
The router robot is able to track the line with the help of IR infrared sensor. This sensor has IR transmitter and IR receiver. The infrared transmitter transmits the light and the receiver (Photodiode) waits for the transmitted light to be reflected and returned. Not all surfaces reflect IR light, only a white surface can fully reflect them, and a black surface will completely absorb them as shown in the figure below.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Board Pico training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store

In this PIC project, we use two IR sensors to check whether the robot is moving on the line or not. These motors need high current. Hence we use a motor driver module like L293D. We will also need a microcontroller like PIC to move the motors based on the IR sensor information.
Each infrared sensor is placed on one side of the line. If neither sensor detects a black line, the PIC microcontroller commands both motors to run.
If the left sensor is on the black line, the robot moves to the left. This means that the right engine turns off and only the left engine moves.

If the right sensor is placed on the black line, the robot will turn to the right. It means that the left engine turns off and only the right engine moves.

If both sensors are on the black line, the robot will stop.

Router project circuit with PIC microcontroller

The circuit consists of two IR sensors and a pair of DC motor gears along with a motor driver module. The motor driver module used in this project is L293D. We will need a motor driver because the output pin of the PIC microcontroller cannot provide enough power to drive the motor. As you can see in the schematic, this module is powered directly from the power supply (5V). This module has four pins (two for each motor) that are connected to the PIC to control the direction of the motors. We also have two IR sensors that connect to the PIC microcontroller. You can download the complete schematic from the bottom of the page.
Suggested article: Smart home project with Android Bluetooth and PIC (device control with mobile)

In this project, we used a power bank that gives us +5V directly through its USB port. Hence we don't need 7805 voltage regulator and we use the same for PIC, sensors and motors. You can also use a 12V battery with a regulator as shown in the schematic.
Parts required for the project
1. PIC16F877A microcontroller (see datasheet)
2. Infrared sensor - 2 pcs
3. Gear DC motor – 2 pcs
4. L293D drive motor
5. Power bank or 12V power supply with 7805 regulator
Get the required parts from the Ironex parts store.
Robot project code description
Above, we showed how the robot moves with pictures, here we also want to explain the code. We need to define for the microcontroller in which states to activate which motors.
If you have any questions about this article, ask in the comments section
In this part of the code, we say that if both IR sensors are not on the black line, both motors will move.
if (RD2==1 && RD3==1) //Both sensors are not on the black line
 {
 RC4=0; RC5=1; //Move motor 1
 RC6=1; RC7=0; //Move the motor 2
 }
In this part of the code, we say that if the left sensor is on the black line, only the right motor will move.
else if (RD2==0 && RD3==1) //The sensors on the Jeep side are on the black line
 {
 RC4=1; RC5=1; //Engine 1 off
 RC6=1; RC7=0; //Move the motor 2
 }
In this part of the code, we say that if the right sensor is on the black line, only the left motor will move.
else if (RD2==1 && RD3==0) //The right sensor is on the black line
 {
 RC4=0; RC5=1; //Move motor 1
 RC6=1; RC7=1; //Engine 2 off
 }
In this part of the code, we say that if both IR sensors are on the black line, both engines will be turned off.
else // Both sensors are on the black line
 {
 RC4=1; RC5=1; //Engine 1 off
 RC6=1; RC7=1; //Engine 2 off
 }
Items in the file: complete source file, complete schematic and...
