import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  BarChart3, 
  Brain, 
  Shield, 
  Users, 
  Settings, 
  Activity,
  Database,
  GitBranch,
  Zap,
  TrendingUp
} from 'lucide-react';
import Navbar from './components/Navbar';
import Sidebar from './components/Sidebar';
import PlatformOverview from './components/PlatformOverview';
import DataScientistDashboard from './components/DataScientistDashboard';
import MLOpsEngineerDashboard from './components/MLOpsEngineerDashboard';
import RiskOperationsDashboard from './components/RiskOperationsDashboard';
import ExecutiveDashboard from './components/ExecutiveDashboard';
import WorkflowVisualization from './components/WorkflowVisualization';

export interface UserPersona {
  id: string;
  name: string;
  icon: React.ReactNode;
  color: string;
  description: string;
}

export interface NavItem {
  id: string;
  name: string;
  icon: React.ReactNode;
  component: React.ComponentType;
}

const personas: UserPersona[] = [
  {
    id: 'data-scientist',
    name: 'Data Scientist',
    icon: <Brain className="w-5 h-5" />,
    color: 'bg-purple-500',
    description: 'Model development and experimentation'
  },
  {
    id: 'mlops-engineer',
    name: 'MLOps Engineer',
    icon: <GitBranch className="w-5 h-5" />,
    color: 'bg-blue-500',
    description: 'Deployment and infrastructure management'
  },
  {
    id: 'risk-operations',
    name: 'Risk Operations',
    icon: <Shield className="w-5 h-5" />,
    color: 'bg-red-500',
    description: 'Fraud monitoring and strategy management'
  },
  {
    id: 'executive',
    name: 'Executive',
    icon: <TrendingUp className="w-5 h-5" />,
    color: 'bg-green-500',
    description: 'Strategic oversight and KPIs'
  }
];

const navigationItems: NavItem[] = [
  {
    id: 'overview',
    name: 'Platform Overview',
    icon: <BarChart3 className="w-5 h-5" />,
    component: PlatformOverview
  },
  {
    id: 'data-scientist',
    name: 'Data Scientist',
    icon: <Brain className="w-5 h-5" />,
    component: DataScientistDashboard
  },
  {
    id: 'mlops-engineer',
    name: 'MLOps Engineer',
    icon: <GitBranch className="w-5 h-5" />,
    component: MLOpsEngineerDashboard
  },
  {
    id: 'risk-operations',
    name: 'Risk Operations',
    icon: <Shield className="w-5 h-5" />,
    component: RiskOperationsDashboard
  },
  {
    id: 'executive',
    name: 'Executive',
    icon: <TrendingUp className="w-5 h-5" />,
    component: ExecutiveDashboard
  },
  {
    id: 'workflows',
    name: 'Workflow Visualization',
    icon: <Activity className="w-5 h-5" />,
    component: WorkflowVisualization
  }
];

function App() {
  const [activeView, setActiveView] = useState('overview');
  const [currentPersona, setCurrentPersona] = useState<string | null>(null);

  const ActiveComponent = navigationItems.find(item => item.id === activeView)?.component || PlatformOverview;

  return (
    <div className="min-h-screen bg-gray-50">
      <Navbar 
        personas={personas}
        currentPersona={currentPersona}
        onPersonaChange={setCurrentPersona}
      />
      
      <div className="flex">
        <Sidebar 
          items={navigationItems}
          activeItem={activeView}
          onItemSelect={setActiveView}
        />
        
        <main className="flex-1 min-h-screen">
          <AnimatePresence mode="wait">
            <motion.div
              key={activeView}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.3 }}
              className="h-full"
            >
              <ActiveComponent />
            </motion.div>
          </AnimatePresence>
        </main>
      </div>
    </div>
  );
}

export default App;