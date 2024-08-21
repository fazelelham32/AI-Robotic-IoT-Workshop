# AI-Robotic-IoT-Workshop

## What is the Internet of Things?
IoT, or Internet of Things, is a term used to describe thousands of physical devices that are connected to the Internet and capable of receiving and sending data. Thanks to the existence of very cheap computer chips and the abundance of wireless networks in the world today, almost anything can be included in the world of IoT. In this system, the size of the object is not important, an object as small as a tablet or as big as an airplane can be equipped with the Internet of Things. Connecting objects to the Internet and adding various sensors to them actually equips them with artificial intelligence. As a result, objects whose function was dependent on human presence until now can transmit information without human interaction with Internet of Things technology. In simpler words, the Internet of Things, by combining the physical and digital world, makes the objects around us smarter and more active.
A simple example of the Internet of Things
In practice, the number of devices that can enter the IoT world is uncountable. Any device that can be controlled by connecting to the Internet or through which information can be exchanged can be part of the IoT. For example, a simple light bulb can be turned into an IoT device by connecting to a mobile application. Now it is possible to turn on and off, adjust the light of the lamp, etc. remotely and through the Internet.

An IoT device can be as soft and cute as a child's doll or as large as a driverless truck. Large devices with different capabilities may consist of several IoT devices. A concrete example of this is a jet engine, which consists of thousands of different sensors, each of which collects and transmits specific information to ensure the efficiency of the jet engine. The Internet of Things has entered even larger projects. The smart city project is actually designed based on the Internet of Things. Where the countless sensors that are installed everywhere are supposed to help humans in knowing and controlling their surroundings.
It is necessary to mention that the title of Internet of Things is used for devices that do not have the ability to connect to the Internet by default. Therefore, computers, mobile phones and the like are not among IoT devices.
Benefits of Internet of Things
The benefits of IoT in business depend on how it is used. It is usually used to increase the agility and efficiency of products. The problem here is that in order to benefit from this opportunity, companies must have complete control over their products and internal system and have the possibility to change it.
Currently, various companies are adding various sensors to their products to be able to transmit data. As a result, if one of the components of the product is disturbed through the information sent, the manufacturing company finds out and prevents heavier losses. Basically, this information is a good measure to evaluate how the company's products work, which can lead to an increase in the efficiency of the products and their production process.
The application of Internet of Things can be divided into two parts: public and private.
General application of Internet of Things: It is not specific to a specific industry and can be useful for everyone, such as a smart air conditioning system or a smart security system.
Specific use of Internet of Things: It is used in a specific field, such as a tracking device or smart health bracelets
Although the use of IoT devices is apparently widespread among people, research shows that different industries use this technology much more.

### Application of Internet of Things in industry
IIoT or Fourth Industrial Revolution is the title used for the application of Internet of Things in industry. The Internet of Things in industry is defined as follows: the use of a combination of sensors, wireless networks and abundant data and their analysis in order to improve the performance of an industrial process.
At first glance, the use of the Internet of Things will lead to the management of the production process and the supply of a standard product, which includes benefits such as increased labor productivity and cost savings. But in fact, this technology can also create new ways to earn money. As we said, by using the Internet of Things in the products of a factory, it is also possible to detect malfunctions in the product and identify defective parts. As a result, the manufacturing plant can earn good income from the sale of required spare parts.
Application of Internet of Things for people
Internet of things, the world around us, including home, workplace, vehicles, etc. . . makes it intelligent, controllable and interactive. For example, smart audio systems such as Amazon's Echo and Google home will play music, answer your questions, set the alarm clock, and so on with just your voice command without having to get up. With smart security systems, you can easily control the inside and outside of the house; Or, with a smart thermostat system, you can heat it up before you get home. Outside the house, the Internet of Things can give you accurate information about the level of crowding or air pollution, and in the near future, driverless cars will change the way of urban design and management. The important point is that all these smart facilities and tools can have consequences for human privacy.
Internet of things security
One of the most important challenges in this field is the issue of Internet of Things security. All IoT devices use high-sensitivity sensors to receive information. As a result, for example, in a smart home, everything you say and everything you do is recorded by sensors. It is necessary to ensure the security of this information to gain consumer trust, but in practice, a limited number of these equipments use special facilities such as encryption to store their information.
Every day new software problems are discovered in these devices. But the problem is that the software system of many of these devices cannot be changed or repaired. Therefore, most of these devices are always at risk. Hackers easily hack devices such as routers or webcams. This issue is more sensitive in the case of devices such as trackers or smart watches that are designed and produced for children because it endangers their safety.
In the industry, the situation of industrial devices equipped with IoT is not better than this. Industries that intend to connect their equipment and machines to the Internet must ensure the security of their network. Because this may lead to industrial espionage and hacker attacks on industrial infrastructure.
last word
Undoubtedly, IoT technology can be a good opportunity to achieve significant improvements. But the ever-increasing and rapid expansion of the Internet of Things has taken away the opportunity for reflection and thinking in this field from people. The important issue is that very cheap sensors and network equipment also increases the production rate of these products on the one hand and makes it more difficult to secure them on the other hand. As a result, people are divided into two groups, some enjoy the possibilities of this technology regardless of security concerns, and others, by banning it, do not allow any sensors and cameras into their privacy. Although it seems that sooner or later this technology will spread all over the world.
The website is fully active and we are always putting the latest projects in the field of Internet of Things for users. Airnex website is obliged to answer your questions. You can ask your questions in the field of circuit design, project source code, etc. through the comments of any project or forum. Or share it privately by contacting the admin. The admin will answer your questions as soon as possible. To see the rest of the list, click on the next page button at the bottom of the page.
Esp training, Arduino training, Internet of Things training, Esp projects, Internet of Things projects

In the previous article called How to build a web server with Arduino and ESP8266, we discussed the basics of building an Arduino web server. Now, let's learn how to control GPIO pins of Arduino board through web page. In this tutorial, we are going to change the state of an LED from a web page that can be accessed from any device with an internet connection.
But first, let's review some essential terms:
• Web server – software, hardware, or a combination of both that contains the files needed to process and serve web pages.
• Web Client – ​​Any device that can send an HTTP/Web request to a Web server.
• Local server – a web server that can only be visited within your LAN (local area network).
• World Server – A web server that can be accessed anywhere in the world via the Internet WAN.
• HTTP POST – A web request that transmits data to a server.
• HTTP GET – A web request that retrieves data from a web server
Port Forwarding – A router setting that forwards traffic from a WAN port to a specific device within your LAN.
LED control circuit from the Internet with Arduino
Using jumper wires, connect the parts as shown below:
 Just like before, we use Arduino UNO to program the ESP-01 module. To do this, we disable the internal chip of the UNO by connecting the RESET pin to GND. Set ESP8266 module as board in Arduino IDE. To set the ESP-01 module in programming mode, connect the GPIO0 pin to GND. Similarly, before uploading, connect and disconnect the ESP-01 module's RESET pin to GND.

 For this project we need the following parts:
• Arduino Uno
• ESP8266 ESP-01 module
• 1 kilo ohm resistance
• 2 * 2 kilo ohm resistance
• 10 kilo ohm resistance
• LED
• Board
• Jumper wires
Get the required parts from the Ironex parts store.
GPIO control project code via web page
The complete code is placed in the downloadable file at the bottom of the page. Here we explain the important parts of the code. We only need ESP8266WiFI.h. It comes with the ESP8266 board library, so there is no need to install it.
#include <ESP8266WiFi.h>
Enter your home modem connection information here.
const char* ssid = "WiFi name";
const char* password = "WiFi password";
Set the web server port number to 80.
WiFiServer server(80);
In the setup section, set the LED pin as output and initialize it to LOW.
Interestingly, the internal LED of ESP-01 is connected to GPIO2 but its LOW is active. If you set the GPIO2 pin to LOW, the LED connected to GPIO2 will turn off while the internal LED will turn on. Make monitor serial settings. The serial monitor is used to display information such as the IP address of the ESP-01 module. It also helps in identifying errors.
Suggested article: MAX7219 matrix LED control with Arduino and Android Bluetooth
Finally, we start the web server using server.begin().
void setup()
{
 Serial.begin(115200);

 pinMode(ledPin, OUTPUT);
 digitalWrite(ledPin, LOW);

 Serial.print("Connecting to ");
 Serial.println(ssid);
 WiFi.begin(ssid, password);

 while (WiFi.status() != WL_CONNECTED)
 {
 delay(100);
 Serial.print(".");
 }
 Serial.println("");
 Serial.println("Connected to WiFi");
 Serial.print("IP: "); Serial.println(WiFi.localIP());

server.begin();
}
Then, in the loop section, we have the server.available () function. This function detects new clients. Always returns false when none exists. On the contrary, if the code detects a new client, it becomes true and goes to the next line.
WiFiClient client = server.available();
 if (!client) {
 return;
 }
It then waits for the client to send a request.
 while(!client.available()){
 }
It reads the request and then prints it on the serial display. The client.flush() function makes sure that all output characters have been sent.
 String request = client.readStringUntil('\r');
 Serial.println(request);
 client.flush();
/LED=ON and /LED=OFF are the names of the requests we use to turn the LED on and off. We will see them later in the HTML code.
If you have any questions about this article, ask in the comments section
 int value = LOW;
 if (request.indexOf("/LED=ON") != -1) {
 digitalWrite(ledPin, HIGH);
 value = HIGH;
 }
 if (request.indexOf("/LED=OFF") != -1){
 digitalWrite(ledPin, LOW);
 value = LOW;
 }
Finally, we create a web page using client.println().
 client.println("HTTP/1.1 200 OK");
 client.println("Content-Type: text/html");
 client.println("");

 client.println("<!DOCTYPE HTML>");
 client.println("<html>");
 client.print("LED status: ");

 if (value == HIGH)
 {
 client.print("ON");
 }
 otherwise
 {
 client.print("OFF");
 }
 client.println("<br><br>");
 client.println("Turn <a href=\"/LED=ON\">ON</a><br>");
 client.println("Turn <a href=\"/LED=OFF\">OFF</a><br>");
 client.println("</html>");

 Serial.println("");
Here, we see how we named the requests /LED=ON and /LED=OFF.



## Here, we see how we named the requests /LED=ON and /LED=OFF.
 client.println("Turn <a href=\"/LED=ON\">ON</a><br>");
 client.println("Turn <a href=\"/LED=OFF\">OFF</a><br>");
1. Upload the code, then open the serial monitor. Sometimes the serial monitor displays strange data and the ESP-01 refuses to connect. An easy solution is to connect and disconnect the ESP-01 module's RESET pin to ground.
2. Enter the IP address given from the serial monitor in a web browser you have. The first line shows whether the LED is currently on or off. To change its mode, simply click on the links.

Let us know in the comments how you implemented this code!
Tips for troubleshooting:
• Never forget to connect Arduino's RESET pin to GND.
• Make sure the upload speed is 115200.
• Check the voltage of your voltage divider circuit. It should give 3.3V to your RX pin.
• Downgrade your ESP8266 board library to version 2.5.0 in the Boards Manager if you keep getting errors when uploading a code to the ESP-01.
Items in the file: Complete source file
Esp training, Arduino training, Internet of Things training, Esp projects, Internet of Things projects
Building a web server with Arduino and ESP8266 (comprehensive training)
03/03/1401
Approximate study time 13 minutes

