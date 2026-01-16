from datetime import datetime

# Team RKV - CampusPulse Database Models
# Lead Backend/QA: Ripunjay
# Purpose: Defines the schema for Students, Canteen Items, and Transactions.

class StudentProfile:
    """
    Represents a student in the CampusPulse ecosystem.
    Includes the 'Internal Wallet' balance and 'Anti-Troll' status.
    """
    def __init__(self, student_id, name, initial_balance=500.0):
        self.student_id = student_id
        self.name = name
        self.wallet_balance = initial_balance
        self.has_active_penalty = False
        self.last_incident_timestamp = None
        self.total_completed_orders = 0

    def __repr__(self):
        return f"<Student: {self.name} ({self.student_id}) | Balance: ₹{self.wallet_balance}>"


class MenuItem:
    """
    Represents an item available in the Canteen.
    Used for the 'Inventory Blindness' solution.
    """
    def __init__(self, item_id, name, price, stock_count):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.stock_count = stock_count
        self.is_available = stock_count > 0

    def update_stock(self, new_count):
        self.stock_count = new_count
        self.is_available = new_count > 0


class OrderRecord:
    """
    Tracks a specific transaction.
    The 'status' field is crucial for the 'Ghost Order' detection logic.
    """
    def __init__(self, order_id, student_id, items, total_amount):
        self.order_id = order_id
        self.student_id = student_id
        self.items = items # List of MenuItem IDs
        self.total_amount = total_amount
        self.status = "PENDING" # PENDING, COLLECTED, GHOSTED
        self.timestamp = datetime.now()

    def mark_collected(self):
        """Called when the Staff scans the QR code and tears the slip."""
        self.status = "COLLECTED"

    def mark_ghosted(self):
        """Called if the pickup window expires without a scan."""
        self.status = "GHOSTED"
