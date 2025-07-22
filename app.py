import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import random
import json
from streamlit_option_menu import option_menu
from streamlit_card import card

# Import our custom modules
from components.navbar import render_navbar
from components.sidebar import render_sidebar
from components.platform_overview import render_platform_overview
from components.data_scientist_dashboard import render_data_scientist_dashboard
from components.mlops_engineer_dashboard import render_mlops_engineer_dashboard
from components.risk_operations_dashboard import render_risk_operations_dashboard
from components.executive_dashboard import render_executive_dashboard
from components.workflow_visualization import render_workflow_visualization
from utils.mock_data import generate_mock_metrics, get_deployment_flows
from utils.styling import apply_custom_css

# Page configuration
st.set_page_config(
    page_title="Seller Risk MLOps Platform",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def initialize_session_state():
    """Initialize session state variables"""
    if 'current_persona' not in st.session_state:
        st.session_state.current_persona = None
    if 'active_view' not in st.session_state:
        st.session_state.active_view = 'overview'
    if 'metrics' not in st.session_state:
        st.session_state.metrics = generate_mock_metrics()
    if 'last_update' not in st.session_state:
        st.session_state.last_update = datetime.now()

def main():
    """Main application function"""
    # Initialize session state
    initialize_session_state()
    
    # Apply custom CSS styling
    apply_custom_css()
    
    # Update metrics every 3 seconds for real-time simulation
    current_time = datetime.now()
    if (current_time - st.session_state.last_update).seconds >= 3:
        st.session_state.metrics = generate_mock_metrics()
        st.session_state.last_update = current_time
        st.rerun()
    
    # Render navbar
    render_navbar()
    
    # Create main layout with sidebar
    with st.sidebar:
        st.session_state.active_view = render_sidebar()
    
    # Main content area
    if st.session_state.active_view == 'overview':
        render_platform_overview()
    elif st.session_state.active_view == 'data-scientist':
        render_data_scientist_dashboard()
    elif st.session_state.active_view == 'mlops-engineer':
        render_mlops_engineer_dashboard()
    elif st.session_state.active_view == 'risk-operations':
        render_risk_operations_dashboard()
    elif st.session_state.active_view == 'executive':
        render_executive_dashboard()
    elif st.session_state.active_view == 'workflows':
        render_workflow_visualization()
    
    # Footer
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            """
            <div style='text-align: center; color: #666; font-size: 0.9em;'>
                🛡️ Seller Risk MLOps Platform - Interactive Demo<br>
                Built with ❤️ for the Walmart MLOps Team
            </div>
            """,
            unsafe_allow_html=True
        )

if __name__ == "__main__":
    main()