# 🔧 Straiker Ascend AI Assessment Tool - Technical Documentation

## 🏗️ Architecture Overview

### System Components
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Data Layer    │
│   (Dash/React)  │◄──►│   (Flask)       │◄──►│   (SQLite)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Visualization │    │   Analysis      │    │   Storage       │
│   (Plotly)      │    │   Engine        │    │   (Files)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Technology Stack
- **Frontend**: Dash (React-based), Plotly.js, Bootstrap
- **Backend**: Python Flask, Pandas, NumPy
- **Database**: SQLite (development), PostgreSQL (production)
- **Visualization**: Plotly Express, NetworkX
- **Styling**: Custom CSS, Bootstrap Darkly theme

## 📁 Code Structure

### Core Files
```
enhanced_dashboard.py          # Main application entry point
├── CSS Styling (lines 16-294)     # Custom cyberpunk theme
├── Data Loading (lines 295-376)    # Database and file operations
├── Layout Definition (lines 377-430) # UI component structure
├── Callback Functions (lines 431-2000+) # Interactive functionality
└── Server Configuration (lines 2000+) # Flask/Dash server setup
```

### Key Components

#### 1. Data Models (`models.py`)
```python
class SecurityAssessment:
    """Core data model for security assessments"""
    - id: str
    - application_id: str
    - control_id: str
    - status: str
    - score: float
    - evasions_applied: List[str]
    - timestamp: datetime
```

#### 2. Configuration (`config.py`)
```python
class Config:
    """Application configuration settings"""
    - DATABASE_URL: str
    - DEBUG_MODE: bool
    - LOG_LEVEL: str
    - SECRET_KEY: str
```

#### 3. Analysis Engine
- **Evasion Detection**: Identifies AI evasion techniques
- **Control Assessment**: Evaluates security control effectiveness
- **Risk Scoring**: Calculates threat levels and priorities
- **Network Analysis**: Maps attack paths and correlations

## 🔄 Data Flow

### 1. Data Ingestion
```
Raw Data → Validation → Transformation → Storage
    ↓           ↓            ↓           ↓
CSV/JSON → Schema Check → Normalize → SQLite
```

### 2. Analysis Pipeline
```
Stored Data → Feature Extraction → Analysis → Visualization
     ↓              ↓                ↓           ↓
   SQLite → Pandas Processing → Algorithms → Plotly Charts
```

### 3. Interactive Updates
```
User Action → Callback Trigger → Data Query → UI Update
     ↓              ↓              ↓           ↓
   Click → Dash Callback → Database → Chart Refresh
```

## 🎨 UI/UX Architecture

### Theme System
```css
:root {
  --straiker-primary: #00ff88;
  --straiker-secondary: #ff6b6b;
  --straiker-accent: #4ecdc4;
  --straiker-bg: #0a0a0a;
  --straiker-text: #ffffff;
}
```

### Component Hierarchy
```
App Layout
├── Header (Straiker Branding)
├── Navigation Tabs
│   ├── Overview Tab
│   ├── Evasion Analysis Tab
│   ├── Control Analysis Tab
│   ├── Attack Paths Tab
│   └── Data Upload Tab
└── Footer
```

### Responsive Design
- **Mobile First**: Optimized for mobile devices
- **Breakpoints**: 768px, 1024px, 1440px
- **Grid System**: Bootstrap-based responsive layout
- **Touch Support**: Mobile-friendly interactions

## 🔧 API Reference

### Callback Functions

#### 1. Tab Navigation
```python
@app.callback(
    Output('tab-content', 'children'),
    Input('main-tabs', 'active_tab')
)
def render_tab_content(active_tab):
    """Renders content based on active tab"""
```

#### 2. Sunburst Chart Interaction
```python
@app.callback(
    Output('metadata-modal', 'is_open'),
    Output('metadata-content', 'children'),
    Input('attack-paths-chart', 'clickData')
)
def handle_attack_paths_click(click_data):
    """Handles sunburst chart drill-down"""
```

#### 3. Data Table Interactions
```python
@app.callback(
    Output('table-modal', 'is_open'),
    Output('table-content', 'children'),
    Input('evasion-table', 'active_cell')
)
def handle_table_click(active_cell):
    """Handles data table row clicks"""
```

### Data Processing Functions

#### 1. Data Loading
```python
def load_assessment_data():
    """Loads and validates assessment data"""
    - Validates data schema
    - Handles missing values
    - Converts data types
    - Returns pandas DataFrame
```

#### 2. Analysis Functions
```python
def calculate_security_metrics(df):
    """Calculates security metrics from data"""
    - Pass/fail rates
    - Risk scores
    - Trend analysis
    - Benchmark comparisons
```

#### 3. Visualization Functions
```python
def create_sunburst_chart(df):
    """Creates interactive sunburst chart"""
    - Hierarchical data structure
    - Color coding by risk level
    - Interactive drill-down
    - Metadata on click
```

## 🗄️ Database Schema

### Tables

