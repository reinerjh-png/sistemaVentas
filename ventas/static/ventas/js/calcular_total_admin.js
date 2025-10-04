document.addEventListener("DOMContentLoaded", function () {
    function actualizarTotales() {
        let total = 0;

        // Recorremos todas las filas del inline
        document.querySelectorAll("tr.form-row").forEach(function (row) {
            const productoSelect = row.querySelector("select[id$='producto']");
            const cantidadInput = row.querySelector("input[id$='cantidad']");
            const subtotalInput = row.querySelector("input[id$='subtotal']");

            if (productoSelect && cantidadInput && subtotalInput) {
                const selectedOption = productoSelect.options[productoSelect.selectedIndex];
                if (!selectedOption) return;

                // Tomamos el texto del producto, buscamos el precio en él si lo contiene
                const text = selectedOption.text;
                // Supone que el producto se llama "iPhone 13 ($2000)"
                const precioMatch = text.match(/\$(\d+(\.\d+)?)/);
                const precio = precioMatch ? parseFloat(precioMatch[1]) : 0;

                const cantidad = parseFloat(cantidadInput.value) || 0;
                const subtotal = precio * cantidad;

                subtotalInput.value = subtotal.toFixed(2);
                total += subtotal;
            }
        });

        const totalField = document.querySelector("#id_total");
        if (totalField) totalField.value = total.toFixed(2);
    }

    document.body.addEventListener("change", actualizarTotales);
    document.body.addEventListener("keyup", actualizarTotales);
});
