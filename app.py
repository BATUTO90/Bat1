<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>BATUTO-fokuz</title>
<link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet" />
<style>
body {
  background-color: #000;
  color: #fff;
  font-family: 'Montserrat', sans-serif;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}
h2 {
  margin-bottom: 10px;
}
#prompt { width: 90%; padding: 10px; font-size: 1em; border-radius: 8px; border: none; }
button { padding: 10px 20px; margin-top: 10px; border: none; border-radius: 8px; background: #1E90FF; color: #fff; cursor: pointer; font-size: 1em; }
#imgResult {
  width: 180px; /* proporción 9/16 aprox */
  aspect-ratio: 9/16; /* usa si soporta el navegador */
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
#imgResult img {
  width: 100%;
  height: auto;
  border-radius: 8px;
}
</style>
</head>
<body>
<h2>Generador de Imágenes AI</h2>
<input type="text" id="prompt" placeholder="Escribe tu prompt" />
<button onclick="generarImagen()">Generar</button>
<div id="imgResult">Aquí aparecerá la imagen</div>

<script>
async function generarImagen() {
  const prompt = document.getElementById('prompt').value;
  if (!prompt) return alert('Escribe un prompt');
  document.getElementById('imgResult').innerHTML = 'Cargando...';

  const response = await fetch('/generate', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({prompt: prompt})
  });
  const data = await response.json();
  if (data.image) {
    document.getElementById('imgResult').innerHTML =
      `<img src="data:image/png;base64,${data.image}"/>`;
  } else {
    document.getElementById('imgResult').innerHTML = 'Error al generar.';
  }
}
</script>
</body>
</html>
