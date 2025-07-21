import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  GitBranch, 
  ArrowRight, 
  Database, 
  Server, 
  Cloud, 
  CheckCircle, 
  Clock, 
  Play,
  Pause,
  RotateCcw,
  Zap,
  Shield
} from 'lucide-react';

interface WorkflowStep {
  id: string;
  title: string;
  description: string;
  status: 'pending' | 'running' | 'completed' | 'failed';
  duration?: string;
  details?: string[];
}

interface DeploymentFlow {
  id: string;
  name: string;
  description: string;
  icon: React.ReactNode;
  color: string;
  steps: WorkflowStep[];
}

const WorkflowVisualization: React.FC = () => {
  const [selectedFlow, setSelectedFlow] = useState<string>('flow1');
  const [isPlaying, setIsPlaying] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);

  const deploymentFlows: DeploymentFlow[] = [
    {
      id: 'flow1',
      name: 'Same Project (Element → Element)',
      description: 'Deploy models within the same project environment',
      icon: <Database className="w-6 h-6" />,
      color: 'bg-blue-500',
      steps: [
        {
          id: 'step1',
          title: 'Model Registration',
          description: 'Register new model version in Element registry',
          status: 'completed',
          duration: '30s',
          details: ['Validate model artifacts', 'Check model schema', 'Generate model metadata']
        },
        {
          id: 'step2',
          title: 'Quality Gates',
          description: 'Run automated quality checks and validation',
          status: 'running',
          duration: '2m 15s',
          details: ['Performance benchmarking', 'Data drift detection', 'Model bias assessment']
        },
        {
          id: 'step3',
          title: 'Staging Deployment',
          description: 'Deploy to staging environment for testing',
          status: 'pending',
          details: ['Create staging endpoint', 'Configure load balancer', 'Run smoke tests']
        },
        {
          id: 'step4',
          title: 'Production Deployment',
          description: 'Deploy to production with canary release',
          status: 'pending',
          details: ['Blue-green deployment', 'Traffic splitting', 'Monitor metrics']
        }
      ]
    },
    {
      id: 'flow2',
      name: 'Cross-Project (Element → Element)',
      description: 'Deploy models across different project boundaries',
      icon: <GitBranch className="w-6 h-6" />,
      color: 'bg-green-500',
      steps: [
        {
          id: 'step1',
          title: 'Cross-Project Authorization',
          description: 'Validate permissions and access controls',
          status: 'completed',
          duration: '45s',
          details: ['Check IAM policies', 'Validate project permissions', 'Audit trail logging']
        },
        {
          id: 'step2',
          title: 'Model Export',
          description: 'Export model from source project',
          status: 'completed',
          duration: '1m 30s',
          details: ['Package model artifacts', 'Export feature definitions', 'Generate compatibility report']
        },
        {
          id: 'step3',
          title: 'Cross-Project Transfer',
          description: 'Secure transfer to target project',
          status: 'running',
          duration: '3m 45s',
          details: ['Encrypted model transfer', 'Dependency resolution', 'Environment compatibility check']
        },
        {
          id: 'step4',
          title: 'Target Deployment',
          description: 'Deploy in target project environment',
          status: 'pending',
          details: ['Environment setup', 'Model registration', 'Integration testing']
        }
      ]
    },
    {
      id: 'flow3',
      name: 'Element → WCNP (Real-time)',
      description: 'Deploy to Walmart Cloud Native Platform for real-time inference',
      icon: <Zap className="w-6 h-6" />,
      color: 'bg-yellow-500',
      steps: [
        {
          id: 'step1',
          title: 'WCNP Integration Setup',
          description: 'Configure WCNP deployment pipeline',
          status: 'completed',
          duration: '1m 15s',
          details: ['Setup Kubernetes namespace', 'Configure service mesh', 'Deploy monitoring stack']
        },
        {
          id: 'step2',
          title: 'Model Containerization',
          description: 'Package model in optimized container',
          status: 'completed',
          duration: '2m 30s',
          details: ['Build Docker image', 'Optimize for inference', 'Security scanning']
        },
        {
          id: 'step3',
          title: 'Real-time Endpoint Creation',
          description: 'Create high-performance inference endpoint',
          status: 'running',
          duration: '4m 20s',
          details: ['Deploy to Kubernetes', 'Configure auto-scaling', 'Setup load balancing']
        },
        {
          id: 'step4',
          title: 'Performance Validation',
          description: 'Validate latency and throughput requirements',
          status: 'pending',
          details: ['Latency testing (<50ms)', 'Throughput validation (100K+ TPS)', 'Stress testing']
        }
      ]
    },
    {
      id: 'flow4',
      name: 'External → Element',
      description: 'Import and deploy models from external sources',
      icon: <Cloud className="w-6 h-6" />,
      color: 'bg-purple-500',
      steps: [
        {
          id: 'step1',
          title: 'External Model Import',
          description: 'Import model from external source',
          status: 'completed',
          duration: '2m 45s',
          details: ['Download model artifacts', 'Validate model format', 'Security scanning']
        },
        {
          id: 'step2',
          title: 'Compatibility Assessment',
          description: 'Assess compatibility with Element platform',
          status: 'completed',
          duration: '1m 50s',
          details: ['Framework compatibility', 'Dependency analysis', 'Feature mapping']
        },
        {
          id: 'step3',
          title: 'Model Adaptation',
          description: 'Adapt model for Element deployment',
          status: 'running',
          duration: '5m 10s',
          details: ['Convert model format', 'Update dependencies', 'Create wrapper services']
        },
        {
          id: 'step4',
          title: 'Element Integration',
          description: 'Integrate with Element ecosystem',
          status: 'pending',
          details: ['Register in model catalog', 'Setup monitoring', 'Configure governance']
        }
      ]
    }
  ];

  const currentFlow = deploymentFlows.find(flow => flow.id === selectedFlow)!;

  const getStatusIcon = (status: string) => {
    switch (status) {
      case 'completed':
        return <CheckCircle className="w-5 h-5 text-green-500" />;
      case 'running':
        return <Clock className="w-5 h-5 text-yellow-500 animate-spin" />;
      case 'failed':
        return <div className="w-5 h-5 rounded-full bg-red-500 flex items-center justify-center">
          <div className="w-2 h-2 bg-white rounded-full"></div>
        </div>;
      default:
        return <div className="w-5 h-5 rounded-full border-2 border-gray-300"></div>;
    }
  };

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'completed':
        return 'border-green-200 bg-green-50';
      case 'running':
        return 'border-yellow-200 bg-yellow-50';
      case 'failed':
        return 'border-red-200 bg-red-50';
      default:
        return 'border-gray-200 bg-gray-50';
    }
  };

  const simulateFlow = () => {
    setIsPlaying(!isPlaying);
    if (!isPlaying) {
      // Start simulation
      setCurrentStep(0);
      const interval = setInterval(() => {
        setCurrentStep(prev => {
          if (prev >= currentFlow.steps.length - 1) {
            clearInterval(interval);
            setIsPlaying(false);
            return prev;
          }
          return prev + 1;
        });
      }, 2000);
    }
  };

  const resetSimulation = () => {
    setIsPlaying(false);
    setCurrentStep(0);
  };

  return (
    <div className="p-6 space-y-6">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Workflow Visualization</h1>
          <p className="text-gray-600 mt-1">
            Interactive deployment flow simulation and monitoring
          </p>
        </div>
        
        <div className="flex items-center space-x-3">
          <button
            onClick={simulateFlow}
            className={`btn-${isPlaying ? 'warning' : 'primary'}`}
          >
            {isPlaying ? <Pause className="w-4 h-4 mr-2" /> : <Play className="w-4 h-4 mr-2" />}
            {isPlaying ? 'Pause' : 'Simulate'}
          </button>
          <button onClick={resetSimulation} className="btn-secondary">
            <RotateCcw className="w-4 h-4 mr-2" />
            Reset
          </button>
        </div>
      </div>

      {/* Flow Selection */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {deploymentFlows.map((flow) => (
          <motion.button
            key={flow.id}
            onClick={() => setSelectedFlow(flow.id)}
            className={`p-4 rounded-lg border-2 text-left transition-all duration-200 ${
              selectedFlow === flow.id
                ? 'border-walmart-blue bg-blue-50'
                : 'border-gray-200 bg-white hover:border-gray-300 hover:shadow-md'
            }`}
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
          >
            <div className="flex items-center space-x-3 mb-3">
              <div className={`w-10 h-10 ${flow.color} rounded-lg flex items-center justify-center text-white`}>
                {flow.icon}
              </div>
              <div className="flex-1">
                <h3 className="font-semibold text-gray-900 text-sm">{flow.name}</h3>
              </div>
            </div>
            <p className="text-xs text-gray-600">{flow.description}</p>
          </motion.button>
        ))}
      </div>

      {/* Selected Flow Visualization */}
      <div className="card">
        <div className="card-header">
          <div className="flex items-center space-x-3">
            <div className={`w-8 h-8 ${currentFlow.color} rounded-lg flex items-center justify-center text-white`}>
              {currentFlow.icon}
            </div>
            <div>
              <h3 className="text-lg font-semibold text-gray-900">{currentFlow.name}</h3>
              <p className="text-sm text-gray-600">{currentFlow.description}</p>
            </div>
          </div>
        </div>

        {/* Workflow Steps */}
        <div className="space-y-4">
          {currentFlow.steps.map((step, index) => (
            <motion.div
              key={step.id}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className={`p-4 rounded-lg border ${getStatusColor(step.status)} ${
                isPlaying && index === currentStep ? 'ring-2 ring-walmart-blue' : ''
              }`}
            >
              <div className="flex items-start space-x-4">
                <div className="flex-shrink-0 mt-1">
                  {getStatusIcon(step.status)}
                </div>
                
                <div className="flex-1">
                  <div className="flex items-center justify-between mb-2">
                    <h4 className="font-semibold text-gray-900">{step.title}</h4>
                    {step.duration && (
                      <span className="text-sm text-gray-500">{step.duration}</span>
                    )}
                  </div>
                  
                  <p className="text-sm text-gray-600 mb-3">{step.description}</p>
                  
                  {step.details && (
                    <div className="space-y-1">
                      {step.details.map((detail, detailIndex) => (
                        <div key={detailIndex} className="flex items-center space-x-2 text-xs text-gray-500">
                          <div className="w-1 h-1 bg-gray-400 rounded-full"></div>
                          <span>{detail}</span>
                        </div>
                      ))}
                    </div>
                  )}
                  
                  {step.status === 'running' && (
                    <div className="mt-3">
                      <div className="flex items-center justify-between text-xs text-gray-600 mb-1">
                        <span>Progress</span>
                        <span>67%</span>
                      </div>
                      <div className="progress-bar">
                        <div className="progress-fill bg-walmart-blue" style={{ width: '67%' }}></div>
                      </div>
                    </div>
                  )}
                </div>
                
                {index < currentFlow.steps.length - 1 && (
                  <div className="flex-shrink-0 mt-6">
                    <ArrowRight className="w-4 h-4 text-gray-400" />
                  </div>
                )}
              </div>
            </motion.div>
          ))}
        </div>
      </div>

      {/* Flow Statistics */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="card">
          <div className="card-header">
            <h3 className="text-lg font-semibold text-gray-900">Flow Performance</h3>
          </div>
          <div className="space-y-4">
            <div className="flex justify-between">
              <span className="text-sm text-gray-600">Average Duration</span>
              <span className="font-semibold text-gray-900">8m 32s</span>
            </div>
            <div className="flex justify-between">
              <span className="text-sm text-gray-600">Success Rate</span>
              <span className="font-semibold text-green-600">97.3%</span>
            </div>
            <div className="flex justify-between">
              <span className="text-sm text-gray-600">Deployments Today</span>
              <span className="font-semibold text-walmart-blue">23</span>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="card-header">
            <h3 className="text-lg font-semibold text-gray-900">Current Status</h3>
          </div>
          <div className="space-y-4">
            <div className="flex items-center space-x-3">
              <div className="status-dot status-online"></div>
              <span className="text-sm text-gray-600">All systems operational</span>
            </div>
            <div className="flex items-center space-x-3">
              <CheckCircle className="w-4 h-4 text-green-500" />
              <span className="text-sm text-gray-600">Quality gates passing</span>
            </div>
            <div className="flex items-center space-x-3">
              <Shield className="w-4 h-4 text-blue-500" />
              <span className="text-sm text-gray-600">Security scans complete</span>
            </div>
          </div>
        </div>

        <div className="card">
          <div className="card-header">
            <h3 className="text-lg font-semibold text-gray-900">Next Actions</h3>
          </div>
          <div className="space-y-3">
            <button className="w-full btn-primary text-sm">
              Deploy to Production
            </button>
            <button className="w-full btn-secondary text-sm">
              Run A/B Test
            </button>
            <button className="w-full btn-secondary text-sm">
              View Logs
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default WorkflowVisualization;