// Define your OpenAI API key and endpoint
const apiEndpoint = 'https://api.openai.com/v1/completions';

document.getElementById('send-btn').addEventListener('click', async () => {
  const userInput = document.getElementById('user-input').value;
  if (userInput) {
    // Display user message in the chat box
    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<p><strong>You:</strong> ${userInput}</p>`;
    
    // Call OpenAI API
    const response = await fetch(apiEndpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model: "gpt-3.5-turbo",
        prompt: userInput,
        max_tokens: 150,
      }),
    });
    
    const data = await response.json();
    const botReply = data.choices[0].text;
    
    // Display bot reply in the chat box
    chatBox.innerHTML += `<p><strong>Bot:</strong> ${botReply}</p>`;
    
    // Clear the user input field
    document.getElementById('user-input').value = '';
  }
});
