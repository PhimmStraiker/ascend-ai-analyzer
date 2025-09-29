# 🛡️ Straiker Ascend AI Assessment Tool

A comprehensive cybersecurity assessment dashboard for analyzing AI model vulnerabilities and security controls. Built with a futuristic cyberpunk theme, this tool provides deep insights into AI security posture through interactive visualizations and detailed analysis.

## 🚀 Features

### 📊 Interactive Dashboard
- **Real-time Analytics**: Live security metrics and threat detection
- **Interactive Sunburst Charts**: Drill-down analysis of attack paths
- **Dynamic Visualizations**: Heatmaps, network graphs, and trend analysis
- **Responsive Design**: Optimized for desktop and mobile viewing

### 🔍 Analysis Capabilities
- **Evasion Technique Analysis**: Comprehensive breakdown of AI evasion methods
- **Control Group Assessment**: Security control effectiveness evaluation
- **Attack Path Visualization**: Interactive network analysis of threat vectors
- **Risk Scoring**: Automated risk assessment and prioritization

### 🎨 Modern UI/UX
- **Cyberpunk Theme**: Futuristic design with neon accents and animations
- **Straiker Branding**: Official Straiker logo and color scheme
- **Intuitive Navigation**: Easy-to-use tabbed interface
- **Accessibility**: High contrast and readable typography

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd ascend_ai_analyzer
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

4. **Run the Application**
   ```bash
   python enhanced_dashboard.py
   ```

5. **Access the Dashboard**
   Open your browser and navigate to: `http://localhost:8050`

## 📖 Usage Guide

### Dashboard Navigation

#### 🔬 Overview Tab
- **Security Metrics**: High-level security posture indicators
- **Threat Summary**: Current threat landscape overview
- **Performance Indicators**: System health and response metrics

#### ⚡ Evasion Analysis Tab
- **Evasion Techniques**: Detailed breakdown of AI evasion methods
- **Success Rates**: Effectiveness metrics for different techniques
- **Trend Analysis**: Historical evasion pattern analysis
- **Interactive Tables**: Click to drill down into specific techniques

#### 🛡️ Control Analysis Tab
- **Security Controls**: Comprehensive control group analysis
- **Failure Rates**: Control effectiveness metrics
- **Risk Assessment**: Control failure impact analysis
- **Recommendations**: Actionable security improvements

#### 🎯 Attack Paths Tab
- **Network Visualization**: Interactive sunburst charts
- **Path Analysis**: Click on segments to explore attack vectors
- **Metadata Drill-down**: Detailed information on specific paths
- **Risk Correlation**: Cross-reference evasion and control failures

#### 📡 Data Upload Tab
- **File Upload**: Import new assessment data
- **Data Validation**: Automatic data quality checks
- **Format Support**: CSV, JSON, and Excel file formats
- **Batch Processing**: Handle large datasets efficiently

### Interactive Features

#### Sunburst Chart Navigation
1. **First Ring (Center)**: Base prompt analysis
2. **Second Ring**: Evasion technique breakdown
3. **Third Ring**: Control-specific analysis (click for metadata)

#### Data Tables
- **Sortable Columns**: Click headers to sort data
- **Filtering**: Use search boxes to filter results
- **Export**: Download filtered data as CSV
- **Pagination**: Navigate through large datasets

#### Modal Windows
- **Detailed Views**: Click table rows for detailed information
- **Metadata Display**: Comprehensive data about specific records
- **Export Options**: Save detailed reports

## 🔧 Configuration

### Environment Variables
```bash
# Database Configuration
DATABASE_URL=sqlite:///ascend_ai_analyzer.db

# Security Settings
SECRET_KEY=your-secret-key-here
DEBUG_MODE=false

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=logs/dashboard.log
```

### Customization Options
- **Theme Colors**: Modify CSS variables in the dashboard
- **Logo Replacement**: Update logo files in the static directory
- **Data Sources**: Configure database connections in config.py
- **Analysis Parameters**: Adjust thresholds in models.py

