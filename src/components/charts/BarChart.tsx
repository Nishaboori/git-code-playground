import React from 'react';
import { BarChart as RechartsBarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

interface BarChartProps {
  data?: any[];
  dataKey?: string;
  nameKey?: string;
  color?: string;
}

const BarChart: React.FC<BarChartProps> = ({ 
  data = [
    { name: 'Fraud Detector v1', accuracy: 89.2, precision: 87.5, recall: 91.3 },
    { name: 'Fraud Detector v2', accuracy: 92.1, precision: 90.2, recall: 93.8 },
    { name: 'Risk Scorer v1', accuracy: 85.7, precision: 83.1, recall: 88.2 },
    { name: 'Risk Scorer v2', accuracy: 88.9, precision: 86.7, recall: 91.1 },
  ],
  dataKey = 'accuracy',
  nameKey = 'name',
  color = '#3b82f6'
}) => {
  const CustomTooltip = ({ active, payload, label }: any) => {
    if (active && payload && payload.length) {
      const data = payload[0].payload;
      return (
        <div className="bg-white p-3 border border-gray-200 rounded-lg shadow-lg">
          <p className="text-sm font-medium text-gray-900 mb-2">{label}</p>
          <p className="text-sm text-blue-600">{`Accuracy: ${data.accuracy}%`}</p>
          <p className="text-sm text-green-600">{`Precision: ${data.precision}%`}</p>
          <p className="text-sm text-purple-600">{`Recall: ${data.recall}%`}</p>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="h-64">
      <ResponsiveContainer width="100%" height="100%">
        <RechartsBarChart data={data} margin={{ top: 20, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
          <XAxis 
            dataKey={nameKey} 
            stroke="#6b7280"
            fontSize={12}
            angle={-45}
            textAnchor="end"
            height={80}
          />
          <YAxis 
            stroke="#6b7280"
            fontSize={12}
          />
          <Tooltip content={<CustomTooltip />} />
          <Bar 
            dataKey={dataKey} 
            fill={color}
            radius={[4, 4, 0, 0]}
          />
        </RechartsBarChart>
      </ResponsiveContainer>
    </div>
  );
};

export default BarChart;