// Espera a que todo el contenido del DOM esté completamente cargado antes de ejecutar el script.
document.addEventListener("DOMContentLoaded", function() {
        // Selecciona el enlace que apunta a la URL del 'dashboard'.
        document.querySelector("a[href='{% url 'dashboard' %}']").addEventListener("click", function(event) {
            // Previene la acción por defecto del enlace (navegación normal).
            event.preventDefault();
            // Redirige manualmente a la URL del 'dashboard'.
            window.location.href = "{% url 'dashboard' %}";
        });
    });