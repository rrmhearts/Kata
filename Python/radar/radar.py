import numpy as np

def estimate_max_range(p_transmit_w, gain_db, freq_hz, rcs_m2, s_min_w):
    """
    Estimates the maximum detectable range of a radar system.
    
    Args:
        p_transmit_w (float): Peak transmitted power in Watts.
        gain_db (float): Antenna gain in decibels (dBi).
        freq_hz (float): Operating frequency in Hertz.
        rcs_m2 (float): Radar Cross Section of the target in square meters.
        s_min_w (float): Minimum detectable signal (sensitivity) in Watts.
        
    Returns:
        float: Maximum range in meters.
    """
    # Constants
    c = 3e8  # Speed of light
    wavelength = c / freq_hz
    
    # Convert Gain from dB to linear scale
    gain_linear = 10**(gain_db / 10)
    
    # Radar Range Equation solved for R
    numerator = p_transmit_w * (gain_linear**2) * (wavelength**2) * rcs_m2
    denominator = ((4 * np.pi)**3) * s_min_w
    
    max_range = (numerator / denominator)**(0.25)
    
    return max_range

def estimate_rcs(shape, dimensions, freq_hz):
    """
    Estimates RCS for simple geometric shapes.
    
    Args:
        shape (str): 'sphere', 'plate', or 'cylinder'
        dimensions (dict): Necessary dimensions (radius, length, area)
        freq_hz (float): Operating frequency
    """
    c = 3e8
    wavelength = c / freq_hz
    
    if shape == 'sphere':
        # r = dimensions['radius']
        return np.pi * (dimensions['radius']**2)
    
    elif shape == 'plate':
        # area = dimensions['area']
        return (4 * np.pi * (dimensions['area']**2)) / (wavelength**2)
    
    elif shape == 'cylinder':
        # r = dimensions['radius'], l = dimensions['length']
        r, l = dimensions['radius'], dimensions['length']
        return (2 * np.pi * r * (l**2)) / wavelength
    
    else:
        return None

if __name__ == "__main__":
    # Example: RCS of a 1m^2 flat metal plate at 10GHz
    plate_rcs = estimate_rcs('plate', {'area': 1.0}, 10e9)
    print(f"RCS of Flat Plate: {plate_rcs:.2f} m^2 ({10*np.log10(plate_rcs):.2f} dBsm)")

    # Example Usage:
    # 50kW transmitter, 35dBi gain, 10GHz frequency, 1m^2 target, -100dBm sensitivity
    sensitivity_watts = 10**(-100 / 10) * 0.001 # Convert -100 dBm to Watts
    r_max = estimate_max_range(50000, 35, 10e9, 1.0, sensitivity_watts)

    print(f"Maximum Detection Range: {r_max / 1000:.2f} km")