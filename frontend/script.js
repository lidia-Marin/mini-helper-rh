async function enviarPregunta() {
    const pregunta = document.getElementById("pregunta").value;

    const response = await fetch("http://127.0.0.1:8000/preguntar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ pregunta })
    });

    const data = await response.json();
    document.getElementById("respuesta").innerText = data.respuesta;
}
