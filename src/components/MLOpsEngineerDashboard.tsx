import React from 'react';
import { motion } from 'framer-motion';
import { GitBranch, Server, Settings, Monitor } from 'lucide-react';

const MLOpsEngineerDashboard: React.FC = () => {
  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">MLOps Engineering</h1>
          <p className="text-gray-600 mt-1">
            Model deployment, infrastructure management, and CI/CD pipelines
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="card text-center"
        >
          <GitBranch className="w-12 h-12 text-blue-500 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Deployment Pipeline</h3>
          <p className="text-gray-600">Manage CI/CD workflows</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="card text-center"
        >
          <Server className="w-12 h-12 text-green-500 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Infrastructure</h3>
          <p className="text-gray-600">Monitor system resources</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="card text-center"
        >
          <Monitor className="w-12 h-12 text-purple-500 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Monitoring</h3>
          <p className="text-gray-600">Real-time system health</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="card text-center"
        >
          <Settings className="w-12 h-12 text-orange-500 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Configuration</h3>
          <p className="text-gray-600">Manage platform settings</p>
        </motion.div>
      </div>
    </div>
  );
};

export default MLOpsEngineerDashboard;