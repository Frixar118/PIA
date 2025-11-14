document.addEventListener("DOMContentLoaded", function() {
    const botones = document.querySelectorAll(".ver-detalle");

    botones.forEach(boton => {
        boton.addEventListener("click", function() {
            const descripcion = this.previousElementSibling;
            descripcion.style.display = descripcion.style.display === "none" ? "block" : "none";
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const botonesResaltar = document.querySelectorAll(".resaltar-boton");

    botonesResaltar.forEach(boton => {
        boton.addEventListener("click", function() {
            const contenedor = this.closest(".auto");
            if (contenedor.style.backgroundColor === "goldenrod") {
                contenedor.style.backgroundColor = "";
                this.textContent = "Resaltar";
            } else {
                contenedor.style.backgroundColor = "goldenrod";
                this.textContent = "Quitar resaltado";
            }
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const botonesEventos = document.querySelectorAll(".evento .ver-detalle");

    botonesEventos.forEach(boton => {
        boton.addEventListener("click", function() {
            const descripcion = this.previousElementSibling;
            descripcion.style.display = descripcion.style.display === "none" ? "block" : "none";
            this.textContent = this.textContent === "Ver más" ? "Ver menos" : "Ver más";
        });
    });
});


document.addEventListener("DOMContentLoaded", function() {
    const textarea = document.getElementById("textoComentario");
    const contador = document.getElementById("contador");

    if (textarea) {
        textarea.addEventListener("input", function() {
            contador.textContent = `${textarea.value.length} / 200 caracteres`;
        });
    }
});
