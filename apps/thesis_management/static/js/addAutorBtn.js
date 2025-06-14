export const addNewAutorRow = async (contenedor_autores, contador) => {
  // Crear el nuevo contenedor para los inputs del autor
  const newAutorRow = document.createElement("div");
  newAutorRow.classList.add("form-row");
  newAutorRow.id = `autor-row-${contador}`;

  // Contenido HTML para los nuevos campos
  newAutorRow.innerHTML = `
        <label for="id_autor_nombres_${contador}">Nombres:</label>
        <input type="text" name="autor_nombres_${contador}" id="id_autor_nombres_${contador}" required>
        <label for="id_autor_apellidos_${contador}">Apellidos:</label>
        <input type="text" name="autor_apellidos_${contador}" id="id_autor_apellidos_${contador}" required>
        <button type="button" class="remove-btn" data-row-id="${contador}">Eliminar</button>
    `;

  // Agregación de los nuevos rows al contenedor de autores
  contenedor_autores.appendChild(newAutorRow);
};
