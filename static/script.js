// Declare webocket and connect
var ws = new WebSocket("wss://bms5spxaid.execute-api.eu-west-2.amazonaws.com/production");

ws.onopen = function(){
	console.log("connection open");                
}

ws.onmessage = function(event) {
		appendMessage("Bot", "Bot: " + event.data);
       // Add your logic and appendMessage("bot", botResponse);
       userInput.value = "";
}

ws.onclose = function(event){
	console.log("Connection closed")
}

const chatLog = document.getElementById("chatLog");
const userInput = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");

sendButton.addEventListener("click", sendMessage);


function sendMessage() {
   const userMessage = userInput.value.trim();
   if (userMessage !== "") {
		appendMessage("User", "User: " + userMessage);
		// Add your logic and appendMessage("bot", botResponse);
		userInput.value = "";
	
		ws.send(JSON.stringify({ 'action':'sendMessage', 'message': userMessage }));
		console.log("message sent...");
   }
}

function appendMessage(sender, message) {   
   const messageElement = document.createElement("div");
   messageElement.classList.add("message", sender);
   messageElement.textContent = message;
   chatLog.appendChild(messageElement);
   chatLog.scrollTop = chatLog.scrollHeight;
}