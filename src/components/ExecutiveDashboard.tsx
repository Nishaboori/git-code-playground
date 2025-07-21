import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, DollarSign, Users, Target } from 'lucide-react';

const ExecutiveDashboard: React.FC = () => {
  return (
    <div className="p-6 space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">Executive Dashboard</h1>
          <p className="text-gray-600 mt-1">
            Strategic overview and key performance indicators
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="card text-center"
        >
          <TrendingUp className="w-12 h-12 text-green-500 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Performance KPIs</h3>
          <p className="text-gray-600">Track business metrics</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="card text-center"
        >
          <DollarSign className="w-12 h-12 text-blue-500 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">ROI Analysis</h3>
          <p className="text-gray-600">Cost savings and returns</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="card text-center"
        >
          <Users className="w-12 h-12 text-purple-500 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Platform Adoption</h3>
          <p className="text-gray-600">User engagement metrics</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="card text-center"
        >
          <Target className="w-12 h-12 text-red-500 mx-auto mb-4" />
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Strategic Goals</h3>
          <p className="text-gray-600">Objective progress tracking</p>
        </motion.div>
      </div>
    </div>
  );
};

export default ExecutiveDashboard;