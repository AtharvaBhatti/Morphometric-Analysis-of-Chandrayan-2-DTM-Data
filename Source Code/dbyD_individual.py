import rasterio
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

# 1) Load the DTM
dtm_path = r'D:\CV\run\crater_outputs\crater_6_dtm.tif'
with rasterio.open(dtm_path) as src:
    dtm = src.read(1)
    transform = src.transform

# 2) Lunar‐meters per degree at your crater latitude
R = 1_737_400  # lunar radius in meters
phi_center = 9.254512  # your crater center latitude in degrees
m_per_deg_lat = 2 * np.pi * R / 360
m_per_deg_lon = m_per_deg_lat * np.cos(np.deg2rad(phi_center))

# 3) Pixel size in meters
dx_m = transform.a * m_per_deg_lon
dy_m = -transform.e * m_per_deg_lat

# 4) Extract a horizontal profile through the center row
row = dtm.shape[0] // 2
profile = dtm[row, :]

# 5) Build a distance axis in meters
distance = np.arange(profile.size) * dx_m

# 6) Smooth profile and find rim & bottom indices
smoothed = gaussian_filter1d(profile, sigma=3)
min_idx   = np.argmin(smoothed)
left_rc   = np.argmax(smoothed[:min_idx])
right_rc  = np.argmax(smoothed[min_idx:]) + min_idx

# 7) Compute diameter (D), depth (d), and ratio d/D
D = distance[right_rc] - distance[left_rc]                     # rim-to-rim in meters
d = smoothed[[left_rc, right_rc]].mean() - smoothed[min_idx]    # mean rim elevation minus bottom

d_over_D = d / D

# 8) Print the results
print(f"Diameter (D) = {D:.1f} m")
print(f"Depth    (d) = {d:.1f} m")
print(f"d/D         = {d_over_D:.3f}")

# 9) (Optional) Plot the profile
plt.figure(figsize=(10,5))
plt.plot(distance, smoothed, label='Smoothed Elevation')
plt.scatter(distance[[left_rc, right_rc]], smoothed[[left_rc, right_rc]], c='red', label='Rims (Rc)')
plt.scatter(distance[min_idx], smoothed[min_idx], c='blue', label='Crater Bottom')
plt.title(f'Crater Profile: D≈{D:.1f} m, d≈{d:.1f} m, d/D≈{d_over_D:.3f}')
plt.xlabel('Distance (m)')
plt.ylabel('Elevation (m)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
