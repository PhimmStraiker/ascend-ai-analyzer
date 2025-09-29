#!/bin/bash

# Straiker Ascend AI Assessment Tool - GitHub Preparation Script
# This script prepares the project for GitHub repository creation

set -e  # Exit on any error

echo "🚀 Straiker Ascend AI Assessment Tool - GitHub Preparation"
echo "========================================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is required but not installed."
    echo "Please install Git and try again."
    exit 1
fi

echo "✅ Git found"

# Initialize git repository if not already initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

# Add all files to git
echo "📁 Adding files to Git..."
git add .

# Create initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Straiker Ascend AI Assessment Tool

- Complete dashboard with cyberpunk theme
- Interactive sunburst charts with drill-down
- Comprehensive security analysis features
- Full documentation and user guides
- Production-ready deployment configuration"

echo "✅ Initial commit created"

# Create a comprehensive project summary
cat > PROJECT_SUMMARY.md << EOF
# 🛡️ Straiker Ascend AI Assessment Tool - Project Summary

## 📊 Project Overview
A comprehensive cybersecurity assessment dashboard for analyzing AI model vulnerabilities and security controls. Built with a futuristic cyberpunk theme, this tool provides deep insights into AI security posture through interactive visualizations and detailed analysis.

## 🎯 Key Features
- **Interactive Dashboard**: Real-time security metrics and threat detection
- **Sunburst Charts**: Drill-down analysis of attack paths with metadata popups
- **Comprehensive Analysis**: Evasion techniques, control assessment, and risk scoring
- **Modern UI/UX**: Cyberpunk theme with Straiker branding
- **Production Ready**: Full deployment configuration and documentation

## 🏗️ Technical Stack
- **Frontend**: Dash (React-based), Plotly.js, Bootstrap
- **Backend**: Python Flask, Pandas, NumPy
- **Database**: SQLite (development), PostgreSQL (production)
- **Visualization**: Plotly Express, NetworkX
- **Styling**: Custom CSS with cyberpunk theme

