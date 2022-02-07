// Search Bar Control
// open google search window
const search = document.getElementById('search');
const google = 'https://www.google.com/search?q=site%3A+';
const site = 'https://nighthawkcodingsociety.com';

function submitted(event) {
    if (event.key === 'Enter') {
        event.preventDefault();
        const url = google
            + site
            + '+'
            + search.value;
        const win = window.open(url, '_blank');
        win.focus();
    }
}
search.addEventListener('keypress', submitted);
