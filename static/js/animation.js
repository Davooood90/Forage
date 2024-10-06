// Function to fade in an element
function fadeIn(element, duration) {
    let opacity = 0;  // Initial opacity
    element.style.opacity = opacity;

    // Set an interval to slowly increase opacity
    let interval = 10;  // Interval in milliseconds
    let increment = interval / duration;  // How much to increase per step

    let fadeEffect = setInterval(() => {
        if (opacity >= 1) {
            clearInterval(fadeEffect);  // Stop when fully visible
        } else {
            opacity += increment;
            element.style.opacity = opacity;
        }
    }, interval);
}

// Get the logos by their IDs
let primaryLogo = document.getElementById('primaryLogo');
let smallerLogo = document.getElementById('smallerLogo');

// Call fadeIn function on logos
// Set duration to 5 seconds for slow fade-in
fadeIn(primaryLogo, 5000);  // Fade in over 5 seconds
fadeIn(smallerLogo, 8000);  // Fade in slower over 8 seconds


function openPopup() {
    // Open a new window
    const popup = window.open("", "popup", "width=400,height=300");

    // Content for the pop-up
    popup.document.write(`
        <html>
            <head>
                <title>Dietary Restrictions</title>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
            </head>
            <body>
                <div class="container">
                    <h5>Dietary Restrictions</h5>
                    <p>Please list any dietary restrictions here.</p>
                    <button onclick="window.close();" class="btn btn-secondary">Close</button>
                </div>
            </body>
        </html>
    `);
    popup.document.close(); // Close the document to finish loading
}

// Get the button by its ID
let openModalButton = document.getElementById('openModalButton');

// Add click event listener to the button
openModalButton.addEventListener('click', openPopup);