import streamlit as st
import time
from utils.mock_data import get_deployment_flows

def render_workflow_step(step, index, is_current=False):
    """Render a workflow step with status styling"""
    status_styles = {
        'completed': {'color': '#10b981', 'bg': '#f0fdf4', 'icon': '✅'},
        'running': {'color': '#f59e0b', 'bg': '#fffbeb', 'icon': '🔄'},
        'pending': {'color': '#6b7280', 'bg': '#f9fafb', 'icon': '⏳'},
        'failed': {'color': '#ef4444', 'bg': '#fef2f2', 'icon': '❌'}
    }
    
    style = status_styles.get(step['status'], status_styles['pending'])
    border_style = "border: 2px solid #004c91;" if is_current else ""
    
    st.markdown(f"""
        <div style="background: {style['bg']}; border-left: 4px solid {style['color']}; padding: 1rem; margin: 0.5rem 0; border-radius: 8px; {border_style}">
            <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 0.5rem;">
                <div style="display: flex; align-items: center; gap: 0.5rem;">
                    <span style="font-size: 1.2rem;">{style['icon']}</span>
                    <strong style="color: {style['color']};">{step['title']}</strong>
                </div>
                {f"<span style='color: #666; font-size: 0.9rem;'>{step.get('duration', '')}</span>" if step.get('duration') else ""}
            </div>
            <p style="margin: 0.5rem 0; color: #333;">{step['description']}</p>
            <div style="margin-top: 0.5rem;">
                {"".join([f"<div style='font-size: 0.8rem; color: #666; margin: 0.2rem 0;'>• {detail}</div>" for detail in step.get('details', [])])}
            </div>
            {f'<div style="margin-top: 0.5rem;"><div style="background: #e5e7eb; height: 6px; border-radius: 3px;"><div style="background: {style["color"]}; height: 6px; border-radius: 3px; width: 67%;"></div></div><div style="font-size: 0.8rem; color: #666; margin-top: 0.2rem;">Progress: 67%</div></div>' if step['status'] == 'running' else ''}
        </div>
    """, unsafe_allow_html=True)

