import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Brain, 
  Flask, 
  Database, 
  Code, 
  Play, 
  GitBranch, 
  TrendingUp,
  Search,
  Filter,
  Plus,
  BarChart3,
  Zap,
  CheckCircle,
  Clock,
  AlertCircle
} from 'lucide-react';
import MetricCard from './MetricCard';
import BarChart from './charts/BarChart';
import LineChart from './charts/LineChart';

const DataScientistDashboard: React.FC = () => {
  const [activeTab, setActiveTab] = useState('experiments');
  const [selectedModel, setSelectedModel] = useState('fraud-detector-v2');

  const experiments = [
    {
      id: 'exp-001',
      name: 'Fraud Detection XGBoost v2.1',
      status: 'running',
      accuracy: 92.1,
      f1Score: 89.7,
      runtime: '2h 34m',
      created: '2 hours ago'
    },
    {
      id: 'exp-002', 
      name: 'Risk Scoring Neural Network',
      status: 'completed',
      accuracy: 88.9,
      f1Score: 85.3,
      runtime: '1h 45m',
      created: '5 hours ago'
    },
    {
      id: 'exp-003',
      name: 'Seller Behavior LSTM',
      status: 'failed',
      accuracy: 0,
      f1Score: 0,
      runtime: '0h 12m',
      created: '1 day ago'
    }
  ];

  const features = [
    { name: 'payment_decline_rate_7d', importance: 0.234, type: 'numerical', source: 'payment_events' },
    { name: 'seller_age_days', importance: 0.198, type: 'numerical', source: 'seller_profile' },
    { name: 'avg_transaction_amount', importance: 0.156, type: 'numerical', source: 'transactions' },
    { name: 'country_risk_score', importance: 0.142, type: 'categorical', source: 'geo_data' },
    { name: 'product_category_risk', importance: 0.128, type: 'categorical', source: 'catalog' }
  ];

  const modelMetrics = [
    {
      title: 'Active Experiments',
      value: '8',
      change: '+2 this week',
      trend: 'up' as const,
      icon: <Flask className="w-6 h-6" />,
      color: 'bg-purple-500'
    },
    {
      title: 'Best Model Accuracy',
      value: '92.1%',
      change: '+3.2% improvement',
      trend: 'up' as const,
      icon: <TrendingUp className="w-6 h-6" />,
      color: 'bg-green-500'
    },
    {
      title: 'Training Time',
      value: '2.3h',
      change: '15% faster',
      trend: 'up' as const,
      icon: <Zap className="w-6 h-6" />,
      color: 'bg-yellow-500'
    },
    {
      title: 'Features Available',
      value: '247',
      change: '+12 new features',
      trend: 'up' as const,
      icon: <Database className="w-6 h-6" />,
      color: 'bg-blue-500'
    }
  ];

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'running':
        return <Clock className="w-4 h-4 text-yellow-500 animate-spin" />;
      case 'completed':
        return <CheckCircle className="w-4 h-4 text-green-500" />;
      case 'failed':
        return <AlertCircle className="w-4 h-4 text-red-500" />;
      default:
        return <Clock className="w-4 h-4 text-gray-500" />;
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'running':
        return 'bg-yellow-100 text-yellow-800';
      case 'completed':
        return 'bg-green-100 text-green-800';
      case 'failed':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Data Science Workspace</h1>
          <p className="text-gray-600 mt-1">
            Model development, experimentation, and feature engineering
          </p>
        </div>
        
        <div className="flex items-center space-x-3">
          <button className="btn-secondary">
            <Database className="w-4 h-4 mr-2" />
            Feature Store
          </button>
          <button className="btn-primary">
            <Plus className="w-4 h-4 mr-2" />
            New Experiment
          </button>
        </div>
      </div>

      {/* Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {modelMetrics.map((metric, index) => (
          <motion.div
            key={metric.title}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
          >
            <MetricCard {...metric} />
          </motion.div>
        ))}
      </div>

      {/* Tab Navigation */}
      <div className="border-b border-gray-200">
        <nav className="-mb-px flex space-x-8">
          {[
            { id: 'experiments', name: 'Experiments', icon: <Flask className="w-4 h-4" /> },
            { id: 'models', name: 'Model Registry', icon: <Brain className="w-4 h-4" /> },
            { id: 'features', name: 'Feature Discovery', icon: <Database className="w-4 h-4" /> },
            { id: 'playground', name: 'Testing Playground', icon: <Play className="w-4 h-4" /> }
          ].map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center space-x-2 py-2 px-1 border-b-2 font-medium text-sm ${
                activeTab === tab.id
                  ? 'border-walmart-blue text-walmart-blue'
                  : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
              }`}
            >
              {tab.icon}
              <span>{tab.name}</span>
            </button>
          ))}
        </nav>
      </div>

      {/* Tab Content */}
      <AnimatePresence mode="wait">
        <motion.div
          key={activeTab}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          transition={{ duration: 0.3 }}
        >
          {activeTab === 'experiments' && (
            <div className="space-y-6">
              <div className="flex items-center justify-between">
                <h2 className="text-xl font-semibold text-gray-900">Recent Experiments</h2>
                <div className="flex items-center space-x-3">
                  <div className="relative">
                    <Search className="w-4 h-4 absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
                    <input
                      type="text"
                      placeholder="Search experiments..."
                      className="pl-10 pr-4 py-2 border border-gray-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-walmart-blue focus:border-transparent"
                    />
                  </div>
                  <button className="btn-secondary">
                    <Filter className="w-4 h-4" />
                  </button>
                </div>
              </div>

              <div className="grid grid-cols-1 gap-4">
                {experiments.map((experiment, index) => (
                  <motion.div
                    key={experiment.id}
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    transition={{ delay: index * 0.1 }}
                    className="card hover:shadow-md transition-shadow cursor-pointer"
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-4">
                        {getStatusIcon(experiment.status)}
                        <div>
                          <h3 className="font-semibold text-gray-900">{experiment.name}</h3>
                          <p className="text-sm text-gray-600">{experiment.created}</p>
                        </div>
                      </div>
                      
                      <div className="flex items-center space-x-6">
                        <div className="text-right">
                          <p className="text-sm font-medium text-gray-900">Accuracy</p>
                          <p className="text-lg font-bold text-walmart-blue">{experiment.accuracy}%</p>
                        </div>
                        <div className="text-right">
                          <p className="text-sm font-medium text-gray-900">F1 Score</p>
                          <p className="text-lg font-bold text-green-600">{experiment.f1Score}%</p>
                        </div>
                        <div className="text-right">
                          <p className="text-sm font-medium text-gray-900">Runtime</p>
                          <p className="text-sm text-gray-600">{experiment.runtime}</p>
                        </div>
                        <span className={`px-2 py-1 rounded-full text-xs font-medium ${getStatusColor(experiment.status)}`}>
                          {experiment.status}
                        </span>
                      </div>
                    </div>
                  </motion.div>
                ))}
              </div>
            </div>
          )}

          {activeTab === 'models' && (
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
              <div className="card">
                <div className="card-header">
                  <h3 className="text-lg font-semibold text-gray-900">Model Performance Comparison</h3>
                  <p className="text-sm text-gray-600">Accuracy scores across model versions</p>
                </div>
                <BarChart />
              </div>
              
              <div className="card">
                <div className="card-header">
                  <h3 className="text-lg font-semibold text-gray-900">Training Progress</h3>
                  <p className="text-sm text-gray-600">Loss and accuracy over epochs</p>
                </div>
                <LineChart />
              </div>
            </div>
          )}

          {activeTab === 'features' && (
            <div className="space-y-6">
              <div className="flex items-center justify-between">
                <h2 className="text-xl font-semibold text-gray-900">Feature Discovery</h2>
                <button className="btn-primary">
                  <Plus className="w-4 h-4 mr-2" />
                  Create Feature
                </button>
              </div>

              <div className="card">
                <div className="card-header">
                  <h3 className="text-lg font-semibold text-gray-900">Top Features by Importance</h3>
                  <p className="text-sm text-gray-600">Most impactful features for fraud detection</p>
                </div>
                
                <div className="space-y-4">
                  {features.map((feature, index) => (
                    <motion.div
                      key={feature.name}
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ delay: index * 0.1 }}
                      className="flex items-center justify-between p-4 border border-gray-100 rounded-lg hover:border-gray-200 transition-colors"
                    >
                      <div className="flex items-center space-x-4">
                        <div className="w-2 h-8 bg-walmart-blue rounded" style={{ width: `${feature.importance * 100}px` }}></div>
                        <div>
                          <h4 className="font-medium text-gray-900">{feature.name}</h4>
                          <p className="text-sm text-gray-600">Source: {feature.source}</p>
                        </div>
                      </div>
                      <div className="flex items-center space-x-4">
                        <span className={`px-2 py-1 rounded text-xs font-medium ${
                          feature.type === 'numerical' ? 'bg-blue-100 text-blue-800' : 'bg-green-100 text-green-800'
                        }`}>
                          {feature.type}
                        </span>
                        <span className="font-bold text-gray-900">{(feature.importance * 100).toFixed(1)}%</span>
                      </div>
                    </motion.div>
                  ))}
                </div>
              </div>
            </div>
          )}

          {activeTab === 'playground' && (
            <div className="space-y-6">
              <div className="card">
                <div className="card-header">
                  <h3 className="text-lg font-semibold text-gray-900">Model Testing Playground</h3>
                  <p className="text-sm text-gray-600">Test your models with real-time inference</p>
                </div>
                
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                  <div className="space-y-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Select Model
                      </label>
                      <select 
                        value={selectedModel}
                        onChange={(e) => setSelectedModel(e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-walmart-blue focus:border-transparent"
                      >
                        <option value="fraud-detector-v2">Fraud Detector v2.1</option>
                        <option value="risk-scorer-v1">Risk Scorer v1.3</option>
                        <option value="behavior-analyzer">Behavior Analyzer v1.0</option>
                      </select>
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Test Input (JSON)
                      </label>
                      <textarea
                        rows={8}
                        className="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-walmart-blue focus:border-transparent font-mono text-sm"
                        placeholder={`{
  "seller_id": "12847",
  "payment_decline_rate_7d": 0.15,
  "seller_age_days": 45,
  "avg_transaction_amount": 150.50,
  "country_risk_score": "medium",
  "product_category_risk": "electronics"
}`}
                      />
                    </div>
                    
                    <button className="btn-primary w-full">
                      <Play className="w-4 h-4 mr-2" />
                      Run Inference
                    </button>
                  </div>
                  
                  <div className="space-y-4">
                    <div>
                      <h4 className="text-sm font-medium text-gray-700 mb-2">Model Output</h4>
                      <div className="bg-gray-50 p-4 rounded-lg border">
                        <div className="space-y-2">
                          <div className="flex justify-between">
                            <span className="text-sm text-gray-600">Risk Score:</span>
                            <span className="font-bold text-red-600">0.847</span>
                          </div>
                          <div className="flex justify-between">
                            <span className="text-sm text-gray-600">Confidence:</span>
                            <span className="font-bold text-gray-900">94.2%</span>
                          </div>
                          <div className="flex justify-between">
                            <span className="text-sm text-gray-600">Prediction:</span>
                            <span className="font-bold text-red-600">HIGH RISK</span>
                          </div>
                          <div className="flex justify-between">
                            <span className="text-sm text-gray-600">Inference Time:</span>
                            <span className="font-bold text-green-600">23ms</span>
                          </div>
                        </div>
                      </div>
                    </div>
                    
                    <div>
                      <h4 className="text-sm font-medium text-gray-700 mb-2">Feature Contributions</h4>
                      <div className="space-y-2">
                        {[
                          { feature: 'payment_decline_rate_7d', contribution: 0.34 },
                          { feature: 'seller_age_days', contribution: 0.28 },
                          { feature: 'country_risk_score', contribution: 0.21 },
                          { feature: 'avg_transaction_amount', contribution: 0.17 }
                        ].map((item, index) => (
                          <div key={index} className="flex items-center space-x-3">
                            <div className="w-24 text-xs text-gray-600 truncate">{item.feature}</div>
                            <div className="flex-1 bg-gray-200 rounded-full h-2">
                              <div 
                                className="bg-walmart-blue h-2 rounded-full" 
                                style={{ width: `${item.contribution * 100}%` }}
                              ></div>
                            </div>
                            <div className="w-12 text-xs font-medium text-gray-900">
                              {(item.contribution * 100).toFixed(0)}%
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </motion.div>
      </AnimatePresence>
    </div>
  );
};

export default DataScientistDashboard;