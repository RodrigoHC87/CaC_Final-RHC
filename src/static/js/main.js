
//- Marcador de posición del usuario en la página
document.addEventListener('DOMContentLoaded', function() {
    const currentLocation = window.location.pathname;
    console.log("Ruta actual:", currentLocation);  // Debugging: muestra la ruta actual

    const links = document.querySelectorAll('.nav-link');

    links.forEach(link => {
        const linkPath = new URL(link.href).pathname;  // Obtener la ruta completa del enlace
        console.log("Comparando con:", linkPath);  // Debugging: muestra cada href de los enlaces
        if (linkPath === currentLocation) {
            link.classList.add('active');
        }
    });
});