import streamlit as st 

def mostrar_catalogo_fauna():
    st.header("🐾 Catálogo Oficial de la Fauna Silvestre de Colombia")
    st.write("Explora la riqueza biológica de nuestro país organizada por clases taxonómicas.")

    # Base de datos estructurada con tu lista exacta de especies
    especies_fauna = {
        "🐆 Mamíferos": [
            "Jaguar (Panthera onca)", "Puma (Puma concolor)", "Oso andino (Tremarctos orfatus)",
            "Danta de montaña (Tapirus pinchaque)", "Venado cola blanca (Odocoileus virginianus)",
            "Armadillo gigante (Priodonte maximus)", "Nutria gigante (Pteronura brasiliensis)",
            "Mono araña (Ateles hybridus)", "Mono nocturno (Aotus lemurinus)", "Mono aullador rojo (Alouatta seniculus)",
            "Trigrillo (Leopardus tigrinus)", "Guatín (Dasyprocta fuliginosa)", "Zorro cangrejero (Cerdocyon thous)",
            "Oso Hormiguero (Myrmecophaga tridactyla)"
        ],

        "🦅 Aves": [
            "Cóndor andino (Vultur gryphus)", "Águila Harpía (Harpia harpyja)", "Guacamaya Roja (Ara macao)",
            "Guacamaya azul y amarillo (Ara ararauna)", "Tucán del Chocó (Ramphastos brevis)",
            "Barranquero andino (Momontus aequeatorialis)", "Gallito de las rocas (Rupicola peruvianus)",
            "Colibrí picoespada (Ensifera ensifera)", "Flamenco americano (Phoenicopterus ruber)",
            "Paujil pico azul (Crax alberti)"
        ],
        "🐊 Reptiles": [
            "Anaconda verde (Eunectes murinus)", "Boa constrictora (Boa constrictor)", "Caimán del Orinoco (Crocodylus intermediate)",
            "Babilla (Caima crocodilus)", "Iguana Verde (Iguana iguana)", "Tortuga charapa (Podocnemis expansa)",
            "Tortuga carey (Eretmochelys imbricata)"
        ],
        "🐸 Anfibios": [
            "Rana dorada venenosa(Phyllobates terribilis)", "Rana alerquín (Atelopus)", "Rana arborícola (Hypsiboas)",
            "Salamandra andina (Bolitoglossa)"
        ],
        "🐟 Peces": [
            "Pirarucú (Arapaima gigas)", "Bagre rayado (Pseudoplatystoma magdaleniatum)", "Dorado (Salminus brasilensis)",
            "Pez león (Pterois volitans) - Especie Invasora"
        ],
        "🦋 Invetebrados": [
            "Mariposa morfo azul (Morpho peleides)", "Mariposa alas de cristal (Greta oto)", "Escarabajo Hércules (Dynastes hercules)",
            "Hormiga arriera (Atta laeviagata)", "Tarántula Goliat (Theraphosa blondi)", "Araña bananera (Phoneutria)"
        ]
    }

    # Buscador unificado en tiempo real
    busqueda = st.text_input("🔍 Buscar especie en el catálogo nacional:", "").lower()

    if busqueda:
        st.subheader("🎯 Resultados de la Búsqueda")
        encontrados = False
        for categoria, animales in especies_fauna.items():
            filtrados = [a for a in animales if busqueda in a.lower()]
            if filtrados:
                encontrados = True
                with st.expander(f"{categoria} ({len(filtrados)})", expanded=True):
                    for animal in filtrados:
                        st.markdown(f"• **{animal}**")
            if not encontrados:
                st.warning("⚠️ No se encontraron especies que coincidan con tu busqueda.")
    else:
        # Pestañas interactivas de Streamlit para una navegacion limpia
        pestañas = st.tabs(list(especies_fauna.keys()))

        for idx, (categoria, animales) in enumerate(especies_fauna.items()):
            with pestañas[idx]:
                st.subheader(f"Lista de {categoria}")
                # Distribución estética en 2 columnas para optimizar el espacio vertical
                col1, col2 = st.columns(2)
                mitad = len(animales) // 2 + len(animales) % 2

                with col1:
                    for animal in animales[:mitad]:
                        st.markdown(f"🔹 {animal}")
                with col2:
                    for animal in animales[mitad:]:
                        st.markdown("f 🔹 {animal}")