// Function to load images dynamically from images.json
async function loadImages() {
    const container = document.querySelector('.chart-container');
    container.innerHTML = ""; // Clear existing images

    try {
        const response = await fetch('img/images.json');
        const imagePaths = await response.json();

        imagePaths.forEach(path => {
            const chartDiv = document.createElement('div');
            chartDiv.className = 'chart';

            const img = document.createElement('img');
            img.src = path;
            img.alt = path.split('/').pop().split('.')[0]; // Use file name as alt text

            chartDiv.appendChild(img);
            container.appendChild(chartDiv);
        });
    } catch (error) {
        console.error("Error loading images:", error);
    }
}

// Function to refresh images every 30 seconds to check for updates
function refreshImages() {
    loadImages(); // Load images initially
    setInterval(loadImages, 30000); // Refresh images every 30 seconds
}

// Initialize the image loading process
document.addEventListener("DOMContentLoaded", refreshImages);
