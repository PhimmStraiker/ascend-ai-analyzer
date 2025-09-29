#!/bin/bash

# Ascend AI Analyzer - Quick Start Script
echo "🚀 Starting Ascend AI Analysis"
echo "=================================================="

# Check if we're in the right directory
if [ ! -f "analyze_data.py" ]; then
    echo "❌ Error: Please run this script from the ascend_ai_analyzer directory"
    exit 1
fi

# Setup environment
echo "📦 Setting up environment..."
python setup.py

# Run the analysis
echo "🔍 Running comprehensive analysis..."
python analyze_data.py

# Check if analysis was successful
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Analysis completed successfully!"
    echo ""
    echo "📊 Next steps:"
    echo "1. View reports in the 'reports/' directory"
    echo "2. Start web API: python app.py"
    echo "3. Start dashboard: python dashboard.py"
    echo ""
    echo "🌐 Web interfaces:"
    echo "   API: http://localhost:8000"
    echo "   Dashboard: http://localhost:8050"
else
    echo "❌ Analysis failed. Check the error messages above."
    exit 1
fi
