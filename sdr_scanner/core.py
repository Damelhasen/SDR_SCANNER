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


#####INITS########


####FUNCTIONS#####

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
    step = int(step)
    scanned_frequencies = []

    sdr_device.center_freq = (freq_start*10**6)

    for i in range(freq_start, freq_end, step):
        sdr_device.center_freq = (i*10**6)
        sleep(step_time)
        scanned_frequencies.append({i: sdr_device.read_samples(256*1024)})
    return scanned_frequencies
        
        
##################
def main():
    SDR_SELECTION = input("Select SDR Device (1 for RTL-SDR, 2 for Airspy): ")
    if SDR_SELECTION == '1':
        sdr_device = sdr()

    sdr_device.sample_rate = 2.4e6
    sdr_device.center_freq = 98.6e6
    sdr_device.gain = 'auto'

    temp_scan = scanner(sdr_device, 98.6, 108.0, 1.0, .5)
    print(temp_scan)
    write("sdr_scanner\Scanned_Frquencies.txt" , temp_scan)
        


if __name__ == "__main__":
    main()


        


 