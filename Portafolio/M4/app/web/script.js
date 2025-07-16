const productos = [
  {
    id: "prod-001",
    nombre: "Dinamita Triple X",
    descripcion: "¡Explosión garantizada! Ideal para túneles falsos en cañones.",
    img: "img/dinamita.png"
  },
  {
    id: "prod-002",
    nombre: "Imán Industrial ACME",
    descripcion: "Poder de atracción insuperable. No se hace responsable por atraer rocas, trenes o el propio Coyote.",
    img: "img/iman.png"
  },
  {
    id: "prod-003",
    nombre: "Yunque Volador",
    descripcion: "Clásico ACME. No garantizamos precisión en la caída.",
    img: "/img/yunque.png"
  }
];

const contenedor = document.getElementById('product-container');

productos.forEach(p => {
  contenedor.innerHTML += `
    <div style="border:1px solid #ccc; padding: 10px; margin:10px; max-width:200px">
      <img src="${p.img}" alt="${p.nombre}" style="width:100%">
      <h3>${p.nombre}</h3>
      <p>${p.descripcion}</p>
    </div>
  `;
});
