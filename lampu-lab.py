import streamlit as st
import paho.mqtt.client as mqtt
import threading

# Fungsi loop MQTT di background
def mqtt_loop(client):
    client.loop_forever()

# MQTT client global
if "mqtt_client" not in st.session_state:
    client = mqtt.Client(client_id="STREAMLIT_LAMP1")
    client.connect("broker.mqtt-dashboard.com", 1883, 60)
    # Jalankan loop di thread terpisah
    thread = threading.Thread(target=mqtt_loop, args=(client,), daemon=True)
    thread.start()
    st.session_state.mqtt_client = client

client = st.session_state.mqtt_client

st.title("Kontrol Lampu 1")

# Status lampu
if "lampu1" not in st.session_state:
    st.session_state.lampu1 = False  # OFF awal

# Checkbox toggle
lampu1 = st.checkbox("Lampu 1", value=st.session_state.lampu1)

# Jika status berubah, kirim MQTT
if lampu1 != st.session_state.lampu1:
    st.session_state.lampu1 = lampu1
    if lampu1:
        client.publish("TERIMA_DATA", "1")
    else:
        client.publish("TERIMA_DATA", "2")

st.write(f"Status Lampu 1: **{'ON' if st.session_state.lampu1 else 'OFF'}**")
