from openai import OpenAI
client=OpenAI(api_key="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")
command='''[14:56, 22/2/2026] Harsh: ??
[14:57, 22/2/2026] Urmi❣️: Abhi to koi ootp ni aaya
[14:58, 22/2/2026] Harsh: Ek baar airplane mode par karke
[14:58, 22/2/2026] Urmi❣️: ?
[14:59, 22/2/2026] Harsh: Check kr raha hai
[15:00, 22/2/2026] Harsh: Hogya
[15:00, 22/2/2026] Harsh: Thankyou'''
completion=client.chat.completions.create(
    model="gpt-5.2",

    messages=[
        {"role":"system","content":"You are a girl named Urmi who speaks hindi as well as english. She is from India and also a coder. You will analyse the chat history and give response like Urmi"},
        {"role":"user","content":command}
    ]
)
print(completion.choices[0].message.content)