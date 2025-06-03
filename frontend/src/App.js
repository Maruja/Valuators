import logo from './logo.svg';
import './App.css';

import React, { useEffect, useState } from 'react';

function App() {
  const [addresses, setAddresses] = useState([]);
  const [search, setSearch] = useState('');


  useEffect(() => {
    fetch('http://localhost:5000/Address')
      .then(response => response.json())
      .then(data => setAddresses(data));
  }, []);

  const handleSearch = () => {
    fetch(`http://localhost:5000/CP_code/${search}`)
      .then(response => {
        if(!response.ok) {
          throw new Error("no se encontraron direcciones con el CP proporcionado !!!");
        }
        return response.json();
      })
      .then(data => setAddresses(data))
      .catch(err => {
        console.error(err.message);
        setAddresses([]);//limpia la lista si no hay resultados.     
      });
  };
  

  return (
    <div>
      <h1>Lista de direcciones</h1>
      <input
      type="text"
      placeholder="Escribe un código postal"
      value={search}
      onChange={(e) => setSearch(e.target.value)}
      />
      <button onClick={handleSearch}>Buscar</button>

      <ul>
        {addresses.map(addr => (
          <li key={addr.id_address}>{addr.D_mnpio} - {addr.d_codigo} - {addr.d_estado} - {addr.d_asenta}</li>
        ))}
      </ul>
    </div>
  );
}


export default App;
