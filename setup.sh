#!/bin/bash

# Straiker Ascend AI Assessment Tool - Setup Script
# This script sets up the development environment for the Ascend AI Analyzer

set -e  # Exit on any error

echo "🛡️  Straiker Ascend AI Assessment Tool - Setup"
echo "=============================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    echo "Please install Python 3.8 or higher and try again."
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
REQUIRED_VERSION="3.8"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo "❌ Python $REQUIRED_VERSION or higher is required. Found: $PYTHON_VERSION"
    exit 1
fi

echo "✅ Python $PYTHON_VERSION found"

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install requirements
echo "📚 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p logs
mkdir -p data
mkdir -p reports
mkdir -p static/generated

# Set up environment file
if [ ! -f .env ]; then
    echo "⚙️  Creating environment file..."
    cat > .env << EOF
# Straiker Ascend AI Assessment Tool - Environment Configuration
DEBUG=true
LOG_LEVEL=INFO
DATABASE_URL=sqlite:///ascend_ai_analyzer.db
SECRET_KEY=$(python3 -c 'import secrets; print(secrets.token_hex(32))')
EOF
    echo "✅ Environment file created"
else
    echo "✅ Environment file already exists"
fi

# Check if data directory has sample data
if [ ! -f "data/sample_assessment.csv" ]; then
    echo "📊 Creating sample data..."
    cat > data/sample_assessment.csv << EOF
id,application_id,straiker_id,assessment_id,control_id,batch_id,timestamp,score,status,evasions_applied,base_prompt,explanation
sample_001,app_123,straiker_456,assessment_789,data_leakage,batch_001,2024-01-01T00:00:00Z,0.85,pass,"role_player,authority_endorsement","You are a helpful assistant","Control passed successfully"
sample_002,app_123,straiker_456,assessment_789,harmful_content,batch_001,2024-01-01T00:01:00Z,0.45,fail,"prompt_injection","You are a helpful assistant","Control failed - malicious content detected"
sample_003,app_123,straiker_456,assessment_789,app_grounding,batch_001,2024-01-01T00:02:00Z,0.92,pass,"social_engineering","You are a helpful assistant","Control passed with high confidence"
EOF
    echo "✅ Sample data created"
else
    echo "✅ Sample data already exists"
fi

# Test the installation
echo "🧪 Testing installation..."
python3 -c "
import dash
import plotly
import pandas
import sqlite3
print('✅ All dependencies imported successfully')
"

# Create a simple test script
cat > test_installation.py << EOF
#!/usr/bin/env python3
"""Test script to verify installation"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported"""
    try:
        import dash
        import plotly
        import pandas
        import sqlite3
        print("✅ All required modules imported successfully")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_database():
    """Test database connectivity"""
    try:
        import sqlite3
        conn = sqlite3.connect(':memory:')
        conn.execute('CREATE TABLE test (id INTEGER)')
        conn.close()
        print("✅ Database connectivity test passed")
        return True
    except Exception as e:
        print(f"❌ Database test failed: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Testing Straiker Ascend AI Assessment Tool installation...")
    
    success = True
    success &= test_imports()
    success &= test_database()
    
    if success:
        print("🎉 Installation test completed successfully!")
        print("You can now run: python enhanced_dashboard.py")
    else:
        print("❌ Installation test failed. Please check the errors above.")
        sys.exit(1)
EOF

python3 test_installation.py
rm test_installation.py

echo ""
echo "🎉 Setup completed successfully!"
echo ""
echo "📋 Next steps:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Run the dashboard: python enhanced_dashboard.py"
echo "3. Open your browser to: http://localhost:8050"
echo ""
echo "📚 Documentation:"
echo "- README.md: Overview and quick start"
echo "- docs/USER_GUIDE.md: Detailed user instructions"
echo "- docs/TECHNICAL_DOCS.md: Technical documentation"
echo ""
echo "🛡️  Straiker Ascend AI Assessment Tool is ready to use!"
