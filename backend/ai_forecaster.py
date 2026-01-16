import random
from datetime import datetime

"""
CAMPUSPULSE: AI INVENTORY FORECASTING ENGINE
Lead Architect: Kunal
Integrated AI: Google Gemini 2.5 Flash Simulation

Purpose: This module analyzes historical student traffic patterns 
at JIIT to predict stock depletion risks during peak hours.
"""

class InventoryForecaster:
    def __init__(self, api_key=""):
        self.api_key = api_key
        self.model_endpoint = "gemini-2.5-flash-preview-09-2025"

    def predict_depletion(self, item_name, current_stock):
        """
        Simulates a predictive analysis call to Gemini.
        In a production environment, this would send historical sales data
        and current time to the Gemini API to get a depletion timestamp.
        """
        now = datetime.now()
        is_peak_hour = 12 <= now.hour <= 14 # Peak 12:00 PM to 2:00 PM at JIIT
        
        # Simulation Logic for Hackathon Demo
        if current_stock == 0:
            return {
                "item": item_name,
                "risk_level": "CRITICAL",
                "forecast": "Item is currently unavailable. AI suggests restocking immediately.",
                "confidence": 0.99
            }

        if is_peak_hour:
            if current_stock < 10:
                risk = "HIGH"
                eta = "5-10 minutes"
            else:
                risk = "MEDIUM"
                eta = "25-30 minutes"
        else:
            risk = "LOW"
            eta = "2+ hours"

        return {
            "item": item_name,
            "risk_level": risk,
            "forecast": f"At current consumption rates, stock will deplete in {eta}.",
            "recommended_action": "Trigger early restock" if risk == "HIGH" else "Monitor",
            "confidence": 0.92 if is_peak_hour else 0.85
        }

    def get_smart_restock_suggestions(self):
        """
        Generates AI-driven restocking quantities for the next morning.
        """
        # Simulated suggestions based on JIIT exam seasons or events
        return [
            {"item": "Cold Coffee", "reason": "High humidity forecast", "suggested_increase": "+20%"},
            {"item": "Samosa", "reason": "Mid-term exam week peak", "suggested_increase": "+35%"},
            {"item": "Dosa", "reason": "Consistent demand", "suggested_increase": "0%"}
        ]

# --- Demo Execution (Used for testing during the Hackathon) ---
if __name__ == "__main__":
    forecaster = InventoryForecaster()
    
    # Test a high-demand item during a simulated peak
    print("--- CampusPulse AI Insight ---")
    insight = forecaster.predict_depletion("Samosa", 8)
    print(f"Item: {insight['item']}")
    print(f"Risk: {insight['risk_level']}")
    print(f"Forecast: {insight['forecast']}")
    print(f"Action: {insight['recommended_action']}")
