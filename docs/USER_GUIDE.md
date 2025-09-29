# 📖 Straiker Ascend AI Assessment Tool - User Guide

## 🎯 Getting Started

### First Time Setup
1. **Launch the Application**
   - Run `python enhanced_dashboard.py`
   - Open your browser to `http://localhost:8050`
   - You'll see the Straiker cyberpunk-themed dashboard

2. **Navigate the Interface**
   - Use the tabs at the top to switch between different analysis views
   - Each tab provides different insights into your AI security posture

## 🔬 Overview Tab - Your Security Dashboard

### Key Metrics
- **Total Assessments**: Number of security tests performed
- **Pass Rate**: Percentage of successful security controls
- **Threat Level**: Current risk assessment
- **Active Controls**: Number of security measures in place

### Understanding the Data
- **Green Indicators**: Healthy security posture
- **Yellow Indicators**: Moderate risk, attention needed
- **Red Indicators**: High risk, immediate action required

## ⚡ Evasion Analysis Tab - Understanding AI Attacks

### What You'll See
- **Evasion Techniques**: Methods attackers use to bypass AI security
- **Success Rates**: How often each technique works
- **Impact Analysis**: Which techniques cause the most damage

### How to Use
1. **Browse Techniques**: Scroll through the list of evasion methods
2. **Click for Details**: Click on any technique to see detailed information
3. **Filter Results**: Use the search box to find specific techniques
4. **Export Data**: Download filtered results for further analysis

### Common Evasion Techniques
- **Role Playing**: Attackers pretend to be different personas
- **Authority Endorsement**: Using fake credentials
- **Prompt Injection**: Inserting malicious code into prompts
- **Social Engineering**: Manipulating human psychology

## 🛡️ Control Analysis Tab - Security Measures

### Control Groups
- **Data Leakage Prevention**: Controls that stop information leaks
- **Harmful Content Filtering**: Blocks dangerous or inappropriate content
- **Application Grounding**: Keeps AI responses within safe boundaries

### Understanding Control Effectiveness
- **Pass Rate**: Percentage of times controls work correctly
- **Failure Analysis**: Why controls sometimes fail
- **Improvement Recommendations**: How to strengthen weak controls

### Using the Control Analysis
1. **Review Control Performance**: See which controls are working well
2. **Identify Weaknesses**: Look for controls with high failure rates
3. **Click for Details**: Get specific information about control failures
4. **Plan Improvements**: Use the data to strengthen your security

## 🎯 Attack Paths Tab - Visual Threat Analysis

### The Sunburst Chart
This is the most powerful feature of the dashboard. It shows how different attack methods combine to create security risks.

#### How to Navigate
1. **Center (Base Prompt)**: Click to see overall attack landscape
2. **Second Ring (Evasion Techniques)**: Click to see specific attack methods
3. **Third Ring (Controls)**: Click to see how controls respond to attacks

#### Understanding the Visualization
- **Size of Segments**: Larger segments = more common attacks
- **Color Coding**: Different colors represent different risk levels
- **Interactive Drill-down**: Click segments to explore deeper

#### Getting Detailed Information
1. **Click on Third Ring**: This is where you get the most detailed information
2. **Metadata Window**: Shows specific examples of attacks and responses
3. **Export Options**: Save detailed analysis for reports

### Network Analysis
- **Attack Correlations**: How different attacks relate to each other
- **Control Interactions**: How security controls work together
- **Risk Patterns**: Identify common attack sequences

## 📡 Data Upload Tab - Adding New Information

### Supported File Types
- **CSV Files**: Comma-separated data files
- **JSON Files**: Structured data format
- **Excel Files**: Microsoft Excel spreadsheets

### Upload Process
1. **Select File**: Choose your data file
2. **Validate Data**: System checks data quality
3. **Preview**: Review data before importing
4. **Import**: Add data to the analysis

### Data Requirements
Your data should include these columns:
- `control_id`: Name of the security control
- `status`: Whether the control passed or failed
- `evasions_applied`: Which attack techniques were used
- `score`: Numerical assessment score

## 🔍 Advanced Features

### Filtering and Search
- **Global Search**: Find specific information across all data
- **Column Filters**: Filter data by specific criteria
- **Date Ranges**: Analyze data from specific time periods
- **Status Filters**: Focus on specific types of results

### Exporting Data
- **CSV Export**: Download filtered data for external analysis
- **PDF Reports**: Generate comprehensive security reports
- **JSON Export**: Export data for integration with other tools

### Customization
- **View Preferences**: Adjust how data is displayed
- **Column Selection**: Choose which data columns to show
- **Sorting Options**: Organize data by different criteria

## 📊 Understanding Your Results

### Security Metrics
- **Overall Score**: Your general security posture (0-100)
- **Risk Level**: Low, Medium, High, or Critical
- **Trends**: Whether security is improving or declining
- **Benchmarks**: How you compare to industry standards

### Action Items
- **Immediate Actions**: Critical issues that need immediate attention
- **Short-term Goals**: Issues to address within 30 days
- **Long-term Strategy**: Ongoing security improvements

### Reporting
- **Executive Summary**: High-level overview for leadership
- **Technical Details**: In-depth analysis for security teams
- **Compliance Reports**: Documentation for audits and certifications

## 🚨 Troubleshooting Common Issues

### Dashboard Won't Load
1. **Check Browser**: Use Chrome, Firefox, Safari, or Edge
2. **Clear Cache**: Refresh the page or clear browser cache
3. **Check URL**: Make sure you're using `http://localhost:8050`

### Data Not Showing
1. **Check File Format**: Ensure your data file is in the correct format
2. **Verify Data**: Make sure required columns are present
3. **Try Different File**: Test with a sample data file

### Slow Performance
1. **Close Other Tabs**: Reduce browser memory usage
2. **Check Data Size**: Large datasets may take longer to load
3. **Refresh Page**: Sometimes a simple refresh helps

### Can't Click on Charts
1. **Wait for Loading**: Charts may take a moment to become interactive
2. **Check Browser**: Some older browsers may not support all features
3. **Try Different Browser**: Test with a different web browser

## 💡 Best Practices

### Regular Analysis
- **Weekly Reviews**: Check for new security issues
- **Monthly Reports**: Generate comprehensive security reports
- **Quarterly Assessments**: Deep dive into security posture

### Data Management
- **Regular Backups**: Keep copies of your analysis data
- **Version Control**: Track changes to your security configurations
- **Documentation**: Keep notes about security decisions and changes

### Team Collaboration
- **Share Insights**: Use the export features to share findings
- **Document Findings**: Keep records of security analysis
- **Follow Up**: Track progress on security improvements

## 📞 Getting Help

### Self-Service Resources
- **Tooltip Help**: Hover over elements for quick explanations
- **Context Menus**: Right-click for additional options
- **Help Icons**: Look for question mark icons for guidance

### Support Channels
- **Documentation**: Check this user guide and README
- **Technical Support**: Contact your IT team for technical issues
- **Training**: Request additional training sessions

### Feedback
- **Report Issues**: Let us know if you find bugs or problems
- **Suggest Improvements**: Share ideas for making the tool better
- **Share Success Stories**: Tell us how the tool helps your security

---

**Remember**: This tool is designed to help you understand and improve your AI security posture. Take time to explore all the features and don't hesitate to ask for help when needed!
