import React from 'react';
import { motion } from 'framer-motion';
import { TrendingUp, TrendingDown, Minus } from 'lucide-react';

interface MetricCardProps {
  title: string;
  value: string;
  change: string;
  trend: 'up' | 'down' | 'stable';
  icon: React.ReactNode;
  color: string;
}

const MetricCard: React.FC<MetricCardProps> = ({ title, value, change, trend, icon, color }) => {
  const getTrendIcon = () => {
    switch (trend) {
      case 'up':
        return <TrendingUp className="w-4 h-4 text-green-500" />;
      case 'down':
        return <TrendingDown className="w-4 h-4 text-red-500" />;
      default:
        return <Minus className="w-4 h-4 text-gray-400" />;
    }
  };

  const getTrendColor = () => {
    switch (trend) {
      case 'up':
        return 'text-green-600';
      case 'down':
        return 'text-red-600';
      default:
        return 'text-gray-600';
    }
  };

  return (
    <motion.div
      className="metric-card"
      whileHover={{ scale: 1.02, y: -2 }}
      transition={{ duration: 0.2 }}
    >
      <div className="flex items-center justify-between mb-4">
        <div className={`w-12 h-12 ${color} rounded-lg flex items-center justify-center text-white`}>
          {icon}
        </div>
        {getTrendIcon()}
      </div>
      
      <div className="space-y-1">
        <h3 className="text-2xl font-bold text-gray-900 animate-counter">{value}</h3>
        <p className="text-sm font-medium text-gray-600">{title}</p>
        <p className={`text-xs ${getTrendColor()}`}>{change}</p>
      </div>
    </motion.div>
  );
};

export default MetricCard;