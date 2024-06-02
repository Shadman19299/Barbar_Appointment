const cacheName = 'y-simple-page-v1';
const urlsToCache = [
    '/',
    '/index.html',
    '/style.css', // Replace with your CSS file
    '/script.js', // Replace with your JavaScript file
];


self.addEventListener('install', function(event) {
    event.waitUntil(
        caches.open(cacheName)
           .then(function(cache) {
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', function(event) {
    event.respondWith(
        caches.match(event.request)
           .then(function(response) {
                if (response) {
                    return response;
                }
                return fetch(event.request);
            })
    );
});