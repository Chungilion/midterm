// Wait until the window has fully loaded before showing the content
window.addEventListener('load', () => {
    document.body.classList.remove('loading');
    document.body.classList.add('loaded');

    // Dynamically set the background image for the animated character
    const character = document.querySelector('.animated-character');
    character.style.backgroundImage = "url('character/lingsha.png')"; // Updated path
});

// Function to dynamically load chart images from images.json
async function loadChartImages() {
    const container = document.querySelector('.chart-container');
    container.innerHTML = ""; // Clear existing images

    try {
        const response = await fetch('img/images.json'); // Main chart images JSON
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
        console.error("Error loading chart images:", error);
    }
}

// Load chart images when DOM content is fully loaded
document.addEventListener("DOMContentLoaded", loadChartImages);

// Parallax effect for background layers and character
function handleParallax() {
    const scrollPosition = window.scrollY;

    // Parallax effect for background layers
    document.querySelector('.layer-1').style.transform = `translateY(${scrollPosition * 0.2}px)`;
    document.querySelector('.layer-2').style.transform = `translateY(${scrollPosition * 0.4}px)`;
    document.querySelector('.particles').style.transform = `translateY(${scrollPosition * 0.1}px)`;

    // Parallax effect for the animated character
    const character = document.querySelector('.animated-character');
    character.style.transform = `translateY(${scrollPosition * 0.1}px)`;
}

// Attach scroll event listener to apply the parallax effect
window.addEventListener('scroll', handleParallax);
