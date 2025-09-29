"""
Enhanced Straiker Dashboard with All Features
"""
import dash
from dash import dcc, html, Input, Output, State, dash_table, callback_context
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import ast
import base64
import io
import os
from logo_data import STRAIKER_LOGO_B64, RED_SHIELD_B64

# Initialize Dash app with custom Straiker theme
app = dash.Dash(__name__, external_stylesheets=[
    dbc.themes.DARKLY,
    "https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600;700&display=swap"
], suppress_callback_exceptions=True)

# Custom Straiker CSS
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600;700&display=swap');
            
            :root {
                --straiker-primary: #6366f1;
                --straiker-secondary: #8b5cf6;
                --straiker-accent: #06d6a0;
                --straiker-danger: #ef4444;
                --straiker-warning: #f59e0b;
                --straiker-success: #10b981;
                --straiker-dark: #0a0a0a;
                --straiker-darker: #000000;
                --straiker-light: #1a1a1a;
                --straiker-lighter: #2d2d2d;
                --straiker-text: #ffffff;
                --straiker-text-muted: #9ca3af;
                --straiker-gradient: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #06d6a0 100%);
                --straiker-glow: 0 0 20px rgba(99, 102, 241, 0.3);
                --straiker-glow-strong: 0 0 30px rgba(99, 102, 241, 0.6);
            }
            
            body {
                font-family: 'Exo 2', sans-serif;
                background: var(--straiker-dark);
                color: var(--straiker-text);
                overflow-x: hidden;
            }
            
            .straiker-header {
                background: var(--straiker-gradient);
                border-radius: 12px;
                padding: 2rem;
                margin-bottom: 2rem;
                box-shadow: var(--straiker-glow);
                position: relative;
                overflow: hidden;
            }
            
            .straiker-header::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: linear-gradient(45deg, transparent 30%, rgba(255,255,255,0.1) 50%, transparent 70%);
                animation: shimmer 3s infinite;
            }
            
            @keyframes shimmer {
                0% { transform: translateX(-100%); }
                100% { transform: translateX(100%); }
            }
            
            .straiker-logo {
                width: 50px;
                height: 50px;
                margin-right: 20px;
                filter: drop-shadow(0 0 10px rgba(99, 102, 241, 0.5));
            }
            
            .straiker-title {
                font-family: 'Orbitron', monospace;
                font-size: 3rem;
                font-weight: 900;
                color: white;
                text-shadow: 0 0 20px rgba(99, 102, 241, 0.8);
                margin: 0;
                background: linear-gradient(45deg, #ffffff, #e0e7ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            .straiker-subtitle {
                font-family: 'Exo 2', sans-serif;
                font-size: 1.3rem;
                color: rgba(255, 255, 255, 0.9);
                margin: 0;
                font-weight: 300;
            }
            
            .straiker-card {
                background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
                border: 1px solid rgba(99, 102, 241, 0.2);
                border-radius: 12px;
                padding: 1.5rem;
                margin-bottom: 1rem;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }
            
            .straiker-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 2px;
                background: var(--straiker-gradient);
            }
            
            .straiker-card:hover {
                transform: translateY(-2px);
                box-shadow: var(--straiker-glow);
                border-color: rgba(99, 102, 241, 0.4);
            }
            
            .straiker-metric {
                text-align: center;
                padding: 1rem;
            }
            
            .straiker-metric-value {
                font-family: 'Orbitron', monospace;
                font-size: 2.5rem;
                font-weight: 700;
                margin: 0;
                background: var(--straiker-gradient);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            .straiker-metric-label {
                font-size: 0.9rem;
                color: var(--straiker-text-muted);
                margin: 0;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            
            .straiker-tab {
                background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
                border: 1px solid rgba(99, 102, 241, 0.2);
                border-radius: 8px;
                margin: 0 0.25rem;
                transition: all 0.3s ease;
            }
            
            .straiker-tab:hover {
                background: linear-gradient(135deg, #2d2d2d 0%, #3d3d3d 100%);
                border-color: rgba(99, 102, 241, 0.4);
                box-shadow: 0 0 15px rgba(99, 102, 241, 0.2);
            }
            
            .straiker-tab.active {
                background: var(--straiker-gradient);
                border-color: var(--straiker-primary);
                box-shadow: var(--straiker-glow);
            }
            
            .straiker-button {
                background: var(--straiker-gradient);
                border: none;
                border-radius: 8px;
                padding: 0.75rem 1.5rem;
                color: white;
                font-weight: 600;
                text-transform: uppercase;
                letter-spacing: 1px;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3);
            }
            
            .straiker-button:hover {
                transform: translateY(-2px);
                box-shadow: var(--straiker-glow-strong);
            }
            
            .straiker-table {
                background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
                border-radius: 12px;
                overflow: hidden;
                border: 1px solid rgba(99, 102, 241, 0.2);
            }
            
            .straiker-table th {
                background: var(--straiker-gradient);
                color: white;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 1px;
                border: none;
            }
            
            .straiker-table td {
                border: 1px solid rgba(99, 102, 241, 0.1);
                color: var(--straiker-text);
            }
            
            .straiker-table tr:hover {
                background: rgba(99, 102, 241, 0.1);
            }
            
            .straiker-modal {
                background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
                border: 1px solid rgba(99, 102, 241, 0.3);
                border-radius: 12px;
                box-shadow: var(--straiker-glow-strong);
            }
            
            .straiker-modal-header {
                background: var(--straiker-gradient);
                border: none;
                color: white;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 1px;
            }
            
            .cyber-grid {
                background-image: 
                    linear-gradient(rgba(99, 102, 241, 0.1) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(99, 102, 241, 0.1) 1px, transparent 1px);
                background-size: 20px 20px;
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                pointer-events: none;
                z-index: -1;
            }
            
            .glow-effect {
                box-shadow: 0 0 20px rgba(99, 102, 241, 0.3);
            }
            
            .pulse-animation {
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0.7); }
                70% { box-shadow: 0 0 0 10px rgba(99, 102, 241, 0); }
                100% { box-shadow: 0 0 0 0 rgba(99, 102, 241, 0); }
            }
            
            .straiker-widget-heading {
                font-family: 'Orbitron', monospace;
                font-size: 1.5rem;
                font-weight: 700;
                color: var(--straiker-text);
                text-align: center;
                margin-bottom: 0.5rem;
                text-transform: uppercase;
                letter-spacing: 1px;
                background: var(--straiker-gradient);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
            }
            
            .straiker-widget-subtitle {
                font-family: 'Exo 2', sans-serif;
                font-size: 0.9rem;
                color: var(--straiker-text-muted);
                text-align: center;
                margin-bottom: 1rem;
                font-weight: 300;
                letter-spacing: 0.5px;
            }
        </style>
    </head>
    <body>
        <div class="cyber-grid"></div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Straiker Control Hierarchy
CONTROL_GROUPS = {
    "Data Leakage": ["PII: Name", "PII: Address", "PII: Phone Number", "PII: Email", "PII: SSN", "PII: Credit Card"],
    "Harmful Content": ["Violence", "Hate Speech", "Discrimination", "Self-Harm", "Sexual Content"],
    "LaVa": ["Hallucination", "Misinformation", "Bias", "Inappropriate Response"],
    "Application Grounding": ["System Prompt Leakage", "Internal Knowledge", "Confidential Data"],
    "System Prompt Leakage": ["Prompt Injection", "Jailbreak", "Role Play"],
    "LLM Evasion": ["Typoglycemia", "Base64 Encoding", "Character Substitution"],
    "Excessive Agency": ["Unauthorized Actions", "System Access", "Data Manipulation"]
}

# Global data storage
data = pd.DataFrame()

# Load data function
def load_data(csv_content=None):
    global data
    try:
        if csv_content is not None:
            # Parse uploaded CSV content
            df = pd.read_csv(io.StringIO(csv_content), encoding='utf-8')
        else:
            # Load default CSV file
            csv_file = "/Users/phimmasonephonpaseuth/Projects/Straiker Projects/Customers/Comcast/Comcast XPE Wizard - Light Assessment Results.csv"
            df = pd.read_csv(csv_file, encoding='utf-8')
        
        # Parse evasions with better error handling
        def parse_evasions(x):
            if pd.isna(x) or x == '' or x == '[]' or x == 'null':
                return []
            try:
                if isinstance(x, str):
                    # Handle different string formats
                    if x.startswith('[') and x.endswith(']'):
                        content = x[1:-1]
                        if not content.strip():
                            return []
                        # Split by comma and clean up
                        parts = [p.strip().strip('"\'') for p in content.split(',') if p.strip()]
                        return [p for p in parts if p]  # Remove empty strings
                    else:
                        # Try to parse as JSON-like string
                        import json
                        try:
                            parsed = json.loads(x)
                            if isinstance(parsed, list):
                                return [str(item) for item in parsed if item]
                        except:
                            # If JSON parsing fails, treat as single item
                            return [str(x)] if x else []
                elif isinstance(x, list):
                    return [str(item) for item in x if item]
                else:
                    return [str(x)] if x else []
            except Exception as e:
                print(f"Error parsing evasions: {e}, value: {x}")
                return []
        
        df['evasions_applied'] = df['evasions_applied'].apply(parse_evasions)
        df['has_evasions'] = df['evasions_applied'].apply(lambda x: len(x) > 0)
        
        data = df
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