Contents [show]
With the emergence of intelligent systems and the use of data and artificial intelligence, predictions about the Internet of Things have come true. The Internet of Things has become the fourth industrial revolution and has successfully changed technology and residential production. What better time than today to learn the Internet of Things? In this tutorial, we are going to set up a web server using Arduino and ESP8266-01. Let's get started!
Web server vs client
A web server is software, hardware, or a combination of both that contains the files needed to process and serve web pages. A web client is simply any device that can send an HTTP/Web request to a web server. HTTP or Hypertext Transfer Protocol is a unique protocol that web server and web client use to communicate.
For a better understanding, imagine that you want to enter irenx.ir. First, you enter the address in your browser, after a few seconds, you will see the main page of Airnex.
In this example, your computer is a web client. Your computer sends a web request using a web browser, such as Chrome or Firefox. The web browser sends the request to the web server that hosts Airnex. Then, the data needed to display the main page of Airnex will be received on your computer. A web server that hosts a website is usually a dedicated computer that stores large amounts of data. They also have unique IP addresses.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Pico board training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
Arduino web server
You will not need large servers that are specific to sites. You can simply connect an Arduino to an ESP8266 module and build a simple but useful web server. With an arduino web server, you can create a web page that displays sensor data or control the bases through it.
A web server that can be accessed anywhere in the world through the Internet is called a global server. Also, a web server that is accessible only on your local area network (LAN) is called a local server. There are many ways to create a global server. In this tutorial, we are going to use a method called port forwarding.
Web requests
To receive data from web servers, clients (requester - user) use HTTP requests. There are several types of HTTP requests, but you only need to learn two to create an Arduino server. These requests are called HTTP GET and HTTP POST.
• HTTP GET is a web request that retrieves data from a web browser. Nothing changes on the server. It only receives and reads data.
• HTTP POST is a web request that transmits data to a server. That is, it adds something new to the server. A typical example of a GET request is the simple browsing of a website. On the other hand, POST requests are used to type text into a web page, for example, username and password. ESP8266-01 module
 The ESP8266 is a Wi-Fi chip developed by Espressif Systems. This module provides full WiFi networking capabilities and enables users to run a web server or web client with a separate or even stand-alone processor. This module is well compatible with Arduino, which means you can program it using Arduino IDE. We are going to use ESP-01 version ESP8266 module. This module is developed by a third-party developer called AI-Thinker. The ESP8266 has a built-in MCU (microcontroller unit) that allows users to control the digital I/O pins directly through the Arduino IDE.

• GND – Ground
• GPIO2 – Programmable I/O pin with an internal pull-up resistor
• GPIO0 – Programmable I/O pin with internal pull-up resistor
• RX – UART receiver pin
• VCC – 3.3V pin
• REST – External reset pin
• CH_PD – Chip enable pin
• TX – transmitter pin UART

### Setting up a local web server with Arduino
Before creating a global server, we need to know how a local server works. To set up a local server, we need to find a way to send AT commands to the ESP-01. These commands come from the pre-installed AT ESP-01 firmware. We can use FTDI cable to send them directly or we can use a separate processor like Arduino. In this tutorial, we are going to use an Arduino.
Suggested article: Audio recording with Arduino (Eavesdropping with Arduino board)
First you need the following parts:
• Arduino Uno
• ESP8266 ESP-01 module
• Two resistors of 1 kilo ohm
• Board
• Jumper wires
Get the required parts from the Ironex parts store.
Then connect the ESP-01 to the Arduino as shown below:
If you have any questions about this article, ask in the comments section

The maximum input voltage of ESP8266-01 is 3.6V. Always double check the pins when connecting it to a 3.3V power supply. If you accidentally connect it to a 5V power supply, the module may be permanently damaged.
Both 1 kOhm resistors act as pull-up and pull-down resistors for CH_PD and RX pins, respectively.
Using the Arduino IDE
After preparing the hardware, we will now proceed to the programming.
Open the Arduino IDE. Go to File >> Examps >> Basics >> BareMinimum then upload the code. This is to ensure that no program is running on the Arduino board. Then open the serial monitor. Make sure to set the baud rate to the default, which is usually 115200. Then type the following AT command:
AT
If you see “OK”, it means ESP8266-01 is working. If you don't get a response, connect the RST pin to GND and try again.
AT commands in ESP8266
ESP8266 AT commands allow users to perform operations such as connectivity testing, operating mode setting, WiFi connection, IP address determination, etc.
Mode setting
After confirming the operation of the chip, set the operation mode by typing the following AT command:
AT+CWMODE=1
The ESP8266-01 has three working modes: (1) station (STA); (2) access point (AP); and (3) both
In the first case, you configure the WiFi module to act as a station (STA). This module acquires the ability to connect to an existing WiFi network.
In the second mode, you configure the WiFi module to act as an access point (AP). This module acts as a WiFI network where devices such as computers can connect to it.
In the third mode, you configure the WiFi module to act as both AP and STA.
If we want to use it as a web server, we need to set the module to AP mode. To check what mode the ESP8266 is in, type AT+CWMODE. The answer will be number 1, 2 or 3, which corresponds to the mode of operation.

### Connect to Wi-Fi
To connect to a Wi-Fi network, type the following command:
AT+CWJAP= “SSID”, “Password”
These are case sensitive, so be sure to type the WiFi network name and password exactly. Also, there should not be a space between the quotation mark and the comma. If the connection is successful, you will receive an OK response.
Verify the connection using this AT command:
AT+CIFSR
This AT command gives the IP and MAC addresses of the ESP-01 module. Make sure to write down both your IP and MAC address as we will use it for port forwarding later.
Enable connections
We also need to configure the ESP-01 to support multiple connections as we need it as a server. To do this, enter this command in the serial monitor:
AT+CIPMUX=1
Additionally, start the server using the command:
AT+CIPSERVER=1,80
The first number shows the status of the port. A value of 0 means closed while a value of 1 means open. On the other hand, the second number indicates the port number. Port 80 is the default port number of the HTTP protocol, which we also use for HTML pages.
At this point, we have established a connection between your home router and the ESP-01. Now we are ready to send HTTP requests from your computer to the module.
Send and receive data
To send a GET request, simply enter the IP address of your ESP-01 module in your browser. This will send a response on your monitor serial. The response contains several useful information such as the details of the file to be recovered, the name of the browser used for the request, the operating system, etc.
Note that if your web browser does not display anything, it is because there is no data to recover yet.
Suggested article: Door security lock project with Arduino numeric keyboard with handmade lock
We're going to send a plain "Hello World" to test our connection. Type the following command into your serial monitor:
AT+CIPSEND=0,12
The first number indicates the channel through which the data is to be transmitted. While the second number shows the number of characters sent. Since we are going to send "Hello World", we need to set the second number to 12 so that it will be sent completely including the space.
After pressing enter, the > sign will appear. This means that the server is already waiting for the message. Next, type Hello World into your serial monitor. After some time, the serial monitor will display SEND OK. Finally, to display the data in your web browser, close the communication channel by typing the following command:
AT+CIPCLOSE=0
As soon as you press Enter, a Hello World message should appear in your web browser.
Setting up a global server with ESP8266
Now that we are done with the local server, we will proceed with connecting the ESP-01 to the Internet. In this section, we are going to create a global server that displays the date, time, temperature, and humidity on a web page that you can access anywhere.
Using the parts listed below, connect your Arduino and ESP8266 ESP-01 module as shown in the image below:
• Arduino Uno
• ESP8266 ESP-01 module
• DHT22 temperature and humidity sensor
• Two 10K ohm resistors
• A 1K ohm resistor
• A 2.2K ohm resistor
• Board
• Jumper wires


Previously, we used the serial monitor to send AT commands to the ESP-01. This time we will do the actual programming.
Connect the RST (Reset) pin of the Arduino to GND (Ground). Setting RST to GND disables the Arduino chip so we can use the board as an ESP programmer. Next, we turn on the ESP-01. Unlike before, we will not be using the Arduino's 3.3V supply. Since we are using the sensor now, we will need more current. Fortunately, the 5V base provides enough current for both, but we need a voltage divider to change the voltage to 3.3V. Connect a 1 kOhm and 2.2 kOhm resistor in series as shown in the picture above. Connect the end of the series to GND. Finally, connect the other leg of the 1k ohm resistor to the positive rail of the board.
Next, we turn on the DHT22. The DHT22 module requires 3.3V to 5V to operate. You can connect it to any source. If you want to use 5V, connect it to the pin before the voltage divider. Then, use a 10k pull-up resistor along the data line connecting the DHT22 and the ESP-01.
Then, connect the EN/CH-PD (Enable) pin to the 3.3V power supply to initialize the ESP-01 module. Use a 10k pull-up resistor.
Finally. Connect GPIO pin 0 to GND to start programming mode.
Programming ESP8266 to build a web server
In the first step, with the ESP8266 tutorial, install the required items of this board in the Arduino software.
Then install all required libraries. ESP8266WiFi.h and ESP8266WebServer.h are internal, so they will be available in Boards Manager after installing the ESP8266 board. These two libraries provide access to functions that help you connect to a WiFi network, set up a server, and handle HTTP requests.
The DHT.h library is a library from Adafruit that supports DHT temperature and humidity sensors. You can download this library from here.
NTPClient.h and WiFiUdp.h are for NTP server synchronization and UDP protocol management respectively. The NTPClient library can be downloaded from here. The WiFiUdp.h library is built-in, so there is no need to install it.
After installing the libraries, put the complete code in the download file at the bottom of the page in the Arduino software and then upload it to the ESP8266 module.
Here we explain the important parts of the code.
First, we include all the libraries:
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <DHT.h>
#include <NTPClient.h>
#include <WiFiUdp.h>
Then, to connect to your home Wi-Fi, enter your network information in the two lines below.
const char* ssid = "wifi name";
const char* password = "wifi password";
Next, we initialize a WifiUDP and NTPClient instance. Setting up an NTPClient object requires a WiFiUDP object, an NTP server, and an offset to specify your time zone. We use pool.ntp.org as the NTP server address. It will automatically detect the nearest time server from your location. Finally, for the UTC offset for your time zone, use this formula:
UTC X = X * 60 * 60
We are in Iran at GMT+3:30 so for me,
Suggested article: servo motor control project with Flex sensor and Arduino
UTC 3.5 = 3.5 * 60 * 60 = 12600
WiFiUDP ntpUDP;
const long utcOffsetInSeconds = 12600;
NTPClient timeClient(ntpUDP, "pool.ntp.org", utcOffsetInSeconds);
The epoch time function returns the number of seconds since January 1, 1970. We use this function along with the time structure to get the date.
unsigned long epochTime = timeClient.getEpochTime();

struct tm *ptm = gmtime ((time_t *)&epochTime);
Now open port 80 using ESP8266WebServer server(80); we open
Then in the Setup function, we initialize the monitor serial to 115200 to display commands and information. Additionally, using the start functions, we connect to WiFi, start the server, and then start the DHT sensor and time server.
void setup() {
 Serial.begin(115200);
 pinMode(DHTPin, INPUT);

 Serial.println("Connecting to ");
 Serial.println(ssid);

 WiFi.begin(ssid, password);

 while (WiFi.status() != WL_CONNECTED) {
 delay(1000);
 Serial.print(".");
 }
 Serial.println("");
 Serial.println("Connected to WiFi");
 Serial.print("IP: "); Serial.println(WiFi.localIP());

 server.on("/", handle_OnConnect);
 server.onNotFound(handle_NotFound);
 server.begin();
 dht.begin();
 timeClient.begin();
}
Next is the time to set up the loop. The loop section contains only one line. This line is a function of the ESPWebserver library. It monitors the presence of a web client and handles HTTP requests just like POST and GET.
void loop() {
 server.handleClient();
}
If handleClient() detects a request from a web client and connects successfully, it redirects the schema to the handle_OnConnect() function. On the other hand, if there is an error in the connection, it goes to handle_NotFound().

void handle_OnConnect(){
}
void handle_NotFound(){
}
Inside the handle_OnConnect() function there are commands that get the date, time, temperature and humidity from the relevant libraries.


