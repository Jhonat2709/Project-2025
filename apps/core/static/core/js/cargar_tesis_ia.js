document.addEventListener('DOMContentLoaded', function() {
    console.log('cargar_tesis_ia.js loaded and DOMContentLoaded fired');
    const fileInput = document.getElementById('id_documento');
    const submitButton = document.getElementById('submit-button');
    const tituloInput = document.getElementById('id_titulo');
    const autoresInput = document.getElementById('id_autores');
    const palabrasClaveInput = document.getElementById('id_palabras_clave');
    const resumenTextarea = document.getElementById('id_resumen');
    const numeroPaginasInput = document.getElementById('id_numero_paginas');

    // Deshabilitar el botón de cargar documento al inicio
    submitButton.disabled = true;

    fileInput.addEventListener('change', async function(event) {
        const file = event.target.files[0];
        if (!file) {
            submitButton.disabled = true;
            return;
        }

        // Deshabilitar el botón de cargar documento mientras se procesa el archivo
        submitButton.disabled = true;

        const formData = new FormData();
        formData.append('file', file);

        try {
            const response = await fetch('/thesis_management/process_file/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken') // Función para obtener el token CSRF
                }
            });

            if (response.ok) {
                const data = await response.json();
                // Rellenar los campos del formulario con los datos extraídos
                if (data.titulo) tituloInput.value = data.titulo;
                if (data.autores) autoresInput.value = data.autores.join(', ');
                if (data.palabras_clave) palabrasClaveInput.value = data.palabras_clave.join(', ');
                if (data.resumen) resumenTextarea.value = data.resumen;
                if (data.numero_paginas) numeroPaginasInput.value = data.numero_paginas;

                // Habilitar el botón de cargar documento
                submitButton.disabled = false;
            } else {
                console.error('Error al procesar el archivo:', response.statusText);
                alert('Error al procesar el archivo. Por favor, inténtelo de nuevo.');
            }
        } catch (error) {
            console.error('Error en la solicitud:', error);
            alert('Error en la comunicación con el servidor. Por favor, inténtelo de nuevo.');
        } finally {
            // Asegurarse de que el botón se habilite si hay un error o si el procesamiento falla
            // Esto podría ser condicional si se quiere que el usuario corrija algo antes de reintentar
            // submitButton.disabled = false; // Descomentar si se quiere habilitar siempre
        }
    });

    // Función para obtener el token CSRF de las cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});