# Load initial data
data = load_data()
print(f"Data loaded: {len(data)} records")
if not data.empty:
    print(f"Columns: {list(data.columns)}")
    print(f"Status counts: {data['status'].value_counts().to_dict()}")

# Calculate metrics function
def calculate_metrics():
    global data
    if not data.empty:
        total_tests = len(data)
        passed_tests = len(data[data['status'] == 'pass'])
        failed_tests = len(data[data['status'] == 'fail'])
        unknown_tests = len(data[data['status'] == 'unknown'])
        pass_rate = passed_tests / total_tests if total_tests > 0 else 0
        tests_with_evasions = len(data[data['has_evasions'] == True])
        unique_controls = len(data['control_id'].unique()) if 'control_id' in data.columns else 0
        return total_tests, passed_tests, failed_tests, unknown_tests, pass_rate, tests_with_evasions, unique_controls
    else:
        return 0, 0, 0, 0, 0, 0, 0

# Calculate initial metrics
total_tests, passed_tests, failed_tests, unknown_tests, pass_rate, tests_with_evasions, unique_controls = calculate_metrics()

# Layout
app.layout = dbc.Container([
    # Straiker Cyberpunk Header
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Div([
                    # Left side - Official Straiker Logo
                    html.Img(
                        src=STRAIKER_LOGO_B64,
                        className="straiker-logo",
                        style={'marginRight': '20px', 'height': '60px', 'width': 'auto'}
                    ),
                    html.Div([
                        html.H1("STRAIKER", className="straiker-title", style={'fontSize': '3.5rem', 'margin': '0', 'marginBottom': '5px'}),
                        html.H2("ASCEND AI ASSESSMENT TOOL", className="straiker-subtitle", style={'fontSize': '1.8rem', 'margin': '0', 'fontWeight': '400'})
                    ], style={'textAlign': 'center'}),
                    # Right side - Red Ascend AI Shield
                    html.Img(
                        src=RED_SHIELD_B64,
                        className="straiker-logo",
                        style={'marginLeft': '20px', 'height': '60px', 'width': 'auto'}
                    )
                ], style={'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center', 'marginBottom': '20px'})
            ], className="straiker-header")
        ], width=12)
    ]),
    
    # Cyberpunk Navigation Tabs
    dbc.Row([
        dbc.Col([
            html.Div([
    dbc.Tabs([
                    dbc.Tab(
                        label="🔬 OVERVIEW",
                        tab_id="overview",
                        className="straiker-tab"
                    ),
                    dbc.Tab(
                        label="⚡ EVASION ANALYSIS",
                        tab_id="evasion",
                        className="straiker-tab"
                    ),
                    dbc.Tab(
                        label="🛡️ CONTROL ANALYSIS",
                        tab_id="control",
                        className="straiker-tab"
                    ),
                    dbc.Tab(
                        label="🎯 ATTACK PATHS",
                        tab_id="network",
                        className="straiker-tab"
                    ),
                    dbc.Tab(
                        label="📡 DATA UPLOAD",
                        tab_id="upload",
                        className="straiker-tab"
                    )
                ], id="main-tabs", active_tab="overview", className="mb-4")
            ], style={'background': 'linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%)', 'padding': '1rem', 'borderRadius': '12px', 'border': '1px solid rgba(99, 102, 241, 0.2)'})
        ], width=12)
    ], className="mb-4"),
    
    # Adaptive metrics cards
    html.Div(id="adaptive-metrics", className="mb-4"),
    
    # Content area
    html.Div(id="tab-content", className="mt-4"),
    
    # Straiker Cyberpunk Modals
    dbc.Modal([
        dbc.ModalHeader("⚡ NEURAL SCAN RESULTS", className="straiker-modal-header"),
        dbc.ModalBody([
            html.Div(id="drill-content")
        ], className="straiker-modal")
    ], id="drill-modal", is_open=False, size="xl", className="straiker-modal"),
    
    # Control details modal
    dbc.Modal([
        dbc.ModalHeader("🛡️ SECURITY CONTROL ANALYSIS", className="straiker-modal-header"),
        dbc.ModalBody([
            html.Div(id="control-details-content")
        ], className="straiker-modal")
    ], id="control-modal", is_open=False, size="lg", className="straiker-modal"),
    
    # Record details modal for drill-down
    dbc.Modal([
        dbc.ModalHeader("📡 THREAT INTELLIGENCE REPORT", className="straiker-modal-header"),
        dbc.ModalBody([
            html.Div(id="record-details-content")
        ], className="straiker-modal")
    ], id="record-modal", is_open=False, size="xl", className="straiker-modal"),
    
    # Control analysis modal
    dbc.Modal([
        dbc.ModalHeader("🔬 CONTROL MATRIX ANALYSIS", className="straiker-modal-header"),
        dbc.ModalBody([
            html.Div(id="control-analysis-details-content")
        ], className="straiker-modal")
    ], id="control-analysis-modal", is_open=False, size="xl", className="straiker-modal"),
    
    # Evasion analysis modal
    dbc.Modal([
        dbc.ModalHeader("⚡ EVASION TECHNIQUE BREAKDOWN", className="straiker-modal-header"),
        dbc.ModalBody([
            html.Div(id="evasion-analysis-details-content")
        ], className="straiker-modal")
    ], id="evasion-analysis-modal", is_open=False, size="xl", className="straiker-modal"),
    
    # Attack paths modal
    dbc.Modal([
        dbc.ModalHeader("🎯 ATTACK VECTOR ANALYSIS", className="straiker-modal-header"),
        dbc.ModalBody([
            html.Div(id="attack-paths-details-content")
        ], className="straiker-modal")
    ], id="attack-paths-modal", is_open=False, size="xl", className="straiker-modal")
    
], fluid=True, style={'background-color': '#0a0a0a', 'min-height': '100vh'})

