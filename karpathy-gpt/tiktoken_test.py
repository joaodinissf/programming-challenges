import tiktoken
from tqdm import tqdm

model = "gpt-4o"
encoder = tiktoken.encoding_for_model(model)
print(encoder)

# Test the encoding and decoding
message = "Hello, world!"
tokens = encoder.encode(message)
print(f"Encoded tokens: {tokens}")
decoded_message = encoder.decode(tokens)
print(f"Decoded message: {decoded_message}")

print("# tokens: ", encoder.n_vocab)

num_tokens = 100
enumerated_tokens = enumerate(encoder.decode_batch([[i] for i in range(num_tokens)]))
with open("tokens.txt", "w") as f:
    for k, v in tqdm(enumerated_tokens, desc="Writing tokens"):
        f.write(f"{k}: {v} - {[ord(c) for c in v]}\n")
