# **SDRScan**
**by Johan Sheby**

---
SDRSCan is a simple python program that lets you automatically scan through large radio spectrums and bands using an Software Defined Radio .



# Features
SDRScan features two modes of scanning , custom where you are able to input the : 
* Start frequency
* End frequency
* Step Frequency
* Step Length (seconds)

and band mode where you are able to select pre programed frquency ranges : 
* FM
* AM
* Aviation
* Maritime

# Hardware Support
This program currently only supports RTL-SDRS (Tested with the [ RTL-SDR V4](https://www.rtl-sdr.com/rtl-sdr-blog-v4-end-of-line/))
Airspy and Noolec Support : Maybe :man-shrugging: 

# Installation
1. Ensure Proper Drivers are installed (refer [here](https://www.rtl-sdr.com/rtl-sdr-quick-start-guide/))

```
pip install sdr-scanner
##PLEASE ENSURE YOUR RTL_SDR IS PLUGGED IN BEFORE RUNNING NEXT COMMAND
sdr-scanner
```
# AI Use 

AI Has been used in this project to : 
* Set up folder structure for PyPi
* Autofill
* Repetive copy pasting 
* Running Tests 
* Troubleshooting drivers 

#Links
https://pypi.org/project/sdr-scanner/1.0.1/
