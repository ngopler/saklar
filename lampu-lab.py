import streamlit as st
import paho.mqtt.client as mqtt

# MQTT client dibuat sekali di awal (global)
if "mqtt_client" not in st.session_state:
    client = mqtt.Client(
        client_id="STREAMLIT_LAMP1",
        callback_api_version=mqtt.CallbackAPIVersion.VERSION1
    )
    client.connect("broker.mqtt-dashboard.com", 1883, 60)
    client.loop_start()
    st.session_state.mqtt_client = client

client = st.session_state.mqtt_client

st.title("Kontrol Lampu 1")

# Status lampu
if "lampu1" not in st.session_state:
    st.session_state.lampu1 = False  # OFF awal

def toggle_lampu1():
    st.session_state.lampu1 = not st.session_state.lampu1
    if st.session_state.lampu1:
        client.publish("TERIMA_DATA", "1")  # ON
    else:
        client.publish("TERIMA_DATA", "2")  # OFF

# Tombol toggle
if st.button("Toggle Lampu 1"):
    toggle_lampu1()

st.write(f"Status Lampu 1: **{'ON' if st.session_state.lampu1 else 'OFF'}**")
