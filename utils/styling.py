import streamlit as st

def apply_custom_css():
    """Apply custom CSS styling for Walmart branding and modern UI"""
    st.markdown("""
    <style>
    /* Walmart Brand Colors */
    :root {
        --walmart-blue: #004c91;
        --walmart-blue-light: #0071ce;
        --walmart-blue-dark: #003d73;
        --success-green: #00a652;
        --warning-orange: #ff8c00;
        --error-red: #e53e3e;
        --accent-purple: #8b5cf6;
        --accent-teal: #14b8a6;
    }
    
    /* Main app styling */
    .main {
        padding: 0rem 1rem;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(90deg, var(--walmart-blue) 0%, var(--walmart-blue-light) 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    /* Metric card styling */
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-left: 4px solid var(--walmart-blue);
        margin-bottom: 1rem;
        transition: transform 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: var(--walmart-blue);
        margin: 0;
    }
    
    .metric-title {
        font-size: 0.9rem;
        color: #666;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .metric-change {
        font-size: 0.8rem;
        margin-top: 0.5rem;
    }
    
    .metric-change.positive {
        color: var(--success-green);
    }
    
    .metric-change.negative {
        color: var(--error-red);
    }
    
    .metric-change.neutral {
        color: #666;
    }
    
    /* Status indicators */
    .status-indicator {
        display: inline-flex;
        align-items: center;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin: 0.25rem;
    }
    
    .status-healthy {
        background-color: #d1fae5;
        color: #065f46;
    }
    
    .status-warning {
        background-color: #fef3c7;
        color: #92400e;
    }
    
    .status-error {
        background-color: #fee2e2;
        color: #991b1b;
    }
    
    .status-running {
        background-color: #dbeafe;
        color: #1e40af;
    }
    
    /* Workflow step styling */
    .workflow-step {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        position: relative;
    }
    
    .workflow-step.completed {
        border-left: 4px solid var(--success-green);
        background-color: #f0fdf4;
    }
    
    .workflow-step.running {
        border-left: 4px solid var(--warning-orange);
        background-color: #fffbeb;
    }
    
    .workflow-step.pending {
        border-left: 4px solid #d1d5db;
        background-color: #f9fafb;
    }
    
    .workflow-step.failed {
        border-left: 4px solid var(--error-red);
        background-color: #fef2f2;
    }
    
    /* Progress bar */
    .progress-bar {
        width: 100%;
        height: 8px;
        background-color: #e5e7eb;
        border-radius: 4px;
        overflow: hidden;
        margin: 0.5rem 0;
    }
    
    .progress-fill {
        height: 100%;
        background: linear-gradient(90deg, var(--walmart-blue) 0%, var(--walmart-blue-light) 100%);
        transition: width 0.5s ease;
        border-radius: 4px;
    }
    
    /* Sidebar styling */
    .sidebar .sidebar-content {
        background-color: #f8fafc;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, var(--walmart-blue) 0%, var(--walmart-blue-light) 100%);
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1rem;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0, 76, 145, 0.3);
    }
    
    /* Alert styling */
    .alert {
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid;
    }
    
    .alert-success {
        background-color: #f0fdf4;
        border-left-color: var(--success-green);
        color: #065f46;
    }
    
    .alert-warning {
        background-color: #fffbeb;
        border-left-color: var(--warning-orange);
        color: #92400e;
    }
    
    .alert-error {
        background-color: #fef2f2;
        border-left-color: var(--error-red);
        color: #991b1b;
    }
    
    .alert-info {
        background-color: #eff6ff;
        border-left-color: var(--walmart-blue);
        color: #1e40af;
    }
    
    /* Card styling */
    .custom-card {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        border: 1px solid #e5e7eb;
        margin-bottom: 1rem;
    }
    
    .custom-card h3 {
        color: var(--walmart-blue);
        margin-top: 0;
        margin-bottom: 1rem;
        font-size: 1.2rem;
        font-weight: 600;
    }
    
    /* Animation classes */
    .fade-in {
        animation: fadeIn 0.5s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom scrollbar */
    ::-webkit-scrollbar {
        width: 6px;
        height: 6px;
    }
    
    ::-webkit-scrollbar-track {
        background: #f1f5f9;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #cbd5e1;
        border-radius: 3px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #94a3b8;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .main {
            padding: 0rem 0.5rem;
        }
        
        .main-header {
            padding: 1rem;
        }
        
        .metric-card {
            padding: 1rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)