import React from 'react';
import { motion } from 'framer-motion';
import { NavItem } from '../App';

interface SidebarProps {
  items: NavItem[];
  activeItem: string;
  onItemSelect: (itemId: string) => void;
}

const Sidebar: React.FC<SidebarProps> = ({ items, activeItem, onItemSelect }) => {
  return (
    <aside className="sidebar w-64 min-h-screen">
      <div className="p-6">
        <h2 className="text-sm font-semibold text-gray-500 uppercase tracking-wider mb-4">
          Navigation
        </h2>
        
        <nav className="space-y-1">
          {items.map((item) => (
            <motion.button
              key={item.id}
              onClick={() => onItemSelect(item.id)}
              className={`sidebar-item w-full ${
                activeItem === item.id ? 'active' : ''
              }`}
              whileHover={{ x: 4 }}
              whileTap={{ scale: 0.98 }}
            >
              {item.icon}
              <span className="text-sm font-medium">{item.name}</span>
            </motion.button>
          ))}
        </nav>
      </div>

      {/* Quick Stats */}
      <div className="px-6 py-4 border-t border-gray-200 mt-auto">
        <div className="space-y-3">
          <div className="flex items-center justify-between text-sm">
            <span className="text-gray-500">Active Models</span>
            <span className="font-semibold text-walmart-blue">12</span>
          </div>
          <div className="flex items-center justify-between text-sm">
            <span className="text-gray-500">Deployments Today</span>
            <span className="font-semibold text-success">8</span>
          </div>
          <div className="flex items-center justify-between text-sm">
            <span className="text-gray-500">Avg Latency</span>
            <span className="font-semibold text-accent-teal">24ms</span>
          </div>
        </div>
        
        <div className="mt-4 p-3 bg-blue-50 rounded-lg">
          <div className="flex items-center space-x-2">
            <div className="status-dot status-online"></div>
            <span className="text-xs text-blue-700 font-medium">System Healthy</span>
          </div>
          <p className="text-xs text-blue-600 mt-1">All services operational</p>
        </div>
      </div>
    </aside>
  );
};

export default Sidebar;