from dotenv import load_dotenv
from groq import Groq
import os

# load_dotenv()

GROQ_API_KEY="YOUR_GROQ_API_KEY"

groq = Groq(api_key=GROQ_API_KEY)

def classify_with_llm(log_message):
    prompt = f''' Classify the log message into one of the these categories:
    (1) Workflow Error, (2) Deprecation Warning.
    If you can't figure out a catefory , return "Unclassified".
    Onl return the category name, No preamble.
    Log message: {log_message}'''

    
    chat_completion = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
    ])
    
    return chat_completion.choices[0].message.content.strip()

if __name__ == "__main__":
    logs = [
        "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active.",
        "Invoice generation process aborted for order ID 8910 due to invalid tax calculation module.",
        "The 'BulkEmailSender' feature is no longer supported. Use 'EmailCampaignManager' for improved functionality.",
        "The 'ReportGenerator' module will be retired in version 4.0. Please migrate to the 'AdvancedAnalyticsSuite' by Dec 2025"
    ]
    
    for log in logs:
        label = classify_with_llm(log)
        print(log, "->", label)
    
    
