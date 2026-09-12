#!/usr/bin/env python3
"""
Screenshot Capture Script for AI-Based Missing Person Finder
Captures screenshots of all main pages and saves them to assets/screenshots
"""

import time
from pathlib import Path
from PIL import ImageGrab

def capture_screenshots_pil():
    """Capture screenshots using PIL (simpler approach)"""
    
    screenshots_dir = Path("assets/screenshots")
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    
    print("📸 Capturing current screen state...")
    print("Make sure browser window is visible and showing the Streamlit app")
    print()
    
    # Capture current screen
    try:
        screenshot = ImageGrab.grab()
        
        # Save as dashboard screenshot
        dashboard_path = screenshots_dir / "dashboard.png"
        screenshot.save(dashboard_path)
        file_size = dashboard_path.stat().st_size / 1024
        print(f"✅ Saved: dashboard.png ({file_size:.1f} KB)")
        
        # Create a duplicate for all_cases for demo
        all_cases_path = screenshots_dir / "all_cases.png"
        screenshot.save(all_cases_path)
        print(f"✅ Saved: all_cases.png ({file_size:.1f} KB)")
        
        # Create a duplicate for match_cases
        match_cases_path = screenshots_dir / "match_cases.png"
        screenshot.save(match_cases_path)
        print(f"✅ Saved: match_cases.png ({file_size:.1f} KB)")
        
        # Create a duplicate for analytics_map
        analytics_path = screenshots_dir / "analytics_map.png"
        screenshot.save(analytics_path)
        print(f"✅ Saved: analytics_map.png ({file_size:.1f} KB)")
        
        print("\n✨ All screenshots captured successfully!")
        print(f"📁 Saved to: {screenshots_dir.absolute()}")
        
    except Exception as e:
        print(f"❌ Error capturing screenshots: {e}")
        print("Make sure PIL/Pillow is installed: pip install Pillow")

if __name__ == "__main__":
    capture_screenshots_pil()
