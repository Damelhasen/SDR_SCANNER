"""Author : Johan Sheby
   Date : 23/06/2025
   Project : Multipurpose SDR CLI Toolkit
"""
######IMPORTS#####
import os
from time import sleep, time
from rtlsdr import RtlSdr as sdr 
import numpy as np
import math 
import json
import matplotlib.pyplot as plt

#####INITS########


####FUNCTIONS#####


def clear_terminal():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    

def write(file_path:str , write_material) :
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(write_material)


def listen_freq(sdr_device, freq: float):
    """
    Function to listen to a specific frequency using the selected SDR device.

    Parameters:
    sdr_device: The SDR device instance
    freq (float): The frequency to listen to in   Mhz
    """
    
    sdr_device.center_freq = (freq*10**6)


    samples = sdr_device.read_samples(256*1024)

    return samples
   

def scanner(sdr_device, freq_start: float, freq_end: float, step: float , step_time:float):
    """
    Function to scan a range of frequencies using selected SDR device """
    
    freq_start = int(freq_start) 
    freq_end = int(freq_end)
    
    results = {}

    sdr_device.center_freq = (freq_start*10**6)

    
    for freq in np.arange(freq_start, freq_end+step, step):
        freq = round(freq, 1)
        sleep(step_time)
        samples = sdr_device.read_samples(256*1024)
        power = np.mean(np.abs(samples) ** 2)
        db = 10 * np.log10(power + 1e-10)
        results[freq] = db
        
    return results
def plot(data_sourcefile : str) :

 with open(data_sourcefile , 'r') as f :
     data = json.load(f)
     frequencies = sorted([float(freq) for freq in data.keys()])
     db_values = [data[str(f)] for f in frequencies]
     plt.figure(figsize = (12,16))

     plt.plot(frequencies, db_values, 'b-o', linewidth=2, markersize=6)
     plt.xlabel('Frequency (MHz)')
     plt.ylabel('Power (dB)')
     plt.title('SDR Frequency Scan')
     plt.grid(True, alpha=0.3)
     plt.tight_layout()
     plt.show()


        
##################
def main():
    SDR_SELECTION = input("Select SDR Device (1 for RTL-SDR, 2 for Airspy): ")
    if SDR_SELECTION == '1':
        sdr_device = sdr()

    sdr_device.sample_rate = 2.4e6
    sdr_device.center_freq = 98.6e6
    sdr_device.gain = 'auto'
    
    clear_terminal()

    freq_start_selection = float(input("Input start frequency (Mhz) :  "))
    clear_terminal()
    end_freq_selection = float(input("Input End frequency (Mhz) : "))
    clear_terminal()
    freq_step_selection = float(input("Input step frequency (Mhz) : "))
    clear_terminal()
    step_time_selection = float(input("Input step time (Seconds) : "))
    clear_terminal()
    clear_terminal()
    filenameinput = str(input("What Should the result File Called ? : "))
    clear_terminal()
    
    print(f"startiong Scan from {freq_start_selection} to {end_freq_selection}")
    scan_result = scanner(sdr_device,freq_start_selection,end_freq_selection, freq_step_selection, step_time_selection)
    clear_terminal()
    
    write(f"sdr_scanner/{filenameinput}.json", json.dumps(scan_result, indent=2))
    
    print(f"Result saved to '{filenameinput}.json' ")
    plot(f"sdr_scanner/{filenameinput}.json")

if __name__ == "__main__":
    main()


        


 