Inside the handle_OnConnect() function there are commands that get the date, time, temperature and humidity from the relevant libraries. Using the time structure we set earlier, we get the current date. For the time, we use getFormattedTime() directly from the NTPClient library. The same goes for temperature and humidity, where we use dht.readTemperature() and dht.readHumidity() directly from the DHT library. Finally, server.send() returns the data to the client.
void handle_OnConnect() {

 timeClient.update();

 epochTime = timeClient.getEpochTime();
 String Time = timeClient.getFormattedTime();

 tm *ptm = gmtime ((time_t *)&epochTime);

 int monthDay = ptm->tm_mday;
 int currentMonth = ptm->tm_mon+1;
 int currentYear = ptm->tm_year+1900;

 Time = timeClient.getFormattedTime();
 Date = String(currentYear) + "-" + String(currentMonth) + "-" + String(monthDay);
 Temperature = dht.readTemperature();
 Humidity = dht.readHumidity();

 server.send(200, "text/html", SendHTML(Temperature,Humidity,Time,Date));
}
Finally, we use SendHTML() to create a web page for the collected data.
String SendHTML(float TemperatureWeb, float HumidityWeb, String TimeWeb, String DateWeb){
 String ptr = "<!DOCTYPE html> <html>\n";
 ptr +="<head><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0, user-scalable=no\">\n";
 ptr +="<title>ESP8266 Global Server</title>\n";

 ptr +="</head>\n";
 ptr +="<body>\n";
 ptr +="<div id=\"webpage\">\n";
 ptr +="<h1>ESP8266 Global Server</h1>\n";

 ptr +="<p>Date: ";
 ptr += (String) DateWeb;
 ptr +="</p>";
 ptr +="<p>Time: ";
 ptr += (String)TimeWeb;
 ptr +="</p>";
 ptr +="<p>Temperature: ";
 ptr +=(int)TemperatureWeb;
 ptr +="C</p>";
 ptr +="<p>Humidity: ";
 ptr +=(int)HumidityWeb;
 ptr +="%</p>";

 ptr +="</div>\n";
 ptr +="</body>\n";
 ptr +="</html>\n";
 return ptr;
}
View the result of building the web server
Upload the code to ESP-01. Select “Generic ESP8266 Module” as the board. Be sure to select the correct port number as well.

After uploading, open Serial Monitor and you should see something like this:

Using a browser, enter the given IP address. Then you can see the result:

This is still a local server. To make this web page available outside of your home network, we need to use a technique called port forwarding.


## ESP8266 port forwarding
Port forwarding is a network router feature that forwards traffic from a specific port on the WAN to a device inside your local network. Here's how port forwarding is done:
1. First, know your IP address. You can do this by typing "my pi" in Google.
2. Visit your router's homepage. Enter your router's IP address in your web browser. Each model is different but for most modems it is set to 198.168.1.1.
3. Then enter the DHCP section. Add the IP address of the ESP8266 module to Static to keep it constant. for Sur
4. Learn how to change DHCP settings. Add the ESP-01 IP address to static to keep it static. For our example server above, it would be “192.168.0.18”. Also enter the MAC address you got from the AT+CIFSR command. After applying these, your router will reserve the address 192.168.0.18 for the ESP-01.
5. Then go to Port Forwarding settings. Create a virtual server using the TCP protocol. Use port 80 then enter the IP address of ESP-01. Don't forget to save the changes you made to your router.
6. Finally, configure your firewall settings to allow port 80 to communicate directly with your devices.
Any incoming HTTP requests from your port #80 will now be redirected to the ESP-01. Visiting the IP address outside the home also takes you to a web page that shows the current day, time, temperature, and humidity.
If you have any questions, be sure to leave a comment!
Items in the file: Complete source file
Airnex/Arduino training/IoT dashboard with Arduino and relay control + sensor display
Esp training, Arduino training, Internet of Things training, Esp projects, Arduino projects, Internet of Things projects
IoT dashboard with Arduino and relay control + sensor display
12/18/1400
Approximate reading time is 6 minutes

Contents [show]
If you are tired of seeing your sensor data on a plain white screen, then this tutorial is for you. Adafruit IO is going to make your data look good on the internet.
The fourth industrial revolution
The first industrial revolution was the discovery of the steam engine. Production was simplified, giving researchers time to create new things. More than a hundred years later, the Second Revolution took place, introducing electricity and speeding up production again. Then, with less time, came the third revolution with early computers and digital communications.
We are now living in the fourth industrial revolution, also known as Industry 4.0. This era is still under construction, but the goal is to integrate technology into the everyday life of humanity. Things like machine learning, artificial intelligence, 3D printing, self-driving vehicles, online banking and even genome editing are among the few gifts of this age. All of these are focused on a technology called IoT.
Internet of Things
The Internet of Things (IoT) is a system of interconnected devices that are able to communicate with each other over a network without the need for human-to-human or human-to-computer interaction. The Internet of Things is the heart of modern automation. An IoT system could include sensors, mobile devices, CCTV cameras, trains or even your shower. The Internet of Things can connect anything. And with all the devices connected to each other, you can get data from one point to trigger an action at another. You can also collect data to analyze and improve the entire IoT system.



## The easiest way to practice IoT is to use Arduino and a web service called Adafruit IO.
What is ADAFRUIT IO?
Adafruit IO is a free Internet of Things web platform developed by Adafruit Industries. It acts as a control panel for a variety of devices including sensors built with the Arduino platform. It is designed not only for data visualization but also for device control. With Adafruit IO, you can use graphs to display your data, as well as buttons and switches to enable specific features on your device. Adafruit IO has documented libraries that you can use to reduce programming hours.
Here are some terms you should learn before proceeding:
• Dashboard – Provides charts, reports and many other visualization techniques for your data.
• Trigger – reacts to your data. For example, you can use a trigger to send an email when a sensor's temperature exceeds a threshold value.
• Feed – Contains the data you upload to Adafruit IO. The feed also includes the date and time your information was uploaded.
Suggested article: Whistling Arduino project to turn on a light bulb or whatever
To demonstrate how to use Adafruit IO with Arduino, we're going to connect a DHT22 temperature and humidity sensor and two-channel 5V relay to the Arduino UNO, then transmit the temperature and humidity values ​​to an ESP8266 module every 5 seconds. The ESP8266 module is set to update your Adafruit IO dashboard when it receives data from the Arduino.
Let's start by setting up Adafruit IO.
Launch ADAFRUIT IO
First, go to the Adafruit IO website and create an account. After logging in, go to the home page. Under Actions, select Create a New Dashboard.

After giving the dashboard a name and a short description, click Create.
Next, go to your new dashboard.
You need to fill your dashboard with blocks. To do this, select the blue + button on the right side of the dashboard.

If you have any questions about this article, ask in the comments section
Blocks are switches, buttons, levers, gauges, and visualization techniques that represent and react to your data. For the sample project we need a line graph and two gauges to display the temperature and humidity of the room and two buttons to control the relay.

After selecting a block, Adafruit will prompt you to select a feed. We need two feeds to maintain the temperature and humidity values ​​of the DHT sensor. Create a feed using the create button on the right.
Next, configure the block settings as desired.

Do the same with the relay buttons so that you can control and monitor both data at the same time.

You need your username and key to fill the blocks with data. To get both information, go back to the main page and click on Adafruit IO Key. A window will appear displaying your username and password. Take a pen and paper and write them down.

Installing the ADAFRUIT IO library on Arduino
To install the library on the Arduino, go to the Library Manager and search for “Adafruit IO Arduino”. Select the latest version and click Install. This will require you to install other libraries that Adafruit IO Arduino needs to work properly. Be sure to update your ESP8266 board library as well. Older versions show an error when uploading the code.

Relay and sensor connection circuit to Arduino for Internet of Things
We are going to connect the DHT22 sensor and a two-channel 5V relay to the Arduino, then transmit the sensor reading to the ESP8266 module every 5 seconds. The ESP8266 module is set to update your Adafruit IO dashboard when it receives data from the Arduino.

Required parts
• Arduino UNO
• ESP8266-01 module
• DHT22 temperature and humidity sensor
• 3* 1 kilo ohm resistance
• 10 kilo ohm resistance
2-channel 5V relay (or 2 5V relays)
• Jumper wires
• Board
Suggested article: Saving data in SD memory card with Arduino (+Excel)
Get the required parts from the Ironex parts store.
Code to send sensor data to Adafruit and control the relay
The complete code is placed in the downloadable file at the bottom of the page. Here we explain the important parts of the code. We are going to use the SerialTransfer.h library to send sensor data from the Arduino UNO to the ESP module and vice versa.
These are the important lines we have used from this library:
• SerialTransfer myTransfer – Creates a SerialTransfer instance called myTransfer.
• myTransfer.begin (Serial) – starts serial communication.
• myTransfer.txObj(status, sizeof(status)) – Creates an object specifically for status.
• myTransfer.sendData(sizeof(status)) – Sends the status in a packet of its size.
• myTransfer.rxObj(status, sizeof(status)) – Gets the status from the sender.
In this project, UNO has two tasks. It must first read the data from the DHT sensor and then send it to the ESP module every five seconds. Second, it must wait for Adafruit IO input to enable or disable a specific channel on the relays. Just like before, we communicate with the DHT sensor using the DHT.h library. To use the library correctly, you must specify the pin of the sensor connector and the type of DHT sensor you are using. Then, using these two, we create a DHT object. The code should look like this: DHT dht(DHTPIN, DHTTYPE). After creating the object, we initialize the sensor using dht.begin() to use functions like dht.readTemperature() and dht.readHumidity. Finally, we use SerialTransfer.h to send data to the ESP module.
On the other hand, another task of the ESP module is to detect the data received from the Arduino and send them to the Adafruit IO server. Additionally, it should receive the relay button status from the Adafruit IO dashboard and send it to the Arduino UNO. We use io() to connect the ESP module to the Adafruit IO server. Next, we specify the feeds we're going to interact with using io.feed() . We have a total of 4 feeds for temperature and humidity values ​​and the status of each channel in the relay module. We use onMessage() and get() to call the helper function for the relay button and retrieve the data from it. Next, the loop section must include io.run() to keep the connection online. We use save() to send the temperature and humidity values ​​to Adafruit IO.
result
Your Arduino will populate the dashboard as soon as it connects to the Adafruit IO server. I let the device transmit data for about 15 minutes then pressed the Relay Channel 1 button.

The serial monitor is simple but in fact it is very useful. As you can see, Arduino has identified the high signal from Adafruit IO, so it illuminates Relay 1.

We hope this makes it easier for you to build a web -based IoT control panel with Arduino. If you have any questions, let us know under your supervision.
Suggested Paper: Arduino Application in Industry (Introducing Arduino Industrial PLC)
Files: Source and Library
ESP Training Arduino Training IoT Esp Projects ESP Projects IoT
Send sensor information to the Internet with the Arduino board
1400/12/11
The approximate time of study 7 minutes

Contents [View]
Recent advances in information and communication technologies have created a new style of calculations. During this period, users can access features such as data storage and computational power over the Internet. This is usually known as cloud computing.
In this tutorial we will talk about the process of writing data in the cloud. Then use Arduino Uno, DT22 humidity and temperature sensor and WiFi ESP8266 module to write data in cloud. We will also mention the basics such as cloud, Thingpeak, sending and drawing data to Thingspeak, and setting up stimuli and actions. Finally, we will build a project to illustrate these concepts.
What is Cloud Cloud?
In the not too distant years, hard drives, CDs and floppy disks were the main data storage devices. However, these had disadvantages. In the first step, you need to buy many external devices to back up your information, which results in additional costs. Secondly, increasing the volume of data produced by users requires more processing power, which costs more and requires service and maintenance resources. On the other hand, the cloud is useful because it involves gathering data centers that can be accessed through the Internet. They provide services such as email, data storage, data processing and data recovery that can be done from anywhere in the world. The cloud has fixed the disadvantages of external storage devices by giving users the ability to manage online resources. Users can now rent the storage space and online services they need.

Arduino Training Course ESP32 STM32 Training Course
Do you want a Disclosure Discount Training Course Pico Training Course?
AVR Training Course Proteus Training Course IoT Training Course
The diagram above shows the concept of IoT. In general, calculations, storage and databases are managed by third -party institutions in remote data centers instead of user or user infrastructure. The same files from any device can be accessed through the Internet. In addition, users are allowed to create and manage their accounts. The top cloud platforms in the market today are:
• Amazon Web Services
• Google Cloud Platform
• Microsoft Azure
• IBM Bluemix
• Alibaba
IoT (IoT)
IoT, commonly known as IoT. It is an emerging technology area in which devices or objects are capable of connecting and transmitting data through the network without human interference. These objects have sensory capabilities and have unique IDs for addressing and communication. To transfer data from the devices over the Internet, the cloud computing provides infrastructure for data to reach the destination. Over the years, sellers have created many connected devices, and IoT cloud platforms have been developed. Examples of IoT cloud platforms include Thingsboard, Thingworx, IBM Watson IoT, Node-Read, ThingSEAK and ThingSpeak.
Suggested Paper: The thermometer project with Arduino and the LM35 sensor (temperature measurement)
In this article, we will focus on Thingspeak.

