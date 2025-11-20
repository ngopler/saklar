import streamlit as st
import paho.mqtt.client as mqtt

broker = "broker.mqtt-dashboard.com"
port = 1883
topic = "TERIMA_DATA"

# 1. MQTT hanya dibuat sekali
if "client" not in st.session_state:
    client = mqtt.Client("STREAM_LAMP1")   # ← versi aman
    client.connect(broker, port, 60)
    client.loop_start()
    st.session_state.client = client

client = st.session_state.client

st.title("Kontrol Lampu 1")

# 2. Tombol ON / OFF
col1, col2 = st.columns(2)

if col1.button("Lampu 1 ON"):
    client.publish(topic, "1")
    st.session_state.lampu1 = True

if col2.button("Lampu 1 OFF"):
    client.publish(topic, "2")
    st.session_state.lampu1 = False

# 3. Tampilkan status
status = st.session_state.get("lampu1", False)
st.write("Status:", "🟢 ON" if status else "🔴 OFF")
