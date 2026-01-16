from datetime import datetime, timedelta

"""
CAMPUSPULSE: ANTI-TROLL PENALTY SYSTEM
Lead Backend/QA: Ripunjay

Logic: If a student 'ghosts' an order (marked by staff slip-tear), 
a ₹5 surcharge is applied to their next transaction. 
The system includes a 4-day 'Smart Reset' for accidental misses.
"""

class PenaltyManager:
    def __init__(self):
        self.penalty_fee = 5.0
        self.cooldown_days = 4

    def check_penalty_status(self, student_data):
        """
        Determines if the ₹5 fee should be applied based on 
        the 4-day cooldown logic.
        """
        if not student_data.get('has_penalty'):
            return 0.0
            
        last_incident = student_data.get('last_incident_date')
        if not last_incident:
            return 0.0

        # Smart Reset Logic: Check if 4 days have passed
        days_passed = (datetime.now() - last_incident).days
        
        if days_passed >= self.cooldown_days:
            # Auto-reset penalty after 4 days
            return 0.0
        else:
            return self.penalty_fee

    def trigger_ghost_order(self, student_id):
        """
        Logic to be called by the Canteen Staff Interface 
        when an order remains uncollected.
        """
        return {
            "student_id": student_id,
            "status": "FLAGGED",
            "penalty_applied": True,
            "timestamp": datetime.now()
        }
