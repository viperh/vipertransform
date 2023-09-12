import re

# Definim tot alfabetul in smallcaps
small_caps = {
    'a': 'ᴀ', 'b': 'ʙ', 'c': 'ᴄ', 'd': 'ᴅ', 'e': 'ᴇ', 'f': 'ғ',
    'g': 'ɢ', 'h': 'ʜ', 'i': 'ɪ', 'j': 'ᴊ', 'k': 'ᴋ', 'l': 'ʟ',
    'm': 'ᴍ', 'n': 'ɴ', 'o': 'ᴏ', 'p': 'ᴘ', 'q': 'ǫ', 'r': 'ʀ',
    's': 's', 't': 'ᴛ', 'u': 'ᴜ', 'v': 'ᴠ', 'w': 'ᴡ', 'x': 'x',
    'y': 'ʏ', 'z': 'ᴢ',
    'A': 'ᴀ', 'B': 'ʙ', 'C': 'ᴄ', 'D': 'ᴅ', 'E': 'ᴇ', 'F': 'ғ',
    'G': 'ɢ', 'H': 'ʜ', 'I': 'ɪ', 'J': 'ᴊ', 'K': 'ᴋ', 'L': 'ʟ',
    'M': 'ᴍ', 'N': 'ɴ', 'O': 'ᴏ', 'P': 'ᴘ', 'Q': 'ǫ', 'R': 'ʀ',
    'S': 's', 'T': 'ᴛ', 'U': 'ᴜ', 'V': 'ᴠ', 'W': 'ᴡ', 'X': 'x',
    'Y': 'ʏ', 'Z': 'ᴢ'
}

def to_small_caps(s):
    replacements = {}

    # Extrage si salveaza placeholderele si orice altceva trebuie salvat
    def replacer(match):
        unique_id = f"@@@{len(replacements)}@@@"
        replacements[unique_id] = match.group(0)
        return unique_id

    patterns = [
        r'(?<=[%{]).+?(?=[%}])',  # Placeholders like %player%
        r'&[0-9a-fklor](?![a-zA-Z])',  # Color codes like &a, &l, ensuring not followed by alphabets
        r'<gradient:(#[0-9a-fA-F]{3,8}(:#[0-9a-fA-F]{3,8})+)>',  # Gradient patterns
        r'&#[0-9a-fA-F]{3,8}',    # Hex color codes with &
        r'#[0-9a-fA-F]{3,8}',     # Hex color codes
        r'\{#[0-9a-fA-F]{3,8}\}'  # Another hex color pattern
    ]
    for pattern in patterns:
        s = re.sub(pattern, replacer, s)

    # Transforma textul ramas in smallcaps
    transformed = ''.join(small_caps.get(c, c) for c in s)

    # Readauga placeholderele salvate
    for unique_id, original in replacements.items():
        transformed = transformed.replace(unique_id, original)

    return transformed


# Citeste continutul introdus de utilizator
print("Adauga continutul de transformat. Cand ai terminat, scrie 'STOP' si apasa Enter:")
content = []
while True:
    line = input()
    if line.strip().upper() == 'STOP':
        break
    content.append(line)

# Transforma continutul in forma finala
transformed_content = []
for line in content:
    stripped_line = line.strip()
    if ":" in stripped_line and not stripped_line.startswith("#"):
        key, value = line.split(":", 1)
        if key.strip() in ["material", "head"]:
            transformed_content.append(line)
        else:
            # Verifica spatierea initiala a fisierului
            indentation = line[:line.index(key)]
            transformed_content.append(f"{indentation}{key}: {to_small_caps(value.strip())}")
    elif stripped_line.startswith("-"):
        # Verifica formatarea initiala a fisierului
        indentation = line[:line.index("-")]
        transformed_content.append(f"{indentation}- {to_small_caps(stripped_line[1:].strip())}")
    else:
        transformed_content.append(line)

# Curata terminalul
print("\n" * 100)

# Printeaza Continut in Terminal
print('\n'.join(transformed_content))
print("\nCopy the above content.")
