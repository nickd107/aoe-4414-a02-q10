# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km ...
#   converts llh to ecef frame

# Parameters: LLH coordinates
#   lat_deg:
#   lon_deg:
#   hae_km:

# Output: ECEF coordinates
# r_x_km
# r_y_km
# r_z_km
# Written by Nick Dickson

# import Python modules
import math # math module
import sys # argv

# constants
R_E_KM = 6378.1363
E_E    = 0.081819221456

## calculate demoninator
# (eccentricity, latitude in radians)
def calc_denom(ecc, lat_rad):
  return math.sqrt(1.0-ecc**2.0 * math.sin(lat_rad)**2.0)

# initialize script arguments
lat_deg = float('nan') 
lon_deg = float('nan') 
hae_km = float('nan') 

# parse script arguments
if len(sys.argv) == 4:
  lat_deg = float(sys.argv[1])
  lon_deg = float(sys.argv[2])
  hae_km = float(sys.argv[3])
else:
  print(\
    'Usage: '\
    'python3 llh_to_ecef.py lat_deg lon_deg hae_km'\
  )
  exit()

### script below this line ###

# calculate (Based on slides 2)
lat_rad = lat_deg*math.pi/180.0
lon_rad = lon_deg*math.pi/180.0
denom = calc_denom(E_E, lat_rad)
C_E = R_E_KM/denom
S_E = (R_E_KM*(1-E_E**2))/denom
r_x = (C_E+hae_km)*math.cos(lat_rad)*math.cos(lon_rad)
r_y = (C_E+hae_km)*math.cos(lat_rad)*math.sin(lon_rad)
r_z = (S_E+hae_km)*math.sin(lat_rad)

print('r_x_km= '+str(r_x))
print('r_y_km= '+str(r_y))
print('r_z_km= '+str(r_z))