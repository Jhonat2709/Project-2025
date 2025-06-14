document.addEventListener('DOMContentLoaded', function() {
    // Selecciona los elementos del DOM necesarios: el sidebar y el botón para mostrar/ocultar.
    const sidebar = document.querySelector('.sidebar');
    const sidebarToggle = document.getElementById('sidebarToggle');

    // Función para establecer el estado del sidebar (colapsado o expandido).
    function setSidebarState(collapsed) {
        if (collapsed) {
            // Si se debe colapsar: Añade clases para estilos de colapso y guarda el estado.
            sidebar.classList.add('collapsed');
            document.body.classList.add('sidebar-collapsed');
            localStorage.setItem('sidebarState', 'collapsed');
        } else {
            // Si se debe expandir: Remueve clases de colapso y guarda el estado.
            sidebar.classList.remove('collapsed');
            document.body.classList.remove('sidebar-collapsed');
            localStorage.setItem('sidebarState', 'expanded');
        }
    }
    // Verifica si el botón de despliegue existe en la página.
    if (sidebarToggle) {
        // Añade un listener para el evento 'click' en el botón.
        sidebarToggle.addEventListener('click', function() {
            const isCollapsed = sidebar.classList.contains('collapsed');
            setSidebarState(!isCollapsed); // Invierte el estado actual del sidebar.
        });
    }
    // Establece el estado inicial del sidebar al cargar la página.
    // 'false' aquí significa que no está colapsado, por lo tanto, se mostrará expandido por defecto.
    setSidebarState(false); 
});