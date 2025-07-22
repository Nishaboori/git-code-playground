import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from utils.mock_data import generate_experiment_data, generate_feature_data, generate_model_performance_data

def render_data_scientist_dashboard():
    """Render the Data Scientist workspace dashboard"""
    
    st.title("🧠 Data Science Workspace")
    st.markdown("Model development, experimentation, and feature engineering")
    
    # Metrics row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Active Experiments", "8", "+2 this week")
    with col2:
        st.metric("Best Model Accuracy", "92.1%", "+3.2%")
    with col3:
        st.metric("Training Time", "2.3h", "15% faster")
    with col4:
        st.metric("Features Available", "247", "+12 new")
    
    # Tab navigation
    tab1, tab2, tab3, tab4 = st.tabs(["🧪 Experiments", "🧠 Model Registry", "📊 Feature Discovery", "🎮 Testing Playground"])
    
    with tab1:
        st.markdown("### Recent Experiments")
        
        experiments = generate_experiment_data()
        df_exp = pd.DataFrame(experiments)
        
        # Display experiments table
        for exp in experiments[:5]:
            status_colors = {
                'running': '🟡',
                'completed': '🟢', 
                'failed': '🔴',
                'pending': '⚪'
            }
            
            col1, col2, col3, col4, col5 = st.columns([3, 1, 1, 1, 1])
            
            with col1:
                st.markdown(f"**{exp['name']}**")
                st.caption(f"Created {exp['created']}")
            
            with col2:
                st.markdown(f"{status_colors[exp['status']]} {exp['status'].title()}")
            
            with col3:
                st.metric("Accuracy", f"{exp['accuracy']}%")
            
            with col4:
                st.metric("F1 Score", f"{exp['f1_score']}%")
            
            with col5:
                st.markdown(f"**{exp['runtime']}**")
            
            st.divider()
    
    with tab2:
        st.markdown("### Model Performance Comparison")
        
        model_data = generate_model_performance_data()
        df_models = pd.DataFrame(model_data)
        
        # Model performance chart
        fig = px.bar(
            df_models,
            x='name',
            y=['accuracy', 'precision', 'recall'],
            title="Model Metrics Comparison",
            barmode='group',
            color_discrete_sequence=['#004c91', '#0071ce', '#00a652']
        )
        
        fig.update_layout(height=400, template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
        
        # Model details
        st.markdown("### Model Registry")
        for model in model_data:
            with st.expander(f"📦 {model['name']}"):
                col1, col2, col3, col4 = st.columns(4)
                with col1:
                    st.metric("Accuracy", f"{model['accuracy']}%")
                with col2:
                    st.metric("Precision", f"{model['precision']}%")
                with col3:
                    st.metric("Recall", f"{model['recall']}%")
                with col4:
                    st.metric("F1 Score", f"{model['f1_score']}%")
    
    with tab3:
        st.markdown("### Feature Discovery")
        
        features = generate_feature_data()
        
        st.markdown("#### Top Features by Importance")
        
        for feature in features:
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            
            with col1:
                st.markdown(f"**{feature['name']}**")
                st.caption(f"Source: {feature['source']}")
            
            with col2:
                type_color = "#3b82f6" if feature['type'] == 'numerical' else "#10b981"
                st.markdown(f"<span style='background: {type_color}; color: white; padding: 2px 8px; border-radius: 12px; font-size: 0.8em;'>{feature['type']}</span>", unsafe_allow_html=True)
            
            with col3:
                importance_pct = feature['importance'] * 100
                st.progress(feature['importance'])
            
            with col4:
                st.markdown(f"**{importance_pct:.1f}%**")
        
        # Feature importance chart
        df_features = pd.DataFrame(features)
        fig_features = px.bar(
            df_features,
            x='importance',
            y='name',
            orientation='h',
            title="Feature Importance Ranking",
            color='importance',
            color_continuous_scale='Blues'
        )
        fig_features.update_layout(height=400, template="plotly_white")
        st.plotly_chart(fig_features, use_container_width=True)
    
    with tab4:
        st.markdown("### Model Testing Playground")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Test Input")
            
            selected_model = st.selectbox(
                "Select Model",
                ["Fraud Detector v2.1", "Risk Scorer v1.3", "Behavior Analyzer v1.0"]
            )
            
            # Input form
            seller_id = st.text_input("Seller ID", "12847")
            decline_rate = st.slider("Payment Decline Rate (7d)", 0.0, 1.0, 0.15)
            seller_age = st.number_input("Seller Age (days)", 1, 365, 45)
            avg_amount = st.number_input("Avg Transaction Amount", 0.0, 1000.0, 150.50)
            country_risk = st.selectbox("Country Risk Score", ["low", "medium", "high"])
            category_risk = st.selectbox("Product Category", ["electronics", "clothing", "home", "other"])
            
            if st.button("🚀 Run Inference", use_container_width=True):
                st.session_state.inference_run = True
        
        with col2:
            st.markdown("#### Model Output")
            
            if hasattr(st.session_state, 'inference_run'):
                # Simulate model output
                risk_score = 0.847
                confidence = 0.942
                prediction = "HIGH RISK"
                inference_time = "23ms"
                
                st.markdown(f"""
                    <div style="background: #f8fafc; padding: 1rem; border-radius: 8px; border-left: 4px solid #ef4444;">
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <span><strong>Risk Score:</strong></span>
                            <span style="color: #ef4444; font-weight: bold;">{risk_score}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <span><strong>Confidence:</strong></span>
                            <span>{confidence:.1%}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                            <span><strong>Prediction:</strong></span>
                            <span style="color: #ef4444; font-weight: bold;">{prediction}</span>
                        </div>
                        <div style="display: flex; justify-content: space-between;">
                            <span><strong>Inference Time:</strong></span>
                            <span style="color: #10b981; font-weight: bold;">{inference_time}</span>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                
                st.markdown("#### Feature Contributions")
                
                contributions = [
                    ("payment_decline_rate_7d", 0.34),
                    ("seller_age_days", 0.28),
                    ("country_risk_score", 0.21),
                    ("avg_transaction_amount", 0.17)
                ]
                
                for feature, contrib in contributions:
                    col_name, col_bar, col_pct = st.columns([2, 2, 1])
                    with col_name:
                        st.caption(feature)
                    with col_bar:
                        st.progress(contrib)
                    with col_pct:
                        st.caption(f"{contrib:.0%}")
            else:
                st.info("Run an inference to see model output")
    
    # Action buttons
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🆕 New Experiment", use_container_width=True):
            st.success("New experiment created!")
    
    with col2:
        if st.button("📊 Feature Store", use_container_width=True):
            st.info("Opening Feature Store...")
    
    with col3:
        if st.button("🔄 Retrain Model", use_container_width=True):
            st.success("Model retraining initiated!")