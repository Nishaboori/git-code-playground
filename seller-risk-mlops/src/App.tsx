import React from 'react';
import { BrowserRouter as Router, Routes, Route, useNavigate } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import ExecutiveDashboard from './components/ExecutiveDashboard';
import DataScientistDashboard from './components/DataScientistDashboard';
import MLOpsEngineerDashboard from './components/MLOpsEngineerDashboard';
import RiskOperationsDashboard from './components/RiskOperationsDashboard';
import './App.css';
import { TrendingUp, Beaker, GitBranch, Shield } from 'lucide-react';
import { UserPersona } from './types';

const navItems = [
  { id: 'executive', name: 'Executive', icon: <TrendingUp className="w-5 h-5 mr-2" />, component: ExecutiveDashboard },
  { id: 'datascientist', name: 'Data Scientist', icon: <Beaker className="w-5 h-5 mr-2" />, component: DataScientistDashboard },
  { id: 'mlops', name: 'MLOps Engineer', icon: <GitBranch className="w-5 h-5 mr-2" />, component: MLOpsEngineerDashboard },
  { id: 'riskops', name: 'Risk Operations', icon: <Shield className="w-5 h-5 mr-2" />, component: RiskOperationsDashboard },
];

function AppContent() {
  const navigate = useNavigate();
  const [active, setActive] = React.useState('executive');

  React.useEffect(() => {
    // Navigate to the selected dashboard route
    switch (active) {
      case 'executive':
        navigate('/');
        break;
      case 'datascientist':
        navigate('/datascientist');
        break;
      case 'mlops':
        navigate('/mlops');
        break;
      case 'riskops':
        navigate('/riskops');
        break;
      default:
        navigate('/');
    }
  }, [active, navigate]);

  return (
    <div className="flex min-h-screen">
      <Sidebar items={navItems} activeItem={active} onItemSelect={setActive} />
      <main className="flex-1 bg-gray-50">
        <Routes>
          <Route path="/" element={<ExecutiveDashboard />} />
          <Route path="/datascientist" element={<DataScientistDashboard />} />
          <Route path="/mlops" element={<MLOpsEngineerDashboard />} />
          <Route path="/riskops" element={<RiskOperationsDashboard />} />
        </Routes>
      </main>
    </div>
  );
}

function App() {
  return (
    <Router>
      <AppContent />
    </Router>
  );
}

export default App;
