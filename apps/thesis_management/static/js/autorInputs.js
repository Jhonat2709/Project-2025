export const cleanAutors = (i_autor, contenedor_autores, contador) => {

    // Creación del div autor-row-n
    const div_autor_row = document.createElement("div");
    div_autor_row.id = `autor-row-${contador}`;
    div_autor_row.classList.add("form-row");

    // Label para nombres de autor
    const label_nombres = document.createElement("label");
    label_nombres.textContent = "Nombres:";
    label_nombres.htmlFor = `id_autor_nombres_${contador}`;

    // Input para nombres de autor
    const input_nombres = document.createElement("input");
    input_nombres.type = "text";
    input_nombres.name = `autor_nombres_${contador}`;
    input_nombres.id = `id_autor_nombres_${contador}`;
    input_nombres.required = true;
    input_nombres.value = i_autor.Nombre || "";

    // Label para apellidos de autor
    const label_apellidos = document.createElement("label");
    label_apellidos.textContent = "Apellidos:";
    label_apellidos.htmlFor = `id_autor_apellidos_${contador}`;

    // Input para apellidos de autor
    const input_apellidos = document.createElement("input");
    input_apellidos.type = "text";
    input_apellidos.name = `autor_apellidos_${contador}`;
    input_apellidos.id = `id_autor_apellidos_${contador}`;
    input_apellidos.required = true;
    input_apellidos.value = i_autor.Apellido || "";

    // Botón para eliminar el autor
    const button_eliminar = document.createElement("button");
    button_eliminar.type = "button";
    button_eliminar.classList.add("remove-btn");
    button_eliminar.textContent = "Eliminar";
    button_eliminar.setAttribute("data-row-id", contador);

    // Añadir labels e inputs al div autor-row
    div_autor_row.appendChild(label_nombres);
    div_autor_row.appendChild(input_nombres);
    div_autor_row.appendChild(label_apellidos);
    div_autor_row.appendChild(input_apellidos);
    div_autor_row.appendChild(button_eliminar);

    // Añadir el div autor-row al contenedor de autores
    contenedor_autores.appendChild(div_autor_row);
}