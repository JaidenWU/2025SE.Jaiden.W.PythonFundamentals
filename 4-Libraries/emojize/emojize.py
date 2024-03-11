# prompts the user for a str in English
# outputs the “emojized” version of that str
# converting any codes (or aliases) therein to their corresponding emoji.

import emoji

prompt = input("Type your emoji ")
print(emoji.emojize(f"Output: {prompt}", language="alias"))
