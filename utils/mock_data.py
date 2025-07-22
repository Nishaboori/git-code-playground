import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_mock_metrics():
    """Generate realistic mock metrics for the platform"""
    base_metrics = {
        'total_models': 47,
        'active_deployments': 12,
        'avg_latency': 24.5,
        'fraud_prevented': 89.7,
        'cost_savings': 2.4,
        'system_uptime': 99.95,
        'throughput': 1850
    }
    
    # Add some realistic variation
    variations = {
        'avg_latency': random.uniform(-2, 2),
        'fraud_prevented': random.uniform(-0.5, 0.5),
        'system_uptime': random.uniform(-0.05, 0.05),
        'throughput': random.uniform(-200, 200)
    }
    
    updated_metrics = base_metrics.copy()
    for key, variation in variations.items():
        if key in updated_metrics:
            updated_metrics[key] = max(0, updated_metrics[key] + variation)
    
    return updated_metrics

def get_deployment_flows():
    """Get deployment flow configurations"""
    return [
        {
            'id': 'flow1',
            'name': 'Same Project (Element → Element)',
            'description': 'Deploy models within the same project environment',
            'icon': '🗂️',
            'color': '#3b82f6',
            'steps': [
                {
                    'id': 'step1',
                    'title': 'Model Registration',
                    'description': 'Register new model version in Element registry',
                    'status': 'completed',
                    'duration': '30s',
                    'details': ['Validate model artifacts', 'Check model schema', 'Generate model metadata']
                },
                {
                    'id': 'step2',
                    'title': 'Quality Gates',
                    'description': 'Run automated quality checks and validation',
                    'status': 'running',
                    'duration': '2m 15s',
                    'details': ['Performance benchmarking', 'Data drift detection', 'Model bias assessment']
                },
                {
                    'id': 'step3',
                    'title': 'Staging Deployment',
                    'description': 'Deploy to staging environment for testing',
                    'status': 'pending',
                    'details': ['Create staging endpoint', 'Configure load balancer', 'Run smoke tests']
                },
                {
                    'id': 'step4',
                    'title': 'Production Deployment',
                    'description': 'Deploy to production with canary release',
                    'status': 'pending',
                    'details': ['Blue-green deployment', 'Traffic splitting', 'Monitor metrics']
                }
            ]
        },
        {
            'id': 'flow2',
            'name': 'Cross-Project (Element → Element)',
            'description': 'Deploy models across different project boundaries',
            'icon': '🔄',
            'color': '#10b981',
            'steps': [
                {
                    'id': 'step1',
                    'title': 'Cross-Project Authorization',
                    'description': 'Validate permissions and access controls',
                    'status': 'completed',
                    'duration': '45s',
                    'details': ['Check IAM policies', 'Validate project permissions', 'Audit trail logging']
                },
                {
                    'id': 'step2',
                    'title': 'Model Export',
                    'description': 'Export model from source project',
                    'status': 'completed',
                    'duration': '1m 30s',
                    'details': ['Package model artifacts', 'Export feature definitions', 'Generate compatibility report']
                },
                {
                    'id': 'step3',
                    'title': 'Cross-Project Transfer',
                    'description': 'Secure transfer to target project',
                    'status': 'running',
                    'duration': '3m 45s',
                    'details': ['Encrypted model transfer', 'Dependency resolution', 'Environment compatibility check']
                },
                {
                    'id': 'step4',
                    'title': 'Target Deployment',
                    'description': 'Deploy in target project environment',
                    'status': 'pending',
                    'details': ['Environment setup', 'Model registration', 'Integration testing']
                }
            ]
        },
        {
            'id': 'flow3',
            'name': 'Element → WCNP (Real-time)',
            'description': 'Deploy to Walmart Cloud Native Platform for real-time inference',
            'icon': '⚡',
            'color': '#f59e0b',
            'steps': [
                {
                    'id': 'step1',
                    'title': 'WCNP Integration Setup',
                    'description': 'Configure WCNP deployment pipeline',
                    'status': 'completed',
                    'duration': '1m 15s',
                    'details': ['Setup Kubernetes namespace', 'Configure service mesh', 'Deploy monitoring stack']
                },
                {
                    'id': 'step2',
                    'title': 'Model Containerization',
                    'description': 'Package model in optimized container',
                    'status': 'completed',
                    'duration': '2m 30s',
                    'details': ['Build Docker image', 'Optimize for inference', 'Security scanning']
                },
                {
                    'id': 'step3',
                    'title': 'Real-time Endpoint Creation',
                    'description': 'Create high-performance inference endpoint',
                    'status': 'running',
                    'duration': '4m 20s',
                    'details': ['Deploy to Kubernetes', 'Configure auto-scaling', 'Setup load balancing']
                },
                {
                    'id': 'step4',
                    'title': 'Performance Validation',
                    'description': 'Validate latency and throughput requirements',
                    'status': 'pending',
                    'details': ['Latency testing (<50ms)', 'Throughput validation (100K+ TPS)', 'Stress testing']
                }
            ]
        },
        {
            'id': 'flow4',
            'name': 'External → Element',
            'description': 'Import and deploy models from external sources',
            'icon': '☁️',
            'color': '#8b5cf6',
            'steps': [
                {
                    'id': 'step1',
                    'title': 'External Model Import',
                    'description': 'Import model from external source',
                    'status': 'completed',
                    'duration': '2m 45s',
                    'details': ['Download model artifacts', 'Validate model format', 'Security scanning']
                },
                {
                    'id': 'step2',
                    'title': 'Compatibility Assessment',
                    'description': 'Assess compatibility with Element platform',
                    'status': 'completed',
                    'duration': '1m 50s',
                    'details': ['Framework compatibility', 'Dependency analysis', 'Feature mapping']
                },
                {
                    'id': 'step3',
                    'title': 'Model Adaptation',
                    'description': 'Adapt model for Element deployment',
                    'status': 'running',
                    'duration': '5m 10s',
                    'details': ['Convert model format', 'Update dependencies', 'Create wrapper services']
                },
                {
                    'id': 'step4',
                    'title': 'Element Integration',
                    'description': 'Integrate with Element ecosystem',
                    'status': 'pending',
                    'details': ['Register in model catalog', 'Setup monitoring', 'Configure governance']
                }
            ]
        }
    ]

