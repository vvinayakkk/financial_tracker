
document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:5000/generate_plots')
        .then(response => response.blob())
        .then(data => {
            const url = URL.createObjectURL(data);
            const img = document.createElement('img');
            img.src = url;
            document.getElementById('plot').appendChild(img);
        });
});
