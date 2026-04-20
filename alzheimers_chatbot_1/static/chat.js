async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value.trim();
    if (message === "") return;

    // Disable input while bot responds
    input.disabled = true;

    // User message
    const userDiv = document.createElement("div");
    userDiv.className = "user-message";
    userDiv.textContent = message;
    chatBox.appendChild(userDiv);

    input.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    // Typing indicator
    const typingDiv = document.createElement("div");
    typingDiv.className = "bot-message typing";
    typingDiv.textContent = "Bot is typing...";
    chatBox.appendChild(typingDiv);
    chatBox.scrollTop = chatBox.scrollHeight;

    // Send to backend
    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    const data = await response.json();

    // Remove typing indicator
    chatBox.removeChild(typingDiv);

    // Small delay to feel natural
    setTimeout(() => {
        const botDiv = document.createElement("div");
        botDiv.className = "bot-message";
        botDiv.textContent = data.reply;
        chatBox.appendChild(botDiv);

        chatBox.scrollTop = chatBox.scrollHeight;

        // Re-enable input
        input.disabled = false;
        input.focus();
    }, 600);
}
