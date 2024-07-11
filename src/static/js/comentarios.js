
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
                    text: 'Tu comentario ha sido publicado',
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


//- Alerta de confirmación al borrar comentarios

const btnDelete = document.querySelectorAll('.btn-delete');

if (btnDelete) {
    const btnArray = Array.from(btnDelete);
    btnArray.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault(); // Prevenir la acción predeterminada para manejarla nosotros

            // Mostrar la alerta de confirmación usando SweetAlert2
            Swal.fire({
                title: '¿Estás seguro?',
                text: 'No podrás revertir esto!',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Sí, eliminarlo!',
                cancelButtonText: 'No, cancelar!',
                reverseButtons: true
            }).then((result) => {
                if (result.isConfirmed) {
                    // Si el usuario confirma, redirigir a la URL del botón de eliminar
                    window.location.href = btn.href;
                } else if (result.dismiss === Swal.DismissReason.cancel) {
                    // Si el usuario cancela, mostrar un mensaje opcional
                    Swal.fire(
                        'Cancelado',
                        'Tu contacto está a salvo :)',
                        'error'
                    );
                }
            });
        });
    });
}
