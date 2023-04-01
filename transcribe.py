import os
import openai

# Set up the OpenAI API key
openai.api_key = "api-key"

# Prompt the user for the audio file name
filename = input("Enter the name of the audio file (including the file extension): ")

# Check if the audio file exists
if not os.path.exists(filename):
    print("Error: File not found.")
    exit()

# Prompt the user for the target language
target_language = input("Enter the target language code (e.g. 'en', 'fr', 'es'): ")

# Prompt the user for the source language
source_language = input("Enter the source language code (e.g. 'en', 'fr', 'es'): ")

# Open the audio file in binary mode
audio_file = open(filename, "rb")

transcript = openai.Audio.translate("whisper-1", audio_file,{
        "response-format": "text",
        "language": target_language,
        "source_language": source_language
    }
)

# Print the transcription
print(transcript["text"])

# Save the transcription to a file
transcript_filename = "transcript_{}.txt".format(filename)
with open(transcript_filename, "w") as transcript_file:
    transcript_file.write(transcript["text"])