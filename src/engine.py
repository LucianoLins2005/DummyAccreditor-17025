import numpy as np
import pandas as pd

class DummyCalibrationEngine:
    def __init__(self):
        # Critérios de Aceitação - CFR 49 Part 572 Subpart E (Hybrid III)
        # Ensaio: Thorax Impact Test (Velocidade de 6.7 m/s)
        self.norm = "CFR 49 Part 572 Subpart E"
        self.criteria = {
            "Thorax_Peak_Force_N": {"min": 5250, "max": 6320}, # Newton
            "Thorax_Deflection_mm": {"min": 63.5, "max": 72.4}, # mm
            "Internal_Hysteresis_Pct": {"min": 69, "max": 85}   # %
        }

    def simulate_test_data(self):
        """Simula a coleta de dados de um ensaio de pêndulo no tórax"""
        t = np.linspace(0, 0.1, 150)
        # Força de impacto (N) simulada dentro da norma
        force_n = 5800 * np.sin(np.pi * t / 0.1) + np.random.normal(0, 10, 150)
        # Deflexão do tórax (mm) simulada
        deflection_mm = 68 * np.sin(np.pi * t / 0.1) + np.random.normal(0, 0.5, 150)
        return pd.DataFrame({"Timestamp": t, "Force_N": force_n, "Deflection_mm": deflection_mm})

    def evaluate_compliance(self, data):
        """Avaliação de Resultados conforme Item 7.8 da ISO 17025"""
        peak_force = data['Force_N'].max()
        peak_defl = data['Deflection_mm'].max()
        
        results = {
            "Force": {"value": round(peak_force, 2), "status": "PASS" if 5250 <= peak_force <= 6320 else "FAIL"},
            "Deflection": {"value": round(peak_defl, 2), "status": "PASS" if 63.5 <= peak_defl <= 72.4 else "FAIL"},
            "Uncertainty_k2": round(peak_force * 0.015, 2) # Incerteza calculada de 1.5%
        }
        return results