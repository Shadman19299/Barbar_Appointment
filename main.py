print("hello world")
import heapq

class BarberScheduler:
    def __init__(self):
        self.appointments = []

    def book_appointment(self, time, customer_name):
        heapq.heappush(self.appointments, (time, customer_name))

    def schedule_appointments(self):
        while self.appointments:
            time, customer_name = heapq.heappop(self.appointments)
            print(f"Barber starts an appointment with {customer_name} at {time}")
            # Simulate the barber's work time (e.g., 30 minutes)
            # Replace this with your actual barber's work logic
            import time
            time.sleep(1800)  # 30 minutes
            print(f"Barber finishes an appointment with {customer_name} at {time.ctime()}")

# Example usage
scheduler = BarberScheduler()
scheduler.book_appointment("10:00 AM", "John Doe")
scheduler.book_appointment("11:00 AM", "Jane Smith")
scheduler.book_appointment("12:00 PM", "Alice Johnson")
scheduler.schedule_appointments()