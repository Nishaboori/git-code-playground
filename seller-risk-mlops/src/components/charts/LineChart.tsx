import React, { useState, useEffect } from 'react';
import { LineChart as RechartsLineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const LineChart: React.FC = () => {
  const [data, setData] = useState([
    { time: '00:00', latency: 25, throughput: 1200 },
    { time: '04:00', latency: 23, throughput: 1350 },
    { time: '08:00', latency: 28, throughput: 1800 },
    { time: '12:00', latency: 26, throughput: 2100 },
    { time: '16:00', latency: 24, throughput: 1950 },
    { time: '20:00', latency: 22, throughput: 1600 },
  ]);

  // Simulate real-time updates
  useEffect(() => {
    const interval = setInterval(() => {
      setData(prevData => {
        const newData = [...prevData];
        const lastPoint = newData[newData.length - 1];
        
        // Update the last point with slight variations
        newData[newData.length - 1] = {
          ...lastPoint,
          latency: Math.max(20, Math.min(30, lastPoint.latency + (Math.random() - 0.5) * 2)),
          throughput: Math.max(1000, Math.min(2500, lastPoint.throughput + (Math.random() - 0.5) * 200))
        };
        
        return newData;
      });
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  const CustomTooltip = ({ active, payload, label }: any) => {
    if (active && payload && payload.length) {
      return (
        <div className="bg-white p-3 border border-gray-200 rounded-lg shadow-lg">
          <p className="text-sm font-medium text-gray-900">{`Time: ${label}`}</p>
          <p className="text-sm text-blue-600">{`Latency: ${payload[0].value.toFixed(1)}ms`}</p>
          <p className="text-sm text-green-600">{`Throughput: ${payload[1].value.toFixed(0)} req/s`}</p>
        </div>
      );
    }
    return null;
  };

  return (
    <div className="h-64">
      <ResponsiveContainer width="100%" height="100%">
        <RechartsLineChart data={data} margin={{ top: 5, right: 30, left: 20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
          <XAxis 
            dataKey="time" 
            stroke="#6b7280"
            fontSize={12}
          />
          <YAxis 
            yAxisId="left"
            stroke="#6b7280"
            fontSize={12}
          />
          <YAxis 
            yAxisId="right"
            orientation="right"
            stroke="#6b7280"
            fontSize={12}
          />
          <Tooltip content={<CustomTooltip />} />
          <Line 
            yAxisId="left"
            type="monotone" 
            dataKey="latency" 
            stroke="#3b82f6" 
            strokeWidth={2}
            dot={{ fill: '#3b82f6', strokeWidth: 2, r: 4 }}
            activeDot={{ r: 6, stroke: '#3b82f6', strokeWidth: 2, fill: '#ffffff' }}
          />
          <Line 
            yAxisId="right"
            type="monotone" 
            dataKey="throughput" 
            stroke="#10b981" 
            strokeWidth={2}
            dot={{ fill: '#10b981', strokeWidth: 2, r: 4 }}
            activeDot={{ r: 6, stroke: '#10b981', strokeWidth: 2, fill: '#ffffff' }}
          />
        </RechartsLineChart>
      </ResponsiveContainer>
      
      <div className="flex items-center justify-center space-x-6 mt-4 text-sm">
        <div className="flex items-center space-x-2">
          <div className="w-3 h-3 bg-blue-500 rounded-full"></div>
          <span className="text-gray-600">Latency (ms)</span>
        </div>
        <div className="flex items-center space-x-2">
          <div className="w-3 h-3 bg-green-500 rounded-full"></div>
          <span className="text-gray-600">Throughput (req/s)</span>
        </div>
      </div>
    </div>
  );
};

export default LineChart;