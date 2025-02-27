function getMeaning() {
    let word = document.getElementById("wordInput").value;
    fetch(`http://127.0.0.1:5000/search?word=${word}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").innerText = 
                data.meaning ? `Meaning: ${data.meaning}` : "Word not found!";
        })
        .catch(error => console.error("Error fetching data:", error));
}
