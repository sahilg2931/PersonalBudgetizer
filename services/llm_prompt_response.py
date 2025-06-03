import cohere # type: ignore
import os
import time


api_key = os.getenv("COHERE_API_KEY")
client = cohere.ClientV2(api_key)


def call_cohere_chat_with_retry(prompt: str, retries=5, delay=5) -> str:
    for attempt in range(retries):
        try:
            response = client.chat(
                model="command-a-03-2025",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0,
                max_tokens=8100,
            )
            # Access the text content from the response
            return response.message.content[0].text.strip()
        except Exception as e:
            print(f"⚠️ Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
            delay *= 2
    print("❌ All retries failed.")
    return ""