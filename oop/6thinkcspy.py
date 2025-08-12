class SMS_store :
  def __init__(self):
    self.messages = []

  def add_new_arrival(self,from_number, time_arrived, text_of_SMS):
    new_message = (False, from_number, time_arrived, text_of_SMS)
    self.messages.append(new_message)

  def message_count(self):
    return len(self.messages)
  
  def get_unread_indexes(self):
    return [(i,msg) for i, msg in enumerate(self.messages) if not msg[0]] # with enumerate you get the index as well as the value , here i is the position and msg is the value
  
  def get_message(self, i):
   if 0<= i < len(self.messages):
     has_been_viewed, from_number, time_arrived, text_of_SMS = self.messages[i] #Gets the message tuple at position i 
     if not has_been_viewed:
       #update the message to mark it as read
       self.messages[i] = (True, from_number, time_arrived, text_of_SMS)
     return (from_number, time_arrived, text_of_SMS)
   else:
     return None
   
  def delete(self, i):
    if 0 <= i <len(self.messages):
      del self.messages[i]
    else:
      raise IndexError("Index out of range")
    
  def clear(self):
    self.messages.clear()

my_inbox = SMS_store()

#add new messages
my_inbox.add_new_arrival("1234567890", "2023-10-01 10:00:00", "Hello, this is a test message.")
my_inbox.add_new_arrival("0987654321", "2023-10-01 10:05:00", "This is another test message.")
my_inbox.add_new_arrival("1122334455", "2023-10-01 10:10:00", "Yet another test message.")



print("Total messages:", my_inbox.message_count())

print("Unread message indexes:", my_inbox.get_unread_indexes())

# Get a message
print("Message at index 0:", my_inbox.get_message(0))
print("Unread message indexes after reading one:", my_inbox.get_unread_indexes())

# Delete a message
my_inbox.delete(1)
print("Total messages after deletion:", my_inbox.message_count())

# Clear all messages
my_inbox.clear()
print("Total messages after clearing:", my_inbox.message_count())