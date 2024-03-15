from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors


style_encabezado = TableStyle(
                    [
                    ('BACKGROUND', (0, 0), (0, 0), colors.grey),
                    ('BACKGROUND', (1, 0), (1, 0), colors.white),
                    ('BACKGROUND', (2, 0), (2, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 9),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
                    ('BACKGROUND', (0, 1), (0, -1), colors.lightgrey),
                    ('BACKGROUND', (1, 1), (1, -1), colors.white),
                    ('BACKGROUND', (2, 1), (2, -1), colors.lightgrey),
                    ])

style_encabezado2 = TableStyle(
                    [
                    ('BACKGROUND', (0, 0), (0, 0), colors.grey),
                    ('BACKGROUND', (1, 0), (1, 0), colors.white),
                    ('BACKGROUND', (2, 0), (2, 0), colors.grey),
                    ('BACKGROUND', (3, 0), (3, 0), colors.white),
                    ('BACKGROUND', (4, 0), (4, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 9),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
                    ('BACKGROUND', (0, 1), (0, -1), colors.lightgrey),
                    ('BACKGROUND', (1, 1), (1, -1), colors.white),
                    ('BACKGROUND', (2, 1), (2, -1), colors.lightgrey),
                    ('BACKGROUND', (3, 1), (3, -1), colors.white),
                    ('BACKGROUND', (4, 1), (4, -1), colors.lightgrey),
                    ])


style_articulo = TableStyle(
                    [
                    ('BACKGROUND', (0, 0), (0, 0), colors.grey),
                    ('BACKGROUND', (1, 0), (1, 0), colors.white),
                    ('BACKGROUND', (2, 0), (2, 0), colors.grey),
                    ('BACKGROUND', (3, 0), (3, 0), colors.white),
                    ('BACKGROUND', (4, 0), (4, 0), colors.grey),
                    ('BACKGROUND', (5, 0), (5, 0), colors.white),
                    ('BACKGROUND', (6, 0), (6, 0), colors.grey),
                    ('BACKGROUND', (7, 0), (7, 0), colors.white),
                    ('BACKGROUND', (8, 0), (8, 0), colors.grey),
                    ('BACKGROUND', (9, 0), (9, 0), colors.white),
                    ('BACKGROUND', (10, 0), (10, 0), colors.grey),
                    ('BACKGROUND', (11, 0), (11, 0), colors.white),
                    ('BACKGROUND', (12, 0), (12, 0), colors.grey),
                    ('BACKGROUND', (13, 0), (13, 0), colors.white),
                    ('BACKGROUND', (14, 0), (14, 0), colors.grey),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                    ('FONTSIZE', (0, 0), (-1, -1), 9),
                    ('WORDWRAP', (0, 0), (-1, -1)),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
                    ('BACKGROUND', (0, 1), (0, -1), colors.lightgrey),
                    ('BACKGROUND', (1, 1), (1, -1), colors.white),
                    ('BACKGROUND', (2, 1), (2, -1), colors.lightgrey),
                    ('BACKGROUND', (3, 1), (3, -1), colors.white),
                    ('BACKGROUND', (4, 1), (4, -1), colors.lightgrey),
                    ('BACKGROUND', (5, 1), (5, -1), colors.white),
                    ('BACKGROUND', (6, 1), (6, -1), colors.lightgrey),
                    ('BACKGROUND', (7, 1), (7, -1), colors.white),
                    ('BACKGROUND', (8, 1), (8, -1), colors.lightgrey),
                    ('BACKGROUND', (9, 1), (9, -1), colors.white),
                    ('BACKGROUND', (10, 1), (10, -1), colors.lightgrey),
                    ('BACKGROUND', (11, 1), (11, -1), colors.white),
                    ('BACKGROUND', (12, 1), (12, -1), colors.lightgrey),
                    ('BACKGROUND', (13, 1), (13, -1), colors.white),
                    ('BACKGROUND', (14, 1), (14, -1), colors.lightgrey),
                    ])

style_total = TableStyle(
                    [
                    ('BACKGROUND', (0, 0), (-1, -1), colors.lightgrey),
                    ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
                    ('FONTSIZE', (0, 0), (-1, -1), 9),
                    ('BOTTOMPADDING', (0, 0), (-1, 0), 2),
                    ])