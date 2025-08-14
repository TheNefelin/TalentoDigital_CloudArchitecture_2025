document.addEventListener('DOMContentLoaded', () => {
    const contenedor = document.getElementById('contenido-dinamico');

    async function obtenerDatos() {
        try {
            const respuesta = await fetch('repo/data.json');
            if (!respuesta.ok) {
                throw new Error(`HTTP error! status: ${respuesta.status}`);
            }
            const datos = await respuesta.json();
            mostrarDatos(datos);
        } catch (error) {
            console.error('Error al cargar los datos:', error);
            contenedor.innerHTML = '<p>Lo sentimos, no se pudieron cargar los datos.</p>';
        }
    }

    function mostrarDatos(datos) {
        contenedor.innerHTML = '';

        datos.forEach(item => {
            const tarjeta = document.createElement('div');
            tarjeta.classList.add('tarjeta');

            // Título y descripción
            const titulo = document.createElement('h2');
            titulo.textContent = item.titulo;

            const descripcion = document.createElement('p');
            descripcion.textContent = item.descripcion;

            tarjeta.appendChild(titulo);
            tarjeta.appendChild(descripcion);

            // Conceptos clave
            if (item.conceptos_clave && item.conceptos_clave.length > 0) {
                const listaConceptos = document.createElement('ul');
                listaConceptos.classList.add('conceptos-clave');
                item.conceptos_clave.forEach(concepto => {
                    const li = document.createElement('li');
                    li.textContent = concepto;
                    listaConceptos.appendChild(li);
                });
                tarjeta.appendChild(listaConceptos);
            }

            // Ejemplos
            if (item.ejemplos && item.ejemplos.length > 0) {
                const tituloEjemplos = document.createElement('h3');
                tituloEjemplos.textContent = 'Ejemplos en C#';
                tarjeta.appendChild(tituloEjemplos);

                item.ejemplos.forEach(ejemplo => {
                    const seccionEjemplo = document.createElement('div');
                    seccionEjemplo.classList.add('ejemplo');

                    const nombreEjemplo = document.createElement('h4');
                    nombreEjemplo.textContent = ejemplo.nombre;
                    seccionEjemplo.appendChild(nombreEjemplo);

                    const explicacionEjemplo = document.createElement('p');
                    explicacionEjemplo.textContent = ejemplo.explicacion;
                    seccionEjemplo.appendChild(explicacionEjemplo);

                    const codigoEjemplo = document.createElement('pre');
                    const codigoElemento = document.createElement('code');
                    codigoElemento.textContent = ejemplo.codigo;
                    codigoEjemplo.appendChild(codigoElemento);
                    seccionEjemplo.appendChild(codigoEjemplo);

                    tarjeta.appendChild(seccionEjemplo);
                });
            }

            contenedor.appendChild(tarjeta);
        });
    }

    obtenerDatos();
});