# Callback for adaptive metrics
@app.callback(
    Output('adaptive-metrics', 'children'),
    Input('main-tabs', 'active_tab')
)
def update_adaptive_metrics(active_tab):
    """Update metrics based on active tab"""
    # Recalculate metrics with current data
    total_tests, passed_tests, failed_tests, unknown_tests, pass_rate, tests_with_evasions, unique_controls = calculate_metrics()
    
    if active_tab == "overview":
        # Straiker Overview metrics with cyberpunk styling
        return dbc.Row([
            dbc.Col([
                html.Div([
                    html.H3(f"{total_tests:,}", className="straiker-metric-value"),
                    html.P("TOTAL SCANS", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H3(f"{pass_rate:.1%}", className="straiker-metric-value", style={'color': '#10b981'}),
                    html.P("SECURITY RATE", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H3(f"{tests_with_evasions:,}", className="straiker-metric-value", style={'color': '#8b5cf6'}),
                    html.P("EVASION ATTEMPTS", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H3(f"{unique_controls}", className="straiker-metric-value", style={'color': '#06d6a0'}),
                    html.P("CONTROLS ACTIVE", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H3(f"{failed_tests:,}", className="straiker-metric-value", style={'color': '#ef4444'}),
                    html.P("THREATS DETECTED", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H3(f"{unknown_tests:,}", className="straiker-metric-value", style={'color': '#f59e0b'}),
                    html.P("ANALYZING", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2)
        ])
    elif active_tab == "evasion":
        # Evasion-specific metrics
        evasion_data = []
        for _, row in data.iterrows():
            if row['has_evasions'] and isinstance(row['evasions_applied'], list):
                for evasion in row['evasions_applied']:
                    evasion_data.append({'evasion': evasion, 'status': row['status']})
        
        if evasion_data:
            evasions_df = pd.DataFrame(evasion_data)
            unique_evasions = len(evasions_df['evasion'].unique())
            failed_evasions = len(evasions_df[evasions_df['status'] == 'fail'])
            evasion_success_rate = 1 - (failed_evasions / len(evasions_df)) if len(evasions_df) > 0 else 0
        else:
            unique_evasions = failed_evasions = 0
            evasion_success_rate = 0
            
        return dbc.Row([
            dbc.Col([
                html.Div([
                    html.H3(f"{unique_evasions}", className="straiker-metric-value", style={'color': '#8b5cf6'}),
                    html.P("EVASION TECHNIQUES", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=3),
            dbc.Col([
                html.Div([
                    html.H3(f"{evasion_success_rate:.1%}", className="straiker-metric-value", style={'color': '#10b981'}),
                    html.P("EVASION SUCCESS", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=3),
            dbc.Col([
                html.Div([
                    html.H3(f"{failed_evasions}", className="straiker-metric-value", style={'color': '#ef4444'}),
                    html.P("BLOCKED EVASIONS", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=3),
            dbc.Col([
                html.Div([
                    html.H3(f"{len(evasion_data)}", className="straiker-metric-value", style={'color': '#f59e0b'}),
                    html.P("TOTAL ATTEMPTS", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=3)
        ])
    elif active_tab == "control":
        # Control-specific metrics
        if 'control_id' in data.columns:
            control_metrics = data.groupby('control_id').agg({
                'id': 'count',
                'status': lambda x: (x == 'fail').sum()
            }).reset_index()
            control_metrics.columns = ['Control', 'Total_Tests', 'Failed_Tests']
            control_metrics['Failure_Rate'] = control_metrics['Failed_Tests'] / control_metrics['Total_Tests']
            
            # Calculate passed and failed controls
            passed_controls = len(control_metrics[control_metrics['Failed_Tests'] == 0])
            failed_controls = len(control_metrics[control_metrics['Failed_Tests'] > 0])
            total_failure_rate = control_metrics['Failed_Tests'].sum() / control_metrics['Total_Tests'].sum()
        else:
            passed_controls = failed_controls = 0
            total_failure_rate = 0
            
        # Multiturn attacks analysis
        multiturn_data = data[data['chat_history'].notna() & (data['chat_history'] != '') & (data['chat_history'] != '[]') & (data['chat_history'] != 'null')]
        multiturn_count = len(multiturn_data)
        multiturn_with_evasions = len(multiturn_data[multiturn_data['has_evasions'] == True])
        successful_multiturn = len(multiturn_data[multiturn_data['status'] == 'fail'])
        
        return dbc.Row([
            dbc.Col([
                        html.Div([
                    html.H3(f"🛡️ {passed_controls}", className="straiker-metric-value", style={'color': '#10b981'}),
                    html.P("SECURE CONTROLS", className="straiker-metric-label")
                ], className="straiker-metric straiker-card", id="passed-controls-card", style={"cursor": "pointer"})
            ], width=3),
            dbc.Col([
                        html.Div([
                    html.H3(f"⚠️ {failed_controls}", className="straiker-metric-value", style={'color': '#ef4444'}),
                    html.P("COMPROMISED", className="straiker-metric-label")
                ], className="straiker-metric straiker-card", id="failed-controls-card", style={"cursor": "pointer"})
            ], width=3),
            dbc.Col([
                html.Div([
                    html.H3(f"{total_failure_rate:.1%}", className="straiker-metric-value", style={'color': '#f59e0b'}),
                    html.P("THREAT LEVEL", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=3),
            dbc.Col([
                html.Div([
                    html.H3(f"⚡ {multiturn_count}", className="straiker-metric-value", style={'color': '#8b5cf6'}),
                    html.P("MULTI-ATTACKS", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=3)
        ])
    else:
        # Default Straiker metrics for other tabs
        return dbc.Row([
            dbc.Col([
                html.Div([
                    html.H3(f"{total_tests:,}", className="straiker-metric-value"),
                    html.P("TOTAL SCANS", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H3(f"{pass_rate:.1%}", className="straiker-metric-value", style={'color': '#10b981'}),
                    html.P("SECURITY RATE", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H3(f"{tests_with_evasions:,}", className="straiker-metric-value", style={'color': '#8b5cf6'}),
                    html.P("EVASION ATTEMPTS", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H3(f"{unique_controls}", className="straiker-metric-value", style={'color': '#06d6a0'}),
                    html.P("CONTROLS ACTIVE", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H3(f"{failed_tests:,}", className="straiker-metric-value", style={'color': '#ef4444'}),
                    html.P("THREATS DETECTED", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2),
            dbc.Col([
                html.Div([
                    html.H3(f"{unknown_tests:,}", className="straiker-metric-value", style={'color': '#f59e0b'}),
                    html.P("ANALYZING", className="straiker-metric-label")
                ], className="straiker-metric straiker-card")
            ], width=2)
        ])

@app.callback(
    Output('tab-content', 'children'),
    Input('main-tabs', 'active_tab')
)
def render_tab_content(active_tab):
    if data.empty:
        return dbc.Alert("No data available", color="danger")
    
    if active_tab == "overview":
        # Status distribution
        status_counts = data['status'].value_counts()
        # Keep 'unknown' as is (don't replace with 'Error')
        status_fig = px.pie(
            values=status_counts.values,
            names=status_counts.index,
            title="Test Results Distribution",
            color_discrete_sequence=['#10b981', '#ef4444', '#f59e0b']
        )
        status_fig.update_layout(
            paper_bgcolor='#1a1a1a',
            plot_bgcolor='#1a1a1a',
            font_color='#ffffff'
        )
        
        # Score distribution
        if 'score' in data.columns:
            score_fig = px.histogram(
                data, x='score', nbins=20,
                title="Score Distribution",
                color_discrete_sequence=['#6366f1']
            )
            score_fig.update_layout(
                paper_bgcolor='#1a1a1a',
                plot_bgcolor='#1a1a1a',
                font_color='#ffffff'
            )
        else:
            score_fig = go.Figure()
        
        return dbc.Row([
            dbc.Col([dcc.Graph(figure=status_fig, id="status-chart")], width=6),
            dbc.Col([dcc.Graph(figure=score_fig, id="score-chart")], width=6)
        ])
    
    elif active_tab == "evasion":
        # Evasion analysis
        evasion_data = []
        for _, row in data.iterrows():
            if row['has_evasions'] and isinstance(row['evasions_applied'], list):
                for evasion in row['evasions_applied']:
                    # Extract only the evasion technique name (before the colon)
                    evasion_technique = evasion.split(':')[0] if ':' in evasion else evasion
                    evasion_data.append({
                        'evasion': evasion_technique,
                        'status': row['status']
                    })
        
        if not evasion_data:
            return dbc.Alert("No evasion data available", color="info")
        
        evasions_df = pd.DataFrame(evasion_data)
        evasion_metrics = evasions_df.groupby('evasion').agg({
            'status': ['count', lambda x: (x == 'fail').sum()]
        }).reset_index()
        evasion_metrics.columns = ['Evasion', 'Total_Tests', 'Failed_Tests']
        evasion_metrics['Failure_Rate'] = evasion_metrics['Failed_Tests'] / evasion_metrics['Total_Tests']
        evasion_metrics = evasion_metrics.sort_values('Total_Tests', ascending=False)
        
        # Evasion usage chart
        usage_fig = px.bar(
            evasion_metrics.head(15),
            x='Evasion', y='Total_Tests',
            title="Evasion Technique Usage",
            color='Total_Tests',
            color_continuous_scale='Blues'
        )
        usage_fig.update_layout(
            paper_bgcolor='#1a1a1a',
            plot_bgcolor='#1a1a1a',
            font_color='#ffffff',
            xaxis_tickangle=45
        )
        
        # Straiker Evasion table with cyberpunk styling
        table = dash_table.DataTable(
            data=evasion_metrics.to_dict('records'),
            columns=[
                {"name": "⚡ EVASION TECHNIQUE", "id": "Evasion"},
                {"name": "📊 TOTAL ATTEMPTS", "id": "Total_Tests", "type": "numeric"},
                {"name": "❌ BLOCKED", "id": "Failed_Tests", "type": "numeric"},
                {"name": "📈 SUCCESS RATE", "id": "Failure_Rate", "type": "numeric", "format": {"specifier": ".1%"}}
            ],
            style_cell={
                'backgroundColor': '#1a1a1a', 
                'color': '#ffffff',
                'fontFamily': 'Exo 2, sans-serif',
                'fontSize': '14px',
                'textAlign': 'center',
                'border': '1px solid rgba(99, 102, 241, 0.2)'
            },
            style_header={
                'backgroundColor': 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #06d6a0 100%)',
                'color': 'white',
                'fontWeight': '700',
                'textTransform': 'uppercase',
                'letterSpacing': '1px',
                'fontFamily': 'Orbitron, monospace',
                'fontSize': '12px',
                'border': 'none'
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#2a2a2a'
                },
                {
                    'if': {'filter_query': '{Failure_Rate} > 0.5'},
                    'backgroundColor': '#4a1a1a',
                    'color': '#ff6b6b'
                }
            ],
            style_cell_conditional=[
                {
                    'if': {'column_id': 'Evasion'},
                    'cursor': 'pointer',
                    'textDecoration': 'underline',
                    'color': '#8b5cf6',
                    'fontWeight': '600'
                },
                {
                    'if': {'column_id': 'Total_Tests'},
                    'cursor': 'pointer',
                    'textDecoration': 'underline',
                    'color': '#06d6a0'
                },
                {
                    'if': {'column_id': 'Failed_Tests'},
                    'cursor': 'pointer',
                    'textDecoration': 'underline',
                    'color': '#ef4444'
                }
            ],
            page_size=15,
            id="evasion-table"
        )
        
        return dbc.Row([
            dbc.Col([dcc.Graph(figure=usage_fig, id="evasion-usage-chart")], width=12),
            dbc.Col([table], width=12)
        ])
    
    elif active_tab == "control":
        # Straiker Control Hierarchy Analysis
        if 'control_id' not in data.columns:
            return dbc.Alert("No control data available", color="info")
        
        # Use product_category as control group
        data['control_group'] = data['product_category']
        
        # Control group metrics
        group_metrics = (
            data.groupby('control_group')
            .agg(
                Total_Tests=('id', 'count'),
                Failed_Tests=('status', lambda x: (x == 'fail').sum()),
                Failure_Rate=('status', lambda x: (x == 'fail').sum() / len(x))
            )
            .reset_index()
            .rename(columns={'control_group': 'Control Group'})
        )
        group_metrics = group_metrics.sort_values('Failure_Rate', ascending=False)
        
        # 1. Control Group Failure Rate bar graph
        group_fig = px.bar(
            group_metrics,
            x='Control Group',
            y='Failure_Rate',
            title="Control Group Failure Rates (Straiker Hierarchy)",
            color='Failure_Rate',
            color_continuous_scale='Reds',
            hover_data=['Total_Tests', 'Failed_Tests']
        )
        group_fig.update_layout(
            height=500, 
            xaxis_tickangle=45,
            paper_bgcolor='#1a1a1a',
            plot_bgcolor='#1a1a1a',
            font_color='#ffffff',
            xaxis=dict(color='#ffffff'),
            yaxis=dict(color='#ffffff')
        )
        
        # 2. Three separate pie charts for specific product categories
        def create_pie_chart_for_category(category_name, category_value):
            """Create pie chart for a specific product category"""
            category_data = data[data['product_category'] == category_value]
            failed_category_data = category_data[category_data['status'] == 'fail']
            
            if not failed_category_data.empty:
                control_failures = failed_category_data['control_id'].value_counts().reset_index()
                control_failures.columns = ['Control ID', 'Failures']
                
                if len(control_failures) > 0:
                    # Limit to top 10 for readability, group others as "Others"
                    if len(control_failures) > 10:
                        top_10 = control_failures.head(10)
                        others_sum = control_failures.iloc[10:]['Failures'].sum()
                        if others_sum > 0:
                            others_row = pd.DataFrame({'Control ID': ['Others'], 'Failures': [others_sum]})
                            control_failures = pd.concat([top_10, others_row], ignore_index=True)
                    
                    pie_fig = px.pie(
                        control_failures,
                        values='Failures',
                        names='Control ID',
                        title=f"{category_name} Control Failures",
                        color_discrete_sequence=px.colors.qualitative.Set3
                    )
                    pie_fig.update_layout(
                        height=500,  # Increased height for better readability
                        paper_bgcolor='#1a1a1a',
                        plot_bgcolor='#1a1a1a',
                        font_color='#ffffff',
                        showlegend=True,
                        legend=dict(
                            orientation="v",
                            yanchor="middle",
                            y=0.5,
                            xanchor="left",
                            x=1.01
                        ),
                        font=dict(size=12)
                    )
                    return pie_fig
            
            # Return empty figure if no data
            empty_fig = go.Figure()
            empty_fig.add_annotation(
                text=f"No {category_name} failures to display", 
                xref="paper", yref="paper",
                x=0.5, y=0.5,
                showarrow=False,
                font=dict(size=16, color='#ffffff')
            )
            empty_fig.update_layout(
                height=500,
                paper_bgcolor='#1a1a1a',
                plot_bgcolor='#1a1a1a',
                font_color='#ffffff'
            )
            return empty_fig
        
        # Create pie charts for the three main categories
        data_leakage_pie = create_pie_chart_for_category("Data Leakage", "data_leak")
        harmful_content_pie = create_pie_chart_for_category("Harmful Content", "harmful_content")
        app_grounding_pie = create_pie_chart_for_category("Application Grounding", "app_grounding")
        
        # Debug: Print chart info
        print(f"Data Leakage pie chart created: {data_leakage_pie is not None}")
        print(f"Harmful Content pie chart created: {harmful_content_pie is not None}")
        print(f"App Grounding pie chart created: {app_grounding_pie is not None}")
        
        # Control-Evasion Heatmap
        evasion_control_data = []
        for _, row in data.iterrows():
            if row['has_evasions'] and isinstance(row['evasions_applied'], list):
                for evasion in row['evasions_applied']:
                    evasion_control_data.append({
                        'evasion': evasion,
                        'control': str(row.get('control_id', 'unknown')),
                        'status': row['status']
                    })
        
        if evasion_control_data:
            heatmap_df = pd.DataFrame(evasion_control_data)
            heatmap_pivot = heatmap_df.pivot_table(
                index='control', 
                columns='evasion', 
                values='status', 
                aggfunc=lambda x: (x == 'fail').sum(),
                fill_value=0
            )
            
            # Create heatmap
            heatmap_fig = px.imshow(
                heatmap_pivot.values,
                x=heatmap_pivot.columns,
                y=heatmap_pivot.index,
                color_continuous_scale=['#10b981', '#ef4444'],
                title="Control-Evasion Failure Matrix (Red = Failures, Green = Success)"
            )
            heatmap_fig.update_layout(
                height=600,
                paper_bgcolor='#1a1a1a',
                plot_bgcolor='#1a1a1a',
                font_color='#ffffff',
                xaxis=dict(color='#ffffff'),
                yaxis=dict(color='#ffffff')
            )
        else:
            heatmap_fig = go.Figure()
            heatmap_fig.add_annotation(text="No control-evasion data available", xref="paper", yref="paper")
        
        # Data Leakage sub-controls table
        data_leakage_controls = data[data['product_category'] == 'data_leakage']
        if not data_leakage_controls.empty:
            dl_metrics = (
                data_leakage_controls.groupby('control_id')
                .agg(
                    Total_Tests=('id', 'count'),
                    Failed_Tests=('status', lambda x: (x == 'fail').sum()),
                    Failure_Rate=('status', lambda x: (x == 'fail').sum() / len(x))
                )
                .reset_index()
                .rename(columns={'control_id': 'Sub Control'})
            )
            dl_metrics = dl_metrics.sort_values('Failure_Rate', ascending=False)
            
            dl_table = dash_table.DataTable(
                data=dl_metrics.to_dict('records'),
                columns=[
                    {"name": "Data Leakage Sub Control", "id": "Sub Control"},
                    {"name": "Total Tests", "id": "Total_Tests", "type": "numeric"},
                    {"name": "Failed Tests", "id": "Failed_Tests", "type": "numeric"},
                    {"name": "Failure Rate", "id": "Failure_Rate", "type": "numeric", "format": {"specifier": ".1%"}}
                ],
                style_cell={'backgroundColor': '#1a1a1a', 'color': '#ffffff'},
                style_header={'backgroundColor': '#ef4444', 'color': 'white'},
                page_size=10
            )
        else:
            dl_table = html.P("No Data Leakage controls found")
        
        # Straiker Control Group Summary Statistics Table
        group_summary_table = dash_table.DataTable(
            data=group_metrics.to_dict('records'),
            columns=[
                {"name": "🛡️ CONTROL GROUP", "id": "Control Group"},
                {"name": "📊 TOTAL SCANS", "id": "Total_Tests", "type": "numeric"},
                {"name": "❌ THREATS", "id": "Failed_Tests", "type": "numeric"},
                {"name": "✅ SECURE", "id": "Passed_Tests", "type": "numeric"},
                {"name": "⚠️ ANALYZING", "id": "Unknown_Tests", "type": "numeric"},
                {"name": "📈 THREAT LEVEL", "id": "Failure_Rate", "type": "numeric", "format": {"specifier": ".1%"}}
            ],
            style_cell={
                'backgroundColor': '#1a1a1a', 
                'color': '#ffffff',
                'fontFamily': 'Exo 2, sans-serif',
                'fontSize': '14px',
                'textAlign': 'center',
                'border': '1px solid rgba(99, 102, 241, 0.2)'
            },
            style_header={
                'backgroundColor': 'linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #06d6a0 100%)',
                'color': 'white',
                'fontWeight': '700',
                'textTransform': 'uppercase',
                'letterSpacing': '1px',
                'fontFamily': 'Orbitron, monospace',
                'fontSize': '12px',
                'border': 'none'
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': '#2a2a2a'
                },
                {
                    'if': {'filter_query': '{Failure_Rate} > 0.1'},
                    'backgroundColor': '#4a1a1a',
                    'color': '#ff6b6b'
                }
            ],
            style_cell_conditional=[
                {
                    'if': {'column_id': 'Control Group'},
                    'cursor': 'pointer',
                    'textDecoration': 'underline',
                    'color': '#8b5cf6',
                    'fontWeight': '600'
                },
                {
                    'if': {'column_id': 'Total_Tests'},
                    'cursor': 'pointer',
                    'textDecoration': 'underline',
                    'color': '#06d6a0'
                },
                {
                    'if': {'column_id': 'Failed_Tests'},
                    'cursor': 'pointer',
                    'textDecoration': 'underline',
                    'color': '#ef4444'
                },
                {
                    'if': {'column_id': 'Passed_Tests'},
                    'cursor': 'pointer',
                    'textDecoration': 'underline',
                    'color': '#10b981'
                },
                {
                    'if': {'column_id': 'Unknown_Tests'},
                    'cursor': 'pointer',
                    'textDecoration': 'underline',
                    'color': '#f59e0b'
                }
            ],
            page_size=10,
            id="control-group-summary-table"
        )
        
        # Calculate additional metrics for the table
        for i, row in group_metrics.iterrows():
            control_group = row['Control Group']
            group_data = data[data['control_group'] == control_group]
            passed_tests = len(group_data[group_data['status'] == 'pass'])
            unknown_tests = len(group_data[group_data['status'] == 'unknown'])
            group_metrics.at[i, 'Passed_Tests'] = passed_tests
            group_metrics.at[i, 'Unknown_Tests'] = unknown_tests
        
        return [
            dbc.Row([
                dbc.Col([
                    dcc.Graph(figure=group_fig, id="control-group-chart", style={'height': '500px'})
                ], width=12)
            ], className="mb-4"),
            dbc.Row([
                dbc.Col([
                    html.H4("📊 CONTROL GROUP ANALYSIS", className="straiker-widget-heading"),
                    html.P("Comprehensive breakdown of security control performance metrics", className="straiker-widget-subtitle"),
                    group_summary_table
                ], width=12)
            ], className="mb-4"),
            dbc.Row([
                dbc.Col([
                    html.H4("🔒 DATA LEAKAGE ANALYSIS", className="straiker-widget-heading"),
                    html.P("Threat detection performance in data protection controls", className="straiker-widget-subtitle"),
                    dcc.Graph(figure=data_leakage_pie, id="data-leakage-pie", style={'height': '500px'})
                ], width=4),
                dbc.Col([
                    html.H4("⚠️ HARMFUL CONTENT DETECTION", className="straiker-widget-heading"),
                    html.P("Security analysis of harmful content identification systems", className="straiker-widget-subtitle"),
                    dcc.Graph(figure=harmful_content_pie, id="harmful-content-pie", style={'height': '500px'})
                ], width=4),
                dbc.Col([
                    html.H4("🎯 APPLICATION GROUNDING", className="straiker-widget-heading"),
                    html.P("Neural network grounding and context analysis results", className="straiker-widget-subtitle"),
                    dcc.Graph(figure=app_grounding_pie, id="app-grounding-pie", style={'height': '500px'})
                ], width=4)
            ], className="mb-4")
        ]
    
    elif active_tab == "network":
        # Attack paths with Control-Evasion Matrix and Interactive Pie Chart
        if tests_with_evasions == 0:
            return dbc.Alert("No evasion data available", color="info")
        
        # Calculate control-evasion combination metrics
        evasion_control_data = []
        for _, row in data.iterrows():
            if row['has_evasions'] and isinstance(row['evasions_applied'], list):
                for evasion in row['evasions_applied']:
                    # Extract only the evasion technique name (before the colon)
                    evasion_technique = evasion.split(':')[0] if ':' in evasion else evasion
                    evasion_control_data.append({
                        'evasion': evasion_technique,
                        'control': str(row.get('control_id', 'unknown')),
                        'status': row['status']
                    })
        
        if evasion_control_data:
            heatmap_df = pd.DataFrame(evasion_control_data)
            # Flip the pivot table: evasions on Y-axis, controls on X-axis
            heatmap_pivot = heatmap_df.pivot_table(
                index='evasion', 
                columns='control', 
                values='status', 
                aggfunc=lambda x: (x == 'fail').sum(),
                fill_value=0
            )
            
            # Create improved heatmap with flipped axes
            heatmap_fig = px.imshow(
                heatmap_pivot.values,
                x=heatmap_pivot.columns,
                y=heatmap_pivot.index,
                color_continuous_scale=['#10b981', '#ef4444'],
                title="Control-Evasion Attack Matrix (Red = Failures, Green = Success)",
                labels=dict(x="Control ID", y="Evasion Technique", color="Failures")
            )
            heatmap_fig.update_layout(
                height=800,
                paper_bgcolor='#1a1a1a',
                plot_bgcolor='#1a1a1a',
                font_color='#ffffff',
                xaxis=dict(color='#ffffff', tickangle=45),
                yaxis=dict(color='#ffffff'),
                font=dict(size=12)
            )
            
            # Create interactive pie chart for attack paths using the same data
            attack_paths_data = []
            for item in evasion_control_data:
                if item['status'] == 'fail':  # Only show failed attacks
                    attack_paths_data.append({
                        'Base Prompt': 'Base Prompt',
                        'Evasion': item['evasion'],
                        'Control': item['control']
                    })
            
            if attack_paths_data:
                df_paths = pd.DataFrame(attack_paths_data)
                
                # Create sunburst chart with proper click handling
                sb = px.sunburst(
                    df_paths,
                    path=['Base Prompt', 'Evasion', 'Control'],
                    color_discrete_sequence=['#6366f1', '#f59e0b', '#ef4444'],
                    title="Interactive Attack Paths: Base Prompt → Evasion → Control"
                )
                sb.update_layout(
                    height=600,
                    paper_bgcolor='#1a1a1a',
                    plot_bgcolor='#1a1a1a',
                    font_color='#ffffff'
                )
                # Enable click events
                sb.update_traces(hovertemplate='<b>%{label}</b><br>Count: %{value}<extra></extra>')
            else:
                sb = go.Figure()
                sb.add_annotation(text="No attack path data available", xref="paper", yref="paper")
        else:
            heatmap_fig = go.Figure()
            heatmap_fig.add_annotation(text="No attack path data available", xref="paper", yref="paper")
            sb = go.Figure()
            sb.add_annotation(text="No attack path data available", xref="paper", yref="paper")
        
        return [
            dbc.Row([
                dbc.Col([
                    html.H4("🎯 ATTACK VECTOR MATRIX", className="straiker-widget-heading"),
                    html.P("Threat correlation analysis showing evasion-control failure patterns", className="straiker-widget-subtitle"),
                    dcc.Graph(figure=heatmap_fig, id="attack-paths-matrix", style={'height': '800px'}, config={'displayModeBar': True})
                ], width=12)
            ], className="mb-4"),
            dbc.Row([
                dbc.Col([
                    html.H4("🔄 NEURAL ATTACK PATHS", className="straiker-widget-heading"),
                    html.P("Interactive threat pathway visualization - click final level for details", className="straiker-widget-subtitle"),
                    dcc.Graph(figure=sb, id="attack-paths-pie", style={'height': '600px'})
                ], width=12)
            ])
        ]
    
    elif active_tab == "upload":
        return dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.H4("📁 Upload Ascend AI Results", className="text-white mb-0")
                    ], className="bg-primary"),
                    dbc.CardBody([
                        html.P("Upload a CSV file containing Ascend AI assessment results to analyze with the dashboard.", className="text-muted mb-4"),
                        
                        # File upload component
                        dcc.Upload(
                            id='upload-data',
                            children=html.Div([
                                html.I(className="fas fa-cloud-upload-alt fa-3x text-primary mb-3"),
                                html.H5("Drag and Drop or Click to Upload CSV", className="text-white"),
                                html.P("Supported format: CSV files from Ascend AI", className="text-muted")
                            ], className="text-center p-4 border border-dashed border-primary rounded", 
                               style={'border': '2px dashed #6366f1', 'borderRadius': '8px', 'cursor': 'pointer'}),
                            style={
                                'width': '100%',
                                'height': '200px',
                                'lineHeight': '200px',
                                'borderWidth': '1px',
                                'borderStyle': 'dashed',
                                'borderRadius': '5px',
                                'textAlign': 'center',
                                'margin': '10px'
                            },
                            multiple=False
                        ),
                        
                        # Upload status
                        html.Div(id='upload-status', className="mt-3"),
                        
                        # Current data info
                        html.Div(id='current-data-info', className="mt-4")
                    ])
                ])
            ], width=8),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader([
                        html.H5("📋 Expected CSV Format", className="text-white mb-0")
                    ], className="bg-info"),
                    dbc.CardBody([
                        html.P("Your CSV should contain these columns:", className="text-muted mb-3"),
                        html.Ul([
                            html.Li("id - Unique test identifier"),
                            html.Li("status - Test result (pass/fail/unknown)"),
                            html.Li("control_id - Control identifier"),
                            html.Li("product_category - Control category"),
                            html.Li("evasions_applied - List of evasion techniques"),
                            html.Li("score - Test score (optional)"),
                            html.Li("base_prompt - Test prompt (optional)")
                        ], className="text-white small"),
                        html.Hr(),
                        html.P("The dashboard will automatically parse and analyze your data.", className="text-success small")
                    ])
                ])
            ], width=4)
        ])
    
    return html.Div("Select a tab to view analysis")

# Interactive chart callbacks
@app.callback(
    Output('drill-modal', 'is_open'),
    Output('drill-content', 'children'),
    Input('status-chart', 'clickData'),
    Input('score-chart', 'clickData'),
    prevent_initial_call=True
)
def handle_chart_click(status_click, score_click):
    """Handle chart clicks for drill-down"""
    ctx = callback_context
    if not ctx.triggered:
        return False, ""
    
    if data.empty:
        return True, dbc.Alert("No data available", color="danger")
    
    # Get clicked data
    click_data = status_click or score_click
    if not click_data:
        return False, ""
    
    # Filter records based on click
    if status_click:
        clicked_label = click_data['points'][0]['label']
        filtered_data = data[data['status'] == clicked_label]
        title = f"Records with Status: {clicked_label}"
    else:
        # Score chart click
        clicked_value = click_data['points'][0]['x']
        filtered_data = data[(data['score'] >= clicked_value - 0.1) & (data['score'] <= clicked_value + 0.1)]
        title = f"Records with Score: {clicked_value:.2f}"
    
    # Create drill-down content
    drill_content = [
        html.H4(title, className="text-white mb-3"),
        html.Div([
            create_record_card(record) for _, record in filtered_data.head(20).iterrows()
        ])
    ]
    
    return True, drill_content

# Control details modal callback - completely rewritten
@app.callback(
    Output('control-modal', 'is_open'),
    Output('control-details-content', 'children'),
    Input('passed-controls-card', 'n_clicks'),
    Input('failed-controls-card', 'n_clicks'),
    prevent_initial_call=True
)
def handle_control_card_click(passed_clicks, failed_clicks):
    """Handle control card clicks to show detailed lists"""
    ctx = callback_context
    
    # Only proceed if something was actually clicked
    if not ctx.triggered or not ctx.triggered[0]['value']:
        return False, ""
    
    if data.empty:
        return True, dbc.Alert("No data available", color="danger")
    
    # Get control metrics
    control_metrics = data.groupby('control_id').agg({
        'id': 'count',
        'status': lambda x: (x == 'fail').sum()
    }).reset_index()
    control_metrics.columns = ['Control', 'Total_Tests', 'Failed_Tests']
    
    # Determine which card was clicked
    if ctx.triggered[0]['prop_id'] == 'passed-controls-card.n_clicks':
        # Show passed controls (0 failures)
        passed_controls = control_metrics[control_metrics['Failed_Tests'] == 0]
        title = f"✅ Passed Controls ({len(passed_controls)} total)"
        
        if len(passed_controls) > 0:
            control_list = []
            for _, control in passed_controls.iterrows():
                control_list.append(
                    html.Li([
                        html.Span("✅ ", style={'color': '#10b981', 'fontSize': '1.2em'}),
                        html.Span(control['Control'], style={'color': '#ffffff', 'fontSize': '1.1em'})
                    ], style={'marginBottom': '8px', 'padding': '5px', 'backgroundColor': '#1a1a1a', 'borderRadius': '4px'})
                )
            
            content = [
                html.H4(title, className="text-success mb-3"),
                html.Ul(control_list, style={'listStyle': 'none', 'padding': '0'})
            ]
        else:
            content = [html.H4(title, className="text-success mb-3"), html.P("No passed controls found")]
    
    elif ctx.triggered[0]['prop_id'] == 'failed-controls-card.n_clicks':
        # Show failed controls (at least 1 failure)
        failed_controls = control_metrics[control_metrics['Failed_Tests'] > 0]
        title = f"❌ Failed Controls ({len(failed_controls)} total)"
        
        if len(failed_controls) > 0:
            control_list = []
            for _, control in failed_controls.iterrows():
                control_list.append(
                    html.Li([
                        html.Span("❌ ", style={'color': '#ef4444', 'fontSize': '1.2em'}),
                        html.Span(control['Control'], style={'color': '#ffffff', 'fontSize': '1.1em'}),
                        html.Span(f" ({control['Failed_Tests']} failures)", style={'color': '#f59e0b', 'fontSize': '0.9em', 'marginLeft': '10px'})
                    ], style={'marginBottom': '8px', 'padding': '5px', 'backgroundColor': '#1a1a1a', 'borderRadius': '4px'})
                )
            
            content = [
                html.H4(title, className="text-danger mb-3"),
                html.Ul(control_list, style={'listStyle': 'none', 'padding': '0'})
            ]
        else:
            content = [html.H4(title, className="text-danger mb-3"), html.P("No failed controls found")]
    
    else:
        return False, ""
    
    return True, content

# CSV Upload callback
@app.callback(
    Output('upload-status', 'children'),
    Output('current-data-info', 'children'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
    prevent_initial_call=True
)
def handle_upload(contents, filename):
    """Handle CSV file upload"""
    if contents is None:
        return "", ""
    
    try:
        # Decode the uploaded file
        content_type, content_string = contents.split(',')
        decoded = base64.b64decode(content_string)
        
        # Convert to string and load data
        csv_content = decoded.decode('utf-8')
        new_data = load_data(csv_content)
        
        if new_data.empty:
            return dbc.Alert("Error: Could not parse the uploaded CSV file. Please check the format.", color="danger"), ""
        
        # Success message
        success_alert = dbc.Alert([
            html.H5("✅ Upload Successful!", className="text-success"),
            html.P(f"File: {filename}", className="text-white"),
            html.P(f"Records loaded: {len(new_data):,}", className="text-white"),
            html.P("Dashboard has been updated with new data.", className="text-success")
        ], color="success")
        
        # Current data info
        data_info = dbc.Card([
            dbc.CardHeader([
                html.H6("📊 Current Dataset", className="text-white mb-0")
            ], className="bg-dark"),
            dbc.CardBody([
                html.P(f"Total Tests: {len(new_data):,}", className="text-white"),
                html.P(f"Passed: {len(new_data[new_data['status'] == 'pass']):,}", className="text-success"),
                html.P(f"Failed: {len(new_data[new_data['status'] == 'fail']):,}", className="text-danger"),
                html.P(f"Controls: {len(new_data['control_id'].unique()) if 'control_id' in new_data.columns else 0}", className="text-info"),
                html.P(f"Categories: {len(new_data['product_category'].unique()) if 'product_category' in new_data.columns else 0}", className="text-warning")
            ])
        ])
        
        return success_alert, data_info
        
    except Exception as e:
        error_alert = dbc.Alert([
            html.H5("❌ Upload Failed", className="text-danger"),
            html.P(f"Error: {str(e)}", className="text-white"),
            html.P("Please check that your file is a valid CSV with the expected columns.", className="text-muted")
        ], color="danger")
        return error_alert, ""

# Control Analysis tab callback
@app.callback(
    Output('control-analysis-modal', 'is_open'),
    Output('control-analysis-details-content', 'children'),
    Input('control-group-chart', 'clickData'),
    Input('data-leakage-pie', 'clickData'),
    Input('harmful-content-pie', 'clickData'),
    Input('app-grounding-pie', 'clickData'),
    Input('control-group-summary-table', 'active_cell'),
    State('control-group-summary-table', 'data'),
    prevent_initial_call=True
)
def handle_control_analysis_click(control_group_click, leakage_click, harmful_click, grounding_click, table_click, table_data):
    """Handle Control Analysis tab clicks"""
    try:
        ctx = callback_context
        
        if not ctx.triggered or not ctx.triggered[0]['value']:
            return False, ""
    except Exception as e:
        print(f"Error in control analysis callback: {e}")
        return False, ""
    
    # Handle control group summary table clicks
    if ctx.triggered[0]['prop_id'] == 'control-group-summary-table.active_cell':
        if not table_click or not table_data:
            return False, ""
        
        # Get the row and column data from the table
        row_idx = table_click['row']
        col_id = table_click['column_id']
        row_data = table_data[row_idx]
        control_group = row_data['Control Group']
        
        # Filter data based on the clicked column
        if col_id == 'Total_Tests':
            # Show all tests for this control group
            filtered_data = data[data['control_group'] == control_group]
            title = f"All Tests for: {control_group}"
        elif col_id == 'Failed_Tests':
            # Show only failed tests for this control group
            filtered_data = data[
                (data['control_group'] == control_group) &
                (data['status'] == 'fail')
            ]
            title = f"Failed Tests for: {control_group}"
        elif col_id == 'Passed_Tests':
            # Show only passed tests for this control group
            filtered_data = data[
                (data['control_group'] == control_group) &
                (data['status'] == 'pass')
            ]
            title = f"Passed Tests for: {control_group}"
        elif col_id == 'Unknown_Tests':
            # Show only unknown tests for this control group
            filtered_data = data[
                (data['control_group'] == control_group) &
                (data['status'] == 'unknown')
            ]
            title = f"Unknown Tests for: {control_group}"
        elif col_id == 'Control Group':
            # Show all tests for this control group
            filtered_data = data[data['control_group'] == control_group]
            title = f"All Tests for: {control_group}"
        else:
            return False, ""
        
        if filtered_data.empty:
            return True, dbc.Alert("No records found for this selection", color="info")
        
        # Create detailed record cards
        record_cards = []
        for _, record in filtered_data.head(10).iterrows():
            record_cards.append(create_record_card(record))
        
        content = [
            html.H5(title, className="text-white mb-3"),
            html.P(f"Found {len(filtered_data)} records", className="text-muted mb-3"),
            html.Div(record_cards, className="record-cards")
        ]
        
        return True, content
    
    # Handle chart clicks
    click_data = ctx.triggered[0]['value']
    if not click_data or 'points' not in click_data:
        return False, ""
    
    point = click_data['points'][0]
    label = point.get('label', '')
    
    # Filter data based on the clicked category
    if ctx.triggered[0]['prop_id'] == 'control-group-chart.clickData':
        filtered_data = data[data['product_category'] == label]
    elif ctx.triggered[0]['prop_id'] == 'data-leakage-pie.clickData':
        # For data leakage pie chart
        filtered_data = data[(data['product_category'] == 'data_leak') & (data['status'] == 'fail') & (data['control_id'] == label)]
    elif ctx.triggered[0]['prop_id'] == 'harmful-content-pie.clickData':
        # For harmful content pie chart
        filtered_data = data[(data['product_category'] == 'harmful_content') & (data['status'] == 'fail') & (data['control_id'] == label)]
    elif ctx.triggered[0]['prop_id'] == 'app-grounding-pie.clickData':
        # For app grounding pie chart
        filtered_data = data[(data['product_category'] == 'app_grounding') & (data['status'] == 'fail') & (data['control_id'] == label)]
    else:
        return False, ""
    
    if filtered_data.empty:
        return True, dbc.Alert("No records found for this selection", color="info")
    
    # Create detailed record cards
    record_cards = []
    for _, record in filtered_data.head(10).iterrows():
        record_cards.append(create_record_card(record))
    
    content = [
        html.H5(f"Records for: {label}", className="text-white mb-3"),
        html.P(f"Found {len(filtered_data)} records", className="text-muted mb-3"),
        html.Div(record_cards, className="record-cards")
    ]
    
    return True, content

# Evasion Analysis tab callback
@app.callback(
    Output('evasion-analysis-modal', 'is_open'),
    Output('evasion-analysis-details-content', 'children'),
    Input('evasion-usage-chart', 'clickData'),
    Input('evasion-table', 'active_cell'),
    State('evasion-table', 'data'),
    prevent_initial_call=True
)
def handle_evasion_analysis_click(evasion_click, table_click, table_data):
    """Handle Evasion Analysis tab clicks"""
    try:
        ctx = callback_context
        
        if not ctx.triggered or not ctx.triggered[0]['value']:
            return False, ""
    except Exception as e:
        print(f"Error in evasion analysis callback: {e}")
        return False, ""
    
    # Handle table clicks
    if ctx.triggered[0]['prop_id'] == 'evasion-table.active_cell':
        if not table_click or not table_data:
            return False, ""
        
        # Get the row and column data from the table
        row_idx = table_click['row']
        col_id = table_click['column_id']
        row_data = table_data[row_idx]
        evasion_technique = row_data['Evasion']
        
        # Filter data based on the clicked column
        if col_id == 'Total_Tests':
            # Show all tests for this evasion technique
            filtered_data = data[data['evasions_applied'].apply(lambda x: any(evasion_technique in str(e) for e in x) if isinstance(x, list) else False)]
            title = f"All Tests for: {evasion_technique}"
        elif col_id == 'Failed_Tests':
            # Show only failed tests for this evasion technique
            filtered_data = data[
                data['evasions_applied'].apply(lambda x: any(evasion_technique in str(e) for e in x) if isinstance(x, list) else False) &
                (data['status'] == 'fail')
            ]
            title = f"Failed Tests for: {evasion_technique}"
        elif col_id == 'Evasion':
            # Show all tests for this evasion technique
            filtered_data = data[data['evasions_applied'].apply(lambda x: any(evasion_technique in str(e) for e in x) if isinstance(x, list) else False)]
            title = f"All Tests for: {evasion_technique}"
        else:
            return False, ""
        
        if filtered_data.empty:
            return True, dbc.Alert("No records found for this selection", color="info")
        
        # Create detailed record cards
        record_cards = []
        for _, record in filtered_data.head(10).iterrows():
            record_cards.append(create_record_card(record))
        
        content = [
            html.H5(title, className="text-white mb-3"),
            html.P(f"Found {len(filtered_data)} records", className="text-muted mb-3"),
            html.Div(record_cards, className="record-cards")
        ]
        
        return True, content
    
    # Handle chart clicks
    click_data = ctx.triggered[0]['value']
    if not click_data or 'points' not in click_data:
        return False, ""
    
    point = click_data['points'][0]
    label = point.get('label', '')
    
    # For evasion usage chart, filter by evasion technique
    filtered_data = data[data['evasions_applied'].apply(lambda x: any(label in str(e) for e in x) if isinstance(x, list) else False)]
    
    if filtered_data.empty:
        return True, dbc.Alert("No records found for this selection", color="info")
    
    # Create detailed record cards
    record_cards = []
    for _, record in filtered_data.head(10).iterrows():
        record_cards.append(create_record_card(record))
    
    content = [
        html.H5(f"Records for: {label}", className="text-white mb-3"),
        html.P(f"Found {len(filtered_data)} records", className="text-muted mb-3"),
        html.Div(record_cards, className="record-cards")
    ]
    
    return True, content

# Attack Paths tab callback
@app.callback(
    Output('attack-paths-modal', 'is_open'),
    Output('attack-paths-details-content', 'children'),
    Input('attack-paths-pie', 'clickData'),
    Input('attack-paths-matrix', 'clickData'),
    prevent_initial_call=True
)
def handle_attack_paths_click(attack_click, matrix_click):
    """Handle Attack Paths tab clicks - only show popup for final level (evasion + control)"""
    ctx = callback_context
    
    if not ctx.triggered or not ctx.triggered[0]['value']:
        return False, ""
    
    click_data = ctx.triggered[0]['value']
    if not click_data or 'points' not in click_data:
        return False, ""
    
    point = click_data['points'][0]
    label = point.get('label', '')
    
    # Debug: Print click data to understand the structure
    print(f"DEBUG: Click data structure: {click_data}")
    print(f"DEBUG: Point data: {point}")
    print(f"DEBUG: Label: {label}")
    print(f"DEBUG: Point ID: {point.get('id', 'No ID')}")
    print(f"DEBUG: Point parent: {point.get('parent', 'No parent')}")
    print(f"DEBUG: Point path: {point.get('path', 'No path')}")
    
    # Only show popup for the final level (evasion + control combination)
    if ctx.triggered[0]['prop_id'] == 'attack-paths-pie.clickData':
        # Get the path information from the sunburst click
        path_info = point.get('id', '')
        path_data = point.get('path', '')
        parent = point.get('parent', '')
        
        # Try to determine if this is the final level (evasion + control)
        # Check if we have a parent (meaning this is not the root) and if the label looks like a control
        is_final_level = False
        evasion = None
        control = None
        
        # Check if this is the final level (third ring) by examining the path structure
        # The path should be: Base Prompt/evasion/control
        current_path = point.get('currentPath', '')
        point_id = point.get('id', '')
        label = point.get('label', '')
        
        # Debug the actual structure
        print(f"DEBUG: current_path: '{current_path}', point_id: '{point_id}', label: '{label}'")
        
        # Check if this is a third-level click by examining the point ID structure
        # Third level should have ID like "Base Prompt/evasion/control"
        if point_id and '/' in point_id:
            id_parts = point_id.split('/')
            if len(id_parts) == 3 and id_parts[0] == 'Base Prompt':
                is_final_level = True
                evasion = id_parts[1]  # Second part is the evasion
                control = id_parts[2]  # Third part is the control
                print(f"DEBUG: Final level detected via ID - Evasion: {evasion}, Control: {control}")
            else:
                print(f"DEBUG: Not final level - id_parts: {id_parts}")
                return False, ""
        else:
            print(f"DEBUG: Not final level - no valid point ID")
            return False, ""
        
        if is_final_level and evasion and control:
            print(f"DEBUG: Final level detected - Evasion: {evasion}, Control: {control}")
            
            # Filter for records that match this specific evasion-control combination
            filtered_data = data[
                data['evasions_applied'].apply(
                    lambda x: any(evasion in str(e) for e in x) if isinstance(x, list) else False
                ) & 
                (data['control_id'] == control) &
                (data['status'] == 'fail')  # Only show failed attacks
            ]
            
            if not filtered_data.empty:
                # Create detailed record cards
                record_cards = []
                for _, record in filtered_data.head(10).iterrows():
                    record_cards.append(create_record_card(record))
                
                content = [
                    html.H5(f"Attack Path: {evasion} → {control}", className="text-white mb-3"),
                    html.P(f"Found {len(filtered_data)} failed attacks", className="text-muted mb-3"),
                    html.Div(record_cards, className="record-cards")
                ]
                
                return True, content
            else:
                return True, dbc.Alert("No failed attacks found for this evasion-control combination", color="info")
        else:
            # Not at final level, don't show popup
            print(f"DEBUG: Not final level - is_final_level: {is_final_level}, evasion: {evasion}, control: {control}")
            return False, ""
    
    elif ctx.triggered[0]['prop_id'] == 'attack-paths-matrix.clickData':
        # For matrix clicks, get the x and y coordinates to find evasion-control combination
        x_val = point.get('x', '')  # Control ID
        y_val = point.get('y', '')  # Evasion technique
        
        if x_val and y_val:
            # Filter for records that have this specific evasion-control combination and failed
            filtered_data = data[
                data['evasions_applied'].apply(
                    lambda x: any(y_val in str(e) for e in x) if isinstance(x, list) else False
                ) & 
                (data['control_id'] == x_val) &
                (data['status'] == 'fail')  # Only show failed attacks
            ]
            
            if not filtered_data.empty:
                # Create detailed record cards
                record_cards = []
                for _, record in filtered_data.head(10).iterrows():
                    record_cards.append(create_record_card(record))
                
                content = [
                    html.H5(f"Attack Path: {y_val} → {x_val}", className="text-white mb-3"),
                    html.P(f"Found {len(filtered_data)} failed attacks", className="text-muted mb-3"),
                    html.Div(record_cards, className="record-cards")
                ]
                
                return True, content
            else:
                return True, dbc.Alert("No failed attacks found for this evasion-control combination", color="info")
        else:
            return False, ""
    else:
        return False, ""

# Multiturn analysis callback
@app.callback(
    Output('multiturn-analysis-content', 'children'),
    Input('main-tabs', 'active_tab'),
    prevent_initial_call=False
)
def update_multiturn_analysis(active_tab):
    """Update multiturn analysis content"""
    if active_tab != "control":
        return ""
    
    # Get multiturn data - check for chat_history column and filter properly
    if 'chat_history' not in data.columns:
        return dbc.Alert("No chat_history column found in data", color="warning")
    
    # Filter for records with actual chat history content
    multiturn_data = data[
        data['chat_history'].notna() & 
        (data['chat_history'] != '') & 
        (data['chat_history'] != '[]') & 
        (data['chat_history'] != 'null') &
        (data['chat_history'].astype(str).str.len() > 10)  # Ensure it's not just empty brackets
    ]
    
    if multiturn_data.empty:
        return dbc.Alert("No multiturn attacks found", color="info")
    
    # Calculate multiturn metrics
    multiturn_count = len(multiturn_data)
    multiturn_with_evasions = len(multiturn_data[multiturn_data['has_evasions'] == True])
    successful_multiturn = len(multiturn_data[multiturn_data['status'] == 'fail'])
    
    # Get successful multiturn attacks by control
    successful_multiturn_by_control = multiturn_data[multiturn_data['status'] == 'fail'].groupby('control_id').size().reset_index(name='Successful_Leaks')
    successful_multiturn_by_control = successful_multiturn_by_control.sort_values('Successful_Leaks', ascending=False)
    
    # Create metrics cards
    metrics_cards = dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.H4(f"{multiturn_count}", className="text-info"),
                        html.P("Total Multiturn Attacks", className="text-muted")
                    ], id="total-multiturn-card", style={"cursor": "pointer"})
                ], className="text-center")
            ])
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.H4(f"{multiturn_with_evasions}", className="text-warning"),
                        html.P("With Evasions", className="text-muted")
                    ], id="multiturn-evasions-card", style={"cursor": "pointer"})
                ], className="text-center")
            ])
        ], width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Div([
                        html.H4(f"{successful_multiturn}", className="text-danger"),
                        html.P("Successful Leaks", className="text-muted")
                    ], id="successful-multiturn-card", style={"cursor": "pointer"})
                ], className="text-center")
            ])
        ], width=4)
    ], className="mb-4")
    
    # Create table for successful multiturn attacks by control
    if not successful_multiturn_by_control.empty:
        table = dash_table.DataTable(
            data=successful_multiturn_by_control.to_dict('records'),
            columns=[
                {"name": "Control ID", "id": "control_id", "type": "text"},
                {"name": "Successful Leaks", "id": "Successful_Leaks", "type": "numeric"}
            ],
            style_cell={'backgroundColor': '#1a1a1a', 'color': '#ffffff', 'textAlign': 'left'},
            style_header={'backgroundColor': '#2d2d2d', 'color': '#ffffff', 'fontWeight': 'bold'},
            style_data={'border': '1px solid #333'},
            page_size=10
        )
    else:
        table = html.P("No successful multiturn leaks found", className="text-muted")
    
    return [
        metrics_cards,
        html.H6("Successful Multiturn Leaks by Control", className="text-white mb-3"),
        table
    ]


def create_record_card(record):
    """Create a detailed record card with enhanced metadata"""
    # Parse user_interaction_record if it exists
    user_interaction = record.get('user_interaction_record', '')
    attack_prompt = "N/A"
    bot_response = "N/A"
    
    if user_interaction and isinstance(user_interaction, str):
        try:
            import json
            interaction_data = json.loads(user_interaction)
            attack_prompt = interaction_data.get('assessment_prompt', 'N/A')
            bot_response = interaction_data.get('response', 'N/A')
        except:
            # If JSON parsing fails, try to extract from string format
            import re
            # Look for assessment_prompt= pattern
            prompt_match = re.search(r'assessment_prompt=([^,}]+)', user_interaction)
            if prompt_match:
                attack_prompt = prompt_match.group(1).strip()
            
            # Look for response= pattern
            response_match = re.search(r'response=([^,}]+)', user_interaction)
            if response_match:
                bot_response = response_match.group(1).strip()
    
    # Get explanation
    explanation = record.get('explanation', 'N/A')
    
    # Helper function to create expandable text
    def create_expandable_text(text, field_name, max_length=200):
        if not text or text == 'N/A':
            return html.Span('N/A', style={'color': '#ffffff'})
        
        text_str = str(text)
        if len(text_str) <= max_length:
            return html.Span(text_str, style={'color': '#ffffff', 'whiteSpace': 'pre-wrap', 'wordBreak': 'break-word'})
        
        # Use HTML details/summary for native expand/collapse functionality
        short_text = text_str[:max_length] + "..."
        full_text = text_str
        
        return html.Details([
                html.Summary([
                html.Span(f"({len(text_str)} chars): ", style={'color': '#6366f1', 'fontWeight': 'bold', 'fontSize': '12px'}),
                html.Span(short_text, style={'color': '#ffffff', 'whiteSpace': 'pre-wrap', 'wordBreak': 'break-word'}),
                html.Span(" (click to expand)", style={'color': '#9ca3af', 'fontSize': '12px', 'marginLeft': '5px'})
            ], style={'cursor': 'pointer', 'color': '#ffffff'}),
                html.Div([
                html.Span(full_text, style={'color': '#ffffff', 'whiteSpace': 'pre-wrap', 'wordBreak': 'break-word'})
            ], style={'marginTop': '8px', 'padding': '8px', 'backgroundColor': '#1f2937', 
                     'borderRadius': '4px', 'border': '1px solid #374151'})
            ], style={'marginTop': '5px'})
    
    return html.Div([
        html.Div([
            html.Div([
                html.Span("ID: ", style={'fontWeight': 'bold', 'color': '#6366f1'}),
                html.Span(str(record.get('id', 'N/A')), style={'color': '#ffffff'})
            ], style={'marginBottom': '10px'}),
            html.Div([
                html.Span("Status: ", style={'fontWeight': 'bold', 'color': '#6366f1'}),
                html.Span(str(record.get('status', 'N/A')), 
                         style={'color': '#10b981' if record.get('status') == 'pass' else '#ef4444'})
            ], style={'marginBottom': '10px'}),
            html.Div([
                html.Span("Control: ", style={'fontWeight': 'bold', 'color': '#6366f1'}),
                html.Span(str(record.get('control_id', 'N/A')), style={'color': '#ffffff'})
            ], style={'marginBottom': '10px'}),
            html.Div([
                html.Span("Base Prompt: ", style={'fontWeight': 'bold', 'color': '#6366f1'}),
                create_expandable_text(record.get('base_prompt', 'N/A'), 'base_prompt')
            ], style={'marginBottom': '10px'}),
            html.Div([
                html.Span("Attack Prompt: ", style={'fontWeight': 'bold', 'color': '#f59e0b'}),
                create_expandable_text(attack_prompt, 'attack_prompt')
            ], style={'marginBottom': '10px'}),
            html.Div([
                html.Span("Bot Response: ", style={'fontWeight': 'bold', 'color': '#10b981'}),
                create_expandable_text(bot_response, 'bot_response')
            ], style={'marginBottom': '10px'}),
            html.Div([
                html.Span("Explanation: ", style={'fontWeight': 'bold', 'color': '#8b5cf6'}),
                create_expandable_text(explanation, 'explanation')
            ], style={'marginBottom': '10px'}),
            html.Div([
                html.Span("Evasions: ", style={'fontWeight': 'bold', 'color': '#6366f1'}),
                html.Span(str(record.get('evasions_applied', [])), style={'color': '#ffffff'})
            ], style={'marginBottom': '10px'}),
            html.Div([
                html.Span("Multiturn: ", style={'fontWeight': 'bold', 'color': '#06b6d4'}),
                html.Span("Yes" if record.get('chat_history') and str(record.get('chat_history')).strip() not in ['', '[]', 'null'] else "No", 
                         style={'color': '#10b981' if record.get('chat_history') and str(record.get('chat_history')).strip() not in ['', '[]', 'null'] else '#ef4444'})
            ], style={'marginBottom': '10px'})
        ], style={'backgroundColor': '#0f0f0f', 'border': '1px solid #333', 'borderRadius': '8px', 'padding': '15px', 'margin': '10px 0'})
    ])

if __name__ == "__main__":
    print("Starting enhanced Straiker dashboard...")
    app.run(debug=True, host="0.0.0.0", port=8050)
