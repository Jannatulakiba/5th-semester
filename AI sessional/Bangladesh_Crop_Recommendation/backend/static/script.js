function updateValue(id) {
    document.getElementById(id + "-val").innerText =
        document.getElementById(id).value;
}

function predictCrop() {
    const data = {
        N: Number(document.getElementById("N").value),
        P: Number(document.getElementById("P").value),
        K: Number(document.getElementById("K").value),
        temperature: Number(document.getElementById("temperature").value),
        humidity: Number(document.getElementById("humidity").value),
        ph: Number(document.getElementById("ph").value),
        rainfall: Number(document.getElementById("rainfall").value),

        soil_type: document.getElementById("soil_type").value,
        season: document.getElementById("season").value,
        previous_crop: document.getElementById("previous_crop").value,

        altitude: Number(document.getElementById("altitude").value),
        sunlight: Number(document.getElementById("sunlight").value)
    };

    const chatLog = document.getElementById("chat-log");

    chatLog.innerHTML += `<div class="user"> Farm data submitted...</div>`;
    chatLog.scrollTop = chatLog.scrollHeight;

    fetch("/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(result => {
        chatLog.innerHTML += `
            <div class="bot">
                 Recommended Crop: <b>${result.recommended_crop}</b>
            </div>`;
        chatLog.scrollTop = chatLog.scrollHeight;
    })
    .catch(err => {
        chatLog.innerHTML += `<div class="bot"> Error predicting crop.</div>`;
        chatLog.scrollTop = chatLog.scrollHeight;
        console.error(err);
    });
}
