# Valve Controller
![Valve Controller](/uploads/valve-controller.png "Valve Controller"){.align-right}
The Valve Controller is the heart of a Guardian system. It installs over standard ball valves with no tools and no plumber to automatically shut off the water main during a leak. It also acts as the point of contact between the Guardian app and all connected Water Detectors in the system.

## Installation

**Guardian Set-up/testing**
1.	Close your valve
2.	Mount the Guardian Valve Controller on the valve and plug it in. 
Power LED: solid
Wi-Fi LED: heart beat mode
RF LED: Off
Bottom LED: pulsing red
3.	Turn on your phone’s Bluetooth. Open the latest version of your Guardian app. Enter your log-in credentials
4.	Select “SETUP” under the corresponding PIN for your Guardian, enter your Wi-Fi login details. 
Guardian will reboot
Power LED: Solid>Solid> Solid
Wi-Fi LED: Heart Beat >Off>Solid
RF LED: Off>On>Off
Bottom LED: pulsing red>Pulsing red> Pulsing red
5.	Guardian will update automatically 
Power LED: Solid>solid>solid>solid>off as bottom LED turns purple>solid
Wi-Fi LED: Solid>Off>blinking>solid>off as bottom LED turns blinks purple>solid
RF LED: Off>Off>blink>off>blink>off
Bottom LED: solid blue> solid blue > solid blue> solid blue>solid purple>off>flashes purple 7x>solid blue
6.	Confirm location on your app and start calibration. Bottom LED will be blinking Blue upon opening of valve and blinking red upon closing.
7.	Exit Set up after calibration
8.	Devices>Valve Controller>Settings>Firmware version. Check if Guardian has updated to latest firmware version
9.	Go back to main menu >Add new Device>Add leak/water detector
10.	Activate your leak detector (lick the sensor, put water on it)
11.	Connect your leak detector to Guardian using their PIN. The RF led should blink every time you shake/move the leak detector
12.	Go to Devices>Click on all the connected leak detectors on by one and check if their status is DRY, and battery level is over 90%. Shake/move detector to refresh readings. RF LED should blink 3 times every time you move the detector.
13.	Put water on one of the sensors and see if valve handle shuts and the Guardian beeps. RF led will blink thrice. Check app activity to see if you have received a notification of the leak and of the valve handle closing
14.	Dry the above-mentioned sensor, and RF led will blink thrice, Guardian will stop beeping. Check app activity to see notification that sensor/detector is dry
15.	Devices>Valve Controller>Valve>Open to open valve handle
16.	Repeat above steps to test all connected leak detectors
17.	After testing all leak detectors, open valve handle again
18.	Plug in remote probe to the Guardian, Wet the probe, valve handle should close. Guardian should beep and App should notify you of a leak.
19.	Factory reset and remove Guardian: Devices>Valve controller settings>Remove this Device>Yes
Power LED: Solid
Wi-Fi LED: Heart Beat 
RF LED: Off
Bottom LED: pulsing red
20.	Connect Guardian to the App again. Find your corresponding valve controller and match its PIN and get to “connect to Wi-Fi “page on app (Do not set up Wi-Fi). If your previous log in credentials are not associated/saved with the valve controller, then factory set was successful. If not, connect Guardian again and repeat Calibration. Follow Step 19 again to disconnect after calibration. 
21.	Unplug your Guardian 
	

## Running the tests

### Functional Description of Guardian
#### Top LED Behavior

<table>
<tr><th> Behavior </th><th> This happens when...</th></tr>
<tr><td>Power LED on</th><td>Unit is plugged in.</td><tr>
<tr><td>Power LED off</td><td>Unit is not plugged in.</td></tr>
<tr><td>Wi-Fi LED double blinks</td><td>Hotspot on.</td></tr>
<tr><td>Wi-Fi LED off</td><td>Hotspot off, not connected to Wi-Fi.</td></tr>
<tr><td> Wi-Fi light single blinking </th><td> Hotspot off, connected to Wi-Fi but no cloud access.</th></tr>
<tr><td>Wi-Fi solid LED</th><td>Hotspot off, connected to Wi-Fi and connected to cloud.</td><tr>
<tr><td>Guardian RF LED double blinking</td><td>Bluetooth is on.</td></tr>
<tr><td>Guardian RF single blinking</td><td>Guardian RF message received</td></tr>
<tr><td>Guardian RF LED off</td><td>Bluetooth off and no Guardian RF message received.</td></tr>
</table>
                          
 **Power LED on:**	                                    *Unit is plugged in.*