def generate_experiment_data():
    """Generate mock experiment data"""
    experiments = []
    statuses = ['running', 'completed', 'failed', 'pending']
    algorithms = ['XGBoost', 'Neural Network', 'Random Forest', 'LSTM', 'SVM', 'Gradient Boosting']
    
    for i in range(1, 9):
        experiment = {
            'id': f'exp-{i:03d}',
            'name': f'Fraud Detection {random.choice(algorithms)} v{random.randint(1,3)}.{random.randint(0,9)}',
            'status': random.choice(statuses),
            'accuracy': round(random.uniform(85, 95), 1),
            'f1_score': round(random.uniform(80, 92), 1),
            'precision': round(random.uniform(82, 94), 1),
            'recall': round(random.uniform(78, 96), 1),
            'runtime': f'{random.randint(1,4)}h {random.randint(10,59)}m',
            'created': f'{random.randint(1,7)} days ago'
        }
        experiments.append(experiment)
    
    return experiments

def generate_feature_data():
    """Generate mock feature importance data"""
    features = [
        {'name': 'payment_decline_rate_7d', 'importance': 0.234, 'type': 'numerical', 'source': 'payment_events'},
        {'name': 'seller_age_days', 'importance': 0.198, 'type': 'numerical', 'source': 'seller_profile'},
        {'name': 'avg_transaction_amount', 'importance': 0.156, 'type': 'numerical', 'source': 'transactions'},
        {'name': 'country_risk_score', 'importance': 0.142, 'type': 'categorical', 'source': 'geo_data'},
        {'name': 'product_category_risk', 'importance': 0.128, 'type': 'categorical', 'source': 'catalog'},
        {'name': 'velocity_score', 'importance': 0.089, 'type': 'numerical', 'source': 'behavior_analytics'},
        {'name': 'payment_method_risk', 'importance': 0.053, 'type': 'categorical', 'source': 'payment_events'}
    ]
    return features

