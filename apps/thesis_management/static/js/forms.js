import { sendDocumentToApi } from "./calls.js";
import { cleanAutors } from "./autorInputs.js";
import { deleteAutorRow } from "./deleteButton.js";
import { addNewAutorRow } from "./addAutorBtn.js";

// Ubicación de los elementos del formulario por ID

const titulo_input = document.getElementById("id_titulo");
const numero_paginas_input = document.getElementById("id_numero_paginas");
const resumen_input = document.getElementById("id_resumen");
const palabras_clave_input = document.getElementById("id_palabras_clave_texto");
const file_input = document.getElementById("id_documento");
const contenedor_autores = document.getElementById("autores-container");

// Contador para generación de IDs únicos para los inputs de autore
let contador = 0;

// Obtención del token CSRF desde las cookies
var csrf_token = document.cookie.split("=")[1];

// Función para establecer el último contador
const setUltimoContador = (value) => {
  contador = value;
};

// Escucha del evento de cambio en el input de archivo
file_input.addEventListener("change", async (event) => {
  const archivo = event.target.files[0];
  if (!archivo) return;
  const formData = new FormData();
  formData.append("file", archivo);

  const respuesta = await sendDocumentToApi(event, csrf_token);

  // Conversión de la respuesta a JSON
  const datos = await respuesta.json();

  // Asignación de los valores a los inputs del formulario
  titulo_input.value = datos.titulo || "";
  numero_paginas_input.value = datos.paginas;
  resumen_input.value = datos.resumen || "";
  palabras_clave_input.value = datos["palabras clave"].join(", ");

  // Limpiar el contenedor de autores al cargar el script
  contenedor_autores.innerHTML = "";
  datos.autor.forEach((i_autor) => {
    contador++;
    cleanAutors(i_autor, contenedor_autores, contador);
    setUltimoContador(contador);
  });
});

const addAutorBtn = document.getElementById("add-autor-btn");
// const autoresContainer = document.getElementById("autores-container");  

// Escucha del botón para añadir nuevos autores
addAutorBtn.addEventListener("click", () => {
  contador++;
  addNewAutorRow(contenedor_autores, contador)
});

// Delegación de eventos para los botones de eliminar
contenedor_autores.addEventListener("click", (event) => {
  deleteAutorRow(event);
});

// HACK: Código menos recargado y más modulable 😎