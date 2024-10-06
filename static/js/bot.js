// Set your OpenAI API key
async function loadApiKey() {
    try {
        const response = await fetch('/path/to/config.json');  // Adjust the path to config.json
        if (!response.ok) {
            throw new Error(`Error fetching API key: ${response.statusText}`);
        }
        const config = await response.json();
        return config.API_KEY;
    } catch (error) {
        console.error("Error loading API key:", error);
        return null;
    }
}
// Function to produce range of calories
// Output is "[FoodItem], [MinCalories], [MaxCalories]"
async function chatWithGPT(foodItem) {
    const prompt = `What is the range of calories in 100 grams of a ${foodItem}? Limit your answer to only reply: \"[MIN value of range] - [MAX value of range]\"`;
    const API_KEY = await loadApiKey();
    if (!API_KEY) {
        console.error("API key not found");
        return;
    }
    const url = 'https://api.openai.com/v1/chat/completions';

    const data = {
        model: 'gpt-3.5-turbo', // Specify the model to use
        messages: [{ role: 'user', content: prompt }],
        max_tokens: 150 // Limit the number of tokens in the response
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${API_KEY}`,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            const responseData = await response.json();
            const message = responseData.choices[0].message.content;
            return message;
        } else {
            return `Error: ${response.status}, ${response.statusText}`;
        }
    } catch (error) {
        return `Error: ${error.message}`;
    }
}

function findInfo(foodItem) {
    chatWithGPT(foodItem).then(response => {
        alert(`ChatGPT: A ${foodItem} typically contains ${response} calories per 100 grams`);
    });
}

