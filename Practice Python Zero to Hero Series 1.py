print('Hello World! My First Python Program!')

#Run-Length Encode / Decode (strings)

#Task: Implement:

#rle_encode(s) -> str (e.g., "aaabbc" -> "a3b2c1")

#rle_decode(t) -> str (e.g., "a3b2c1" -> "aaabbc")

def rle_encode(s):
    if not s:
        return ""
    
    encoded = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded.append(s[i - 1] + str(count))
            count = 1
            
    # Append the last character and its count
    encoded.append(s[-1] + str(count))
    
    return ''.join(encoded)

def rle_decode(t: str) -> str:
    if not t:
        return ""

    decoded = []
    i = 0

    while i < len(t):
        char = t[i]
        i += 1

        # must have at least one digit for the count
        if i >= len(t) or not t[i].isdigit():
            raise ValueError("Invalid RLE: missing count")

        num = 0
        while i < len(t) and t[i].isdigit():
            num = num * 10 + int(t[i])
            i += 1

        decoded.append(char * num)

    return "".join(decoded)


# Example usage:
original_string = "aaaabbbccdddfffgghhiiiijjjj"
encoded_string = rle_encode(original_string)    
print(f"Encoded: {encoded_string}")  # Output: "a3b2c1"

decoded_string = rle_decode(encoded_string)
print(f"Decoded: {decoded_string}")  # Output: "aaabbc" 
