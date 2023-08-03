document.getElementById('urlForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var url = document.getElementById('urlInput').value;

    fetch('/scrape', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            'url': url
        })
    }).then(response => response.json())
      .then(data => {
        if(data.success) {
            document.getElementById('results').textContent = data.result;
        } else {
            alert("Error! Check server logs for details.");
        }
    });
});
