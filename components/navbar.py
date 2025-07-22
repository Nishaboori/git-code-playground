import streamlit as st
from datetime import datetime

def render_navbar():
    """Render the top navigation bar with persona switching"""
    
    personas = [
        {
            'id': 'data-scientist',
            'name': 'Data Scientist',
            'icon': '🧠',
            'color': '#8b5cf6',
            'description': 'Model development and experimentation'
        },
        {
            'id': 'mlops-engineer', 
            'name': 'MLOps Engineer',
            'icon': '🔧',
            'color': '#3b82f6',
            'description': 'Deployment and infrastructure management'
        },
        {
            'id': 'risk-operations',
            'name': 'Risk Operations',
            'icon': '🛡️',
            'color': '#ef4444',
            'description': 'Fraud monitoring and strategy management'
        },
        {
            'id': 'executive',
            'name': 'Executive',
            'icon': '📈',
            'color': '#10b981',
            'description': 'Strategic oversight and KPIs'
        }
    ]
    
    # Header with branding and persona selector
    st.markdown("""
        <div class="main-header fade-in">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="width: 40px; height: 40px; background: white; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: bold; color: #004c91;">
                        W
                    </div>
                    <div>
                        <h1 style="margin: 0; font-size: 1.8rem; font-weight: bold;">Seller Risk MLOps Platform</h1>
                        <p style="margin: 0; font-size: 0.9rem; opacity: 0.9;">End-to-End ML Platform • Interactive Demo</p>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem; background: rgba(255,255,255,0.2); padding: 0.5rem 1rem; border-radius: 20px;">
                        <div style="width: 8px; height: 8px; background: #00ff00; border-radius: 50%; animation: pulse 2s infinite;"></div>
                        <span style="font-size: 0.9rem;">All Systems Operational</span>
                    </div>
                    <div style="font-size: 0.9rem; opacity: 0.9;">""" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + """</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Persona selector
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("### 👤 Select User Persona")
        
        # Create persona selection buttons
        cols = st.columns(len(personas))
        for i, persona in enumerate(personas):
            with cols[i]:
                if st.button(
                    f"{persona['icon']} {persona['name']}", 
                    key=f"persona_{persona['id']}",
                    help=persona['description'],
                    use_container_width=True
                ):
                    st.session_state.current_persona = persona['id']
                    st.rerun()
        
        # Show current persona
        if st.session_state.current_persona:
            current = next((p for p in personas if p['id'] == st.session_state.current_persona), None)
            if current:
                st.success(f"🎯 **Current View**: {current['icon']} {current['name']} - {current['description']}")
        else:
            st.info("🏠 **Current View**: Platform Overview - General platform view")
    
    st.markdown("---")