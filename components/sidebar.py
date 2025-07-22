import streamlit as st
from streamlit_option_menu import option_menu

def render_sidebar():
    """Render the sidebar navigation menu"""
    
    st.markdown("### 🧭 Navigation")
    
    # Navigation menu
    selected = option_menu(
        menu_title=None,
        options=[
            "Platform Overview",
            "Data Scientist", 
            "MLOps Engineer",
            "Risk Operations",
            "Executive",
            "Workflow Visualization"
        ],
        icons=[
            "house-fill",
            "brain", 
            "gear-fill",
            "shield-fill",
            "graph-up-arrow",
            "diagram-3-fill"
        ],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#004c91", "font-size": "16px"}, 
            "nav-link": {
                "font-size": "14px", 
                "text-align": "left", 
                "margin": "0px", 
                "--hover-color": "#eee",
                "color": "#333"
            },
            "nav-link-selected": {"background-color": "#004c91"},
        }
    )
    
    st.markdown("---")
    
    # Quick Stats
    st.markdown("### 📊 Quick Stats")
    
    # Get current metrics from session state
    metrics = st.session_state.metrics
    
    # Display key metrics in sidebar
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="Active Models",
            value="12",
            delta="+2 today"
        )
    with col2:
        st.metric(
            label="Avg Latency", 
            value=f"{metrics['avg_latency']:.1f}ms",
            delta="-2.1ms"
        )
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="Fraud Rate",
            value=f"{metrics['fraud_prevented']:.1f}%",
            delta="+0.3%"
        )
    with col2:
        st.metric(
            label="Uptime",
            value=f"{metrics['system_uptime']:.2f}%",
            delta="0.01%"
        )
    
    # System Health Indicator
    st.markdown("---")
    st.markdown("### 🏥 System Health")
    
    st.markdown("""
        <div style="display: flex; align-items: center; gap: 0.5rem; padding: 0.5rem; background: #d1fae5; border-radius: 8px; margin: 0.5rem 0;">
            <div style="width: 8px; height: 8px; background: #10b981; border-radius: 50%; animation: pulse 2s infinite;"></div>
            <span style="font-size: 0.8rem; color: #065f46; font-weight: 500;">System Healthy</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("All services operational")
    
    # Map menu selection to view names
    view_mapping = {
        "Platform Overview": "overview",
        "Data Scientist": "data-scientist",
        "MLOps Engineer": "mlops-engineer", 
        "Risk Operations": "risk-operations",
        "Executive": "executive",
        "Workflow Visualization": "workflows"
    }
    
    return view_mapping.get(selected, "overview")