What is Thingspeak?
Thingpeak is an IoT platform that enables objects or physical devices to connect to the cloud. HTTP and MQTT communication protocols provide communication between objects and clouds. This platform allows registered users to collect, display, analyze, deduce and act on the basis of the need. Thingspeak was released by Iobridge and now supports MATLAB, so the user enables the user to access advanced data analysis tools. Users can visualize their sensor data using multiple MATLAB's internal charts or display data in gammers, charts or custom charts.
Thingpeak allows users to analyze and visualize their sensor data. In addition to simply visualizing your sensor data, this platform has internal features that allow you to process your data. That is, integration, conversion, calculation of new data, and developing IoT applications. More data exchange tools between ThingSpeak and web applications or social media platforms are possible.
Send information to Thingspeak
1. Create an account in Thingspeak.
2. Since we are going to record temperature and humidity data, create a new channel with two fields - temperature and humidity.
3. Get the Write API key. We need it to write data on our Thingpeak channel.
It is relatively easy to send sensor data to the Thingpeak channel. The only thing we need is the key to write channel API and sensor values. For this tutorial, since we are going to send two variables (temperature and humidity), we must have two fields Field1 and Field2. Then, we put all these variables in a single URL, which we can send by typing in a web browser:
https://api.thingspeak.com/update?api_key=drminls2dn88g1ez&field1=4&field2=4
Another way to send this URL is through devices that can use AT commands. These are the instructions that microcontrollers or any appliances use to control any AT -compatible transmitter.

Conversion of sensor data to charts in Thingspeak
In this article we mentioned that we can use Thingpeak to collect, visualize and analyze our sensor data. Now that we have collected our data from the DHT22 sensor, we have to visualize it. Thingpeak allows us to use internal visualization diagrams or create our own custom designs. In this section, we use the following code to create our visualization chart. To compare, we draw temperature changes and moisture changes in the same chart.
To draw your sensor data chart in Thingspeak, click the Visualization Matlab tab and select Custom Radio Button. You will be redirected to an online editor. Copy and paste the MATLAB code to create a custom visualization chart.
If you have questions about this, ask in the comments section
Suggested Article: WS2812B Nonopicel Connection to Arduino
Readchannelid = 1109284;
Fieldid1 = 1;
Fieldid2 = 2;
Readapikey = 'byw217LCLBT8UCSA';

[Data1, time1] = Thingspeakread (Readchannelid, 'Field', Fieldid1, 'Numpoints', 'Readkey', Readapikey);
[Data2, time2] = Thingspeakread (Readchannelid, 'Field', Fieldid2, 'Numpoints', 'Readkey', Readapikey);