## 📁 Project Structure

```
ascend_ai_analyzer/
├── enhanced_dashboard.py      # Main dashboard application
├── config.py                  # Configuration settings
├── models.py                  # Data models and analysis logic
├── requirements.txt           # Python dependencies
├── README.md                  # This documentation
├── data/                      # Data storage directory
├── reports/                   # Generated analysis reports
├── static/                    # Static assets (CSS, images)
├── Straiker-white.png         # Straiker logo
├── Red Ascend Shield.png      # Ascend AI shield icon
└── logo_data.py              # Base64 encoded logo data
```

## 🚀 Deployment

### Local Development
```bash
python enhanced_dashboard.py
```

### Production Deployment
```bash
# Using Gunicorn (recommended)
gunicorn -w 4 -b 0.0.0.0:8050 enhanced_dashboard:app

# Using Docker
docker build -t ascend-ai-analyzer .
docker run -p 8050:8050 ascend-ai-analyzer
```

### Environment Setup
- **Development**: Debug mode enabled, detailed logging
- **Production**: Optimized performance, error handling
- **Testing**: Automated test suite, coverage reports

## 🔒 Security Considerations

### Data Protection
- **Encryption**: All sensitive data encrypted at rest
- **Access Control**: Role-based permissions system
- **Audit Logging**: Comprehensive activity tracking
- **Data Retention**: Configurable data lifecycle management

### Best Practices
- **Regular Updates**: Keep dependencies current
- **Security Scanning**: Automated vulnerability detection
- **Access Monitoring**: Track user activities
- **Backup Strategy**: Regular data backups

## 🐛 Troubleshooting

### Common Issues

#### Dashboard Won't Start
```bash
# Check Python version
python --version

# Verify dependencies
pip list

# Check port availability
lsof -i :8050
```

#### Data Loading Errors
```bash
# Check data file format
file data/your_data.csv

# Verify database connection
python -c "import sqlite3; print('Database OK')"
```

#### Performance Issues
- **Memory Usage**: Monitor with `htop` or `top`
- **Database Optimization**: Check query performance
- **Caching**: Enable Redis for better performance

### Debug Mode
```bash
# Enable debug logging
export DEBUG=true
python enhanced_dashboard.py
```

## 📊 Data Format

### Input Data Structure
```json
{
  "id": "unique_identifier",
  "application_id": "app_123",
  "straiker_id": "straiker_456",
  "assessment_id": "assessment_789",
  "control_id": "control_name",
  "batch_id": "batch_001",
  "timestamp": "2024-01-01T00:00:00Z",
  "score": 0.85,
  "status": "pass|fail|unknown",
  "evasions_applied": ["technique1", "technique2"],
  "base_prompt": "Original prompt text",
  "explanation": "Detailed analysis"
}
```

### Supported File Formats
- **CSV**: Comma-separated values
- **JSON**: JavaScript Object Notation
- **Excel**: Microsoft Excel files (.xlsx)
- **SQLite**: Local database files

## 🤝 Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Submit a pull request

### Code Standards
- **Python**: Follow PEP 8 style guide
- **Documentation**: Update README for new features
- **Testing**: Maintain test coverage above 80%
- **Security**: Follow security best practices

## 📞 Support

### Documentation
- **User Guide**: Comprehensive usage instructions
- **API Reference**: Technical documentation
- **FAQ**: Frequently asked questions
- **Video Tutorials**: Step-by-step guides

### Contact Information
- **Technical Support**: support@straiker.com
- **Documentation**: docs@straiker.com
- **Security Issues**: security@straiker.com

## 📄 License

This project is proprietary software owned by Straiker. All rights reserved.

## 🏆 Acknowledgments

- **Straiker Team**: Core development and design
- **Comcast Partnership**: Requirements and testing
- **Open Source Community**: Libraries and frameworks used

---

**Built with ❤️ by the Straiker Team**

*Empowering AI Security Through Advanced Analytics*