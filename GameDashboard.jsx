import React, { useState, useEffect } from 'react';

export default function GameDashboard() {
  const [ammoCount, setAmmoCount] = useState(15);
  const [infectionLevel, setInfectionLevel] = useState(5);
  const [storageBox, setStorageBox] = useState(['Handgun Ammo', 'Green Herb']);
  const [terminalAlerts, setTerminalAlerts] = useState([]);

  // Auto-increasing virus threat loop simulator
  useEffect(() => {
    const tVirusSpread = setInterval(() => {
      setInfectionLevel(prev => {
        if (prev >= 100) return 100;
        return prev + 1;
      });
    }, 4000);
    return () => clearInterval(tVirusSpread);
  }, []);

  const combineHerbs = (utilityItem, infectionReduction, assetCost) => {
    if (ammoCount >= assetCost) {
      setAmmoCount(prev => prev - assetCost);
      setInfectionLevel(prev => Math.max(0, prev - infectionReduction));
      setStorageBox(prev => [...prev, utilityItem]);
      setTerminalAlerts(prev => [`🟢 System Admin: Applied ${utilityItem} (Infection Down ${infectionReduction}%)`, ...prev.slice(0, 3)]);
    } else {
      setTerminalAlerts(prev => [`🔴 Error: Insufficient component material for ${utilityItem}`, ...prev.slice(0, 3)]);
    }
  };

  return (
    <div style={{ background: '#000', color: '#39ff14', padding: '25px', borderRadius: '4px', border: '2px solid #ff3333', fontFamily: 'monospace' }}>
      <h2 style={{ color: '#ff3333', borderBottom: '2px dashed #ff3333', paddingBottom: '5px' }}>☣️ SURVIVAL HUD SYSTEM</h2>
      
      <div style={{ display: 'flex', gap: '40px', margin: '20px 0', fontSize: '1.1rem' }}>
        <div>💥 Available Ammo: <span style={{ color: '#fff', fontWeight: 'bold' }}>{ammoCount} RDS</span></div>
        <div>⚠️ T-Virus Infection Rate: <span style={{ color: infectionLevel > 50 ? '#ff0000' : '#ffcc00', fontWeight: 'bold' }}>{infectionLevel}%</span></div>
      </div>

      <div style={{ margin: '20px 0' }}>
        <h3>🛠️ Item Modification & Assembly Station</h3>
        <button 
          onClick={() => combineHerbs('Mixed Herb (G+R)', 35, 2)}
          style={{ padding: '10px', marginRight: '10px', background: '#006400', color: '#fff', border: '1px solid #39ff14', cursor: 'pointer' }}
        >
          Mix Herbs (Costs 2 Ammo Resource)
        </button>
        <button 
          onClick={() => setAmmoCount(prev => prev + 10)}
          style={{ padding: '10px', background: '#333', color: '#ffcc00', border: '1px solid #ffcc00', cursor: 'pointer', fontWeight: 'bold' }}
        >
          Scavenge Sector Floor (+10 Ammo Ammo)
        </button>
      </div>

      <div style={{ marginTop: '20px' }}>
        <h3>📦 Tactical Item Slots ({storageBox.length}/8)</h3>
        <ul style={{ color: '#fff' }}>
          {storageBox.map((item, id) => <li key={id}>[Slot {id + 1}] - {item}</li>)}
        </ul>
      </div>

      <div style={{ background: '#111', padding: '10px', borderLeft: '3px solid #ff3333', height: '90px', overflowY: 'auto', marginTop: '20px' }}>
        <small style={{ color: '#888' }}>📡 TERMINAL LOG STREAM:</small>
        {terminalAlerts.map((msg, idx) => <div key={idx} style={{ fontSize: '0.85rem', color: '#39ff14' }}>{msg}</div>)}
      </div>
    </div>
  );
}
