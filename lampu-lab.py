import streamlit as st
import paho.mqtt.client as mqtt
import time

st.title("Kontrol Lampu 1")

# Inisialisasi MQTT client global
if "mqtt_client" not in st.session_state:
    client = mqtt.Client(client_id="STREAMLIT_LAMP1")
    client.connect("broker.mqtt-dashboard.com", 1883, 60)
    client.loop_start()
    st.session_state.mqtt_client = client
    st.session_state.mqtt_connected = True
else:
    client = st.session_state.mqtt_client

# Status lampu
if "lampu1" not in st.session_state:
    st.session_state.lampu1 = False

# Checkbox toggle
lampu1 = st.checkbox("Lampu 1", value=st.session_state.lampu1)

# Jika status berubah, kirim MQTT
if lampu1 != st.session_state.lampu1:
    st.session_state.lampu1 = lampu1
    # Tunggu sebentar supaya MQTT client benar-benar ready
    time.sleep(0.2)
    if lampu1:
        client.publish("TERIMA_DATA", "1")
        st.success("Lampu 1 → ON")
    else:
        client.publish("TERIMA_DATA", "2")
        st.warning("Lampu 1 → OFF")

st.write(f"Status Lampu 1: **{'ON' if st.session_state.lampu1 else 'OFF'}**")