#### 1. Assessments Table
```sql
CREATE TABLE assessments (
    id TEXT PRIMARY KEY,
    application_id TEXT NOT NULL,
    straiker_id TEXT NOT NULL,
    assessment_id TEXT NOT NULL,
    control_id TEXT NOT NULL,
    batch_id TEXT,
    timestamp DATETIME,
    score REAL,
    status TEXT,
    evasions_applied TEXT,
    base_prompt TEXT,
    explanation TEXT
);
```

#### 2. Controls Table
```sql
CREATE TABLE controls (
    control_id TEXT PRIMARY KEY,
    control_name TEXT NOT NULL,
    control_type TEXT,
    description TEXT,
    risk_level TEXT,
    mitigation_strategy TEXT
);
```

#### 3. Evasions Table
```sql
CREATE TABLE evasions (
    evasion_id TEXT PRIMARY KEY,
    evasion_name TEXT NOT NULL,
    technique_type TEXT,
    description TEXT,
    success_rate REAL,
    detection_difficulty TEXT
);
```

### Indexes
```sql
-- Performance indexes
CREATE INDEX idx_assessments_timestamp ON assessments(timestamp);
CREATE INDEX idx_assessments_status ON assessments(status);
CREATE INDEX idx_assessments_control ON assessments(control_id);
```

## 🔒 Security Implementation

### Authentication & Authorization
```python
class SecurityManager:
    def __init__(self):
        self.session_timeout = 3600  # 1 hour
        self.max_login_attempts = 5
        self.password_policy = {
            'min_length': 12,
            'require_special': True,
            'require_numbers': True
        }
```

### Data Protection
- **Encryption**: AES-256 for sensitive data
- **Hashing**: SHA-256 for passwords
- **Sanitization**: Input validation and cleaning
- **Audit Logging**: Comprehensive activity tracking

### Security Headers
```python
@app.after_request
def security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

## 📊 Performance Optimization

### Caching Strategy
```python
# Redis caching for frequently accessed data
@cache.memoize(timeout=300)
def get_security_metrics():
    """Cached security metrics calculation"""
    return calculate_metrics()
```

### Database Optimization
- **Connection Pooling**: Reuse database connections
- **Query Optimization**: Indexed queries and prepared statements
- **Data Pagination**: Limit result sets for large datasets
- **Lazy Loading**: Load data on demand

### Frontend Optimization
- **Asset Minification**: Compressed CSS and JavaScript
- **Image Optimization**: WebP format for logos and icons
- **CDN Integration**: Static asset delivery
- **Progressive Loading**: Load critical content first

## 🧪 Testing Framework

### Unit Tests
```python
def test_data_loading():
    """Test data loading functionality"""
    data = load_assessment_data('test_data.csv')
    assert len(data) > 0
    assert 'control_id' in data.columns
```

### Integration Tests
```python
def test_sunburst_interaction():
    """Test sunburst chart drill-down"""
    click_data = {'points': [{'id': 'Base Prompt/evasion/control']]}
    result = handle_attack_paths_click(click_data)
    assert result[0] == True  # Modal should open
```

### Performance Tests
```python
def test_large_dataset():
    """Test performance with large datasets"""
    start_time = time.time()
    process_large_dataset(10000)
    assert time.time() - start_time < 5.0  # Should complete in < 5 seconds
```

## 🚀 Deployment Guide

### Development Environment
```bash
# Local development setup
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python enhanced_dashboard.py
```

### Production Deployment
```bash
# Using Gunicorn
gunicorn -w 4 -b 0.0.0.0:8050 enhanced_dashboard:app

# Using Docker
docker build -t ascend-ai-analyzer .
docker run -p 8050:8050 ascend-ai-analyzer
```

### Environment Configuration
```bash
# Production environment variables
export FLASK_ENV=production
export DATABASE_URL=postgresql://user:pass@host:port/db
export SECRET_KEY=your-secret-key
export DEBUG=False
```

## 📈 Monitoring & Logging

### Application Monitoring
```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/dashboard.log'),
        logging.StreamHandler()
    ]
)
```

### Performance Metrics
- **Response Time**: Track API response times
- **Memory Usage**: Monitor application memory consumption
- **Database Performance**: Query execution times
- **User Activity**: Track user interactions and patterns

### Error Handling
```python
@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors"""
    logging.error(f"Internal error: {error}")
    return "Internal server error", 500
```

## 🔄 Maintenance & Updates

### Regular Maintenance Tasks
1. **Database Cleanup**: Remove old data and optimize tables
2. **Log Rotation**: Manage log file sizes
3. **Dependency Updates**: Keep packages current
4. **Security Patches**: Apply security updates

### Update Procedures
1. **Backup Data**: Create database and file backups
2. **Test Environment**: Deploy to staging first
3. **Gradual Rollout**: Deploy to production incrementally
4. **Monitoring**: Watch for issues after deployment

### Rollback Procedures
1. **Database Rollback**: Restore from backup if needed
2. **Code Rollback**: Revert to previous version
3. **Configuration Rollback**: Restore previous settings
4. **Communication**: Notify users of any issues

---

**Technical Support**: For technical questions or issues, contact the development team or refer to the project documentation.
