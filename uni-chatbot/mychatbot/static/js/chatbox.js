document.addEventListener("DOMContentLoaded", () => {
  // --- Select important HTML elements ---
  const chatToggle = document.getElementById("chatToggle"); // Floating button to open chat
  const chatBox = document.getElementById("chatBox"); // Entire chat window
  const closeChat = document.getElementById("closeChat"); // Small close button (×)
  const sendBtn = document.getElementById("sendBtn"); // Send message button
  const userInput = document.getElementById("userInput"); // Input text field
  const chatBody = document.getElementById("chatBody"); // Message area container

  // If chat elements aren't found, stop running
  if (!chatToggle || !chatBox) return;

  // --- When user clicks “Chat with me” button ---
  chatToggle.addEventListener("click", () => {
    chatBox.style.display = "flex"; // Show chatbox
    chatToggle.style.display = "none"; // Hide the floating button
  });

  // --- When user clicks the close (×) button ---
  closeChat.addEventListener("click", () => {
    chatBox.style.display = "none"; // Hide chatbox
    chatToggle.style.display = "block"; // Show the floating button again
  });

  // --- Handle message sending ---
  sendBtn.addEventListener("click", sendMessage);

  // Also allow pressing “Enter” to send message
  userInput.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendMessage();
  });

  // --- Function to send a message ---
  function sendMessage() {
    const message = userInput.value.trim(); // Get the text user typed
    if (message === "") return; // Stop if it's empty

    // Create a new div for user's message
    const userMsg = document.createElement("div");
    userMsg.className = "user-message"; // Add class for styling
    userMsg.textContent = message;
    chatBody.appendChild(userMsg); // Add it to chat area

    // Clear input field after sending
    userInput.value = "";

    // Scroll chat down to show latest message
    chatBody.scrollTop = chatBody.scrollHeight;

    // --- Simulate a bot response after a short delay ---
    setTimeout(() => {
      const botMsg = document.createElement("div");
      botMsg.className = "bot-message"; // Style as bot message
      botMsg.textContent = "Sure! I can help you with that.";
      chatBody.appendChild(botMsg);

      // Scroll again to show bot's message
      chatBody.scrollTop = chatBody.scrollHeight;
    }, 700); // Wait 0.7 seconds before showing bot reply
  }
});