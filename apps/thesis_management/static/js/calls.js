export const sendDocumentToApi = async (event, csrf_token) => {
    const archivo = event.target.files[0];
    if (!archivo) return;
    const formData = new FormData();
    formData.append("file", archivo);
    try {
        // Función asíncrona para enviar el archivo
        const respuesta = await fetch(`/thesis_management/process_file/`, {
        method: "POST",
        body: formData,
        headers: {
        "X-CSRFToken": csrf_token,
        },
    });
    return respuesta;
    } catch(error) {
        alert("Ocurrió un error inesperado");
    }
}