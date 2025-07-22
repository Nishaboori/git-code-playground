import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
from utils.mock_data import (
    generate_time_series_data, 
    generate_system_health_data,
    generate_recent_activity,
    generate_model_performance_data
)

def render_metric_card(title, value, change, icon, trend="neutral"):
    """Render a metric card with styling"""
    trend_colors = {
        "positive": "#10b981",
        "negative": "#ef4444", 
        "neutral": "#6b7280"
    }
    
    trend_icons = {
        "positive": "📈",
        "negative": "📉",
        "neutral": "➡️"
    }
    
    st.markdown(f"""
        <div class="metric-card fade-in">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1rem;">
                <div style="font-size: 2rem;">{icon}</div>
                <div style="color: {trend_colors[trend]}; font-size: 1.2rem;">{trend_icons[trend]}</div>
            </div>
            <div class="metric-value">{value}</div>
            <div class="metric-title">{title}</div>
            <div class="metric-change {trend}" style="color: {trend_colors[trend]};">
                {change}
            </div>
        </div>
    """, unsafe_allow_html=True)

def render_platform_overview():
    """Render the main platform overview dashboard"""
    
    st.title("🏠 Platform Overview")
    st.markdown("Comprehensive view of your MLOps platform")
    
    # Get current metrics
    metrics = st.session_state.metrics
    
    # Key Metrics Grid
    st.markdown("### 📊 Key Performance Indicators")
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col1:
        render_metric_card(
            "Total Models",
            str(metrics['total_models']),
            "+3 this week",
            "🧠",
            "positive"
        )
    
    with col2:
        render_metric_card(
            "Active Deployments", 
            str(metrics['active_deployments']),
            "+2 today",
            "🚀",
            "positive"
        )
    
    with col3:
        render_metric_card(
            "Avg Response Time",
            f"{metrics['avg_latency']:.1f}ms",
            "Target: <50ms",
            "⚡",
            "positive" if metrics['avg_latency'] < 30 else "neutral"
        )
    
    with col4:
        render_metric_card(
            "Fraud Prevention Rate",
            f"{metrics['fraud_prevented']:.1f}%",
            "+2.3% vs last month",
            "🛡️",
            "positive"
        )
    
    with col5:
        render_metric_card(
            "Cost Savings",
            f"${metrics['cost_savings']:.1f}M",
            "This quarter",
            "💰",
            "positive"
        )
    
    with col6:
        render_metric_card(
            "System Uptime",
            f"{metrics['system_uptime']:.2f}%",
            "Last 30 days",
            "🔄",
            "positive"
        )
    
    st.markdown("---")
    
    # Charts Section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Performance Trends")
        
        # Generate time series data
        ts_data = generate_time_series_data()
        
        # Create performance chart
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=ts_data['timestamp'],
            y=ts_data['latency'],
            mode='lines+markers',
            name='Latency (ms)',
            line=dict(color='#3b82f6', width=2),
            yaxis='y'
        ))
        
        fig.add_trace(go.Scatter(
            x=ts_data['timestamp'],
            y=ts_data['throughput']/50,  # Scale for visualization
            mode='lines+markers', 
            name='Throughput (req/s ÷ 50)',
            line=dict(color='#10b981', width=2),
            yaxis='y'
        ))
        
        fig.update_layout(
            height=350,
            showlegend=True,
            xaxis_title="Time",
            yaxis_title="Metrics",
            template="plotly_white"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 🔄 Deployment Flow Distribution")
        
        # Deployment flow data
        flow_data = pd.DataFrame({
            'Flow': ['Same Project', 'Cross-Project', 'Element→WCNP', 'External→Element'],
            'Count': [156, 89, 67, 34],
            'Percentage': [45, 26, 19, 10]
        })
        
        fig_pie = px.pie(
            flow_data, 
            values='Count', 
            names='Flow',
            color_discrete_sequence=['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6']
        )
        fig_pie.update_layout(height=350)
        
        st.plotly_chart(fig_pie, use_container_width=True)
    
    # System Health and Activity Section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🏥 System Health")
        
        health_data = generate_system_health_data()
        
        for component in health_data:
            status_class = f"status-{component['status']}"
            status_emoji = "✅" if component['status'] == 'healthy' else "⚠️"
            
            st.markdown(f"""
                <div class="custom-card">
                    <div style="display: flex; justify-content: space-between; align-items: center;">
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <span style="font-size: 1.2rem;">{status_emoji}</span>
                            <strong>{component['name']}</strong>
                        </div>
                        <div style="text-align: right;">
                            <div style="font-size: 0.9rem; font-weight: 500;">{component['uptime']}</div>
                            <div style="font-size: 0.8rem; color: #666;">{component['response_time']}</div>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📋 Recent Activity")
        
        activities = generate_recent_activity()
        
        for activity in activities[:6]:  # Show last 6 activities
            severity_colors = {
                'success': '#10b981',
                'warning': '#f59e0b', 
                'error': '#ef4444',
                'info': '#3b82f6'
            }
            
            severity_icons = {
                'success': '✅',
                'warning': '⚠️',
                'error': '❌', 
                'info': 'ℹ️'
            }
            
            color = severity_colors.get(activity['severity'], '#6b7280')
            icon = severity_icons.get(activity['severity'], '•')
            
            st.markdown(f"""
                <div style="display: flex; align-items: start; gap: 0.75rem; padding: 0.75rem; border-left: 3px solid {color}; background: white; border-radius: 8px; margin: 0.5rem 0;">
                    <div style="font-size: 1rem; margin-top: 0.1rem;">{icon}</div>
                    <div style="flex: 1;">
                        <div style="font-size: 0.9rem; color: #333; margin-bottom: 0.25rem;">{activity['event']}</div>
                        <div style="font-size: 0.8rem; color: #666;">{activity['time']}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick Actions Section
    st.markdown("### 🚀 Quick Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🚀 Deploy New Model", use_container_width=True):
            st.success("Deployment pipeline initiated!")
    
    with col2:
        if st.button("🧪 Create Experiment", use_container_width=True):
            st.success("New experiment created!")
    
    with col3:
        if st.button("🛡️ Monitor Fraud", use_container_width=True):
            st.info("Opening fraud monitoring dashboard...")
    
    with col4:
        if st.button("📊 System Health", use_container_width=True):
            st.info("System diagnostics running...")
    
    # Model Performance Comparison
    st.markdown("---")
    st.markdown("### 🎯 Model Performance Comparison")
    
    model_data = generate_model_performance_data()
    df_models = pd.DataFrame(model_data)
    
    fig_models = px.bar(
        df_models,
        x='name',
        y=['accuracy', 'precision', 'recall', 'f1_score'],
        title="Model Performance Metrics",
        barmode='group',
        color_discrete_sequence=['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6']
    )
    
    fig_models.update_layout(
        height=400,
        xaxis_title="Model",
        yaxis_title="Score (%)",
        template="plotly_white"
    )
    
    st.plotly_chart(fig_models, use_container_width=True)
    
    # Success Metrics Summary
    st.markdown("---")
    st.markdown("### 🎯 Platform Impact Summary")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="custom-card">
                <h4>🚀 Deployment Velocity</h4>
                <p><strong>From weeks to hours</strong></p>
                <p>67% reduction in time-to-market</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="custom-card">
                <h4>💼 Developer Productivity</h4>
                <p><strong>85% time on models</strong></p>
                <p>vs infrastructure management</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="custom-card">
                <h4>💰 ROI Achievement</h4>
                <p><strong>340% return</strong></p>
                <p>on MLOps platform investment</p>
            </div>
        """, unsafe_allow_html=True)