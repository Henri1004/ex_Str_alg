from functools import partial

class SimpleOperations:
    def apply_discount(price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        return round(price - price*discount,2)

    def calculate_tax(price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        return round(price + price*tax_rate,2)


# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
twenty_percent_discount = partial(SimpleOperations.apply_discount, discount =0.2)
vat_tax = partial(SimpleOperations.calculate_tax, tax_rate =0.4)

# Usar las funciones preconfiguradas.
print(twenty_percent_discount(100))
print(vat_tax(100))
