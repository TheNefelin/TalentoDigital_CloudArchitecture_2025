const apiUrl = 'data/personajes.json';

async function fetchCharacters() {
  try {
    const response = await fetch(apiUrl);
    const data = await response.json();
    renderCards(data);
  } catch (error) {
    console.error('Error al obtener personajes:', error);
  }
}

function renderCards(characters) {
  const container = document.getElementById('cards-container');
  characters.forEach(personaje => {
    const card = document.createElement('div');
    card.className = 'card';
    card.innerHTML = `
      <img src="img/${personaje.img}" alt="${personaje.nombre}">
      <div class="card-body">
        <h3>${personaje.nombre}</h3>
        <p><span class="nen-type">Nen:</span> ${personaje.tipo_nen}</p>
        <p><strong>Edad:</strong> ${personaje.edad}</p>
        <p>${personaje.descripcion}</p>
      </div>
    `;
    container.appendChild(card);
  });
}

fetchCharacters();
