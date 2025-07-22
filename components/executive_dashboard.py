import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def render_executive_dashboard():
    """Render the Executive dashboard with strategic KPIs"""
    
    st.title("📈 Executive Dashboard")
    st.markdown("Strategic overview and key performance indicators")
    
    # Executive summary metrics
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Platform ROI", "340%", "+45%")
    with col2:
        st.metric("Cost Savings", "$2.4M", "+$340K")
    with col3:
        st.metric("Time to Market", "67% faster", "+12%")
    with col4:
        st.metric("Platform Adoption", "90%", "+15%")
    with col5:
        st.metric("Model Accuracy", "92.1%", "+3.2%")
    
    st.markdown("---")
    
    # Strategic overview sections
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 💰 Financial Impact")
        
        # ROI over time
        quarters = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 'Q1 2024', 'Q2 2024']
        roi_values = [120, 180, 235, 280, 315, 340]
        
        fig_roi = px.line(
            x=quarters,
            y=roi_values,
            title="Platform ROI Growth (%)",
            markers=True
        )
        fig_roi.update_traces(line_color='#10b981', line_width=4, marker_size=8)
        fig_roi.update_layout(height=300, template="plotly_white")
        st.plotly_chart(fig_roi, use_container_width=True)
        
        # Cost breakdown
        st.markdown("#### Cost Savings Breakdown")
        cost_categories = ['Fraud Prevention', 'Operational Efficiency', 'Developer Productivity', 'Infrastructure']
        savings = [1.2, 0.6, 0.4, 0.2]
        
        fig_costs = px.bar(
            x=cost_categories,
            y=savings,
            title="Cost Savings by Category ($M)",
            color=savings,
            color_continuous_scale='Greens'
        )
        fig_costs.update_layout(height=300, template="plotly_white")
        st.plotly_chart(fig_costs, use_container_width=True)
    
    with col2:
        st.markdown("### 🎯 Strategic Objectives")
        
        # Objective progress
        objectives = [
            {"name": "Fraud Prevention Rate", "target": 95, "current": 89.7, "status": "On Track"},
            {"name": "Platform Adoption", "target": 95, "current": 90, "status": "Ahead"},
            {"name": "Model Accuracy", "target": 90, "current": 92.1, "status": "Exceeded"},
            {"name": "Cost Reduction", "target": 20, "current": 24, "status": "Exceeded"},
        ]
        
        for obj in objectives:
            progress = min(obj['current'] / obj['target'], 1.0)
            status_color = '#10b981' if obj['status'] == 'Exceeded' else '#3b82f6' if obj['status'] == 'Ahead' else '#f59e0b'
            
            st.markdown(f"**{obj['name']}**")
            st.progress(progress)
            
            col_a, col_b, col_c = st.columns([1, 1, 1])
            with col_a:
                st.caption(f"Current: {obj['current']}")
            with col_b:
                st.caption(f"Target: {obj['target']}")
            with col_c:
                st.markdown(f"<span style='color: {status_color}; font-weight: bold; font-size: 0.8em;'>{obj['status']}</span>", unsafe_allow_html=True)
            
            st.markdown("")
        
        # Team productivity metrics
        st.markdown("#### Team Productivity")
        
        productivity_data = {
            'Metric': ['Model Development Time', 'Deployment Frequency', 'Issue Resolution', 'Feature Velocity'],
            'Improvement': ['-67%', '+340%', '-45%', '+125%'],
            'Status': ['Excellent', 'Excellent', 'Good', 'Excellent']
        }
        
        for i, metric in enumerate(productivity_data['Metric']):
            col_a, col_b, col_c = st.columns([2, 1, 1])
            with col_a:
                st.markdown(f"**{metric}**")
            with col_b:
                improvement = productivity_data['Improvement'][i]
                color = '#10b981' if improvement.startswith('+') or improvement.startswith('-') else '#6b7280'
                st.markdown(f"<span style='color: {color}; font-weight: bold;'>{improvement}</span>", unsafe_allow_html=True)
            with col_c:
                status = productivity_data['Status'][i]
                status_color = '#10b981' if status == 'Excellent' else '#f59e0b'
                st.markdown(f"<span style='color: {status_color}; font-size: 0.8em;'>{status}</span>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Platform adoption and usage
    st.markdown("### 📊 Platform Adoption & Usage")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # User adoption by role
        roles = ['Data Scientists', 'MLOps Engineers', 'Risk Analysts', 'Executives']
        adoption_rates = [95, 88, 92, 78]
        
        fig_adoption = px.bar(
            x=roles,
            y=adoption_rates,
            title="Adoption Rate by Role (%)",
            color=adoption_rates,
            color_continuous_scale='Blues'
        )
        fig_adoption.update_layout(height=300, template="plotly_white")
        st.plotly_chart(fig_adoption, use_container_width=True)
    
    with col2:
        # Monthly active models
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
        active_models = [28, 32, 38, 42, 45, 47]
        
        fig_models = px.line(
            x=months,
            y=active_models,
            title="Active Models Growth",
            markers=True
        )
        fig_models.update_traces(line_color='#8b5cf6', line_width=3, marker_size=8)
        fig_models.update_layout(height=300, template="plotly_white")
        st.plotly_chart(fig_models, use_container_width=True)
    
    with col3:
        # Platform reliability
        reliability_metrics = ['Uptime', 'Performance', 'Security', 'Compliance']
        scores = [99.95, 94.2, 98.7, 100]
        
        fig_reliability = px.bar(
            x=reliability_metrics,
            y=scores,
            title="Platform Reliability Scores",
            color=scores,
            color_continuous_scale='Greens'
        )
        fig_reliability.update_layout(height=300, template="plotly_white")
        st.plotly_chart(fig_reliability, use_container_width=True)
    
    # Risk and compliance summary
    st.markdown("---")
    st.markdown("### 🛡️ Risk Management & Compliance")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Risk Mitigation Effectiveness")
        
        risk_types = ['Payment Fraud', 'Account Fraud', 'Data Breaches', 'Operational Risk']
        mitigation_scores = [94.2, 89.7, 99.1, 87.3]
        
        for i, risk_type in enumerate(risk_types):
            score = mitigation_scores[i]
            color = '#10b981' if score >= 90 else '#f59e0b' if score >= 80 else '#ef4444'
            
            col_a, col_b = st.columns([2, 1])
            with col_a:
                st.markdown(f"**{risk_type}**")
                st.progress(score / 100)
            with col_b:
                st.markdown(f"<span style='color: {color}; font-weight: bold; font-size: 1.1em;'>{score}%</span>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### Compliance Status")
        
        compliance_items = [
            {"area": "Data Privacy (GDPR)", "status": "✅ Compliant", "last_audit": "Q1 2024"},
            {"area": "Financial Regulations", "status": "✅ Compliant", "last_audit": "Q4 2023"},
            {"area": "Security Standards", "status": "✅ Compliant", "last_audit": "Q2 2024"},
            {"area": "Model Governance", "status": "⚠️ Review Needed", "last_audit": "Q1 2024"},
        ]
        
        for item in compliance_items:
            col_a, col_b, col_c = st.columns([2, 1, 1])
            with col_a:
                st.markdown(f"**{item['area']}**")
            with col_b:
                st.markdown(item['status'])
            with col_c:
                st.caption(item['last_audit'])
    
    # Future roadmap and recommendations
    st.markdown("---")
    st.markdown("### 🚀 Strategic Roadmap & Recommendations")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### Next Quarter Priorities")
        
        priorities = [
            "🎯 Expand to international markets",
            "🤖 Implement advanced AI governance",
            "📊 Launch real-time analytics platform", 
            "🔒 Enhance security monitoring",
            "📈 Scale infrastructure for 10x growth"
        ]
        
        for priority in priorities:
            st.markdown(f"• {priority}")
    
    with col2:
        st.markdown("#### Investment Recommendations")
        
        investments = [
            {"area": "AI/ML Infrastructure", "amount": "$500K", "roi": "280%"},
            {"area": "Security Enhancement", "amount": "$300K", "roi": "190%"},
            {"area": "Team Expansion", "amount": "$800K", "roi": "340%"},
            {"area": "Platform Scaling", "amount": "$400K", "roi": "220%"},
        ]
        
        for inv in investments:
            col_a, col_b, col_c = st.columns([2, 1, 1])
            with col_a:
                st.markdown(f"**{inv['area']}**")
            with col_b:
                st.markdown(inv['amount'])
            with col_c:
                st.markdown(f"<span style='color: #10b981; font-weight: bold;'>{inv['roi']}</span>", unsafe_allow_html=True)
    
    # Executive actions
    st.markdown("---")
    st.markdown("### 📋 Executive Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("📊 Detailed Report", use_container_width=True):
            st.success("Generating comprehensive executive report...")
    
    with col2:
        if st.button("💰 Budget Planning", use_container_width=True):
            st.info("Opening budget planning interface...")
    
    with col3:
        if st.button("🎯 Set Objectives", use_container_width=True):
            st.info("Strategic objective setting initiated...")
    
    with col4:
        if st.button("👥 Team Review", use_container_width=True):
            st.info("Team performance review dashboard...")
    
    # Key insights summary
    st.markdown("---")
    st.markdown("### 💡 Key Insights & Recommendations")
    
    st.success("🎉 **Platform Performance**: Exceeding targets across all key metrics with 340% ROI")
    st.info("📈 **Growth Opportunity**: Ready to scale internationally with current infrastructure")
    st.warning("⚠️ **Action Required**: Model governance framework needs review and update")
    st.info("🚀 **Strategic Focus**: Invest in AI governance and security for next phase growth")