import React from 'react';
import { Link } from 'react-router-dom';

const Sidebar = () => {
  return (
    <aside className="w-64 bg-gray-800 text-white p-4">
      <nav>
        <ul>
          <li className="mb-2">
            <Link to="/" className="block p-2 rounded hover:bg-gray-700">Ana Sayfa</Link>
          </li>
          <li className="mb-2">
            <Link to="/plates" className="block p-2 rounded hover:bg-gray-700">Plaka Yönetimi</Link>
          </li>
          {/* Add other links here for sites, doors, cameras etc. */}
        </ul>
      </nav>
    </aside>
  );
};

export default Sidebar;
