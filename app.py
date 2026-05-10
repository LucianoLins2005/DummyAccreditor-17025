import streamlit as st
from src.engine import DummyCalibrationEngine
import plotly.graph_objects as go

engine = DummyCalibrationEngine()

st.set_page_config(page_title="ISO 17025 Lab Assistant", layout="wide")
st.title("🔬 ISO 17025 Dummy Certification - Technical Report")

# SEÇÃO 1: PREPARAÇÃO DO ENSAIO (ISO 17025 §7.2)
st.sidebar.header("🛠️ Test Preparation (ISO 17025 §7.2)")
st.sidebar.info(f"**Standard:** {engine.norm}")
st.sidebar.write("**Equipment:** Linear Impact Pendulum (23.4 kg)")
st.sidebar.write("**ATD Model:** Hybrid III 50th Male")
test_type = st.sidebar.selectbox("Test Type", ["Thorax Impact (6.7 m/s)", "Head Drop", "Knee Impact"])

st.subheader("📋 Equipment Setup & Environmental Conditions")
col_env1, col_env2, col_env3 = st.columns(3)
col_env1.metric("Soak Temperature", "21.2 °C", "Stable")
col_env2.metric("Relative Humidity", "45%", "OK")
col_env3.metric("Impact Velocity", "6.72 m/s", "Verified")

st.markdown("---")

# SEÇÃO 2: EXECUÇÃO E COLETA DE DADOS
if st.button("🔴 Start Test Sequence"):
    df_test = engine.simulate_test_data()
    results = engine.evaluate_compliance(df_test)
    
    # Gráfico de Força vs Deflexão (Curva de Histerese)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_test['Deflection_mm'], y=df_test['Force_N'], name="Test Curve", line_color="#007bff"))
    fig.update_layout(title="Thoracic Response Curve (Force vs Deflection)", 
                      xaxis_title="Deflection (mm)", yaxis_title="Force (N)")
    st.plotly_chart(fig, use_container_width=True)

    # SEÇÃO 3: RELATO DE RESULTADOS (ISO 17025 §7.8)
    st.subheader("📑 Calibration Certificate Summary")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.write("**Peak Force (N)**")
        st.write(f"Result: {results['Force']['value']} N")
        st.write(f"Limits: 5250 - 6320 N")
        st.success(results['Force']['status']) if results['Force']['status'] == "PASS" else st.error("FAIL")

    with c2:
        st.write("**Max Deflection (mm)**")
        st.write(f"Result: {results['Deflection']['value']} mm")
        st.write(f"Limits: 63.5 - 72.4 mm")
        st.success(results['Deflection']['status']) if results['Deflection']['status'] == "PASS" else st.error("FAIL")

    with c3:
        st.write("**Measurement Uncertainty**")
        st.write(f"Estimated (k=2): ±{results['Uncertainty_k2']} N")
        st.info("Confidence Level: 95%")

    # Autenticação do Relatório
    st.markdown("---")
    st.caption(f"Digital Certificate generated per ISO 17025 protocols. Device: Hybrid III ATD. Method: {engine.norm}.")