def generate_time_series_data():
    """Generate time series data for charts"""
    # Generate performance trends
    dates = pd.date_range(start=datetime.now() - timedelta(days=7), end=datetime.now(), freq='H')
    
    performance_data = []
    base_latency = 25
    base_throughput = 1500
    
    for i, date in enumerate(dates):
        # Add some realistic variation and daily patterns
        hour = date.hour
        daily_factor = 1 + 0.3 * np.sin(2 * np.pi * hour / 24)  # Daily pattern
        noise = np.random.normal(0, 0.1)
        
        latency = max(20, base_latency + 3 * daily_factor + 2 * noise)
        throughput = max(1000, base_throughput * daily_factor + 200 * noise)
        
        performance_data.append({
            'timestamp': date,
            'latency': round(latency, 1),
            'throughput': int(throughput),
            'accuracy': round(89 + 2 * np.sin(i * 0.1) + noise, 1)
        })
    
    return pd.DataFrame(performance_data)

def generate_system_health_data():
    """Generate system health status data"""
    components = [
        {'name': 'Model Serving', 'status': 'healthy', 'uptime': '99.98%', 'response_time': '23ms'},
        {'name': 'Feature Store', 'status': 'healthy', 'uptime': '99.95%', 'response_time': '12ms'},
        {'name': 'Data Pipeline', 'status': 'healthy', 'uptime': '99.92%', 'response_time': '45ms'},
        {'name': 'Monitoring', 'status': 'warning', 'uptime': '98.87%', 'response_time': '78ms'},
        {'name': 'API Gateway', 'status': 'healthy', 'uptime': '99.99%', 'response_time': '8ms'},
        {'name': 'Authentication', 'status': 'healthy', 'uptime': '99.94%', 'response_time': '15ms'}
    ]
    return components

def generate_recent_activity():
    """Generate recent activity feed"""
    activities = [
        {'time': '2 min ago', 'event': 'Model fraud-detector-v2.1 deployed to production', 'type': 'deployment', 'severity': 'success'},
        {'time': '5 min ago', 'event': 'High-risk seller flagged: Seller ID 12847', 'type': 'alert', 'severity': 'warning'},
        {'time': '12 min ago', 'event': 'Feature store updated with new payment patterns', 'type': 'update', 'severity': 'info'},
        {'time': '18 min ago', 'event': 'A/B test started: Champion vs Challenger model', 'type': 'experiment', 'severity': 'info'},
        {'time': '25 min ago', 'event': 'Data pipeline completed: 2.3M transactions processed', 'type': 'pipeline', 'severity': 'success'},
        {'time': '35 min ago', 'event': 'Model performance alert: Accuracy dropped to 87%', 'type': 'alert', 'severity': 'error'},
        {'time': '42 min ago', 'event': 'New feature deployed: real-time risk scoring', 'type': 'deployment', 'severity': 'success'},
        {'time': '1 hour ago', 'event': 'Weekly model retraining completed successfully', 'type': 'training', 'severity': 'success'}
    ]
    return activities

def generate_model_performance_data():
    """Generate model performance comparison data"""
    models = [
        {'name': 'Fraud Detector v1', 'accuracy': 89.2, 'precision': 87.5, 'recall': 91.3, 'f1_score': 89.4},
        {'name': 'Fraud Detector v2', 'accuracy': 92.1, 'precision': 90.2, 'recall': 93.8, 'f1_score': 92.0},
        {'name': 'Risk Scorer v1', 'accuracy': 85.7, 'precision': 83.1, 'recall': 88.2, 'f1_score': 85.6},
        {'name': 'Risk Scorer v2', 'accuracy': 88.9, 'precision': 86.7, 'recall': 91.1, 'f1_score': 88.8},
        {'name': 'Behavior Analyzer v1', 'accuracy': 83.4, 'precision': 81.2, 'recall': 85.6, 'f1_score': 83.3}
    ]
    return models

def generate_fraud_detection_data():
    """Generate real-time fraud detection events"""
    events = []
    risk_levels = ['LOW', 'MEDIUM', 'HIGH', 'CRITICAL']
    
    for i in range(20):
        event = {
            'timestamp': datetime.now() - timedelta(minutes=random.randint(1, 120)),
            'seller_id': f'S{random.randint(10000, 99999)}',
            'risk_score': round(random.uniform(0.1, 0.95), 3),
            'risk_level': random.choice(risk_levels),
            'confidence': round(random.uniform(0.7, 0.99), 3),
            'reason': random.choice([
                'High payment decline rate',
                'Unusual transaction pattern',
                'New seller from high-risk region',
                'Rapid price changes detected',
                'Suspicious inventory behavior',
                'Multiple account flags'
            ])
        }
        events.append(event)
    
    return sorted(events, key=lambda x: x['timestamp'], reverse=True)