#!/usr/bin/env python3
"""
Seller Risk MLOps Platform Demo Launcher
========================================

This script launches the interactive Streamlit demo for the Seller Risk MLOps Platform.
It provides an easy way to start the application with proper configuration and helpful information.
"""

import os
import sys
import subprocess
import webbrowser
import time
from pathlib import Path

def print_banner():
    """Print the demo banner with platform information"""
    banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    🛡️  SELLER RISK MLOPS PLATFORM DEMO                      ║
║                                                                              ║
║  Interactive Streamlit Demo - Comprehensive MLOps Platform Visualization    ║
║  Built for Walmart's Seller Risk Management Team                            ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required.")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]} (Compatible)")

def check_dependencies():
    """Check if required dependencies are installed"""
    required_packages = [
        'streamlit',
        'plotly', 
        'pandas',
        'numpy'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}: Installed")
        except ImportError:
            missing_packages.append(package)
            print(f"❌ {package}: Missing")
    
    if missing_packages:
        print("\n🔧 Installing missing dependencies...")
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
            ])
            print("✅ Dependencies installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies. Please run manually:")
            print("   pip install -r requirements.txt")
            sys.exit(1)

def print_demo_info():
    """Print demo information and features"""
    info = """
🚀 PLATFORM FEATURES:
   • Multi-Persona Dashboards (Data Scientist, MLOps Engineer, Risk Ops, Executive)
   • Interactive Workflow Visualization with 4 deployment flows
   • Real-time Performance Simulation (<50ms latency, 100K+ TPS)
   • Natural Language Strategy Interface
   • Comprehensive Fraud Detection Monitoring

📊 KEY METRICS DEMONSTRATED:
   • 89.7% Fraud Prevention Rate
   • $2.4M Cost Savings (Quarterly)
   • 340% ROI on MLOps Investment
   • 67% Faster Time-to-Market
   • 99.95% System Uptime

🎯 DEMO SCENARIOS:
   1. Platform Overview - Start here for system-wide metrics
   2. Data Scientist - Experiment tracking and model development
   3. MLOps Engineer - Deployment pipelines and infrastructure
   4. Risk Operations - Real-time fraud monitoring and strategy
   5. Executive - Strategic KPIs and business impact
   6. Workflow Visualization - Interactive deployment simulation

🔧 NAVIGATION:
   • Use the sidebar to switch between different views
   • Click persona buttons to experience role-based dashboards
   • Try interactive features like model testing and strategy creation
   • Monitor real-time metrics that update every 3 seconds
    """
    print(info)

def launch_streamlit():
    """Launch the Streamlit application"""
    print("🚀 Starting Streamlit application...")
    print("   URL: http://localhost:8501")
    print("   Press Ctrl+C to stop the server")
    print("   The browser will open automatically in 3 seconds...")
    
    # Start Streamlit in a subprocess
    try:
        # Wait a moment then open browser
        time.sleep(3)
        webbrowser.open('http://localhost:8501')
        
        # Start Streamlit
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'app.py',
            '--server.port=8501',
            '--server.address=localhost',
            '--browser.gatherUsageStats=false'
        ])
        
    except KeyboardInterrupt:
        print("\n\n👋 Demo stopped. Thank you for exploring the Seller Risk MLOps Platform!")
    except Exception as e:
        print(f"\n❌ Error starting Streamlit: {e}")
        print("   Try running manually: streamlit run app.py")

def main():
    """Main demo launcher function"""
    print_banner()
    
    # Check system requirements
    print("🔍 Checking system requirements...")
    check_python_version()
    
    # Verify we're in the right directory
    if not Path('app.py').exists():
        print("❌ Error: app.py not found. Please run this script from the project directory.")
        sys.exit(1)
    
    print("✅ Project directory: Correct")
    
    # Check and install dependencies
    print("\n📦 Checking dependencies...")
    check_dependencies()
    
    # Print demo information
    print_demo_info()
    
    # Prompt to continue
    input("\n🎬 Press Enter to start the demo (or Ctrl+C to cancel)...")
    
    # Launch the application
    launch_streamlit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Demo cancelled. Run again anytime with: python run_demo.py")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("   Please check the error and try again.")
        sys.exit(1)