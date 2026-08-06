import io
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generar_pdf_certificado(nombre_usuario, toneladas_co2, agua_m3, arboles_necesarios, tipo_arbol):
    """
    Genera un certificado de mitigación ambiental en PDF incluyendo métricas de agua y carbono.
    """
    buffer = io.BytesIO()
    
    doc = SimpleDocTemplate(
        buffer, 
        pagesize=letter,
        rightMargin=50, leftMargin=50, topMargin=50, bottomMargin=50
    )
    
    story = []
    styles = getSampleStyleSheet()
    
    estilo_titulo = ParagraphStyle('TituloCertificado', parent=styles['Heading1'], fontSize=24, leading=28, textColor=colors.HexColor("#1A4620"), alignment=1, spaceAfter=20)
    estilo_subtitulo = ParagraphStyle('SubtituloCertificado', parent=styles['Normal'], fontSize=11, leading=15, textColor=colors.HexColor("#555555"), alignment=1, spaceAfter=30)
    estilo_cuerpo = ParagraphStyle('CuerpoCertificado', parent=styles['Normal'], fontSize=11, leading=18, alignment=4, spaceAfter=15)
    
    story.append(Paragraph("🌿 EcoAventuraColombia", estilo_titulo))
    story.append(Paragraph("CERTIFICADO DE COMPROMISO AMBIENTAL Y MITIGACIÓN DE HUELLA HÍDRICA Y CARBONO", estilo_subtitulo))
    story.append(Spacer(1, 15))
    
    texto_introduccion = f"""
    Por medio del presente documento técnico, la plataforma de ciencia ciudadana <b>EcoAventuraColombia</b> 
    hace un reconocimiento especial a <b>{nombre_usuario}</b>, por haber completado el diagnóstico integral 
    de emisiones y consumo de recursos naturales correspondiente al ciclo de monitoreo actual.
    """
    story.append(Paragraph(texto_introduccion, estilo_cuerpo))
    
    # Cuadro resumido con los 5 datos técnicos perfectamente distribuidos en anchos fijos
    datos_tabla = [
        [Paragraph("<b>Indicador Ambiental</b>", styles['Normal']), Paragraph("<b>Métrica Diagnosticada</b>", styles['Normal'])],
        ["Emisiones de CO₂ Estimadas:", f"{toneladas_co2:.2f} Toneladas de CO₂ / año"],
        ["Consumo de Agua Estimado:", f"{agua_m3:.2f} M³ de Agua / año"],
        ["Meta de Compensación Ecológica:", f"{arboles_necesarios} Ejemplares Forestales"],
        ["Especie Forestal Seleccionada:", f"{tipo_arbol}"]
    ]
    
    tabla_resumen = Table(datos_tabla, colWidths=[250, 250])
    tabla_resumen.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (1, 0), colors.HexColor("#1A4620")),
        ('TEXTCOLOR', (0, 0), (1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#F4F6F4")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#D0D5D0")),
    ]))
    
    story.append(Spacer(1, 10))
    story.append(tabla_resumen)
    story.append(Spacer(1, 20))
    
    texto_compromiso = f"""
    La siembra programada de estos <b>{arboles_necesarios} ejemplares</b> representa una acción de alto impacto 
    para la restauración ecológica de las cuencas hidrográficas y zonas de recarga del territorio nacional, 
    ayudando a proteger los hábitats de la fauna silvestre y asegurar la resiliencia climática regional.
    """
    story.append(Paragraph(texto_compromiso, estilo_cuerpo))
    story.append(Spacer(1, 40))
    
    story.append(Paragraph("________________________________________", ParagraphStyle('Linea', parent=styles['Normal'], alignment=1)))
    story.append(Paragraph("<b>Unidad de Gestión del Cambio Climático</b><br/>Sistema Integrado EcoAventuraColombia", ParagraphStyle('Firma', parent=styles['Normal'], alignment=1, fontSize=10)))
    
    doc.build(story)
    buffer.seek(0)
    return buffer





