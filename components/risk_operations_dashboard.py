import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime
from utils.mock_data import generate_fraud_detection_data

def render_risk_operations_dashboard():
    """Render the Risk Operations Center dashboard"""
    
    st.title("🛡️ Risk Operations Center")
    st.markdown("Real-time fraud monitoring and strategy management")
    
    # Key metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Fraud Prevented", "89.7%", "+2.3%")
    with col2:
        st.metric("High Risk Alerts", "23", "+5")
    with col3:
        st.metric("Avg Response Time", "1.2s", "-0.3s")
    with col4:
        st.metric("Cost Savings", "$2.4M", "+$340K")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🚨 Real-time Monitoring", "📝 Strategy Management", "👁️ Seller Monitoring", "📊 Analytics"])
    
    with tab1:
        st.markdown("### 🚨 Live Fraud Detection Events")
        
        # Auto-refresh toggle
        auto_refresh = st.checkbox("🔄 Auto-refresh (every 5 seconds)")
        
        if auto_refresh:
            st.info("🔄 Live monitoring active - events updating automatically")
        
        # Generate fraud events
        fraud_events = generate_fraud_detection_data()
        
        # Display recent events
        for event in fraud_events[:8]:
            risk_colors = {
                'LOW': '#10b981',
                'MEDIUM': '#f59e0b', 
                'HIGH': '#ef4444',
                'CRITICAL': '#dc2626'
            }
            
            color = risk_colors.get(event['risk_level'], '#6b7280')
            
            col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 2])
            
            with col1:
                st.markdown(f"**{event['seller_id']}**")
                st.caption(event['timestamp'].strftime("%H:%M:%S"))
            
            with col2:
                st.markdown(f"<span style='color: {color}; font-weight: bold;'>{event['risk_level']}</span>", unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"**{event['risk_score']:.3f}**")
            
            with col4:
                st.markdown(f"{event['confidence']:.1%}")
            
            with col5:
                st.caption(event['reason'])
            
            st.divider()
        
        # Risk level distribution
        st.markdown("### Risk Level Distribution (Last Hour)")
        risk_counts = pd.DataFrame(fraud_events).groupby('risk_level').size().reset_index(name='count')
        
        fig_risk = px.pie(
            risk_counts, 
            values='count', 
            names='risk_level',
            color='risk_level',
            color_discrete_map={'LOW': '#10b981', 'MEDIUM': '#f59e0b', 'HIGH': '#ef4444', 'CRITICAL': '#dc2626'}
        )
        st.plotly_chart(fig_risk, use_container_width=True)
    
    with tab2:
        st.markdown("### 📝 Natural Language Strategy Management")
        
        st.markdown("#### Create New Strategy")
        
        strategy_input = st.text_area(
            "Describe your fraud prevention strategy in natural language:",
            placeholder="Example: Block sellers with more than 5 declined payments in 24 hours from high-risk countries",
            height=100
        )
        
        if st.button("🔍 Analyze Strategy"):
            if strategy_input:
                # Simulate strategy analysis
                st.success("✅ Strategy analyzed successfully!")
                
                st.markdown("#### Generated Configuration:")
                st.code(f"""
# Auto-generated strategy configuration
strategy_name: "Custom Fraud Prevention Rule"
conditions:
  - payment_decline_rate_24h > 5
  - country_risk_level in ['HIGH', 'CRITICAL']
actions:
  - block_seller
  - send_alert
  - require_manual_review
confidence_threshold: 0.85
                """, language="yaml")
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("🚀 Deploy to Shadow Mode"):
                        st.info("Strategy deployed to shadow mode for testing")
                
                with col2:
                    if st.button("💾 Save as Draft"):
                        st.success("Strategy saved as draft")
        
        st.markdown("#### Active Strategies")
        
        strategies = [
            {"name": "High Decline Rate Block", "status": "🟢 Active", "effectiveness": "94.2%"},
            {"name": "New Seller Verification", "status": "🟡 Testing", "effectiveness": "87.5%"},
            {"name": "Velocity Check", "status": "🟢 Active", "effectiveness": "91.8%"},
        ]
        
        for strategy in strategies:
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            
            with col1:
                st.markdown(f"**{strategy['name']}**")
            
            with col2:
                st.markdown(strategy['status'])
            
            with col3:
                st.markdown(f"**{strategy['effectiveness']}**")
            
            with col4:
                if st.button("⚙️", key=f"config_{strategy['name']}"):
                    st.info(f"Opening configuration for {strategy['name']}")
    
    with tab3:
        st.markdown("### 👁️ Seller Risk Monitoring")
        
        # Search seller
        seller_search = st.text_input("🔍 Search Seller ID", placeholder="Enter seller ID...")
        
        if seller_search:
            st.markdown(f"#### Risk Profile: {seller_search}")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Current Risk Score", "0.847", "+0.12")
                st.metric("Account Age", "45 days", "")
            
            with col2:
                st.metric("Payment Decline Rate", "15.3%", "+2.1%")
                st.metric("Transaction Volume", "$12,450", "+$2,100")
            
            with col3:
                st.metric("Risk Level", "HIGH", "↑")
                st.metric("Last Activity", "2 hours ago", "")
            
            # Risk history chart
            st.markdown("#### Risk Score History")
            dates = pd.date_range(start='2024-01-01', periods=30, freq='D')
            risk_scores = [0.3 + 0.5 * (i/30) + 0.1 * (i % 7) / 7 for i in range(30)]
            
            fig_history = px.line(
                x=dates, 
                y=risk_scores,
                title="30-Day Risk Score Trend",
                labels={'x': 'Date', 'y': 'Risk Score'}
            )
            fig_history.update_traces(line_color='#ef4444')
            st.plotly_chart(fig_history, use_container_width=True)
        
        # Top risk sellers
        st.markdown("#### 🔥 Top Risk Sellers (Last 24h)")
        
        top_risk_sellers = [
            {"seller_id": "S12847", "risk_score": 0.947, "reason": "High payment decline rate"},
            {"seller_id": "S98234", "risk_score": 0.923, "reason": "Unusual transaction pattern"},
            {"seller_id": "S45612", "risk_score": 0.891, "reason": "New seller from high-risk region"},
        ]
        
        for seller in top_risk_sellers:
            col1, col2, col3, col4 = st.columns([2, 1, 2, 1])
            
            with col1:
                st.markdown(f"**{seller['seller_id']}**")
            
            with col2:
                st.markdown(f"<span style='color: #ef4444; font-weight: bold;'>{seller['risk_score']:.3f}</span>", unsafe_allow_html=True)
            
            with col3:
                st.caption(seller['reason'])
            
            with col4:
                if st.button("🔍", key=f"investigate_{seller['seller_id']}"):
                    st.info(f"Opening detailed investigation for {seller['seller_id']}")
    
    with tab4:
        st.markdown("### 📊 Fraud Prevention Analytics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Monthly fraud prevention trend
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
            prevention_rates = [85.2, 87.1, 88.9, 89.7, 91.2, 89.7]
            
            fig_trend = px.line(
                x=months, 
                y=prevention_rates,
                title="Monthly Fraud Prevention Rate",
                labels={'x': 'Month', 'y': 'Prevention Rate (%)'}
            )
            fig_trend.update_traces(line_color='#10b981', line_width=3)
            st.plotly_chart(fig_trend, use_container_width=True)
        
        with col2:
            # Cost savings by category
            categories = ['Payment Fraud', 'Account Fraud', 'Product Fraud', 'Other']
            savings = [1.2, 0.8, 0.3, 0.1]
            
            fig_savings = px.bar(
                x=categories,
                y=savings,
                title="Cost Savings by Fraud Type ($M)",
                color=savings,
                color_continuous_scale='Blues'
            )
            st.plotly_chart(fig_savings, use_container_width=True)
        
        # Performance summary
        st.markdown("#### 🎯 Performance Summary")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("**False Positive Rate**")
            st.markdown("2.3% (Target: <5%)")
        
        with col2:
            st.markdown("**Detection Speed**")
            st.markdown("1.2s avg (Target: <2s)")
        
        with col3:
            st.markdown("**Coverage**")
            st.markdown("99.8% of transactions")
        
        with col4:
            st.markdown("**Model Accuracy**")
            st.markdown("94.2% (Target: >90%)")
    
    # Emergency actions
    st.markdown("---")
    st.markdown("### 🚨 Emergency Actions")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("🛑 Block Seller", use_container_width=True):
            st.error("Seller blocking interface opened!")
    
    with col2:
        if st.button("📢 Send Alert", use_container_width=True):
            st.warning("Alert notification sent!")
    
    with col3:
        if st.button("🔍 Manual Review", use_container_width=True):
            st.info("Case escalated for manual review!")
    
    with col4:
        if st.button("📊 Generate Report", use_container_width=True):
            st.success("Fraud report generated!")