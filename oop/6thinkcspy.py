class SMSStore:
    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number: str, time_arrived: str, text_of_SMS: str) -> None:
        new_message = (False, from_number, time_arrived, text_of_SMS)
        self.messages.append(new_message)

    def message_count(self) -> int:
        return len(self.messages)

    def get_unread_indexes(self):
        # List comprehension makes a new list by going through each item in a list or other collection.
        # It can also choose only some items based on a condition.
        # Here, it finds unread messages and gives their positions and details.
        # Returns list of (index, message) tuples where the message is unread (msg[0] == False)
        return [(i, msg) for i, msg in enumerate(self.messages) if not msg[0]]

    def get_message(self, i: int):
        if 0 <= i < len(self.messages):
            has_been_viewed, from_number, time_arrived, text_of_SMS = self.messages[i]
            if not has_been_viewed:
                # Mark the message as read
                self.messages[i] = (True, from_number, time_arrived, text_of_SMS)
            return from_number, time_arrived, text_of_SMS
        else:
            return None

    def delete(self, i: int) -> None:
        try:
            del self.messages[i]
        except IndexError:
            print(f"Error: Index {i} is out of range. No message deleted.")

    def clear(self) -> None:
        self.messages.clear()


if __name__ == "__main__":
    my_inbox = SMSStore()

    # Add new messages
    my_inbox.add_new_arrival("1234567890", "2023-10-01 10:00:00", "Hello, this is a test message.")
    my_inbox.add_new_arrival("0987654321", "2023-10-01 10:05:00", "This is another test message.")
    my_inbox.add_new_arrival("1122334455", "2023-10-01 10:10:00", "Yet another test message.")

    print("Total messages:", my_inbox.message_count())
    print("Unread message indexes:", my_inbox.get_unread_indexes())

    # Get a message and mark it as read
    print("Message at index 0:", my_inbox.get_message(0))
    print("Unread message indexes after reading one:", my_inbox.get_unread_indexes())

    # Delete a message (valid index)
    my_inbox.delete(1)
    print("Total messages after deletion:", my_inbox.message_count())

    # Attempt to delete a message (invalid index)
    my_inbox.delete(10)  # Should print an error message

    # Clear all messages
    my_inbox.clear()
    print("Total messages after clearing:", my_inbox.message_count())
