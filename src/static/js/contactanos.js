
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('form').addEventListener('submit', function(event) {
        var nombre = document.getElementById('nombre').value;
        var apellido = document.getElementById('apellido').value;
        var email = document.getElementById('email').value;
        var telefono = document.getElementById('telefono').value;
        var asunto = document.getElementById('asunto').value;
        var comentario = document.getElementById('comentario').value;

        if (nombre.trim() === '' || apellido.trim() === '' || email.trim() === '' || telefono.trim() === '' || asunto.trim() === '' || comentario.trim() === '') {
            document.getElementById('avisoForm').innerHTML = 'Todos los campos son obligatorios <br>';
            event.preventDefault();
        }
    });
});



