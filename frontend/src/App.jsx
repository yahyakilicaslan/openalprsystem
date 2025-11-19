import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import LiveLog from './components/LiveLog';
import Dashboard from './pages/Dashboard';
import Plates from './pages/Plates';
import './index.css';

function App() {
  return (
    <div className="bg-gray-900 min-h-screen text-white flex flex-col">
      <Header />
      <div className="flex flex-grow">
        <Sidebar />
        <div className="flex-grow">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/plates" element={<Plates />} />
            {/* Add other routes here for sites, doors, cameras etc. */}
          </Routes>
        </div>
      </div>
      <LiveLog />
    </div>
  );
}

export default App;
