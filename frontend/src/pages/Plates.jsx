import React from 'react';

const Plates = () => {
  // Placeholder data
  const plates = [
    { plate: '34ABC123', owner: 'Ahmet Yılmaz', site: 'Site A', block: 'B1', apartment: 5, status: 'İzinli' },
    { plate: '34XYZ789', owner: 'Ayşe Kaya', site: 'Site A', block: 'C2', apartment: 12, status: 'Yasaklı' },
  ];

  return (
    <div className="p-4 bg-gray-900 text-white">
      <h1 className="text-2xl font-bold mb-4">Plaka Yönetimi</h1>

      {/* Yeni Plaka Ekleme Formu */}
      <div className="bg-gray-800 p-4 rounded-lg mb-4">
        <h2 className="text-xl mb-2">Yeni Plaka Kaydı</h2>
        {/* Form elements will go here */}
        <form className="grid grid-cols-2 gap-4">
          <input type="text" placeholder="Ad Soyad" className="p-2 rounded bg-gray-700"/>
          <input type="text" placeholder="Plaka" className="p-2 rounded bg-gray-700"/>
          <select className="p-2 rounded bg-gray-700">
            <option>Site Seç</option>
          </select>
          <select className="p-2 rounded bg-gray-700">
            <option>Blok Seç</option>
          </select>
          <input type="number" placeholder="Daire No" className="p-2 rounded bg-gray-700"/>
          <select className="p-2 rounded bg-gray-700">
            <option>Durum Seç (İzinli/Yasaklı/Misafir)</option>
          </select>
          <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded col-span-2">
            Kaydet
          </button>
        </form>
      </div>

      {/* Plaka Listesi */}
      <div className="bg-gray-800 p-4 rounded-lg">
        <h2 className="text-xl mb-2">Kayıtlı Plakalar</h2>
        <table className="w-full text-left">
          <thead>
            <tr className="border-b border-gray-700">
              <th className="p-2">Plaka</th>
              <th className="p-2">Sahibi</th>
              <th className="p-2">Site/Blok/Daire</th>
              <th className="p-2">Durum</th>
              <th className="p-2">İşlemler</th>
            </tr>
          </thead>
          <tbody>
            {plates.map((plate, index) => (
              <tr key={index} className="border-b border-gray-700">
                <td className="p-2">{plate.plate}</td>
                <td className="p-2">{plate.owner}</td>
                <td className="p-2">{`${plate.site} / ${plate.block} / ${plate.apartment}`}</td>
                <td className="p-2">{plate.status}</td>
                <td className="p-2">
                  <button className="text-sm bg-yellow-500 hover:bg-yellow-700 text-white py-1 px-2 rounded mr-2">Düzenle</button>
                  <button className="text-sm bg-red-500 hover:bg-red-700 text-white py-1 px-2 rounded">Sil</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Plates;