**Power LED off:**	                                   *Unit is not plugged in.*
**Wi-Fi LED double blinks:**	                   *Hotspot on.*
**Wi-Fi LED off:**	                                    *Hotspot off, not connected to Wi-Fi.*
**Wi-Fi light single blinking:**	                *Connected to Wi-Fi but no cloud access.*
**Wi-Fi solid: LED**	                                   *Connected to Wi-Fi and connected to cloud.*
**Guardian RF LED double blinking:**	    *Bluetooth is on.*
**Guardian RF LED single blinking:**	      *Guardian RF message received.*
**Guardian RF LED off:**	                         *Bluetooth off and no Guardian RF message received.*

#### Button Behavior 

<table>
<tr><th> Behavior </th><th> This happens when...</th></tr>
<tr><td>Press button once</th><td>Valve opens, closes or stops.</td><tr>
<tr><td>Hold for 5 seconds</td><td>Guardian beeps and Bluetooth is turned on.</td></tr>
<tr><td>Hold for 15 seconds</td><td>Guardian beeps twice and Wi-Fi AP information is reset.</td></tr>
<tr><td>Hold for 25 seconds</td><td>Guardian beeps thrice, factory reset.</td></tr>
</table>

**Press button once:**	*Valve opens or closes.*
**Hold for 5 seconds:**	*Guardian beeps and Bluetooth is turned on.*
**Hold for 15 seconds:**	*Guardian beeps and Wi-Fi AP information is reset.*
**Hold for 25 seconds:**	*Guardian beeps, factory reset.* 

#### Bottom LED Behavior

 <table>
<tr><th> Behavior </th><th> This happens when...</th></tr>
<tr><td>Breathing red</th><td>Valve handle closed.</td><tr>
<tr><td>Blinking blue</td><td> Valve handle is opening.</td></tr>
<tr><td>Blinking red</td><td>Valve handle open.</td></tr>
<tr><td>Alternating red and blue</td><td> Valve handle is closing.</td></tr>
<tr><td>Flashing purple</td><td>ST update.</td></tr>
</table>

**Breathing red:**	        *Valve handle closed.*
**Blinking blue:**	         *Valve handle is opening.*
**Solid blue:**	                *Valve handle open.*
**Blinking red:**	             *Valve handle is closing.*
**Alternating red and blue:**	 *Valve handle stalled.*
**Flashing purple:**	            *ST update.*

## Specification Sheet

1. [Valve Controller Spec Sheet](/uploads/valve-controller-spec-sheet.pdf "Valve Controller Spec Sheet")

## Power Supply Test Reports

1.  [Gvcp 1 Ca 65 Report](/uploads/gvcp-1-ca-65-report.pdf "Gvcp 1 Ca 65 Report")
2.  [Assa 67 C 2 A 0 Etl C 2 A 060950 60065 C 2 A 0 Cert](/uploads/assa-67-c-2-a-0-etl-c-2-a-060950-60065-c-2-a-0-cert.pdf "Assa 67 C 2 A 0 Etl C 2 A 060950 60065 C 2 A 0 Cert")
3.  [Assa 67 C 2 A 0 Etl C 2 A 060950 60065 C 2 A 0 Report](/uploads/assa-67-c-2-a-0-etl-c-2-a-060950-60065-c-2-a-0-report.pdf "Assa 67 C 2 A 0 Etl C 2 A 060950 60065 C 2 A 0 Report")
 
## API Documents

1. [Gvc 1 Api Document](/uploads/gvc-1-api-document.pdf "Gvc 1 Api Document")
2. [Guardian Api Document Advanced](/uploads/guardian-api-document-advanced.txt "Guardian Api Document Advanced")
3. [Guardian Api Document Advanced](/uploads/guardian-api-document-advanced.txt "Guardian Api Document Advanced")
4. [Json Commands](/uploads/json-commands.txt "Json Commands")

## Certifications 

