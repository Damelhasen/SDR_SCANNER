from rtlsdr import RtlSdr as sdr 


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


if __name__ == '__main__':
    # instantiate the SDR device, call listen, then close
    sdr_device = sdr()
    try:
        print(listen_freq(sdr_device, 98.6))
    finally:
        sdr_device.close()