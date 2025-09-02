document.addEventListener('DOMContentLoaded', () => {
    const addAssetForm = document.getElementById('add-asset-form');
    const assetsTableBody = document.getElementById('assets-table-body'); // Ahora apunta al tbody
    const totalValueSpan = document.getElementById('total-value');
    const noAssetsMessage = document.getElementById('no-assets-message');
    const messageBox = document.getElementById('message-box');

        const serverInfoSpan = document.getElementById('server-info');

    // Función para obtener y mostrar el nombre del servidor
    async function loadServerInfo() {
        try {
            const response = await fetch('/api/server-info');
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            const data = await response.json();
            serverInfoSpan.textContent = data.serverName;
        } catch (error) {
            console.error('Error al obtener la información del servidor:', error);
            serverInfoSpan.textContent = 'Error al cargar info del servidor';
            serverInfoSpan.classList.add('text-red-600');
        }
    }

    // Llama a la nueva función al cargar la página
    loadServerInfo();
    

    // Función para mostrar mensajes al usuario (éxito/error)
    function showMessage(message, isError = false) {
        messageBox.textContent = message;
        messageBox.classList.remove('hidden', 'text-green-600', 'text-red-600');
        if (isError) {
            messageBox.classList.add('text-red-600');
        } else {
            messageBox.classList.add('text-green-600');
        }
        setTimeout(() => {
            messageBox.classList.add('hidden');
        }, 3000); // El mensaje desaparece después de 3 segundos
    }

    // Función para formatear valores monetarios
    function formatCurrency(value) {
        // Usamos Intl.NumberFormat para formatear como moneda, con el símbolo de dólar
        // 'es-CL' para formato chileno (punto para miles, coma para decimales)
        // style: 'currency' y currency: 'USD' para el símbolo del dólar y dos decimales
        return new Intl.NumberFormat('es-CL', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        }).format(value);
    }

    // Función para obtener el valor actual de un activo (mocked)
    function getMockCurrentPrice(assetName) {
        const nameToLookup = (assetName && typeof assetName === 'string') ? assetName.toUpperCase() : ''; 
        const prices = {
            "TSLA": 180.50,
            "AAPL": 170.00,
            "MSFT": 420.00,
            "GOOG": 160.00,
            "BTC": 65000.00,
            "ETH": 3200.00
        };
        return prices[nameToLookup] || (Math.random() * 100 + 50).toFixed(2);
    }

    // Función para renderizar un activo en la tabla
    function renderAsset(asset) {
        console.log('Intentando renderizar activo. Objeto asset recibido:', asset); 
        
        const assetName = asset?.Name || '';
        const assetQuantity = asset?.Quantity || 0;
        const assetPurchasePrice = asset?.PurchasePrice || 0;
        const assetId = asset?.Id;

        const currentPrice = parseFloat(getMockCurrentPrice(assetName)); 
        const currentValue = (assetQuantity * currentPrice); 
        const gainLoss = (currentValue - (assetQuantity * assetPurchasePrice)); 
        const gainLossClass = gainLoss >= 0 ? 'text-green-600' : 'text-red-600';

        const row = document.createElement('tr');
        row.className = 'hover:bg-gray-100'; // Estilo de hover para la fila

        row.innerHTML = `
            <td class="py-3 px-6 text-left whitespace-nowrap">${assetId}</td>
            <td class="py-3 px-6 text-left">${assetName.toUpperCase()}</td>
            <td class="py-3 px-6 text-left">${assetQuantity.toFixed(2)}</td>
            <td class="py-3 px-6 text-left">${formatCurrency(assetPurchasePrice)}</td>
            <td class="py-3 px-6 text-left">${formatCurrency(currentPrice)}</td>
            <td class="py-3 px-6 text-left ${gainLossClass}">${formatCurrency(gainLoss)}</td>
            <td class="py-3 px-6 text-left">${formatCurrency(currentValue)}</td>
            <td class="py-3 px-6 text-center">
                <button class="delete-button bg-red-500 hover:bg-red-600 text-white font-bold py-1 px-3 rounded-md text-xs" data-id="${assetId}">Eliminar</button>
            </td>
        `;
        assetsTableBody.appendChild(row); // Añadir la fila al tbody

        // Añadir el listener para el botón de eliminar
        row.querySelector('.delete-button').addEventListener('click', (e) => {
            const idToDelete = e.target.getAttribute('data-id');
            deleteAsset(idToDelete);
        });
    }

    // Función para cargar los activos desde el backend
    async function loadAssets() {
        console.log('Intentando cargar activos del backend...'); 
        try {
            const response = await fetch('/api/portfolio');
            console.log('Respuesta del backend (HTTP status):', response.status); 
            
            if (!response.ok) {
                const errorText = await response.text(); 
                console.error('Error en la respuesta del servidor:', errorText); 
                throw new Error(`HTTP error! status: ${response.status}, message: ${errorText}`);
            }
            
            const assets = await response.json();
            console.log('Datos recibidos del backend (JSON):', assets); 

            assetsTableBody.innerHTML = ''; // Limpiar el cuerpo de la tabla

            if (assets.length === 0) {
                noAssetsMessage.classList.remove('hidden'); // Mostrar mensaje si no hay activos
            } else {
                noAssetsMessage.classList.add('hidden'); // Ocultar mensaje si hay activos
                assets.forEach(asset => renderAsset(asset));
            }
            calculateTotalValue(assets);

        } catch (error) {
            console.error('Error al cargar activos:', error);
            showMessage(`Error al cargar los activos: ${error.message}`, true);
        }
    }

    // Función para calcular y mostrar el valor total de la cartera
    function calculateTotalValue(assets) {
        let totalValue = 0;
        assets.forEach(asset => {
            const currentPrice = parseFloat(getMockCurrentPrice(asset?.Name || '')); 
            totalValue += (asset?.Quantity || 0) * currentPrice; 
        });
        totalValueSpan.textContent = formatCurrency(totalValue); // Formatear el valor total
    }

    // Manejar el envío del formulario para añadir un activo
    addAssetForm.addEventListener('submit', async (e) => {
        e.preventDefault(); 

        const formData = new FormData(addAssetForm);
        const asset = {
            name: formData.get('name'),
            quantity: parseFloat(formData.get('quantity')),
            purchasePrice: parseFloat(formData.get('purchasePrice'))
        };

        try {
            const response = await fetch('/api/portfolio', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(asset)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
            }

            showMessage('Activo añadido con éxito.');
            addAssetForm.reset(); 
            loadAssets(); 

        } catch (error) {
            console.error('Error al añadir activo:', error);
            showMessage(`Error al añadir activo: ${error.message}`, true);
        }
    });

    // Función para eliminar un activo
    async function deleteAsset(id) {
        const userConfirmed = confirm('¿Estás seguro de que quieres eliminar este activo?');
        if (!userConfirmed) {
            return;
        }

        try {
            const response = await fetch(`/api/portfolio/${id}`, {
                method: 'DELETE'
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.message || `HTTP error! status: ${response.status}`);
            }

            showMessage('Activo eliminado con éxito.');
            loadAssets(); 
        } catch (error) {
            console.error('Error al eliminar activo:', error);
            showMessage(`Error al eliminar activo: ${error.message}`, true);
        }
    }

    // Cargar los activos al iniciar la aplicación
    loadAssets();
});