Yyaxis Left;
plot (time1, data1, '-*', linewidth ', 2)
YTICickFormat ('%. 2F')
ylabel ('Tempure [^0c]')
Xlabel ('Date')

Yyaxis right;
plot (time2, data2, '-O', linewidth ', 2);
YTICickFormat ('%. 2F')
ylabel ('Humidity [%]')
Legend ({'tempure', 'Humidity'}, 'Location', 'northwest')
Grid on
In Matlab's code to visualize our sensor data, the first thing we need is to read data from our channel. Therefore, for that, we need to submit the channel ID to the program with Readchannelid Code = 1109284.
Then we move the API read key to our app Readapikey = 'byw217LCLBT8UCSA'. This API key enables the program to read temperature data from our channel.
Then, we write a function that retrieves the data from our channel and stores that information in two variables: the temperature variable (Data1) and the date variable (Time1). This function is called TextSpeakread () and accepts four parameters - channel ID, field ID, number of points and reading key
[Data1, Time1] = Thingpeakread (Readchannelid, 'Field', Fieldid1, 'Numpoints', 30, 'Readkey', Readapikey)
Finally, using the MATLAB (Time1, Data1, '-*', 'Linewidth', 2) Drawing the temperature by date in a two-dimensional chart we use the rest of the codes to make your designs more beautiful To.
The result is shown on a two -dimensional chart in the chart below.

The blue line represents the temperature (left Y axis) and the red line represents the humidity (the right Y axis). Our options are not limited to creating two -dimensional designs. There are many ways to use the sensor data chart.
Arduino Code Send Sensor Information to the Internet with Email Alert
Now, let's combine what we've done so far to create a project that records the sensor data using Arduino Nano, DT22 and the WiFi ESP8266 module in the cloud.
These are the pieces that you will need:
• Arduino Nano or Ono
• ESP8266 WiFi module
• DHHT22 Humidity and Temperature sensor
• Board board adapter ESP8266
•
## These are the pieces that you will need:
• Arduino Nano or Ono
• ESP8266 WiFi module
• DHHT22 Humidity and Temperature sensor
• Board board adapter ESP8266
• Jumper wires
• Board power supply
• 9V battery
• 100 ohms resistance
• Resistance of 250 ohms
• Resistance of 10 khhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
Make the necessary parts from the Irix Parts Store.
And here you see the full circuit.

Next, we use the following code for Arduino to send sensor data to the cloud using the WiFi ESP8266 module.
#include <SoftwareSerial.H>
#define RX 2
#define tx 3
#include "DHT.H"
#define dhtpin 6
#Define dhttype DHT22

DHTDHT (DHTPIN, DHTTYPE);

Sting AP = "Androidap_7822";
String Pass = "485088C2825F";
Sting API = "Drminls2dn88g1ez";
String host = "api.thingspeak.com";
String port = "80";
String Field1 = "Field1";
String Field2 = "Field2";
Int CounttrueCommand;
Int Counttimecommand;
Boolean found = false;
Float Tempsensor = 1;
Float HumidSensor = 1;
Softwareserial ESP8266 (RX, TX);


Void Setup () {
 Serial.begin (9600);
 ESP8266.begin (9600);
 DHT.BEGIN ();
 Delay (1000);
 SendCommand ("AT", 5, "OK");
 SendCommand ("AT+CWMODE = 1", 5, "OK");
 SendCommand ("AT+" "" "+" AP+"" ""+Pass+"" ", 20," OK ");
}

Void Loop () {
 Tempsensor = GetTempdata ();
 HumidSensor = gethumiddata ();
 String getdata = "get /update? Api_key ="+API+"&"+Field1+"="+String (tempsensor)+"&"+field2+"="+string (HumidSensor);
SendCommand ("AT+CIPMUX = 1", 5, "OK");
 SendCommand ("at+ cipstart = 0, \" tcp \ ", \" "+ host+" \ ","+ port, 15, "OK");
 SendCommand ("at+cipsend = 0,"+string (getdata.length ()+4), 4, ""> ");
 ESP8266.println (GetData); Delay (1500); CounttrueCommand ++;
 SendCommand ("AT+Cipclose = 0", 5, "OK");
}

Float GetTempdata () {)
 Delay (2000);
 Float t = dht.Readtempure ();
 if (isnan (t)) {
 Serial.println ("Failed to Read From DTHT SENSOR!");
 Return 0;
 }
 Return t;
}
Float Gethumiddata () {)
 Delay (2000);
 Float h = dht.readhumidity ();
 IF (ISNAN (H)) {
 Serial.println ("Failed to Read From DTHT SENSOR!");
 Return 0;
 }
 Return H;
}

Void SendCommand (String Command, int MaxTime, Char Readreplay []) {)) {
 Serial.print (CounttrueCommand);
 Serial.print ("at command =>");
 Serial.print (Command);
 Serial.print ("");
 While (CounttimeCommand <(MaxTime*1))
 {
 ESP8266.println (Command); // at+cipsend
 IF (ESP8266.find (Readreplay)) // OK
 {
 Found = True;
 Break;
 }

 Counttimecommand ++;
 }

 IF (Found == True)
 {
 Serial.println ("OK");
 Counttruecommand ++;
 Counttimecommand = 0;
 }

 IF (Found == FALSE)
 {
 Serial.println ("Fail");
 Counttruecommand = 0;
 Counttimecommand = 0;
 }

 Found = false;
 }
You must replace your WiFi name and password in the following lines.
Suggested article: Solder Dough with Arduino
Sting AP = "Androidap_7822";
String Pass = "485088C2825F";
Tempsensor = GetTempdata (); HumidSensor = gethumiddata (); There are functions to obtain temperature and humidity information from DT22.
The important line is mentioned below:
String getdata = "get /update? Api_Key ="+API+"&"+"+"+"+"+"+"+"+"+"+"+"+"+"+"+"+
This line orders Arduino how to send this URL.
 https://api.thingspeak.com/update?api_key=drminls2dn88g1ez&field1=4&field2=4
The result is shown in the picture below:

If you have any questions about anything, write down your supervision!
IRnes/IoT Tutorials/Smart Home with Node Red Node Red in Roseberry Pie
IoT Tutorial Rosebrock Rosebroof Project IoT Projects IoT Projects
Smart Home with Node Red Node Red in Rosberie Pie
1400/11/13
Approximate time of study 5 minutes

Contents [View]
Have you ever wondered why you need node-rest with Home Assistant? Home Assistant and Node-Rd seem to do similar things but are superior to each other in different fields. The main power of Home Assistant is its ability to connect and control all smart devices. The main way to create automation in Home Assistant is to use YAML files for automation but it is complex and can be scary for any beginner. This is where the strengths of the Node-RD are naturally supplement Home Assistant. Node-RD allows flow-based automation to be significantly more powerful and user-friendly.
In this tutorial, I'm going to use Node-Red with Home Assistant to build a smart home system. Launching Node-Red with Home Assistant is very simple and only takes a few minutes. But before you start, you need to make sure you have a home assistant before. If you are a beginner, you can see a home assistant with a rosryan foot.


## LED integration and fan attached with Home Assistant
The first thing to do is to make changes to the Configuration.yaml file to control the LED and fan using Home Assistant and Node-Red. For that, go to https://home-assistant.io/components/ and search for the Raspberry Pi Gpio phrase.

Arduino Training Course ESP32 STM32 Training Course
Do you want a Disclosure Discount Training Course Pico Training Course?
AVR Training Course Proteus Training Course IoT Training Course
Now go down on the Raspberry Pi Gpio page and copy the "Switch" configuration code.

Then go to the File Editor tab and click the folder icon in the upper left corner to review the system files. From there click on the 'configuration.yaml' tab and the configuration file opens. Now place the code you copied from the Home Assistant page and save the file.

When you make the change in the configuration file it is good to check if the configuration is valid. To check the settings, go to the 'configuration' tab and select General and click on 'Check Config'.

Now, if the changes you made, have no error, it shows the configuration Valid message. When the configuration is valid, press "Restart" in server management and wait for the home assistant to restart.

After restarting, go to your Home Assistant interface and see that two new switchs have been added to the home assistant interface.

Now connect the lamp and fan to the bases of 11 and 12 Gpio Raspberry Pi, as shown in the picture below:
If you have questions about this, ask in the comments section
Suggested article: Servo Motor Control Training with Pie and Python

Components needed to build a smart home with node-rest
• Rosberie Pie
• Relay module
• DHT11 sensor
• AC lamp
• 12V fan

Home assistant connection to node-rest
Node-rest and Home Assistant are very easy to connect and there are different ways to do it. The first is the installation of the Node-Reed plugin on Home Assistant and the latter is the Home Assistant Node installation in Node-Download. For this tutorial, we are going to use the first method, namely installing a node-rest plugin on Home Assistant. Now, I assume that you have installed the Home Assistant on the Pie and you have the Home Assistant dashboard. From the Home Assistant dashboard, go to the "Supervisor" tab and then click "Add-on". Here, search and install "Node-RD".

After installing the plugin, you need to make changes to its configuration. To do this, go to "Configuration". Here, first add the credit password. This can be a name or password or anything else. Then place the SSL on FALSE and save the changes.

Now click on Start and enable "Show in SideBar" to make it easy to get available. Open the node-rest Web UI by clicking "Open Web UI".
Before starting the streams, we need to install the Google Assistant Pallet (Nora) with the 90th palette. To do this, click the menu icon in the upper right corner and then click "Manage Palette".

Go to the Install tab and then search and install the ninety 'node-rest-contrib-smartnora'.

Create a smart home stream in Node-Reed
By running NODE-RED on Home Assistant, the next task is to create a flow to control and automate devices connected to Raspberry PI. Here, the process we want to create will have two sequences, one for controlling one lamp and the other to control a fan. We will start by creating a sequence to control a lamp attached to Raspberry Pi. To that, go to the home assistant palette and drag the "Events State" node into the flow section. This node is used to read all the events of mode.

Now double -click on the node and Properties, Page Change and select Switch.LED in Entity ID. Release all other options unchanged.

Then go to the Function palette and drag and release the "switch" node into the flow section.

Double -click the node again to edit its properties. There's not much to change, just add two Payloads that are on and off.

Then drag and release the two "Call Service" nodes from the Home Assistant palette. The Call Service node is used to send a request to the home assistant for each domain. Here, we use this node to change the status of Raspberry Pi Gpio according to the command we receive from Home Assistant.


### Double -click the Node and change the properties on the properties page as shown below. Similarly, change the features of the second contact service node.
Suggested Article: Message Storage Training with Rosebone Pie

Now connect all the nodes together and create a simple stream that reads the button on the Home Assistant dashboard and changes the status of Raspberry Gpio. Next, add another node, the Smart Nora node to this stream to control the lamp using Google Assistant. To get started with Nora, you must register an account on the Nora website. So, continue and click "Login with Google". Make sure you have selected the same Google account as your Google Assistant. On the next page, asks you to confirm the email. Confirm your email address by clicking the link in the email.

Now go to the Nora palette and drag the "switch" node into the flow section.

Now double -click the Switch node to edit it. Then click the pencil icon to configure it. On the next page, enter the user information (email/password) used when creating your Smart NORA account.

Now, connect all the nodes and follow the same process to create a sequence for Fan. But don't forget to change the Entity ID from Switch.LED to Switch.fan. The full flow will be as follows:

This will complete the flow. Run it and go to your Home Assistant dashboard. You should now be able to control the lamp and fan using the dashboard switches as well as using Google Assistant. If you are using Home Assistant, it is difficult to add Google Assistant Features to the smart home system, but with Node-Red it can be done in a matter of minutes. Except for the Google Assistant, the Node-RD platform can be used with Home Assistant to easily configure devices to add some features and excellent automation.
ESP Training ESP32 IoT Training Esp Projects ESP
Build Web Server Video with ESP32-CAM (face recognition)
1402/01/30
The approximate time of study 4 minutes

Contents [View]
There are many human identification systems that use signature, fingerprint, sound, hand geometry, face recognition, etc. to identify people, but none of them can make people in public places such as airports, retailers and railway stations. Do.
Face recognition systems can not only be used for security purposes to identify people in public places, but they can also be used for the goals of attending offices and schools.
In this project, we are going to build an ESP32-CAM face recognition system that will act as a security system for identifying unauthorized individuals. ESP32-CAM is a very small camera module with ESP32-S chip. Using the ESP32-CAM module we can build a face recognition system without the use of sophisticated programming and additional components. Face recognition can also be done using the Raspberry Pi and Pi camera using OpenCV: OpenCV Face Identification Project
Introducing ESP32-CAM

Arduino Training Course ESP32 STM32 Training Course
Do you want a Disclosure Discount Training Course Pico Training Course?
AVR Training Course Proteus Training Course IoT Training Course
The AI-Thinker ESP32-CAM module has an ESP32-S chip, a very small OV2640 camera and a micro SD card slot. The Micro SD card slot can be used to store images taken from the camera or save files. This ESP32-CAM module can be widely used in various IoT projects. It can be used as a face recognition system in offices, schools and other private areas, and can also be used as wireless monitoring, QR wireless identification and many IoT applications.
The ESP32-CAM module can be planned with ESP-IDF or Arduino Ide. The ESP32-CAM module also has several GPIO pins to connect external hardware. ESP32-CAM does not have a USB connector, so you need a FTDI board to plan module.

ESP32-CAM facilities:
• The smallest Wi-Fi BT Soc Module 802.11b/g/n
• CPU with a low -power 32 -bit design
• Maximum clock speed of 160 MHz, computational power up to 600 dmips
• Internal SRAM 520 KB, 4MB External PSRAM
• Supports UART/SPI/I2C/PWM/ADC/DAC
• Support OV2640 and OV7670 cameras, flash lamp on board
• Support for upload wi-fi image
• Support for TF card
• Support for multiple sleep modes
• LWIP and frertos is embedded in
• Supports Sta/AP/STA+AP operation mode
• Support Smart Config/Airkiss Technology
• Support for the promotion of local operating system and serial port (Fota)
ESP32-CAM Technical Specifications:
• Flash memory: 32 MB of default
• RAM: 520 KB SRAM with 4 MB of PSRAM
• Support for TF Card: Max 4G
• Support interface: UART, SPI, I2C, PWM
• Image output format: JPEG, BMP, Grayscale
• GPIO: PIN 4
• Power supply range: 5V
Suggested article: Deep Sleep Activation in ESP8266 Module to Save Energy

### Movie Web Server Circuit with ESP32 CAM
To build the ESP32 CAM security camera we only need the ESP32 camera module and the FTDI module to plan it.

ESP32-CAM does not have a USB connector, so you need an FTDI module to upload code to ESP32-CAM as shown above. The VCC and GND ESP32 base connects to the VCC base and the FTDI GND. The TX and RX Module ESP32 are connected to RX and TX FTDI board.
Note: Connect the Io0 code to GND before uploading. Io0 determines whether ESP32 is in the flash mode. When the GPIO 0 is connected to the GND, the ESP32 is in the code upload mode.
ESP32-CAM FTDI Board
3.3V VCC
If you have questions about this, ask in the comments section
GND GND
Uor tx
UOT RX
After planning the ESP32, remove the FTDI board and feed the module 7805 using a voltage regulator.
Camera Camera Web Server Code with ESP32
You don't need to write code. Simply open the ready code from File> Examps> ESP32> Camera and select CameraWeBserver.

You must enter your WiFi name and password before uploading the code.
constraint char* ssid = "wifi name";
Const chah* password = "password";
Then define the ESP camera module. In the code, they define 5 camera modules, so delete two // from the "Camera_model_ai_thinker" line and place the rest of the modules in comment (ie // first).
Now the code is ready to upload.
To upload the code, connect the FDTI board to your laptop and select "ESP32 Wrover Module" as your board. Also change other settings according to this image:

Press the reset button before uploading the code then click the upload button. If you encounter an error when uploading the code, check that the Io0 is connected to the GND and you have selected the correct settings in the Tools menu.
After uploading the code, remove the Io0 and GND pin. Then open the monitor series and change the rate to 115200. Then press the ESP32 Reset button and the ESP port number will be printed on the serial monitor as shown below.

Now go to your browser to access the camera and enter your IP ESP address. Will take you to the stream page. Click the Start Stream button at the bottom of the page to start playing the ESP32 video.

You can change the playback quality by changing the resolution on the playback page. You can also click on the images by clicking on the "Get Still 'button, but this code has no option to save images.
After the video playback test, we will now test the ESP32 face recognition and face recognition features. To do this, enable Face Recognition & Face Detection in the settings.

To recognize the face, you must first record a face. You can register a new face by clicking on the "Enroll Face" option. There are several efforts to accurately record the face. After storing the face, it recognizes the face as a subjection 0 and can now be used as a face recognition security system.
Suggested article: Installation and work tutorial with Node-Read in Rosry Pie and LED Control
So this is that an ESP camera module can be easily configured for video playback and face recognition. Check the following small videos taken by the ESP32 camera.
Smart Home with Google Voice Assistant and Node-Red Pie
1400/03/29
The approximate time of study 4 minutes

Contents [View]
As you know, IFTTT has recently created "pro" and has created many restrictions on free accounts. According to the new iFTTT subscription rules, you can create or activate only 3 applets at a time. You can easily design different projects with Google Voice Assistant. In this project, we make an easy way to control home appliances from Node-Read and Google Assistant, and there is no need to write many codes. Node-Red is developed by IBM and is an open source programming tool for wiring hardware devices, APIs and online services in a new and interesting way. Node Red provides a browser -based editor with which you can create many knots and connect to each other. In this project, we intend to control the GPIO of the Pie Pie using Google Assistant with Node-Download. For this purpose, we will use the Smart Nora plugin for Node-rest.

#### Installing Node-Reed on Raspberry Pi
Node-RD is already installed on the Raspbian Streetch operating system. If you do not install Node-Red on the leg rosti, you can use the following command to install node.js, NPM and Node-Red on Raspberry PI. This command can also be used to update the available version.
 Bash <(CURL -SL https://raw.githubusercontent.com/node-red/linstallers/master/deb/update-nodejs-and-nodered)

This command does the following:
Arduino Training Course ESP32 STM32 Training Course
Do you want a Disclosure Discount Training Course Pico Training Course?
AVR Training Course Proteus Training Course IoT Training Course
• Removes the current version of Node-Red and Node.js if any.
• Installs the latest version of Node.js LTS. If it detects node.js is already installed, it will ensure that the minimum Node is version 8.
• Cleans NPM Cache.
• Using NPM, it installs the latest version of Node-Red.
• Launches Node-Red to work as a service and provide a set of commands to work with the service.
• After the installation is completed, you should see the Node-Red icon below the list of programming programs.
Working with Node-Red on Roseberry Pie
Node-rest can be run via the Razbari Pi desktop interface. The following route is used to access nodes:
Menu> Programming> Node-Reed

If you are connected to the leg of the foot, run the Node-Read-Start command at the terminal.

Open the Node-Read interface
With the installation of Node-Red in Raspberry PI, we can access its web interface. To do this, go to the browser and address below.
Suggested article: ESP32 programming with Micropython Micropon
http: // your_Pi_ip-ADDRESS: 1880
As shown below, IP Raspberry PI address is shown in the first main line of the Node-Reed terminal.

The following page appears after this.

If you have questions about this, ask in the comments section
Before starting to build flows, we need to install the Google Assistant Pallet (Nora) in Node Red. To do this, click on the menu icon in the upper right corner and then click "Manage Palette".

Go to the Install tab and then search and install the node-rest-contrib-smartnora '.
Create a Smart Nora account
You must register an account on the Nora website to get started with Nora. So to the site
Smart-nora.eu
Go and log in using your Google Account. (With the same account that is also connected to your Google Assistant.)

On the next page, asks you to confirm the email. Confirm your email address by clicking the link in the email.
Create a Flow in Node-Read
By installing all the required nodes, we can create an LED control flow using Google Assistant. To do this, go to the "Nora" palette and drag the Switch node to the flow section.

Now, double -click the Switch node to edit. Then click on the pencil icon to configure. On the next page, enter your (email / password) you used when you have used your Smart Nora account.

Now, go to the Dashboard palette and drag the Switch node to the Flow section.

Then go to the Raspberry Pi palette and drag the "rpi gpio out" node to the Flow section. Double -click the node, select the GPIO18 PIN, and then select "Digital Output" as the output type.

Flow will finally be as follows:

Add Nora to Google Audio Assistant
Lastly, we need to add Nora to Google Assistant or Google Home devices. To do this, open the Google Assistant and click on the account icon in the upper right corner.

Now, scroll down and click "Home Control".

You will see the number of options, so search the Smart Nora, guides you to the login page. Sign in with the same account of your Google Assistant.

LED Control with Google Assistant and Node-Reed
Now everything is ready and you can connect a LED to the base of the GPIO18 and GND of the Pie Pie, as shown below:
Create a Smart Nora account
You must register an account on the Nora website to get started with Nora. So to the site
Smart-nora.eu
Go and log in using your Google Account. (With the same account that is also connected to your Google Assistant.)

On the next page, asks you to confirm the email. Confirm your email address by clicking the link in the email.
Create a Flow in Node-Read
By installing all the required nodes, we can create an LED control flow using Google Assistant. To do this, go to the "Nora" palette and drag the Switch node to the flow section.

Now, double -click the Switch node to edit. Then click on the pencil icon to configure. On the next page, enter your (email / password) you used when you have used your Smart Nora account.

Now, go to the Dashboard palette and drag the Switch node to the Flow section.

Then go to the Raspberry Pi palette and drag the "rpi gpio out" node to the Flow section. Double -click the node, select the GPIO18 PIN, and then select "Digital Output" as the output type.

Flow will finally be as follows:

Add Nora to Google Audio Assistant
Lastly, we need to add Nora to Google Assistant or Google Home devices. To make this work the Google Assistant


What is Microsoft Azure IoT Hub?
Azure IoT Hub is a set of management services that can connect, monitor and control the Internet of Things. The program also includes safe communication for devices, with data processing and analysis that helps device manufacturers in the construction, deployment and management of IoT programs. Azure IoT HUB abrasive data lets us know about the status of connected IoT devices and enables our cloud-to-Device messages to send commands and notifications to connected devices.
One example may be that, using the smart home automation system, we can collect different sensor data and send them to Azure IoT Hub for processing, storing and managing them. We can also control the output devices from the Azure Iot Hub interface. The central hub supports two -way communications for IoT programs and cloud communication devices.
Arduino Training Course ESP32 STM32 Training Course
Do you want a Disclosure Discount Training Course Pico Training Course?
AVR Training Course Proteus Training Course IoT Training Course
Create azure IoT Hub
We are ready to make all the settings needed to set up Microsoft Azure services, but before that make sure you have a Microsoft account. If you don't have that, you can easily log in. Then, use portal.azure.com to the Azure port and log in.
After logging in, go to the Azure home screen, select the Create a Resource button and then search the IoT Hub in the Search the Marketplace. Select the IoT Hub from the search results and then click the Create.

Fill in detail to create IoT Hub.
Suggested article: WhatsApp Installation Training on Pie Pie (Send and Receive Message)

In the Subscription section, you must select Subscription to use it for your hub. In our case, we choose a test account and have selected "Free Trial". In the Resource Group section, select your resource group. If you do not have anything, you should click Create New and create a group of resources.
In the Region Section section, you can use the drop -down menu to select your desired area. In the IoT Hub Name section, you must enter your hub name. This name must be unique because all the necessary communication is happened to this name.
Below the "Size and Scale" tab, select "Free Tier" and click Next. Then click "Review+Create". It takes a few minutes for the IoT Hub to be created. Click on the IoT Hub name you created. As shown in the picture below, note Hostname. Then click Shared Access policies in the settings. Shared Access Policies is highlighted in the picture below. Click on the iothhubownner option in the Policy section. Write down Primary Key and Connection String-Primary Key for future sources. Now, click IoT devices to register a new device on IoT Hub. In the Device Explorer window, click Add to add a device to the hub.

Fill in the following information on the New Devices page.
• Device ID: Enter your device ID. Must be unique.
• Authentication Type: Symmetric Key.
• Auto Generate Keys: Check.
• Connect Device to IoT Hub: Click Enable.
After creating the device, you can find your newly created device in the Device Explorer section. Click on the device name. This shows the details of the device. Note the device Primary Key and Connection String-Primary Key. We need it to communicate.
If you have questions about this, ask in the comments section

Now, when this is done, we can go to the hardware.
Azure IoT test circuit
The hardware part of this project is very simple, the list below shows the components needed for this project.
• Raspberry Pi 3B (we can use any other model of PI)
• 16GB Micro SD memory card
• DHT11 temperature and humidity sensor
• Micro USB power supply with 5V, 2.4A
Make the necessary parts from the Irix Parts Store.

The above circuit sends temperature and humidity to Microsoft IoT Hub. In this circuit, we use the DHT11 sensor to collect temperature and humidity data and use Raspberry Pi 3B as a project brain. The DHT11 sensor has a tripod. VCC and GND pins are connected to the Sensor and DT11 data output to the GPIO 4 Raspberry Pi range.
Pie Pie Programming to send data to Azure IoT Hub
Before starting the coding of this project, we need to create an Azure Cloud Shell (CLI) in the Azure portal. As shown below, click the Azure Cloud Shell Shell button in the portal. Then click on the Create Storage option specified in red.
Suggested article: Rosberie Pie or Orange Pie (Compare Complete)
Once finished, you can open the CLI and execute the following commands to install the Azure plugin used to display sensor data.
az extension add-Name Azure-CLI-IT-EXT
After completing this, we need to install some plugins in Raspberry Pi to connect with the DHT11 sensor and facilitate the communications process for Azure IoT services. Open the Pie Pie Terminal.
Must first have the DHT library for raspbe


### First, we need to download the DHT library for Raspberry Pi, then extract it from the root folder and run the following command to install it.
 sudo python setup.py install
After successful installation, run the following commands to install all dependent packages in Azure IoT Hub.
sudo pip3 install azure-iot-device
sudo pip3 install azure-iot-hub
sudo pip3 install azure-iothub-service-client
sudo pip3 install azure-iothub-device-client
After installing all the prerequisites, it's time to write the code in Python. To do this, first import all libraries:
import random
import Adafruit_DHT
import time
from azure.iot.device import IoTHubDeviceClient, Message
In this project, we use the Raspberry Pi processor to process the DHT11 data.
sensor = Adafruit_DHT.DHT11
pin = 4
Next, we define the connection string.
CONNECTION_STRING = "HostName=sensordata.azure-devices.net;DeviceId=ZZZZZ;SharedAccessKey=ZZZZZZZZZZZZZZZZZZ"
Next, we create an array that will be used to send data to Azure IoT Hub. This can be done as follows:
MSG_SND = '{{"temperature": {temperature},"humidity": {humidity}}}'
We define a while loop. In the while loop, the humidity and temperature data are processed using the Adafruit_DHT.read_retry function. Additionally, we define two special variables and assign the output data to those variables.
while True:
 humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
Next, we'll write a function to connect to the IoT Hub using the connection parameters we defined earlier.
 def iothub_client_init():
 client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
 return client
Finally, both temperature and humidity data are sent to Azure Hub using the format shown in the code below. Also, we used the try and catch method to detect any errors in the code.
 def iothub_client_telemetry_sample_run():
 try:
 client = iothub_client_init()
 print ("Sending data to IoT Hub, press Ctrl-C to exit")
 while True:
 msg_txt_formatted = MSG_SND.format(temperature=temperature, humidity=humidity)
 message = Message(msg_txt_formatted)
 print( "Sending message: {}".format(message) )
 client.send_message(message)
 print ( "Message successfully sent" )
 time.sleep(3)
Send data to Azure Hub
After successfully writing the code, compile it. If the code compiles successfully, run the code. In the terminal window, you should see the message “Message successfully sent”. The window image is shown below:

Now, to see the data in Azure IoT Hub, go to the portal and click on Terminal CLI and replace your credentials with the following commands.
az iot hub monitor-events --hub-name XYZ --device-id XYZ
Replace XYZ with the Hub Name and Device ID. After running the above command, you should see the data on the screen as shown below. This is the data sent from the Raspberry Pi.
Suggested article: How to set up Seven Segment with Raspberry Pi

Items in the file: complete source
Internet of things training, Raspberry Pi project training, Raspberry Pi projects, Internet of things
The project of monitoring electricity consumption on the Internet with Raspberry Pi IoT
05/23/2019
Approximate study time 8 minutes

Contents [show]
The energy consumption monitor and check helps you check the amount of energy consumption in different parts of the building, factory or... and make the necessary decisions based on that. Monitoring energy consumption is a common project and is available in the market, but I think it's more fun to use our own homemade version. In this tutorial, we will build a power consumption monitoring system based on Raspberry Pi, with which we will be able to view energy consumption on the Internet and on the Adafruit.io platform.
The following video will help you understand how this Raspberry pi and IoT project works.
Video display
00:00
01:00
How is energy measured with raspberry pie?
The operation of the energy consumption monitoring project with Raspberry Pi and sending to the Internet is shown in the image below.

choosing units one after another;
Current Sensing Unit: The current sensing unit consists of an SCT-013 current sensor that can measure up to 100 amps, depending on the version you buy. The sensor converts the current through the wire it is connected to into a smaller current that feeds the ADC through a voltage divider circuit.
Voltage Sensing Unit: Here we make a voltage sensor ourselves. Our homemade voltage sensor includes a voltage divider stage that converts the high voltage to a suitable value to feed to the ADC.
Processing unit: The processing unit consists of ADC and Raspberry pi. The ADC takes the analog signal and sends it to the Raspberry Pi, where the exact amount of power consumed is calculated and sent to the Adafruit.io plenum.
Disclaimer: Before we begin, it is important to mention that this project involves connecting to a high voltage power supply, which is very dangerous and you should exercise caution.
Required parts
To build this power consumption monitoring project with Raspberry pi, the following components are required.
1. Raspberry Pi board
2. ADS1115 16bit I2C analog to digital converter
3. YHDC SCT-013-000 sensor
4. 2.5A 5V MicroUSB power adapter
5. Resistor 2W 10 kilo ohms
6. Resistance 0.5W 10 kilo ohms
7. 33 Ohm resistance
8. Resistor 2W 3.3 kilo ohms
9. IN4007 diode – four numbers
10. 3.6v zener diode
11. 10 kilo ohm potentiometer
12. Capacitor 50v 1uf
13. Capacitor 50v 10uf – two numbers
Get the required parts from the Ironex parts store.
Here I am using buster operating system.
Suggested article: Establishing Raspberry Pi Internet with Sim800l GSM/GPRS module
Preparing Raspberry Pi for IoT power consumption monitoring
Before we start connecting the parts and programming, there are some simple things we need to do on the Raspberry Pi.
Step 1: Enable I2C on Raspberry Pi
Our main core in this project is ADC1115 16bit I2C based ADC. The ADC allows us to connect analog sensors to the Raspberry Pi since the Pi itself does not have a built-in ADC. This part takes data through its ADC and transfers it to the Raspberry Pi via I2C. Likewise, we need to enable I2C communication on the Pi so it can communicate with it.
I2C on the Raspberry Pi can be enabled or disabled via the configuration page. To launch it, click on the Raspberry Pi icon on the desktop and click on configuration in preferences.
If you have any questions about this article, ask in the comments section

Enable I2C communication as shown below.

You can also access the Raspbian settings page by running sudo raspi-config.
Step 2: Install the ADS11xx library from Adafruit
The second thing we need to do is install the ADS11xx Python library, which contains functions and routines that make it easy for us to write Python scripts to get the ADC values.
To do this, follow the steps below.
1. At the beginning of the order
sudo apt-get update
Run and then
sudo apt-get upgrade
Run to update your Raspberry Pi.
2. Next, run the cd ~ command to make sure you are in your home directory.
3. In the next step, activate the required items with the following command
sudo apt-get install build-essential python-dev python-smbus git
4. Next, clone the Adafruit git folder by running the opposite command.
git clone https://github.com/adafruit/Adafruit_Python_ADS1x15.git
5. Using this command
cd Adafruit_Python_ADS1x1z
Go to the desired file page and with this command
sudo python setup.py install
Complete the installation.
Step 3: Install the Adafruit.IO Python module
As mentioned at the beginning, we will publish the energy consumption information on Adafruit IO Cloud, which can be viewed from anywhere in the world. You can also do a wide range of actions by connecting IFTTT to it.
The Adafruit.IO python module contains subroutines and functions that we will use to easily transfer data to the cloud. Follow the steps below to install the module.
1. Run cd ~ to return to the home directory.
2. Then run the following command.
sudo pip3 install adafruit-io
This should have the Adafruit IO python module installed.
Step 4: Set up your Adafruit.io account
To use Adafruit IO you definitely need to create an account first to get an AIO key. This AIO key along with your username is used by the Python script to access the Adafruit IO cloud service. To create an account, go to io.adafruit.com, click the get started for free button and fill in all the required parameters. Once registered, you should see the View AIO Key button on the right side of your home screen.
Suggested article: Teaching peer-to-peer communication of Raspberry Pi and Arduino with LoRa
Click on it to get the AIO key. Then write down the Active Key.
To create a feed, click on “Feeds” at the top of the AIO page and click on add new feed.
Call it whatever you want, but to keep things simple, I'll call it energy consumption. You can also decide to create feeds for voltage and current and adapt the code to publish the data.
With all this done, now we are ready to build the project.
Schematic of the energy meter project based on the Internet of Things
The circuit schematic for the Raspberry Pi Energy Monitor project is fairly complex and involves connecting to an AC voltage.

The current transformer used in this project is shown below, as you can see we have three wires from it ie Ground, Cout and 3.3V
Schematic of the voltage section
Connect the parts for the voltage sensor as shown in the figure below.

Information processing unit schematic
Connect everything to the Raspberry Pi according to the circuit schematic below.

Make sure that the GND pins of both sensing units are connected to the GND of the analog-to-digital component or the Raspberry Pi.
After connecting the parts like the schematics, your circuit should look something like below.

Python code to measure energy with Raspberry Pi
I suggest you use Python 3 for this project. The complete code of the project is placed in the downloadable file at the end of the page. Here we explain some parts of the code. The algorithm behind the code is simple. Our Python script reads the voltage and current from the ADS1115. The amount of energy is calculated and sent to the Adafruit platform in kilovolts.
First, we call the required libraries.
import time
import Adafruit_ADS1x15
from Adafruit_IO import *
import math
Next, we create an example of the ADS1115 library that is used to address the ADC. I suggest you see the analog to digital tutorial on Raspberry Pi.
# ADS1115 ADC (16-bit)
adc1 = Adafruit_ADS1x15.ADS1115()
Next, enter your adafruit IO username and “AIO” key.
username = 'Enter your username here'
AIO_KEY = 'your key'
aio = Client(username, AIO_KEY)
Please keep the key safe and do not publish it as it may interfere with your information.
Next, we create variables such as Gain for the ADC, the number of samples we want.
GAIN = 1
samples = 200 # number of samples
places = int(2)
Next, we create a loop that controls the current and voltage and sends the data to the Adafruit io at intervals. The loop starts by setting all variables to 0.
while True:
 # Reset variables
 count = int(0)
 datai = []
 datav = []
 maxIValue = 0 #Maximum current in sample
 maxVValue = 0 #Maximum voltage in sample
 IrmsA0 = 0
 VrmsA1 = 0
 ampsA0 = 0 #peak current
 voltsA1 =0 #Voltage
 kilowatts = float(0)
Since we are working with AC circuits, the output of the SCT-013 and the voltage sensor will be a sine wave, so to calculate the current and voltage from the sine wave, we need to get the peak values. To obtain peak values, we will sample both voltage and current (200 samples) and find the highest values ​​(peak values).
 for count in range(samples):
 datai.insert(count, (abs(adc1.read_adc(0, gain=GAIN))))
 datav.insert(count, (abs(adc1.read_adc(1, gain=GAIN))))
 # If there is another maximum value
 print (datai[count])
 if datai[count] > maxIValue:
 maxIValue = datai[count]
 if datav[count] > maxVValue:
 maxVValue = datav[count]
Next, we standardize the values ​​by converting the ADC values ​​to the actual value and then use the Root Mean Square equation to find the RMS voltage and current.
 # Calculate flow using samples
 # Calibrate Haryan
 IrmsA0 = float(maxIValue / float(2047) * 30)
 IrmsA0 = round(IrmsA0, places)
 ampsA0 = IrmsA0 / math.sqrt(2)
 ampsA0 = round(ampsA0, places)
 # Calculate the voltage
 VrmsA1 = float(maxVValue * 1100/ float(2047))
 VrmsA1 = round(VrmsA1, places)
 voltsA1 = VrmsA1 / math.sqrt(2)
 voltsA1 = round(voltsA1, places)
 print('Voltage: {0}'.format(voltsA1))
 print('Current: {0}'.format(ampsA0))
With this, the energy is calculated and the data is published on adafruit.io.
 # Energy calculation
 power = round(ampsA0 * voltsA1, places)
 print('Power: {0}'.format(power))
 # Send data to adafruit.io
 EnergyUsage = aio.feeds('EnergyUsage')
 aio.send_data('EnergyUsage', power)
For free accounts, adafruit requires a delay between requests and data uploads.
 # Delay before repeating
 time.sleep(0)
Project performance video
After completing the code, save it and hit the run button on the Python IDE. Before this, make sure that the Raspberry Pi is connected to the Internet via WiFi or LAN, and that your aio key and username are correct. After some time, you should see the energy (power) data displayed in the feed on Adafruit.io.
Suggested article: Introducing the NodeMCU board and programming with Arduino
To take things further, you can create a dashboard on adafruit.io and add a graphics component so you can get a graphical representation of the data as shown in the image below.

In this way, you can create a project to measure the amount of energy consumed with a Raspberry Pi based on the Internet of Things.
Items in the file: complete source, complete schematic
Esp training, ESP32 training, Internet of Things training, Esp projects, Internet of Things projects
Home appliance control with Android mobile and ESP32 Bluetooth board
In this ESP32 project, we use an Android phone to communicate with the ESP32 microcontroller via low-power Bluetooth BLE and control the board pins with an Android mobile phone. Programming of this project is done with Arduino software.


Bluetooth modules such as HC-05 and HC-06 can be easily configured with Arduino IDE, but they have their own limitations such as high power consumption and work on old Bluetooth V2.0. Also recently I got myself a new ESP32 DEV kit, these modules have features like built-in Wi-Fi and Bluetooth, ADC and DAC pins, audio support, SD card support, Deep Sleep mode, etc. That means everything is ready for IoT projects.
The following video will help you understand how this project works.

Getting started with ESP32 bluetooth
The first app I wanted to try was a simple app where I could turn a light on or off using an Android app, just like our old projects with the HC-05 bluetooth module. But it turns out that Bluetooth Low Energy (BLE) has more features. I also noticed that there are two types of Bluetooth in the ESP32 module, one is classic Bluetooth and the other is Bluetooth Low Energy (BLE). Why do we have two types of Bluetooth and what should we use for our project?

Comparison of low energy Bluetooth and classic Bluetooth
Bluetooth Low Energy, as the name suggests, uses less energy than classic Bluetooth. But unlike classic Bluetooth, it is not used to transfer files or music. Have you ever wondered how your phone automatically detects that the bluetooth device you're connected to is an audio device or a laptop or phone, maybe you've seen the battery level on the player Wireless audio or fitness bracelets are automatically shown in the status bar. All this is possible with the specification of BLE devices. A BLE device works with Bluetooth V4.0 and can work with low power as a server or as a client, which makes BLE an ideal choice for smart watches, fitness bracelets, etc.
Suggested article: Project to get time from the Internet with ESP32 and NTP board
Classic Bluetooth, on the other hand, is just plain old Bluetooth that we use to transfer files and other data. Almost all BLE devices have classic Bluetooth functionality as well. The Bluetooth used in modules like the HC-05 is a version of classic Bluetooth called Bluetooth SSP (Serial Port Protocol), meaning that Bluetooth follows a standard serial protocol that makes it easier to send and receive data. At the end of this tutorial, we will learn how to use Bluetooth serial capabilities in ESP32.
Here in this article, we use the Bluetooth serial function of ESP32 to pair it with Android mobile phone and use any Bluetooth Terminal app available in Play Store to send commands to ESP32 and control the LED on ESP32 board. .
In future articles we will cover ESP32 BLE as a server. BLE server is generally used to send BLE data to other Bluetooth devices and BLE client is used to scan other BLE devices.
ESP32 bluetooth serial project code for smart home
The complete code for controlling an LED using ESP32 Bluetooth is included in the download file at the bottom of the page. Here we check some parts of the code. As mentioned, this code is written using Arduino software, so I suggest you read ESP32 programming tutorial with Arduino.
Here we set the program so that whenever we enter 1 in our Android phone software, the LED will turn on and whenever we enter 0, the LED will turn off. You can easily change and customize these commands.
At the beginning of our code, we call the bluetooth serial library.
#include "BluetoothSerial.h" //Bluetooth serial library
The next thing we need is an object for Bluetooth related operations. Here I have named an object as ESP_BT, but you can choose any name.
BluetoothSerial ESP_BT; // Object for Bluetooth
Then inside the void setup() function we start the serial communication with baud rate 9600 and start the bluetooth signal with a name. Here I have named it “ESP32_LED_Control”, this will be the name displayed when trying to pair with our phone. Finally I declared the internal LED pin as an output pin because we want to set the state of that pin based on the received bluetooth signal.
void setup() {
 Serial.begin(9600); // Serial communication with baud rate 9600
 ESP_BT.begin("ESP32_LED_Control"); // Bluetooth signal name
 Serial.println("Bluetooth Device is Ready to Pair");

 pinMode (LED_BUILTIN, OUTPUT);//setting the output pin
}

Inside the void loop() function, we check if there is any data from the Bluetooth module, if yes, the data is received and read into the input variable. We also display this value in the serial monitor just to check what is being received.
If you have any questions about this article, ask in the comments section
Suggested article: Building a web server with Arduino and ESP8266 (comprehensive training)
 if (ESP_BT.available()) // check for input signal
 {
 incoming = ESP_BT.read(); // Read what is received
 Serial.print("Received:"); Serial.println(incoming); // Display information in

 Information in serial monitor
Now whatever data is received is stored in the input variable, so we can directly compare this variable with the expected value and perform the required action. But the value sent from Bluetooth will be in the form of char, and Arduino will read the decimal value of char. The complete decimal training article can help you.
Here, as mentioned, we use the numbers 0 and 1. In decimal, the value of char '0' will be equal to 48 and char '1' will be equal to 49.
Here we have compared the input variable with 48 and 49 to check for 0 and 1. If the number is 0, we will turn off the LED and also a confirmation message will be shown on the mobile phone and for the number 1 we will also turn on the LED and a message will be shown on the mobile phone.
 if (incoming == 49) // check incoming
 {
 digitalWrite(LED_BUILTIN, HIGH); // Turn on the LED
 ESP_BT.println("LED turned ON"); // The message displayed on the phone
 }

 if (incoming == 48) // check incoming
 {
 digitalWrite(LED_BUILTIN, LOW); // Turn off the LED
 ESP_BT.println("LED turned OFF"); // The message displayed on the phone
 }
Serial bluetooth test with ESP32 board
Connect your ESP to the Arduino IDE and select the correct Board and Port. It may take some time to upload the code. Open the Serial Monitor (this is only used to describe the functionality and is optional) and then open the Termina Bluetooth software on your phone. According to the given code you should see a device named ESP32_LED_Control. Pair with it.

I use an app called “Bluetooth Terminal” downloaded from the Google app store. Install the Bluetooth app on your mobile and enter the number 1.

The ESP32 module will receive it and turn on the LED as per our code and also give you a confirmation message telling you that the LED is on. You can also check the serial monitor which shows the data received by the ESP32 Bluetooth in decimal format and the Arduino reads 48 for 0 and 49 for 1 as explained in the beginning. A screenshot of my monitor's serial window is shown below.

Likewise, you should turn off the LED by sending 0 from the mobile app.
Items in the file: complete source
Arduino training
Learning to program Arduino with Python Arduino - Python
03/21/2019
Approximate study time 8 minutes

Contents [show]
hello We have prepared a complete tutorial on Arduino programming with Python.
Arduino programming with Python
Arduino has always been developing hardware and software to make learning easier. Python is one of the object-oriented programming languages ​​with dynamic semantics, which is useful for rapid program development. By combining the power of Arduino and Python, many possibilities will be provided because Python provides more productivity possibilities by connecting with other platforms such as MATLAB, OpenCV, etc. In this tutorial, we will learn how to use Python to control an LED on an Arduino board.
In this tutorial we will learn:
1. Install Python on the computer
2. Install PySerial in Python
3. Arduino programming for Arduino and Python communication
4. Python programming for Arduino and Python communication
5. LED control project with Python and Arduino
1. Complete tutorial on installing Python on the computer
Obviously, the first step in this tutorial is to install Python on our computer. The steps mentioned below are applicable only for Windows users who have a 32-bit or 64-bit operating system. MAC and Linux installation methods are different.
Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Pico board training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
Step 1: First, you need to download the Python software from this link. The 32-bit version is downloaded. Note that version 32 can be installed on 64-bit operating systems. And the reason for using this particular version is that it supports Arduino libraries. Please do not update Python and do not download other versions because they do not support Arduino libraries.
Step 2: Open the downloaded file and just click Next. By default, Python is installed at C:\Python27. Do not change the installation location either.
You may receive a warning from your antivirus while installing Python (it's possible!). If you receive a warning, click Allow.
Now Python is successfully installed on our laptop/computer. You can search for Python IDLE to make sure the installation was successful.

In the image above, click on the second option that says "Python IDLE" and open the software. You will come across the following page, which is called Python Shell.


You can directly start coding from here and get the output on the same page or create a new file and write the program there and verify the program.
Now let's check if Python is working properly or not. It is enough to do the test
"Print (1 + 1)"
Type and press Enter. You should see the result as shown below.

If you have any questions about this article, ask in the comments section
2. Training to install PySerial in Python
The next step is to install pyserial. PySerial is a Python API module used to read and write serial data to Arduino or any other microcontroller.
Click this link to download PySerial. The downloaded file will be an exe file that can be installed directly. Do not change any settings during installation. Install it default location.
Now you need to check if PySerial is installed correctly or not. To do this, open Python Shell and type:
import serial
If the library is installed successfully, you will not get any error message as shown in the image below. If you encounter any errors, write them in the comments section and we will try to fix it.
This tutorial assumes you are familiar with Arduino and have experience uploading projects to Arduino. So let's jump right into the Python program. If you are new to Arduino, check the Arduino tutorial and Arduino project section of the site.
As mentioned earlier, we will control the Arduino board using a Python script. Let's start with the Arduino code.
3. Arduino programming for Arduino and Python communication
The full schedule is provided at the end of this section. And reading this part will only help you to understand this project.
Inside the void setup() function, we start the serial communication at 9600 baud rate and declare that we will use the internal LED as an output and turn it off when the program starts. We also send the welcome message (Hi!, I am Arduino) to Python through Serial println:
void setup() {
 Serial.begin(9600); // Set the baudrate to 9600
 pinMode(LED_BUILTIN, OUTPUT); //Set internal LED ie pin 13 as output
 digitalWrite (LED_BUILTIN, LOW); // Turn off the internal LED
 Serial.println("Hi!, I am Arduino"); // Send serial message
}
Inside the loop function void loop(), we read the data that is entered serially and give the value to the "data" variable. Now, based on the value of this variable ("data"), as shown in the figure below, we turn on and off the internal LED of the Arduino.
void loop() {
while (Serial.available()){ // When data is available
 data = Serial.read(); // Read the serial value and put it in the data variable
}

if (data == '1') // If the serial value is 1
digitalWrite (LED_BUILTIN, HIGH); // Turn on the LED

else if (data == '0') // If the serial value is 0
digitalWrite (LED_BUILTIN, LOW); // Turn off the LED
}
The complete Arduino code of this tutorial:
int data;
void setup() {
 Serial.begin(9600);
 pinMode(LED_BUILTIN, OUTPUT);
 digitalWrite (LED_BUILTIN, LOW);
 Serial.println("Hi!, I am Arduino");
}
void loop() {
while (Serial.available()){
 data = Serial.read();
}
if (data == '1')
digitalWrite (LED_BUILTIN, HIGH);
else if (data == '0')
digitalWrite (LED_BUILTIN, LOW);
}
4. Python programming for Arduino and Python communication
The complete Python program for this tutorial is provided at the bottom of this page. And reading this part will only help you to understand this project.
1. First, open Python Shell and click on File -> New.
2. Then a new page will open where we continue coding.
3. Then save the file before writing the code. You can use the shortcut key Ctrl+S. This will save a file in .py format in the location you want with the name you want.
4. Now you can write the code or get the complete code at the bottom of the page and copy it.
In our program, the first step will be to import the serial and time library. The serial library is used to write and read serial data and the time library is used to create a delay in the program. These two libraries can enter our program using the following code.
import serial #Serial imported for Serial communication
import time #Required to use delay functions
The next step is to configure a serial object using the serial library. In this program, we call our serial object "ArduinoSerial". In this line, we must mention the name of the COM port to which our Arduino is connected and say at what baud rate it works.
ArduinoSerial = serial.Serial('com18',9600)
Note: It is very important to specify the correct name of the COM port. You can find it using Device Manager on your computer.
To do this, first open the Device Manager. Then you will find an option called "Ports COM & LPT" as shown in the image below. Make sure the Arduino board is recognized in that section.


Note: The PORT name for my Arduino board appeared as Arduino, your board name may be different based on the board manufacturer. For example it could be CCH450 or something like that, so don't worry about the port name.
If you do not find an option called “Ports COM & LPT”, it means that your board is not recognized. So you need to install the correct drivers for your board.
In some cases you will find more than one COM port listed under the Ports section and you won't know which one is for the Arduino board because the naming will also be different. In this case, just disconnect the board and reconnect it. Check which COM port disappears and reappears, this is the COM port of your Arduino board.
After you have configured your serial object, we need to run the program for two seconds to communicate. This is done by writing the following code.
time.sleep(2)
Now we can read or write anything from Arduino.
With the underscore, everything coming from the Arduino will be read and printed in Python Shell
print ArduinoSerial.readline()
You can also assign the value to a variable and use it for calculations.
The following line sends a value of 1 to the Arduino board. You can replace it with any other decimal number.
ArduinoSerial.write('1')
Now, returning to our program, we write the following lines inside the while loop.
var = raw_input() #get input from user
 print "you entered", var #print the input for confirmation

 if (var == '1'): #if the value is 1
 ArduinoSerial.write('1') #send 1
 print("LED turned ON")
 time.sleep(1)

 if (var == '0'): #if the value is 0
 ArduinoSerial.write('0') #send 0
 print("LED turned OFF")
 time.sleep(1)
The var = raw_input line takes whatever value is typed into the shell script and assigns that value to the var variable.
If the value is 1, it will send serial 1 to Arduino and if it is 0, it will send serial 0 to Arduino.
We have set the value of 1 and in the Arduino program. You can put anything in place of 0 and 1 and set your desired actions for them.
The full Python code of this tutorial:
import serial
import time

ArduinoSerial = serial.Serial('com18',9600)
time.sleep(2)
print ArduinoSerial.readline()
print ("Enter 1 to turn ON LED and 0 to turn OFF LED")

while 1:
 var = raw_input()
 print "you entered", var

 if (var == '1'):
 ArduinoSerial.write('1')
 print("LED turned ON")
 time.sleep(1)

 if (var == '0'):
 ArduinoSerial.write('0')
 print("LED turned OFF")
 time.sleep(1)
After placing this program in Python, you will see the screen like the image below.

Now click on Run -> Run Module or press F5 which may ask you to save the program and then it will run.
5. LED control project with Python and Arduino
This project is very easy to do. Upload the program to your Arduino and make sure it is connected to the same COM port as the Python program. Then launch the Python program as mentioned above.
This will launch the Python shell script as shown below. The window on the left is the shell window that displays the output, and the window on the right is the script that displays the program.

As you can see, the phrase "Hi!, I am Arduino" entered in the Arduino program is received by Python and displayed in its shell window.
When the shell window asks you to enter values, we can enter 0 or 1. If you enter 1, we turn on the LED on the Arduino board, and if we send 0, we turn off the LED on the Arduino board.
I hope you understand this tutorial and can put it into practice. If there is a problem, let me know in the comments, I will be happy to solve your problem.
Raspberry Pi tutorial, Raspberry Pi project
Object classification with Raspberry Pi and Edge Impulse TinyML

Edge Impulse Studio is a machine learning platform that enables developers to generate trained models in the cloud and deploy them on microcontrollers (eg Arduino and STM32) or single board computers like Raspberry Pi. Initially, Edge impulse did not support Raspberry Pi but in April 2021 Edge Impulse announced its full support with Raspberry Pi.
So, in this tutorial, we are going to train an image classifier model on Edge Impulse and then deploy it on Raspberry Pi.
Video display
00:00
00:45
Required parts
• Raspberry Pie
• Pi camera module
Getting started with Edge Impulse
To train a machine learning model with Edge Impulse and Raspberry Pi, create an Edge Impulse account, verify your account, and then create a new project.

Arduino training course, ESP32 training course, STM32 training course, Electronics training course
Pico board training course, Raspberry Pi training course, Altium Designer training course, do you want a course discount?
AVR training course, Proteus training course, Internet of Things training course, board and electronic parts store
Installing Edge Impulse on Raspberry Pi
Now, to use Edge Impulse on Raspberry Pi you must first install Edge Impulse and its dependencies on Raspberry Pi. To install Edge Impulse on Raspberry, use the following commands:
curl -sL https://deb.nodesource.com/setup_12.x | sudo bash -
sudo apt install -y gcc g++ make build-essential nodejs sox gstreamer1.0-tools gstreamer1.0-plugins-good gstreamer1.0-plugins-base gstreamer1.0-plugins-base-apps
sudo npm install edge-impulse-linux -g --unsafe-perm
Now, use the following command to run Edge Impulse:
edge-impulse-linux
You will be prompted to sign in to your Edge Impulse account. You will then be asked to select a project, and finally select the microphone and camera to connect to the project.

Now, as Edge Impulse is running on the Raspberry Pi, we need to connect the Pi camera to the Pi to collect the image. Connect the Pi camera as shown in the image below.

Create a dataset
As mentioned earlier, we use Edge Impulse Studio to train our image classification model. For this purpose, we need to collect a dataset that has samples of objects that we want to classify using the Pi camera. Since the objective is to classify onions and potatoes, you need to collect some image samples of onions and potatoes to be able to distinguish between the two.
You can collect samples using a mobile phone, a Raspberry Pi board, or you can import a data set into the account. The easiest way to load samples into Edge Impulse is using a mobile phone. For that, you need to connect your mobile phone to Edge Impulse.
Suggested article: Character LCD setup with Raspberry Pi and Python code
To connect your mobile phone, click on “Devices” and then click on “connect a new device”.

Now, in the next window click on “Use your Mobile Phone”, a QR code will appear. Scan the QR code with your mobile phone using Google Lens or other QR code scanner apps. This will connect your phone to Edge Impulse Studio.
If you have any questions about this article, ask in the comments section

With your phone connected to Edge Impulse Studio, you can now load your samples. Click on “acquisition data” to load samples. Now, on the data collection page, enter the tag name (for potato) and select “camera” as the sensor. Click on "Start sampling".

This will save the potato image to the Edge Impulse cloud. Take 10 to 20 pictures from different angles. After loading the potato samples, now set the label to 'Onion' and collect another 10-20 images.

These examples are for model training. In the next steps, we collect test data. The test data should be at least 20% of the training data, so collect 3 samples of potatoes and onions.
Potato and onion recognition model training
For this, go to the “Create impulse” page.

Now, on the “Create impulse” page, click “Add a processing block” and click the “add” button next to the “image” block to add a processing block that normalizes the image data and adjusts the color depth. reduces After that, click on the “Transfer Learning (images)” block to get a pre-trained image classification model to set up for the potato and onion detection task. Then click on “Save Impulse”.


