import streamlit as st
import paho.mqtt.client as mqtt

# Konfigurasi MQTT
broker = "broker.mqtt-dashboard.com"
port = 1883
topic = "TERIMA_DATA"

# Buat client MQTT
client = mqtt.Client(
    client_id="STREAMLIT_CONTROLLER",
    callback_api_version=mqtt.CallbackAPIVersion.VERSION1
)
client.connect(broker, port, 60)
client.loop_start()

st.title("Kontrol Lampu IoT via MQTT")

st.write("Gunakan tombol di bawah untuk menghidupkan/mematikan lampu.")

# Tombol Lampu 1
col1, col2 = st.columns(2)
with col1:
    if st.button("Lampu 1 ON"):
        client.publish(topic, "1")
        st.success("Lampu 1 ON")
with col2:
    if st.button("Lampu 1 OFF"):
        client.publish(topic, "2")
        st.warning("Lampu 1 OFF")

# Tombol Lampu 2
col3, col4 = st.columns(2)
with col3:
    if st.button("Lampu 2 ON"):
        client.publish(topic, "3")
        st.success("Lampu 2 ON")
with col4:
    if st.button("Lampu 2 OFF"):
        client.publish(topic, "4")
        st.warning("Lampu 2 OFF")

# Stop MQTT ketika app ditutup
st.experimental_singleton.clear()
