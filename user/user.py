class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"first name: {self.first_name}")
        print(f"last name: {self.last_name}")
        print(f"email: {self.email}")
        print(f"age: {self.age}")
        print(f"rewards member: {self.is_rewards_member}")
        print(f"points: {self.gold_card_points}")
        
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
    def spend_points(self, amount):
        self.gold_card_points -= amount

john_wick = User("John", "Wick", "babayaga.com", 32)
jaime_reyes = User("Jaime", "Reyes", "bluebeetle.com", 16)
chris_hemsworth = User("Chris", "Hemsworth", "extraction.com", 35)

john_wick.enroll()
# chris_hemsworth.display_info()

john_wick.spend_points(50)
jaime_reyes.enroll()
jaime_reyes.spend_points(80)
john_wick.display_info()
jaime_reyes.display_info()
chris_hemsworth.display_info()

