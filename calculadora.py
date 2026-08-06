def calcular_huella_co2(transporte, energia, residuos):
    """
    Calcula las emisiones estimadas de CO2 anuales basadas en factores colombianos.
    """
    co2_transporte = transporte * 52 * 0.12  # kg CO2 al año
    co2_energia = energia * 12 * 0.16        # kg CO2 al año
    co2_residuos = residuos * 52 * 0.50      # kg CO2 al año
    
    huella_total_kg = co2_transporte + co2_energia + co2_residuos
    huella_toneladas = huella_total_kg / 1000
    
    return huella_toneladas, huella_total_kg

def calcular_consumo_agua(metros_cubicos_mes):
    """
    Calcula el consumo anual de agua en litros y metros cúbicos.
    """
    agua_anual_m3 = metros_cubicos_mes * 12
    agua_anual_litros = agua_anual_m3 * 1000
    return agua_anual_m3, agua_anual_litros

def calcular_arboles_compensacion(huella_total_kg, agua_anual_m3, tipo_arbol):
    """
    Estima los árboles necesarios cruzando la huella de carbono y el consumo de agua.
    """
    tasas_absorcion = {
        "Frailejón (Alta Montaña)": 12,        
        "Palma de Cera (Bosque Andino)": 22,   
        "Arboloco (Restauración Rápida)": 35   
    }
    
    capacidad_absorcion = tasas_absorcion.get(tipo_arbol, 20)
    arboles_base = huella_total_kg / capacidad_absorcion
    
    # Si consumes más de 15 m3 al mes por hogar, sumamos árboles para protección de cuencas
    arboles_extra = round(agua_anual_m3 / 100) if agua_anual_m3 > 180 else 0
    
    return max(1, round(arboles_base) + arboles_extra)





