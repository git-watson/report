import os
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import pytz
import subprocess
import numpy as np
from PIL import Image

# Ensure the output directory exists
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)  # Creates directory if it doesn't exist

# ✅ Generate report.bin (Better Text Clarity)
input_file = os.path.join(output_dir, "report.png")
output_file_bin = os.path.join(output_dir, "report.bin")

# Open image and convert to grayscale
img = Image.open(input_file).convert("L")  

# Resize to fit the e-paper display
img = img.resize((400, 300), Image.Resampling.LANCZOS)

# **🛠 Improved Thresholding**
# - Use a slightly softer threshold (around 140 instead of 128)
# - This helps keep small text details from disappearing
threshold = 140
img = img.point(lambda p: 255 if p > threshold else 0)  
img = img.convert("1")  # Convert to 1-bit (pure black & white)

# Convert image to binary format
pixels = np.array(img)
width, height = img.size

byte_array = bytearray()

for y in range(height):
	for x in range(0, width, 8):
		byte = 0
		for bit in range(8):
			if x + bit < width:
				byte |= (1 if pixels[y, x + bit] == 0 else 0) << (7 - bit)
		byte_array.append(byte)

# Save to .bin file
with open(output_file_bin, "wb") as f:
	f.write(byte_array)

print(f"✅ Binary file generated: {output_file_bin}")