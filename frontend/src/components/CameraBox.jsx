import React from 'react';

const CameraBox = ({ camera, status }) => {
  const getBorderColor = () => {
    switch (status) {
      case 'defined':
        return 'border-green-500';
      case 'undefined':
        return 'border-yellow-500';
      case 'banned':
        return 'border-red-500';
      default:
        return 'border-gray-700';
    }
  };

  return (
    <div className={`bg-gray-800 rounded-lg shadow-lg overflow-hidden border-4 ${getBorderColor()}`}>
      <div className="bg-black h-48 flex items-center justify-center">
        <p className="text-white">Camera Feed Placeholder</p>
      </div>
      <div className="p-2 bg-gray-900 text-white text-sm">
        <p>IP: {camera.ip}</p>
        <p>NodeMCU: {camera.nodemcu}</p>
        <p>Door: {camera.door}</p>
      </div>
    </div>
  );
};

export default CameraBox;
