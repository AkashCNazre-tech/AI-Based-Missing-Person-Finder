import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import time
import os

# Ensure screenshots directory exists
screenshots_dir = "assets/screenshots"
os.makedirs(screenshots_dir, exist_ok=True)

print("📸 Capturing screenshots from Streamlit app running at http://localhost:8501")
print("=" * 70)

# These are the 3 specific images the user wants - we'll refer to them
image_names = {
    "dashboard": "Home - Gagandeep Singh profile, case counts, India map",
    "register_new_case": "Register New Case - Face detection with person photo and green bounding box",  
    "view_submitted_cases": "View Submitted Cases - Case details with photo and edit/delete options"
}

print("\n✅ Screenshots needed:")
for key, desc in image_names.items():
    print(f"  • {key}.png - {desc}")

print("\n📝 Instructions to save your 3 images:")
print("=" * 70)
print("""
1. Take screenshots of your Streamlit app pages:
   - Screenshot 1: Home page (Gagandeep Singh dashboard)
   - Screenshot 2: Register New Case page (with face detection)
   - Screenshot 3: View Submitted Cases page (All Cases page)

2. Save them as PNG files with these exact names to: assets/screenshots/
   - dashboard.png
   - register_new_case.png
   - view_submitted_cases.png

3. Once saved, run this command to update README:
   python update_readme.py

4. Then commit and push:
   git add . && git commit -m "Update: Add proper screenshots to README" && git push origin main
""")

print("\n🔄 Alternatively, if you want automatic browser-based capture:")
print("=" * 70)
print("Install Selenium: pip install selenium")
print("Then use the browser_capture.py script\n")
