document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const chartContainer = document.querySelector('.chart-container');

    if (form) {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            let valid = true;
            form.querySelectorAll('input').forEach(input => {
                if (input.type === 'number' && input.value < 0) {
                    valid = false;
                    alert('Please enter a valid positive number for ' + input.name);
                }
            });

            if (!valid) return;

            const formData = new FormData(form);

            fetch(form.action, {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert(data.message);
                    // Reload charts after successful data update
                    refreshCharts();
                } else {
                    alert("Error: " + data.message);
                }
            })
            .catch(error => {
                alert("Network error. Please try again.");
                console.error('Error:', error);
            });
        });
    }

    function refreshCharts() {
        const chartFiles = [
            'line_plot.png',
            'scatter_plot.png',
            'histogram.png',
            'density_contour.png',
            'geograph.png',
            'text_anno.png',
            'three_dim.png',
            'visual_error.png'
        ];

        chartFiles.forEach(file => {
            const img = document.querySelector(`img[src$="${file}"]`);
            if (img) {
                img.src = `static/graph_gen/charts/${file}?timestamp=${new Date().getTime()}`;  // Update src to avoid caching
            }
        });
    }
});