### PCB
1. [Pcb Ul Zpmv 2 Future Supplier 1](/uploads/pcb-ul-zpmv-2-future-supplier-1.pdf "Pcb Ul Zpmv 2 Future Supplier 1")
2. [Pcb Ul Zpmv 2 Future Supplier 2](/uploads/pcb-ul-zpmv-2-future-supplier-2.pdf "Pcb Ul Zpmv 2 Future Supplier 2")
3. [Pcb Ul Zpmv 2 Current Supplier](/uploads/pcb-ul-zpmv-2-current-supplier.pdf "Pcb Ul Zpmv 2 Current Supplier")
 
### Enclosure Plastic
1. [Enclosure Plastic Rohs](/uploads/enclosure-plastic-rohs.pdf "Enclosure Plastic Rohs")
2. [Enclosure Plastic Iec 60696 11 10](/uploads/enclosure-plastic-iec-60696-11-10.pdf "Enclosure Plastic Iec 60696 11 10")
3. [Enclosure Plastic Iso](/uploads/enclosure-plastic-iso.pdf "Enclosure Plastic Iso")

## Packaging
1. [Gvc 1 Giftbox Artwork 20180521](/uploads/gvc-1-giftbox-artwork-20180521-.pdf "Gvc 1 Giftbox Artwork 20180521")

## Icon (Guardian 'G' symbol)
1. [Gicon](/uploads/gicon.ico "Gicon")
2. [Gred](/uploads/gred.ico "Gred")



## Hammer
1. [Readme Txt](/uploads/readme-txt.docx "Readme Txt")
2. [MacHammer 0 0 1](/uploads/machammer-0-0-1.exe "Machammer 0 0 1") &mdash; This tool identifies the IP of the Valve Controller on the same network as the PC.
3. [Helphammer 1 0 1](/uploads/helphammer-1-0-1.exe "Helphammer 1 0 1") &mdash; HelpHammer V1 has optional IP targeting. If you know the IP of your Valve Controller you can use this tool to update the firmware (beta and production) and connect to Wi-Fi. If IP is unknown, you can send the command to all Valve Controllers on the same network as the PC.
4. [Helphammer 2 2 2](/uploads/helphammer-2-2-2.exe "Helphammer 2 2 2")&mdash; HelpHammer V2 has no option to enter the IP. It finds the IP of a Valve Controller on the same network as the PC. You can use this tool to update the firmware (beta and production), connect to Wi-Fi, recalibrate, and do a factory reset.
> NOTE: Use only HelpHammer V2.X.X on networks with ONE Valve Controller on it.

### Python files
1. [Machammer](/uploads/machammer.py "Machammer")
2. [Machammer 002](/uploads/machammer-002.py "Machammer 002")
3. [Megahammer 001](/uploads/megahammer-001.py "Megahammer 001")
4. [Megahammer 003](/uploads/megahammer-003.py "Megahammer 003")
5. [Megahammer 004](/uploads/megahammer-004.py "Megahammer 004")
6. [Megahammer 005](/uploads/megahammer-005.py "Megahammer 005")
7. [Megahammer 006](/uploads/megahammer-006.py "Megahammer 006")
8. [Megahammer 007](/uploads/megahammer-007.py "Megahammer 007")
9. [Threadhammer 002](/uploads/threadhammer-002.py "Threadhammer 002")

### Word files
 1. [Megahammer 001 Py](/uploads/megahammer-001-py.docx "Megahammer 001 Py")
 2. [Megahammer 004 Py](/uploads/megahammer-004-py.docx "Megahammer 004 Py")
 3. [Megahammer 006 Py](/uploads/megahammer-006-py.docx "Megahammer 006 Py")
 4. [Threadhammer 002 Py](/uploads/threadhammer-002-py.docx "Threadhammer 002 Py")
 5. [Recalhammer Py](/uploads/recalhammer-py.docx "Recalhammer Py")

### Executable files
1. [Helphammer 2 0 0](/uploads/helphammer-2-0-0.exe "Helphammer 2 0 0")
2. [Helphammer 2 1 0](/uploads/helphammer-2-1-0.exe "Helphammer 2 1 0")
3. [Helphammer 2 2 1](/uploads/helphammer-2-2-1.exe "Helphammer 2 2 1")
4. [Recalhammer](/uploads/recalhammer.exe "Recalhammer")


