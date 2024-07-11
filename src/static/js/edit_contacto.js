// ------------------------------------------------------------

document.addEventListener('DOMContentLoaded', function() {
    const formulario = document.querySelector('form');

    if (formulario) {
        formulario.addEventListener('submit', function(event) {
            event.preventDefault(); // Prevenir el envío del formulario inicialmente

            var nombre = document.getElementById('nombre').value;
            var correo = document.getElementById('correo').value;
            var asunto = document.getElementById('asunto').value;
            var comentario = document.getElementById('comentario').value;

            if (nombre.trim() === '' || correo.trim() === '' || asunto.trim() === '' || comentario.trim() === '') {
                Swal.fire({
                    title: 'Error',
                    text: 'Todos los campos son obligatorios',
                    icon: 'error',
                    confirmButtonText: 'OK'
                });
            } else {
                Swal.fire({
                    title: 'Success',
                    text: 'Tu comentario ha sido modificado',
                    icon: 'success',
                    confirmButtonText: 'OK'
                }).then((result) => {
                    if (result.isConfirmed) {
                        formulario.submit(); // Enviar el formulario solo después de que el usuario presione "OK"
                    }
                });
            }
        });
    }
});