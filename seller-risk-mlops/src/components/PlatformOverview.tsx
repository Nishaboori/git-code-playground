import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { 
  TrendingUp, 
  Shield, 
  Zap, 
  Clock, 
  Users, 
  Brain,
  GitBranch,
  Database,
  AlertTriangle,
  CheckCircle,
  Activity,
  DollarSign
} from 'lucide-react';
import MetricCard from './MetricCard';
import LineChart from './charts/LineChart';
import BarChart from './charts/BarChart';
import DonutChart from './charts/DonutChart';

const PlatformOverview: React.FC = () => {
  const [currentTime, setCurrentTime] = useState(new Date());

  useEffect(() => {
    const timer = setInterval(() => setCurrentTime(new Date()), 1000);
    return () => clearInterval(timer);
  }, []);

  // Simulated real-time metrics
  const [metrics, setMetrics] = useState({
    totalModels: 47,
    activeDeployments: 12,
    avgLatency: 24,
    fraudPrevented: 89.7,
    costSavings: 2.4,
    systemUptime: 99.95
  });

  useEffect(() => {
    const interval = setInterval(() => {
      setMetrics(prev => ({
        ...prev,
        avgLatency: Math.max(20, Math.min(30, prev.avgLatency + (Math.random() - 0.5) * 2)),
        fraudPrevented: Math.max(85, Math.min(95, prev.fraudPrevented + (Math.random() - 0.5) * 0.5)),
        systemUptime: Math.max(99.9, Math.min(100, prev.systemUptime + (Math.random() - 0.5) * 0.01))
      }));
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  const keyMetrics = [
    {
      title: 'Total Models',
      value: metrics.totalModels.toString(),
      change: '+3 this week',
      trend: 'up' as const,
      icon: <Brain className="w-6 h-6" />,
      color: 'bg-purple-500'
    },
    {
      title: 'Active Deployments',
      value: metrics.activeDeployments.toString(),
      change: '+2 today',
      trend: 'up' as const,
      icon: <GitBranch className="w-6 h-6" />,
      color: 'bg-blue-500'
    },
    {
      title: 'Avg Response Time',
      value: `${metrics.avgLatency.toFixed(1)}ms`,
      change: 'Target: <50ms',
      trend: 'stable' as const,
      icon: <Zap className="w-6 h-6" />,
      color: 'bg-yellow-500'
    },
    {
      title: 'Fraud Prevention Rate',
      value: `${metrics.fraudPrevented.toFixed(1)}%`,
      change: '+2.3% vs last month',
      trend: 'up' as const,
      icon: <Shield className="w-6 h-6" />,
      color: 'bg-red-500'
    },
    {
      title: 'Cost Savings',
      value: `$${metrics.costSavings.toFixed(1)}M`,
      change: 'This quarter',
      trend: 'up' as const,
      icon: <DollarSign className="w-6 h-6" />,
      color: 'bg-green-500'
    },
    {
      title: 'System Uptime',
      value: `${metrics.systemUptime.toFixed(2)}%`,
      change: 'Last 30 days',
      trend: 'stable' as const,
      icon: <Activity className="w-6 h-6" />,
      color: 'bg-teal-500'
    }
  ];

  const systemHealth = [
    { name: 'Model Serving', status: 'healthy', uptime: '99.98%' },
    { name: 'Feature Store', status: 'healthy', uptime: '99.95%' },
    { name: 'Data Pipeline', status: 'healthy', uptime: '99.92%' },
    { name: 'Monitoring', status: 'warning', uptime: '98.87%' },
  ];

  const deploymentFlows = [
    { name: 'Same Project (Element → Element)', count: 156, percentage: 45 },
    { name: 'Cross-Project (Element → Element)', count: 89, percentage: 26 },
    { name: 'Element → WCNP (Real-time)', count: 67, percentage: 19 },
    { name: 'External → Element', count: 34, percentage: 10 },
  ];

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Platform Overview</h1>
          <p className="text-gray-600 mt-1">
            Comprehensive view of your MLOps platform • {currentTime.toLocaleString()}
          </p>
        </div>
        
        <div className="flex items-center space-x-3">
          <div className="flex items-center space-x-2 px-3 py-2 bg-green-50 rounded-lg">
            <CheckCircle className="w-4 h-4 text-green-600" />
            <span className="text-sm text-green-700 font-medium">All Systems Operational</span>
          </div>
          <button className="btn-primary">
            View System Status
          </button>
        </div>
      </div>

      {/* Key Metrics Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-6 gap-6">
        {keyMetrics.map((metric, index) => (
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

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Performance Trends */}
        <div className="card">
          <div className="card-header">
            <h3 className="text-lg font-semibold text-gray-900">Performance Trends</h3>
            <p className="text-sm text-gray-600">Model latency and throughput over time</p>
          </div>
          <LineChart />
        </div>

        {/* Deployment Flow Distribution */}
        <div className="card">
          <div className="card-header">
            <h3 className="text-lg font-semibold text-gray-900">Deployment Flows</h3>
            <p className="text-sm text-gray-600">Distribution of deployment patterns</p>
          </div>
          <DonutChart data={deploymentFlows} />
        </div>
      </div>

      {/* System Health and Recent Activity */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* System Health */}
        <div className="card">
          <div className="card-header">
            <h3 className="text-lg font-semibold text-gray-900">System Health</h3>
            <p className="text-sm text-gray-600">Component status and uptime</p>
          </div>
          
          <div className="space-y-4">
            {systemHealth.map((component, index) => (
              <motion.div
                key={component.name}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1 }}
                className="flex items-center justify-between p-3 rounded-lg border border-gray-100"
              >
                <div className="flex items-center space-x-3">
                  {component.status === 'healthy' ? (
                    <CheckCircle className="w-5 h-5 text-green-500" />
                  ) : (
                    <AlertTriangle className="w-5 h-5 text-yellow-500" />
                  )}
                  <span className="font-medium text-gray-900">{component.name}</span>
                </div>
                <div className="text-right">
                  <div className={`text-sm font-medium ${
                    component.status === 'healthy' ? 'text-green-600' : 'text-yellow-600'
                  }`}>
                    {component.status === 'healthy' ? 'Healthy' : 'Warning'}
                  </div>
                  <div className="text-xs text-gray-500">{component.uptime}</div>
                </div>
              </motion.div>
            ))}
          </div>
        </div>

        {/* Recent Activity */}
        <div className="card">
          <div className="card-header">
            <h3 className="text-lg font-semibold text-gray-900">Recent Activity</h3>
            <p className="text-sm text-gray-600">Latest platform events</p>
          </div>
          
          <div className="space-y-4">
            {[
              { time: '2 min ago', event: 'Model fraud-detector-v2.1 deployed to production', type: 'deployment' },
              { time: '5 min ago', event: 'High-risk seller flagged: Seller ID 12847', type: 'alert' },
              { time: '12 min ago', event: 'Feature store updated with new payment patterns', type: 'update' },
              { time: '18 min ago', event: 'A/B test started: Champion vs Challenger model', type: 'experiment' },
              { time: '25 min ago', event: 'Data pipeline completed: 2.3M transactions processed', type: 'pipeline' }
            ].map((activity, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
                className="flex items-start space-x-3 p-3 rounded-lg hover:bg-gray-50 transition-colors"
              >
                <div className={`w-2 h-2 rounded-full mt-2 ${
                  activity.type === 'deployment' ? 'bg-blue-500' :
                  activity.type === 'alert' ? 'bg-red-500' :
                  activity.type === 'update' ? 'bg-green-500' :
                  activity.type === 'experiment' ? 'bg-purple-500' :
                  'bg-gray-500'
                }`}></div>
                <div className="flex-1">
                  <p className="text-sm text-gray-900">{activity.event}</p>
                  <p className="text-xs text-gray-500 mt-1">{activity.time}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </div>

      {/* Quick Actions */}
      <div className="card">
        <div className="card-header">
          <h3 className="text-lg font-semibold text-gray-900">Quick Actions</h3>
          <p className="text-sm text-gray-600">Common platform operations</p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {[
            { title: 'Deploy New Model', description: 'Push latest model to production', icon: <GitBranch className="w-5 h-5" />, color: 'bg-blue-500' },
            { title: 'Create Experiment', description: 'Start A/B testing new features', icon: <Brain className="w-5 h-5" />, color: 'bg-purple-500' },
            { title: 'Monitor Fraud', description: 'View real-time fraud detection', icon: <Shield className="w-5 h-5" />, color: 'bg-red-500' },
            { title: 'System Health', description: 'Check platform diagnostics', icon: <Activity className="w-5 h-5" />, color: 'bg-green-500' }
          ].map((action, index) => (
            <motion.button
              key={action.title}
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
              className="p-4 text-left bg-white border border-gray-200 rounded-lg hover:border-gray-300 hover:shadow-md transition-all duration-200"
            >
              <div className={`w-10 h-10 ${action.color} rounded-lg flex items-center justify-center text-white mb-3`}>
                {action.icon}
              </div>
              <h4 className="font-medium text-gray-900 mb-1">{action.title}</h4>
              <p className="text-sm text-gray-600">{action.description}</p>
            </motion.button>
          ))}
        </div>
      </div>
    </div>
  );
};

export default PlatformOverview;