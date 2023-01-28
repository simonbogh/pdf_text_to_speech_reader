import platform
import PyPDF2
import pyttsx3

# Open the PDF file
pdfFileObj = open('./document.pdf', 'rb')

# Create a PDF reader object
pdfReader = PyPDF2.PdfReader(pdfFileObj)

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Check the system
if platform.system() == 'Darwin':
    # Set voice to Samantha (macOS)
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
else:
    # use the default voice
    pass

# Set the rate of the voice
engine.setProperty('rate', 190)

# Iterate through each page of the PDF
for _, page in enumerate(pdfReader.pages):
    # Extract the text from the page
    text = page.extract_text()
    # Print the text
    print(text)
    # Speak the text
    engine.say(text)
    engine.runAndWait()

# Close the PDF file
pdfFileObj.close()
