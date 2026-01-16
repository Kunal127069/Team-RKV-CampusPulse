# Team RKV: Skill Swap Barter Logic
# Lead Architect: Kunal
# Purpose: Advanced matchmaking and reputation scaling for the CampusPulse community.

class SkillMatchmaker:
    """
    Logic for the 'Knowledge Barter' system.
    This module handles student discovery, skill intersection, and reputation gamification.
    """
    def __init__(self):
        # Simulated trending skills at JIIT based on recent searches
        self.trending_tags = ['react', 'python', 'figma', 'system design', 'cpp']
        self.reputation_thresholds = {
            "Novice": 0,
            "Contributor": 10,
            "Mentor": 50,
            "Expert": 100
        }

    def calculate_match_score(self, user_needs, provider_offers):
        """
        Calculates match relevance using partial string matching.
        Ensures 'Python Programming' matches with 'Python'.
        """
        score = 0
        user_needs_set = [n.lower().strip() for n in user_needs]
        provider_offers_set = [o.lower().strip() for o in provider_offers]

        for need in user_needs_set:
            for offer in provider_offers_set:
                if need in offer or offer in need:
                    score += 1
                    # Bonus for matching a trending skill at JIIT
                    if offer in self.trending_tags:
                        score += 0.5
        
        return score

    def get_student_level(self, reputation):
        """
        Gamification Logic: Determines student rank based on barter history.
        """
        current_level = "Novice"
        for level, min_rep in self.reputation_thresholds.items():
            if reputation >= min_rep:
                current_level = level
        return current_level

    def verify_barter_completion(self, user_a, user_b):
        """
        Finalizes a skill exchange and updates reputation levels.
        """
        # Simulation of DB update (Atomic transaction logic)
        user_a_rep = user_a.get('reputation', 0) + 1
        user_b_rep = user_b.get('reputation', 0) + 1
        
        return {
            "status": "Barter Securely Logged",
            "transaction_id": "SS-TXN-" + str(hash(user_a['id'] + user_b['id']))[:8],
            "updates": [
                {
                    "id": user_a['id'],
                    "new_reputation": user_a_rep,
                    "level": self.get_student_level(user_a_rep)
                },
                {
                    "id": user_b['id'],
                    "new_reputation": user_b_rep,
                    "level": self.get_student_level(user_b_rep)
                }
            ]
        }

# --- Demo Scenario for Tomorrow's Round ---
# If Kunal (Lead Architect) validates a 'System Design' session for a peer,
# the backend processes the reputation gain and updates the student's status.
