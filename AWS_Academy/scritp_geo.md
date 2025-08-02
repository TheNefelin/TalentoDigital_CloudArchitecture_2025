
```html
<button onclick="obtenerUbicacion()">Obtener mi ubicación</button>
```

```javascript
<script>
function obtenerUbicacion() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      function(position) {
        alert("Latitud: " + position.coords.latitude + 
              "\nLongitud: " + position.coords.longitude);
      },
      function(error) {
        alert("Error al obtener la ubicación: " + error.message);
      }
    );
  } else {
    alert("Geolocalización no soportada por este navegador");
  }
}
</script>
```
