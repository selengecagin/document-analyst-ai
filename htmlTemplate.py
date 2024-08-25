css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://media.istockphoto.com/id/1367545305/vector/artificial-intelligence-silhouette-vector-icons-isolated-on-white-cyber-technologies-icon.jpg?s=612x612&w=0&k=20&c=nkdmZgLC56BH6VNIshsukJfJhnqm6VbnB_Rb3TlvilI=" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://t4.ftcdn.net/jpg/02/61/09/15/360_F_261091593_tnCcIkxFtKvwfJQ44EiezFSzQufXjToS.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''