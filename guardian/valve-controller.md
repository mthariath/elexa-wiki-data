# Valve Controller

The Valve Controller is the heart of a Guardian system. It installs over standard ball valves with no tools and no plumber to automatically shut off the water main during a leak. It also acts as the point of contact between the Guardian app and all connected Water Detectors in the system.

## Getting Started
## Installation

## Running the tests

Functional Description of Guardian

Top LED Behavior:                              Behavior	This happens when...
Power LED on	Unit is plugged in.
Power LED off	Unit is not plugged in.
Wi-Fi LED double blinks	Hotspot on.
Wi-Fi LED off	Hotspot off, not connected to Wi-Fi.
Wi-Fi light single blinking	Connected to Wi-Fi but no cloud access.
Wi-Fi solid LED	Connected to Wi-Fi and connected to cloud.
Guardian RF LED double blinking	Bluetooth is on.
Guardian RF LED single blinking	Guardian RF message received.
Guardian RF LED off	Bluetooth off and no Guardian RF message received.

Button Behavior 
Behavior	This happens when...
Press button once	Valve opens or closes.
Hold for 5 seconds	Guardian beeps and Bluetooth is turned on.
Hold for 15 seconds	Guardian beeps and Wi-Fi AP information is reset.
Hold for 25 seconds	Guardian beeps, factory reset.

Bottom LED Behavior
Behavior	This happens when...
Breathing red	Valve handle closed.
Blinking blue	Valve handle is opening.
Solid blue	Valve handle open.
Blinking red	Valve handle is closing.
Alternating red and blue	Valve handle stalled.
Flashing purple	ST update.





## Deployment


## API

1. [Gvc 1 Api Document](/uploads/gvc-1-api-document.pdf "Gvc 1 Api Document")
2. [Guardian Api Document Advanced](/uploads/guardian-api-document-advanced.txt "Guardian Api Document Advanced")
3. [Guardian Api Document Advanced](/uploads/guardian-api-document-advanced.txt "Guardian Api Document Advanced")
4. [Json Commands](/uploads/json-commands.txt "Json Commands")

## Specification Sheet

1. [Valve Controller Spec Sheet](/uploads/valve-controller-spec-sheet.pdf "Valve Controller Spec Sheet")

## Power Supply Documents

1.  [Gvcp 1 Ca 65 Report](/uploads/gvcp-1-ca-65-report.pdf "Gvcp 1 Ca 65 Report")
2.  [Assa 67 C 2 A 0 Etl C 2 A 060950 60065 C 2 A 0 Cert](/uploads/assa-67-c-2-a-0-etl-c-2-a-060950-60065-c-2-a-0-cert.pdf "Assa 67 C 2 A 0 Etl C 2 A 060950 60065 C 2 A 0 Cert")
3.  [Assa 67 C 2 A 0 Etl C 2 A 060950 60065 C 2 A 0 Report](/uploads/assa-67-c-2-a-0-etl-c-2-a-060950-60065-c-2-a-0-report.pdf "Assa 67 C 2 A 0 Etl C 2 A 060950 60065 C 2 A 0 Report")
 

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

## Icon
1. [Gicon](/uploads/gicon.ico "Gicon")
2. [Gred](/uploads/gred.ico "Gred")
3. [Hell](/uploads/hell.ico "Hell") 


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

### Application files
1. [Helphammer 2 0 0](/uploads/helphammer-2-0-0.exe "Helphammer 2 0 0")
2. [Helphammer 2 1 0](/uploads/helphammer-2-1-0.exe "Helphammer 2 1 0")
3. [Helphammer 2 2 1](/uploads/helphammer-2-2-1.exe "Helphammer 2 2 1")
4. [Recalhammer](/uploads/recalhammer.exe "Recalhammer")