## 📁 Project Structure
\`\`\`
ascend_ai_analyzer/
├── enhanced_dashboard.py      # Main dashboard application
├── config.py                  # Configuration settings
├── models.py                  # Data models and analysis logic
├── requirements.txt           # Python dependencies
├── setup.sh                   # Easy installation script
├── README.md                  # Comprehensive documentation
├── docs/                      # Detailed documentation
│   ├── USER_GUIDE.md         # User instructions
│   └── TECHNICAL_DOCS.md     # Technical documentation
├── data/                     # Data storage directory
├── reports/                  # Generated analysis reports
├── static/                   # Static assets (CSS, images)
└── .gitignore               # Git ignore rules
\`\`\`

## 🚀 Quick Start
1. **Setup**: Run \`./setup.sh\` for automatic installation
2. **Launch**: Run \`python enhanced_dashboard.py\`
3. **Access**: Open browser to \`http://localhost:8050\`

## 📚 Documentation
- **README.md**: Complete project overview and setup
- **docs/USER_GUIDE.md**: Detailed user instructions
- **docs/TECHNICAL_DOCS.md**: Technical implementation details

## 🔒 Security Features
- **Data Protection**: Encryption and secure data handling
- **Access Control**: Role-based permissions system
- **Audit Logging**: Comprehensive activity tracking
- **Input Validation**: Secure data processing

## 🎨 UI/UX Highlights
- **Cyberpunk Theme**: Futuristic design with neon accents
- **Straiker Branding**: Official logos and color scheme
- **Interactive Elements**: Hover effects and animations
- **Responsive Design**: Mobile and desktop optimized

## 📊 Analysis Capabilities
- **Evasion Detection**: AI attack technique identification
- **Control Assessment**: Security measure effectiveness
- **Risk Scoring**: Automated threat prioritization
- **Network Analysis**: Attack path visualization

## 🛠️ Development Ready
- **Version Control**: Git repository with proper structure
- **Documentation**: Comprehensive guides and API docs
- **Testing**: Unit and integration test framework
- **Deployment**: Production-ready configuration

## 📈 Future Enhancements
- **Machine Learning**: AI-powered threat detection
- **Real-time Monitoring**: Live security dashboards
- **API Integration**: RESTful API for external systems
- **Advanced Analytics**: Predictive security modeling

## 🤝 Team Collaboration
- **Code Standards**: PEP 8 Python style guide
- **Documentation**: Comprehensive technical docs
- **Testing**: Automated test suite
- **Security**: Best practices implementation

---
**Built with ❤️ by the Straiker Team**
*Empowering AI Security Through Advanced Analytics*
EOF

echo "✅ Project summary created"

# Create GitHub repository instructions
cat > GITHUB_SETUP.md << EOF
# 🚀 GitHub Repository Setup Instructions

## Creating the Repository

### Option 1: Using GitHub CLI (Recommended)
\`\`\`bash
# Install GitHub CLI if not already installed
# brew install gh  # macOS
# apt install gh   # Ubuntu

# Login to GitHub
gh auth login

# Create repository
gh repo create straiker-ascend-ai-analyzer --public --description "Straiker Ascend AI Assessment Tool - Cybersecurity dashboard for AI model vulnerability analysis"

# Add remote origin
git remote add origin https://github.com/YOUR_USERNAME/straiker-ascend-ai-analyzer.git

# Push to GitHub
git push -u origin main
\`\`\`

### Option 2: Using GitHub Web Interface
1. Go to https://github.com/new
2. Repository name: \`straiker-ascend-ai-analyzer\`
3. Description: \`Straiker Ascend AI Assessment Tool - Cybersecurity dashboard for AI model vulnerability analysis\`
4. Set to Public
5. Don't initialize with README (we already have one)
6. Click "Create repository"
7. Follow the instructions to push existing repository

## Repository Settings

### Recommended Settings
- **Visibility**: Public (for open source) or Private (for internal use)
- **Issues**: Enabled
- **Wiki**: Disabled (using docs/ folder instead)
- **Projects**: Enabled
- **Discussions**: Enabled

### Branch Protection
- **Main branch**: Require pull request reviews
- **Status checks**: Require tests to pass
- **Restrictions**: Require up-to-date branches

## Team Collaboration

### Adding Team Members
1. Go to repository Settings → Manage access
2. Add collaborators with appropriate permissions
3. Set up team-based access control

### Workflow Setup
1. **Feature branches**: Create branches for new features
2. **Pull requests**: Review all changes before merging
3. **Issues**: Track bugs and feature requests
4. **Milestones**: Organize releases and major features

## Documentation

### README.md
- Comprehensive project overview
- Installation and setup instructions
- Usage examples and screenshots
- Contributing guidelines

### Documentation Structure
\`\`\`
docs/
├── USER_GUIDE.md         # End-user documentation
├── TECHNICAL_DOCS.md     # Developer documentation
└── API_REFERENCE.md      # API documentation (future)
\`\`\`

## Security Considerations

### Sensitive Data
- **Never commit**: API keys, passwords, or sensitive data
- **Use .env files**: For environment-specific configuration
- **GitHub Secrets**: For CI/CD pipeline secrets

### Access Control
- **Repository permissions**: Appropriate team access levels
- **Branch protection**: Prevent direct pushes to main
- **Code review**: Require reviews for all changes

## Continuous Integration

### GitHub Actions (Future)
\`\`\`yaml
# .github/workflows/ci.yml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: python -m pytest
\`\`\`

## Release Management

### Versioning
- **Semantic Versioning**: MAJOR.MINOR.PATCH
- **Release Notes**: Document changes in each release
- **Tags**: Create tags for releases

### Changelog
- **CHANGELOG.md**: Track all changes
- **Release Notes**: GitHub release descriptions
- **Migration Guides**: For breaking changes

## Monitoring and Analytics

### GitHub Insights
- **Traffic**: Repository views and clones
- **Contributors**: Team activity and contributions
- **Issues**: Bug tracking and feature requests

### Code Quality
- **Code scanning**: Automated security scanning
- **Dependency review**: Monitor for vulnerabilities
- **Code coverage**: Track test coverage

---

**Ready for GitHub! 🚀**
EOF

echo "✅ GitHub setup instructions created"

# Show current status
echo ""
echo "📊 Repository Status:"
echo "===================="
git status --short

echo ""
echo "📁 Files ready for GitHub:"
echo "=========================="
find . -type f -name "*.py" -o -name "*.md" -o -name "*.txt" -o -name "*.sh" -o -name "*.json" | grep -v __pycache__ | sort

echo ""
echo "🎉 GitHub preparation completed!"
echo ""
echo "📋 Next steps:"
echo "1. Review the files and make any final changes"
echo "2. Run: ./prepare_github.sh (this script)"
echo "3. Follow instructions in GITHUB_SETUP.md"
echo "4. Push to GitHub: git push -u origin main"
echo ""
echo "📚 Documentation created:"
echo "- README.md: Complete project overview"
echo "- docs/USER_GUIDE.md: User instructions"
echo "- docs/TECHNICAL_DOCS.md: Technical docs"
echo "- GITHUB_SETUP.md: GitHub setup instructions"
echo ""
echo "🛡️  Straiker Ascend AI Assessment Tool is ready for GitHub!"
