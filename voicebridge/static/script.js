async function convertTTS() {
    let text = document.getElementById("textInput").value;

    let response = await fetch('/tts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
    });

    let blob = await response.blob();
    let audioUrl = URL.createObjectURL(blob);

    let player = document.getElementById("audioPlayer");
    player.src = audioUrl;
    player.play();
}

async function convertSTT() {
    let fileInput = document.getElementById("audioFile");
    let formData = new FormData();
    formData.append("audio", fileInput.files[0]);

    let response = await fetch('/stt', {
        method: 'POST',
        body: formData
    });

    let data = await response.json();
    document.getElementById("outputText").innerText = data.text;
}