

// Definir una función genérica para mostrar/ocultar texto
function mostrarTexto(boton, textoOculto) {
    // Ocultar todos los textos y restablecer el texto de los botones
    textosOcultos.forEach(texto => {
        if (texto !== textoOculto) {
            texto.classList.remove("mostrar");
            texto.classList.add("ocultar");
        }
    });

    botones.forEach(b => {
        if (b !== boton) {
            b.innerHTML = "leer mas";
        }
    });

    // Mostrar u ocultar el texto del botón actual
    textoOculto.classList.toggle("mostrar");
    textoOculto.classList.toggle("ocultar");

    if (textoOculto.classList.contains("mostrar")) {
        boton.innerHTML = "Ocultar texto";
    } else {
        boton.innerHTML = "leer mas";
    }
}

// Obtener todos los botones y textos ocultos
let botones = document.querySelectorAll("[id^='mostrar_texto_btn']");
let textosOcultos = document.querySelectorAll("[id^='texto_oculto']");

// Agregar event listeners a los botones
botones.forEach((boton, index) => {
    let textoOculto = document.getElementById(`texto_oculto${index + 1}`);

    boton.addEventListener("click", () => mostrarTexto(boton, textoOculto));
});
