import streamlit as st
import paho.mqtt.client as mqtt

# MQTT setup
broker = "broker.mqtt-dashboard.com"
port = 1883
topic = "TERIMA_DATA"

client = mqtt.Client(
    client_id="STREAMLIT_LAMP1",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)
client.connect(broker, port, 60)
client.loop_start()

st.title("Kontrol Lampu 1")

# Inisialisasi status lampu di session_state
if "lampu1" not in st.session_state:
    st.session_state.lampu1 = False  # False = OFF, True = ON

def toggle_lampu1():
    # Toggle status
    st.session_state.lampu1 = not st.session_state.lampu1
    # Kirim MQTT
    if st.session_state.lampu1:
        client.publish(topic, "1")  # Lampu 1 ON
    else:
        client.publish(topic, "2")  # Lampu 1 OFF

# Tombol toggle
if st.button("Toggle Lampu 1"):
    toggle_lampu1()

# Tampilkan status
status = "ON" if st.session_state.lampu1 else "OFF"
st.write(f"Status Lampu 1: **{status}**")
