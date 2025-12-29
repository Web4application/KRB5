import re

PATTERNS = [
    r'(Authorization:.*)',
    r'(Bearer\s+[A-Za-z0-9+/=_\-]+)',
    r'([A-Za-z0-9]{20,})',  # tokens
    r'(\b\d{1,3}(\.\d{1,3}){3}\b)',  # IPv4
    r'([a-f0-9]{2}(:[a-f0-9]{2}){15})',  # MD5 fingerprints
    r'(SHA256:[A-Za-z0-9+/=]+)',
    r'(Message-ID:.*)',
]

def redact(text):
    for p in PATTERNS:
        text = re.sub(p, '[REDACTED]', text, flags=re.IGNORECASE)
    return text

if __name__ == "__main__":
    with open("input.txt") as f:
        print(redact(f.read()))
