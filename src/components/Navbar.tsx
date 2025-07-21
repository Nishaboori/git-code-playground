import React from 'react';
import { motion } from 'framer-motion';
import { ChevronDown, Bell, User, Search } from 'lucide-react';
import { UserPersona } from '../App';

interface NavbarProps {
  personas: UserPersona[];
  currentPersona: string | null;
  onPersonaChange: (persona: string | null) => void;
}

const Navbar: React.FC<NavbarProps> = ({ personas, currentPersona, onPersonaChange }) => {
  const [showPersonaDropdown, setShowPersonaDropdown] = React.useState(false);

  const currentPersonaData = personas.find(p => p.id === currentPersona);

  return (
    <nav className="navbar h-16 px-6 flex items-center justify-between">
      <div className="flex items-center space-x-6">
        <div className="flex items-center space-x-3">
          <div className="w-8 h-8 bg-walmart-blue rounded-lg flex items-center justify-center">
            <span className="text-white font-bold text-sm">W</span>
          </div>
          <div>
            <h1 className="text-xl font-bold text-gray-900">Seller Risk MLOps</h1>
            <p className="text-xs text-gray-500">End-to-End ML Platform</p>
          </div>
        </div>
        
        {/* Quick Search */}
        <div className="hidden md:flex items-center bg-gray-100 rounded-lg px-3 py-2 w-80">
          <Search className="w-4 h-4 text-gray-400 mr-2" />
          <input 
            type="text" 
            placeholder="Search models, experiments, or metrics..." 
            className="bg-transparent flex-1 text-sm outline-none"
          />
        </div>
      </div>

      <div className="flex items-center space-x-4">
        {/* System Status */}
        <div className="hidden lg:flex items-center space-x-2 text-sm">
          <div className="status-dot status-online"></div>
          <span className="text-gray-600">All Systems Operational</span>
        </div>

        {/* Persona Switcher */}
        <div className="relative">
          <button
            onClick={() => setShowPersonaDropdown(!showPersonaDropdown)}
            className="flex items-center space-x-2 px-3 py-2 rounded-lg hover:bg-gray-100 transition-colors"
          >
            {currentPersonaData ? (
              <>
                <div className={`w-6 h-6 ${currentPersonaData.color} rounded flex items-center justify-center text-white text-xs`}>
                  {currentPersonaData.icon}
                </div>
                <span className="text-sm font-medium">{currentPersonaData.name}</span>
              </>
            ) : (
              <>
                <User className="w-5 h-5 text-gray-500" />
                <span className="text-sm text-gray-600">Select Role</span>
              </>
            )}
            <ChevronDown className="w-4 h-4 text-gray-400" />
          </button>

          {showPersonaDropdown && (
            <motion.div
              initial={{ opacity: 0, y: 10 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: 10 }}
              className="absolute right-0 mt-2 w-72 bg-white rounded-lg shadow-lg border border-gray-200 py-2 z-50"
            >
              <div className="px-3 py-2 border-b border-gray-100">
                <p className="text-xs font-medium text-gray-500 uppercase tracking-wider">Switch Perspective</p>
              </div>
              
              {personas.map((persona) => (
                <button
                  key={persona.id}
                  onClick={() => {
                    onPersonaChange(persona.id);
                    setShowPersonaDropdown(false);
                  }}
                  className={`w-full flex items-center space-x-3 px-3 py-3 hover:bg-gray-50 transition-colors ${
                    currentPersona === persona.id ? 'bg-blue-50 border-r-2 border-walmart-blue' : ''
                  }`}
                >
                  <div className={`w-8 h-8 ${persona.color} rounded flex items-center justify-center text-white`}>
                    {persona.icon}
                  </div>
                  <div className="text-left">
                    <p className="text-sm font-medium text-gray-900">{persona.name}</p>
                    <p className="text-xs text-gray-500">{persona.description}</p>
                  </div>
                </button>
              ))}
              
              <div className="border-t border-gray-100 mt-2 pt-2">
                <button
                  onClick={() => {
                    onPersonaChange(null);
                    setShowPersonaDropdown(false);
                  }}
                  className="w-full flex items-center space-x-3 px-3 py-2 hover:bg-gray-50 transition-colors"
                >
                  <div className="w-8 h-8 bg-gray-300 rounded flex items-center justify-center">
                    <User className="w-4 h-4 text-gray-600" />
                  </div>
                  <div className="text-left">
                    <p className="text-sm font-medium text-gray-900">Platform Overview</p>
                    <p className="text-xs text-gray-500">General platform view</p>
                  </div>
                </button>
              </div>
            </motion.div>
          )}
        </div>

        {/* Notifications */}
        <button className="relative p-2 rounded-lg hover:bg-gray-100 transition-colors">
          <Bell className="w-5 h-5 text-gray-600" />
          <div className="absolute -top-1 -right-1 w-3 h-3 bg-red-500 rounded-full flex items-center justify-center">
            <span className="text-xs text-white">3</span>
          </div>
        </button>

        {/* User Menu */}
        <div className="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center">
          <User className="w-4 h-4 text-gray-600" />
        </div>
      </div>
    </nav>
  );
};

export default Navbar;