# DummyAccreditor Pro: ISO 17025 Engineering & ATD Metrological Validation 🛡️📊

## 🎯 Strategic Overview
This repository features a specialized digital twin for **Automotive Impact Laboratories**. It is engineered to manage the accreditation requirements of **ISO/IEC 17025:2017**, focusing on the rigorous certification and calibration of **Anthropomorphic Test Devices (ATDs)**, specifically the **Hybrid III 50th Male**.

The project simulates a high-fidelity laboratory environment, covering the full lifecycle of a test: from environmental stabilization to automated metrological reporting.

---

## 🛠️ Technical Deep Dive & Normative Compliance

### 1. Test Preparation & Environmental Controls (ISO 17025 §7.2)
To ensure the repeatability of polymer responses in Dummies, the system monitors critical laboratory variables:
- **Soak Temperature Management**: Strict monitoring within the **20.6°C to 22.2°C** range as mandated by **CFR 49 Part 572**.
- **Traceability**: Digital logging of equipment setup, including the Linear Impact Pendulum (23.4 kg) and ATD soaking duration.

### 2. Method Selection: Thorax Impact Hysteresis (CFR 49 Part 572 Subpart E)
The engine executes a simulated Thorax Impact at a velocity of **6.7 m/s**, generating and analyzing:
- **Force vs. Deflection (Hysteresis Curve)**: Automated plotting to verify the Dummy's internal damping and structural rib integrity.
- **Strict Acceptance Criteria**:
    - **Peak Force**: 5250 N to 6320 N.
    - **Max Deflection**: 63.5 mm to 72.4 mm.
    - **Internal Hysteresis Area**: 69% to 85%.

### 3. Metrological Reliability & Reporting (ISO 17025 §7.6 & §7.8)
- **Uncertainty Engine**: Automated calculation of **Type A Uncertainty** (Confidence Level 95%, k=2) for all critical measurements.
- **Decision Rules**: Automated "Pass/Fail" verdicts based on normative tolerances, eliminating subjective technical bias.
- **Signal Integrity Diagnostic**: Analysis of SNR (Signal-to-Noise Ratio) to detect intermittent signals, cold solder joints, or damaged internal cabling.

---

## 💻 Tech Stack & Engineering Standards
- **Core**: Python 3.12 (NumPy & Pandas for high-speed data processing).
- **Visualization**: Plotly (Hysteresis and Force-Time telemetry).
- **Regulatory Frameworks**: ISO/IEC 17025:2017, CFR 49 Part 572 (Subpart E), SAE J211 instrumentation standards.

---

## 🚀 Impact for Stellantis (Betim/MG)
This project directly demonstrates the competencies required for the **Product Analyst - Engineering Tests** role:
1. **Technical Rigor**: Execution of laboratory routines following international safety procedures.
2. **Sensor Mastery**: Advanced understanding of load cells, accelerometers, and high-frequency data acquisition.
3. **Data-Driven Quality**: Transforming raw telemetry into accredited, audit-ready technical reports.

---

## ⚙️ Execution Guide
1. **Environment Setup**:
   ```bash
   pip install streamlit pandas numpy plotly