def render_workflow_visualization():
    """Render the workflow visualization dashboard"""
    
    st.title("🔄 Workflow Visualization")
    st.markdown("Interactive deployment flow simulation and monitoring")
    
    # Control buttons
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col1:
        if st.button("▶️ Simulate Flow"):
            st.session_state.simulation_running = True
            st.session_state.current_step = 0
    
    with col2:
        if st.button("⏸️ Pause"):
            st.session_state.simulation_running = False
    
    with col3:
        if st.button("🔄 Reset"):
            st.session_state.simulation_running = False
            st.session_state.current_step = 0
    
    with col4:
        if st.button("📊 View Stats"):
            st.info("Flow statistics updated!")
    
    # Initialize session state
    if 'selected_flow' not in st.session_state:
        st.session_state.selected_flow = 'flow1'
    if 'simulation_running' not in st.session_state:
        st.session_state.simulation_running = False
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0
    
    st.markdown("---")
    
    # Flow Selection
    st.markdown("### 🚀 Select Deployment Flow")
    
    flows = get_deployment_flows()
    
    # Flow selection buttons
    cols = st.columns(len(flows))
    for i, flow in enumerate(flows):
        with cols[i]:
            if st.button(
                f"{flow['icon']} {flow['name']}", 
                key=f"flow_{flow['id']}",
                use_container_width=True,
                help=flow['description']
            ):
                st.session_state.selected_flow = flow['id']
                st.session_state.current_step = 0
                st.rerun()
    
    # Get selected flow
    selected_flow = next((f for f in flows if f['id'] == st.session_state.selected_flow), flows[0])
    
    st.markdown("---")
    
    # Flow Details
    st.markdown(f"### {selected_flow['icon']} {selected_flow['name']}")
    st.markdown(selected_flow['description'])
    
    # Workflow Steps
    st.markdown("#### Workflow Steps")
    
    current_step = st.session_state.current_step if st.session_state.simulation_running else -1
    
    for i, step in enumerate(selected_flow['steps']):
        render_workflow_step(step, i, is_current=(i == current_step))
        
        # Add arrow between steps (except for last step)
        if i < len(selected_flow['steps']) - 1:
            st.markdown("""
                <div style="text-align: center; margin: 0.5rem 0;">
                    <span style="font-size: 1.5rem; color: #666;">⬇️</span>
                </div>
            """, unsafe_allow_html=True)
    
    # Simulation progress
    if st.session_state.simulation_running:
        progress_value = (current_step + 1) / len(selected_flow['steps'])
        st.progress(progress_value)
        st.caption(f"Step {current_step + 1} of {len(selected_flow['steps'])}")
        
        # Auto-advance simulation
        if current_step < len(selected_flow['steps']) - 1:
            time.sleep(2)  # Wait 2 seconds
            st.session_state.current_step += 1
            st.rerun()
        else:
            st.session_state.simulation_running = False
            st.success("🎉 Workflow completed successfully!")
    
    st.markdown("---")
    
    # Flow Statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 📊 Flow Performance")
        st.metric("Average Duration", "8m 32s")
        st.metric("Success Rate", "97.3%", "0.2%")
        st.metric("Deployments Today", "23", "+5")
    
    with col2:
        st.markdown("#### 🏥 Current Status")
        st.markdown("""
            <div style="display: flex; align-items: center; gap: 0.5rem; margin: 0.5rem 0;">
                <div style="width: 8px; height: 8px; background: #10b981; border-radius: 50%; animation: pulse 2s infinite;"></div>
                <span style="font-size: 0.9rem;">All systems operational</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem; margin: 0.5rem 0;">
                <div style="width: 8px; height: 8px; background: #10b981; border-radius: 50%;"></div>
                <span style="font-size: 0.9rem;">Quality gates passing</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem; margin: 0.5rem 0;">
                <div style="width: 8px; height: 8px; background: #3b82f6; border-radius: 50%;"></div>
                <span style="font-size: 0.9rem;">Security scans complete</span>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("#### ⚡ Next Actions")
        if st.button("🚀 Deploy to Production", use_container_width=True):
            st.success("Production deployment initiated!")
        if st.button("🧪 Run A/B Test", use_container_width=True):
            st.info("A/B test configuration started!")
        if st.button("📋 View Logs", use_container_width=True):
            st.info("Opening deployment logs...")
    
    # Flow Comparison Table
    st.markdown("---")
    st.markdown("### 📋 Flow Comparison")
    
    comparison_data = []
    for flow in flows:
        comparison_data.append({
            'Flow': flow['name'],
            'Icon': flow['icon'],
            'Avg Duration': '8m 32s' if flow['id'] == 'flow1' else '12m 15s' if flow['id'] == 'flow2' else '6m 45s' if flow['id'] == 'flow3' else '15m 20s',
            'Success Rate': '97.3%' if flow['id'] == 'flow1' else '94.8%' if flow['id'] == 'flow2' else '98.9%' if flow['id'] == 'flow3' else '92.1%',
            'Complexity': 'Medium' if flow['id'] == 'flow1' else 'High' if flow['id'] == 'flow2' else 'Low' if flow['id'] == 'flow3' else 'High'
        })
    
    # Display comparison table
    for data in comparison_data:
        col1, col2, col3, col4, col5 = st.columns([1, 3, 2, 2, 2])
        
        with col1:
            st.markdown(f"<div style='font-size: 1.5rem; text-align: center;'>{data['Icon']}</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"**{data['Flow']}**")
        
        with col3:
            st.markdown(data['Avg Duration'])
        
        with col4:
            success_rate = float(data['Success Rate'].replace('%', ''))
            color = '#10b981' if success_rate >= 95 else '#f59e0b' if success_rate >= 90 else '#ef4444'
            st.markdown(f"<span style='color: {color}; font-weight: bold;'>{data['Success Rate']}</span>", unsafe_allow_html=True)
        
        with col5:
            complexity_colors = {'Low': '#10b981', 'Medium': '#f59e0b', 'High': '#ef4444'}
            color = complexity_colors.get(data['Complexity'], '#6b7280')
            st.markdown(f"<span style='color: {color}; font-weight: bold;'>{data['Complexity']}</span>", unsafe_allow_html=True)
        
        st.divider()
    
    # Real-time metrics simulation
    if st.session_state.simulation_running:
        st.markdown("### 📈 Real-time Metrics")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Current Latency", "23ms", "-2ms")
        
        with col2:
            st.metric("Throughput", "1,847 req/s", "+156")
        
        with col3:
            st.metric("Error Rate", "0.02%", "-0.01%")
        
        with col4:
            st.metric("CPU Usage", "34%", "+2%")