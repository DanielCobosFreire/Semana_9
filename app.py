# app.py
# CSi - CoFre Sistemas Informáticos
# Semana 9: configuración del proyecto con Flask y manejo de rutas.
# En esta etapa los módulos usan datos de ejemplo (estáticos), ya que
# aún no se requiere conexión a una base de datos.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Página principal informativa (Quiénes somos, Servicios, Solicitudes, Contacto)."""
    return render_template('index.html')


@app.route('/productos')
def productos():
    """Módulo de Productos. Datos de ejemplo mientras no hay base de datos."""
    productos_data = [
        {'nombre': 'Laptop HP 15"', 'categoria': 'Equipos', 'precio': 650.00, 'stock': 12},
        {'nombre': 'Monitor LG 24"', 'categoria': 'Equipos', 'precio': 180.00, 'stock': 20},
        {'nombre': 'Licencia Windows 11 Pro', 'categoria': 'Software', 'precio': 199.00, 'stock': 50},
        {'nombre': 'Servicio de Mantenimiento IT', 'categoria': 'Servicios', 'precio': 45.00, 'stock': None},
    ]
    return render_template('productos.html', productos=productos_data)


@app.route('/clientes')
def clientes():
    """Módulo de Clientes. Datos de ejemplo mientras no hay base de datos."""
    clientes_data = [
        {'nombre': 'Juan Pérez', 'empresa': 'Ferretería El Tornillo',
         'correo': 'juan.perez@ejemplo.com', 'telefono': '098-123-4567'},
        {'nombre': 'María Torres', 'empresa': 'Panadería Dulce Trigo',
         'correo': 'maria.torres@ejemplo.com', 'telefono': '099-234-5678'},
        {'nombre': 'Carlos Mendoza', 'empresa': 'Colegio San Andrés',
         'correo': 'carlos.mendoza@ejemplo.com', 'telefono': '098-345-6789'},
    ]
    return render_template('clientes.html', clientes=clientes_data)


@app.route('/proveedores')
def proveedores():
    """Módulo de Proveedores. Datos de ejemplo mientras no hay base de datos."""
    proveedores_data = [
        {'nombre': 'TecnoSuministros S.A.', 'producto': 'Equipos de cómputo',
         'contacto': 'ventas@tecnosuministros.com'},
        {'nombre': 'DistriSoft Ecuador', 'producto': 'Licencias de software',
         'contacto': 'contacto@distrisoft.ec'},
        {'nombre': 'RedNet Cía. Ltda.', 'producto': 'Infraestructura de red',
         'contacto': 'info@rednet.ec'},
    ]
    return render_template('proveedores.html', proveedores=proveedores_data)


@app.route('/facturacion')
def facturacion():
    """Módulo de Facturación. Datos de ejemplo mientras no hay base de datos."""
    facturas_data = [
        {'numero': 'F-001', 'cliente': 'Juan Pérez', 'fecha': '2026-08-01',
         'total': 850.00, 'estado': 'Pagada'},
        {'numero': 'F-002', 'cliente': 'María Torres', 'fecha': '2026-08-05',
         'total': 199.00, 'estado': 'Pendiente'},
        {'numero': 'F-003', 'cliente': 'Carlos Mendoza', 'fecha': '2026-08-10',
         'total': 45.00, 'estado': 'Pagada'},
    ]
    return render_template('facturacion.html', facturas=facturas_data)


if __name__ == '__main__':
    app.run(debug=True)
