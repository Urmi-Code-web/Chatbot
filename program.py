import pyautogui
import pyperclip
import time
from openai import OpenAI

client=OpenAI(api_key="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")
def is_last_message_from_sender(chat_log,sender_name="Harsh"):
    messages=chat_log.strip().split("/2026 ")[-1]
    if sender_name in messages:
        return True
    return False

pyautogui.click(1073, 1049)
time.sleep(2)
while True:
    # Move mouse to starting position of text selection (760, 240)
    pyautogui.moveTo(760, 240)

    # Drag mouse to ending position (1881, 929) to select the text
    pyautogui.dragTo(1881, 929, duration=1, button='left')

    # Short delay to ensure selection is complete
    time.sleep(1)

    # Press Ctrl + C to copy selected text to clipboard
    pyautogui.hotkey('ctrl', 'c')

    pyautogui.click(755,280)

    # Wait for clipboard to update
    time.sleep(0.5)

    # Retrieve copied text from clipboard and store in variable
    copied_text = pyperclip.paste()

    # Print the copied text
    print(copied_text)

    if is_last_message_from_sender(copied_text):
        completion=client.chat.completions.create(
        model="gpt-5.2",

        messages=[
            {"role":"system","content":"You are a girl named Urmi who speaks hindi as well as english. You are from India and also a coder. You will analyse the chat history and give response like Urmi.Output should beshort and smart like Urmi"},
            {"role":"user","content":copied_text}
        ]
        )
        response=completion.choices[0].message.content
        pyperclip.copy(response)

        # Click at coordinates (981, 981) where you want to paste
        pyautogui.click(981, 981)

        # Small delay before pasting
        time.sleep(0.5)

        # Paste the copied text
        pyautogui.hotkey('ctrl', 'v')

        # Press Enter key
        pyautogui.press('enter')