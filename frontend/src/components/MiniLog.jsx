import React from 'react';

const MiniLog = () => {
  // Placeholder data
  const logs = [
    { plate: '34ABC123', date: '19-11-25', time: '13:30', status: 'Tanımlı', img: 'https://via.placeholder.com/100x50' },
    { plate: '34XYZ789', date: '19-11-25', time: '13:28', status: 'Yasaklı', img: 'https://via.placeholder.com/100x50' },
  ];

  return (
    <div className="bg-gray-800 p-4 rounded-lg shadow-lg h-full">
      <h2 className="text-white text-lg font-bold mb-4">Son Tespitler</h2>
      <div className="space-y-4">
        {logs.map((log, index) => (
          <div key={index} className="flex items-center bg-gray-900 p-2 rounded">
            <img src={log.img} alt="plate" className="w-24 h-12 object-cover rounded mr-4"/>
            <div>
              <p className="text-white font-mono">{log.plate}</p>
              <p className="text-gray-400 text-sm">{log.date} {log.time}</p>
              <p className="text-sm" style={{ color: log.status === 'Tanımlı' ? '#22c55e' : '#ef4444' }}>{log.status}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default MiniLog;
