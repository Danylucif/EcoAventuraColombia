import streamlit as st
import random

def iniciar_trivia():
    st.subheader("🎮 Centro de Experiencias Didácticas")
    st.write("Aprende sobre la biodiversidad de Colombia jugando y sumando puntos.")
    
    # Inicializar variables de estado globales del jugador
    if 'puntaje' not in st.session_state:
        st.session_state.puntaje = 0

    # Menú interno para cambiar de juego
    tipo_juego = st.tabs(["🏆 Cuestionario Ecológico", "🦥 Ahorcado de la Fauna", "🌲 Conecta el Hábitat"])

    # ---------------------------------------------------------
    # PESTAÑA 1: CUESTIONARIO ECOLÓGICO (TRIVIA)
    # ---------------------------------------------------------
    with tipo_juego[0]:
        st.markdown("### ⛰️ Desafío de Preguntas y Respuestas")
        
        opcion_juego = st.selectbox(
            "Selecciona un reto técnico:", 
            ["Reto 1: Fábricas de Agua", "Reto 2: Especies Protegidas"],
            key="select_trivia"
        )

        if opcion_juego == "Reto 1: Fábricas de Agua":
            st.markdown("#### ¿Qué ecosistema es conocido como la 'fábrica de agua' en Colombia?")
            opciones1 = ["Bosque Seco Tropical", "Páramo", "Manglar", "Sabana"]
            respuesta1 = st.radio("Tu respuesta:", opciones1, key="p1")
            
            if st.button("Validar Reto 1", key="btn_p1"):
                if respuesta1 == "Páramo":
                    st.success("🎉 ¡Correcto! Los páramos retienen el agua de la niebla y surten al 70% del país.")
                    st.session_state.puntaje += 10
                else:
                    st.error("❌ Incorrecto. Pista: Es un ecosistema de alta montaña con frailejones.")

        elif opcion_juego == "Reto 2: Especies Protegidas":
            st.markdown("#### ¿Cuál de estos mamíferos habita en las zonas altas andinas y es clave para los bosques?")
            opciones2 = ["Oso de Anteojos", "Delfín Rosado", "Jaguar", "Chigüiro"]
            respuesta2 = st.radio("Tu respuesta:", opciones2, key="p2")
            
            if st.button("Validar Reto 2", key="btn_p2"):
                if respuesta2 == "Oso de Anteojos":
                    st.success("🎉 ¡Excelente! El Oso de Anteojos (Tremarctos ornatus) dispersa semillas en las cordilleras.")
                    st.session_state.puntaje += 10
                else:
                    st.error("❌ Incorrecto. Los demás animales habitan en llanos, ríos o selvas tropicales bajas.")

    # ---------------------------------------------------------
    # PESTAÑA 2: JUEGO DEL AHORCADO
    # ---------------------------------------------------------
    with tipo_juego[1]:
        st.markdown("### 🦥 Descubre el Animal Oculto")
        st.write("Adivina las letras del animal antes de que se agoten tus oportunidades.")

        # Banco de palabras ecológicas
        palabras_fauna = ["FRAILEJON", "JAGUAR", "CONDOR", "ANACONDA", "MANATI", "ARMADILLO"]
        
        # Inicializar variables internas del juego del ahorcado
        if 'palabra_secreta' not in st.session_state:
            st.session_state.palabra_secreta = random.choice(palabras_fauna)
            st.session_state.letras_adivinadas = set()
            st.session_state.intentos_restantes = 6

        palabra = st.session_state.palabra_secreta
        letras = st.session_state.letras_adivinadas

        # Mostrar la palabra oculta con guiones bajos
        progreso_palabra = [letra if letra in letras else " _ " for letra in palabra]
        st.markdown(f"## `{''.join(progreso_palabra)}`")
        st.write(f"❤️ Intentos restantes: **{st.session_state.intentos_restantes}**")

        # Control para ingresar una letra
        letra_ingresada = st.text_input("Escribe una letra (en MAYÚSCULA):", max_chars=1, key="input_letra").upper()

        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("Probar Letra", key="btn_probar"):
                if letra_ingresada:
                    if letra_ingresada in letras:
                        st.warning("⚠️ Ya habías intentado con esa letra.")
                    elif letra_ingresada in palabra:
                        letras.add(letra_ingresada)
                        st.success(f"🎯 ¡Bien hecho! La letra '{letra_ingresada}' sí está.")
                    else:
                        st.session_state.intentos_restantes -= 1
                        st.error(f"❌ La letra '{letra_ingresada}' no pertenece al animal.")
                    
                    # Verificar si ganó
                    if all(l in letras for l in palabra):
                        st.balloons()
                        st.success(f"🏆 ¡Ganaste! El animal era **{palabra}**. Sumas +20 puntos.")
                        st.session_state.puntaje += 20
                        # Reiniciar juego automático
                        del st.session_state.palabra_secreta

                    # Verificar si perdió
                    if st.session_state.intentos_restantes <= 0:
                        st.error(f"💀 Te quedaste sin intentos. El animal era **{palabra}**.")
                        del st.session_state.palabra_secreta
                        
        with col_btn2:
            if st.button("Cambiar / Reiniciar Palabra", key="btn_reset_ahorcado"):
                if 'palabra_secreta' in st.session_state:
                    del st.session_state.palabra_secreta
                st.rerun()

    # ---------------------------------------------------------
    # PESTAÑA 3: ASOCIACIÓN DE ECOSISTEMAS
    # ---------------------------------------------------------
    with tipo_juego[2]:
        st.markdown("### 🌲 Conecta el Hábitat Correcto")
        st.write("Asocia cada especie biológica con el ecosistema donde cumple su función vital.")

        col_izq, col_der = st.columns(2)
        with col_izq:
            especie = st.selectbox("Selecciona la Especie:", ["Rana Dardo Dorada", "Palma de Cera", "Delfín Rosado de Río"], key="sb_especie")
        with col_der:
            habitat = st.selectbox("Selecciona su Ecosistema:", ["Río Amazonas", "Selva del Pacífico", "Bosque Andino / Cocora"], key="sb_habitat")

        if st.button("Verificar Conexión", key="btn_conecta"):
            # Lógica de emparejamiento
            if especie == "Rana Dardo Dorada" and habitat == "Selva del Pacífico":
                st.success("🎯 ¡Perfecto! Es el animal más venenoso del mundo y vive en la selva húmeda del Pacífico.")
                st.session_state.puntaje += 15
            elif especie == "Palma de Cera" and habitat == "Bosque Andino / Cocora":
                st.success("🎯 ¡Excelente! Nuestro árbol nacional crece en los bosques de niebla de la cordillera Andina.")
                st.session_state.puntaje += 15
            elif especie == "Delfín Rosado de Río" and habitat == "Río Amazonas":
                st.success("🎯 ¡Correcto! Este cetáceo de agua dulce navega por las cuencas del Amazonas y Orinoco.")
                st.session_state.puntaje += 15
            else:
                st.error("❌ Combinación incorrecta. Esa especie no se adapta a las condiciones bióticas de ese entorno.")

    # Marcador global permanente en la barra lateral
    st.sidebar.markdown("---")
    st.sidebar.metric(label="🏆 Puntaje EcoAventura", value=f"{st.session_state.puntaje} PTS")
 
