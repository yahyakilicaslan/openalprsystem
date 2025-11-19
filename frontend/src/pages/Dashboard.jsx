import React from 'react';
import CameraBox from '../components/CameraBox';
import MiniLog from '../components/MiniLog';

const Dashboard = () => {
    // Placeholder data for cameras
    const cameras = [
        { ip: '192.168.1.10', nodemcu: '192.168.1.20', door: 'Giriş' },
        { ip: '192.168.1.11', nodemcu: '192.168.1.21', door: 'Çıkış' },
        { ip: '192.168.1.12', nodemcu: '192.168.1.22', door: 'Otopark' },
        { ip: '192.168.1.13', nodemcu: '192.168.1.23', door: 'Misafir' },
    ];

    return (
        <main className="flex-grow p-4 flex">
            {/* Main content area */}
            <div className="flex-grow grid grid-cols-1 md:grid-cols-2 gap-4">
                <CameraBox camera={cameras[0]} status="defined" />
                <CameraBox camera={cameras[1]} status="undefined" />
                <CameraBox camera={cameras[2]} status="banned" />
                <CameraBox camera={cameras[3]} status="idle" />
            </div>

            {/* Right sidebar for mini log */}
            <aside className="w-1/4 ml-4">
                <MiniLog />
            </aside>
        </main>
    );
};

export default Dashboard;
