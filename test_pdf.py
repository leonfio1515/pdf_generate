from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from styles import *


def create_pdf(datos_enc1, datos_enc2, datos_enc3, datos_enc4, datos_articulo, datos_total, amount_total, filename):
    c = canvas.Canvas(filename, pagesize=letter)

    data_encabezado = [['RUT','','Nombre']]
    data_encabezado2 = [['Moneda','','Serie','','Numero']]
    data_encabezado3 = [['Tipo','','F.Pago']]
    data_encabezado4 = [['Fecha','','Vto']]
    data_articulos = [['#','','Iva','', 'Articulo', '', 'Cant.', '', 'Sub. s/iva', '', 'Desc.', '', 'Total s/iva', '', 'Iva Imp']]
    data_tot_name = [['Sub Total No Gravado'],['Sub Total Gravado a IVA 22%'], ['Monto IVA 22%'], ['Sub Total Gravado a IVA 10%'], ['Monto IVA 10%'],  ['TOTAL'], ['Monto No Facturable']]
    data_tot_amount = []
    data_total_name = [['TOTAL A PAGAR']]
    data_total = []

    for rut, null1, nombre in datos_enc1:
        data_encabezado.append([rut, null1, nombre])

    for moneda, null1, serie,null2, numero in datos_enc2:
        data_encabezado2.append([moneda, null1, serie, null2, numero])

    for tipo, null1, f_pago in datos_enc3:
        data_encabezado3.append([tipo, null1, f_pago])

    for fecha, null1, vto in datos_enc4:
        data_encabezado4.append([fecha, null1, vto])

    for num, null1, iva_type, null2, art, null3, cant, null4, sub, null5, desc, null6, total, null7, iva_imp in datos_articulo:
        data_articulos.append([num, null1, iva_type, null2, art, null3, cant, null4, sub, null5, desc, null6, total, null7, iva_imp])

    for monto in datos_total:
        data_tot_amount.append([monto])

    for monto in amount_total:
        data_total.append([monto])


    table_encabezado = Table(data_encabezado, colWidths=[195, 5, 200])
    table_encabezado2 = Table(data_encabezado2, colWidths=[95, 5, 95, 5, 200])
    table_encabezado3 = Table(data_encabezado3, colWidths=[195, 5, 200])
    table_encabezado4 = Table(data_encabezado4, colWidths=[195, 5, 200])
    table_articulo = Table(data_articulos, colWidths=[15, 5, 25, 5, 210, 5, 25, 5, 60, 5, 60, 5, 60, 5, 60])
    table_tot_name = Table(data_tot_name, colWidths=[130])
    table_tot_amount = Table(data_tot_amount, colWidths=[60])
    table_total_name = Table(data_total_name, colWidths=[130])
    table_total = Table(data_total, colWidths=[60])

    # y_pos_art = 600 - table_articulo._height

    table_encabezado.setStyle(style_encabezado)
    table_encabezado.wrapOn(c, 0, 0)
    table_encabezado.drawOn(c, 30, 730)

    table_encabezado2.setStyle(style_encabezado2)
    table_encabezado2.wrapOn(c, 0, 0)
    table_encabezado2.drawOn(c, 30, 690)

    table_encabezado3.setStyle(style_encabezado)
    table_encabezado3.wrapOn(c, 0, 0)
    table_encabezado3.drawOn(c, 30, 650)

    table_encabezado4.setStyle(style_encabezado)
    table_encabezado4.wrapOn(c, 0, 0)
    table_encabezado4.drawOn(c, 30, 610)

    table_articulo.setStyle(style_articulo)
    table_articulo.wrapOn(c, 0, 0)
    table_articulo.drawOn(c, 30, 580 - table_articulo._height)

    table_tot_name.setStyle(style_total)
    table_tot_name.wrapOn(c, 0, 0)
    table_tot_name.drawOn(c, 385, 580 - table_articulo._height - table_tot_name._height -10 )

    table_tot_amount.setStyle(style_total)
    table_tot_amount.wrapOn(c, 0, 0)
    table_tot_amount.drawOn(c, 380 + table_tot_name._width + 10, 580 - table_articulo._height - table_tot_name._height -10 )

    table_total_name.setStyle(style_total)
    table_total_name.wrapOn(c, 0, 0)
    table_total_name.drawOn(c, 385, 580 - table_articulo._height - table_tot_name._height - 50 )

    table_total.setStyle(style_total)
    table_total.wrapOn(c, 0, 0)
    table_total.drawOn(c, 380 + table_tot_name._width + 10, 580 - table_articulo._height - table_tot_name._height - 50 )

    c.save()

# Datos de ejemplo
datos_enc1 = {
    (210703920014,'','Cybe SA')
}

datos_enc2 = {
    ('UYU','','A','', 12345)
}

datos_enc3 = {
    ('Factura','','Contado')
}

datos_enc4 = {
    ('2023-02-16','','2023-03-16')
}

datos_articulo = {
    ('1', '', '22', '', 'Arancel', '', '1', '', '1234455.00', '', '1234455.00', '', '1234455.00', '', '1234455.00' ),
    ('2', '', '22', '', 'Arancel', '', '1', '', '1000', '', '0', '', '1000', '', '220' ),
    ('3', '', '22', '', 'Arancel', '', '1', '', '1000', '', '0', '', '1000', '', '220' ),
    ('4', '', '22', '', 'Arancel', '', '1', '', '1000', '', '0', '', '1000', '', '220' ),
    ('5', '', '22', '', 'Arancel', '', '1', '', '1000', '', '0', '', '1000', '', '220' ),
}

datos_total = (
    '12345',
    '2332',
    '123425345',
    '3543',
    '33333',
    '12345',
    '43453',
)

amount_total = (
    '12345566',
)

# Nombre del archivo PDF de salida
nombre_archivo = "datos.pdf"

# Crea el PDF con el tamaño predeterminado y la tabla de dos columnas
create_pdf(datos_enc1, datos_enc2, datos_enc3, datos_enc4, datos_articulo,datos_total, amount_total, nombre_archivo)

print(f"El archivo PDF '{nombre_archivo}' ha sido creado exitosamente.")
