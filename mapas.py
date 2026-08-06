import folium
import base64
import os

def convertir_imagen_local(ruta):
    if os.path.exists(ruta):
        with open(ruta, "rb") as f:
            return f"data:image/jpg;base64,{base64.b64encode(f.read()).decode()}"
    return "https://unsplash.com"

def crear_mapa_biodiversidad():
    mapa = folium.Map(location=[4.5708, -74.2973], zoom_start=6, control_scale=True)
    
    # Base de datos ampliada a 6 animales estratégicos de Colombia
    fauna_colombia = [
        {"especie": "Cóndor de los Andes", "cientifico": "Vultur gryphus", "coords": [4.8833, -75.3667], "imagen_data": convertir_imagen_local("data/condor.jpg"), "color": "blue", "descripcion": "El ave voladora más grande del mundo. Habita las altas cumbres andinas y los páramos, cumpliendo una función clave como consumidor carroñero."},
        {"especie": "Jaguar", "cientifico": "Panthera onca", "coords": [-1.4429, -71.2185], "imagen_data": convertir_imagen_local("data/jaguar.jpg"), "color": "orange", "descripcion": "El felino más grande de América. Es un depredador tope regulador de ecosistemas, fundamental para el equilibrio biológico de las selvas amazónicas."},
        {"especie": "Rana Dardo Dorada", "cientifico": "Phyllobates terribilis", "coords": [4.8000, -77.3000], "imagen_data": convertir_imagen_local("data/rana.jpg"), "color": "green", "descripcion": "Endémica del Pacífico colombiano. Considerada el animal más venenoso del planeta; su piel segrega batracotoxina, una neurotoxina letal."},
        {"especie": "Oso de Anteojos", "cientifico": "Tremarctos ornatus", "coords": [5.5000, -73.6000], "imagen_data": convertir_imagen_local("data/oso.jpg"), "color": "darkgreen", "descripcion": "Único oso nativo de Sudamérica. Habita bosques de niebla y páramos andinos; es un gran dispersor de semillas y protector de las fuentes hídricas."},
        {"especie": "Delfín Rosado de Río", "cientifico": "Inia geoffrensis", "coords": [-4.2111, -69.9406], "imagen_data": convertir_imagen_local("data/delfin.jpg"), "color": "purple", "descripcion": "Cetáceo de agua dulce icónico de las cuencas de los ríos Amazonas y Orinoco. Se encuentra amenazado por la minería ilegal y la contaminación de las aguas."},
        {"especie": "Guacamaya Bandera", "cientifico": "Ara macao", "coords": [4.1500, -72.5333], "imagen_data": convertir_imagen_local("data/guacamaya.jpg"), "color": "red", "descripcion": "Ave de plumaje colorido que habita en bosques húmedos tropicales y llanuras orientales. Cumple un rol vital reforestando los bosques al dispersar semillas de frutos."}
    ]
    
    for animal in fauna_colombia:
        html_popup = f"""
        <div style="font-family: Arial, sans-serif; width: 210px; color: #333333;">
            <h4 style="margin: 0 0 5px 0; color: #1E4620;">{animal['especie']}</h4>
            <i style="color: #666666; font-size: 11px;">{animal['cientifico']}</i><br><br>
            <img src="{animal['imagen_data']}" alt="{animal['especie']}" style="width: 100%; border-radius: 5px; display: block;"><br>
            <p style="font-size: 11px; line-height: 1.4; text-align: justify; margin: 0;">{animal['descripcion']}</p>
        </div>
        """
        folium.Marker(
            location=animal["coords"],
            popup=folium.Popup(html_popup, max_width=230),
            tooltip=animal["especie"],
            icon=folium.Icon(color=animal["color"], icon="leaf")
        ).add_to(mapa)
        
    return mapa





