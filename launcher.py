#!/usr/bin/env python
"""Smart launcher for HDP PREDICTOR that finds an available port"""
import socket
import subprocess
import sys
import os

def find_available_port(start_port=8501, max_attempts=100):
    """Find an available port starting from start_port"""
    port = start_port
    
    for attempt in range(max_attempts):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                s.listen(1)
                return port
        except OSError:
            port += 1
    
    raise RuntimeError(f"Could not find an available port after {max_attempts} attempts")

def kill_port_process(port):
    """Kill any process using the specified port on Windows"""
    if sys.platform == "win32":
        try:
            os.system(f"netstat -ano | findstr :{port} >nul && taskkill /IM python.exe /F >nul 2>&1")
        except:
            pass

if __name__ == '__main__':
    # Try multiple times to find a port
    port = find_available_port()
    
    print("=" * 70)
    print("🏥 HDP PREDICTOR - Maternal Health Risk Prediction System")
    print("=" * 70)
    print(f"\n✅ Port {port} is available")
    print(f"🚀 Starting HDP PREDICTOR on port {port}...")
    print(f"📱 Access the app at: http://localhost:{port}")
    print("\n⏳ Initializing... (this may take 30-60 seconds)")
    print("-" * 70)
    
    # Run streamlit with the found port
    try:
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'app.py',
            '--server.port', str(port),
            '--server.headless', 'true'
        ])
    except KeyboardInterrupt:
        print("\n\n✋ Application stopped by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
