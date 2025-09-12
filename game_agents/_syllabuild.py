import re

def split_syllables(word):
“””
Split a word into syllables using common English syllabification rules.

```
Args:
    word (str): The word to split into syllables
    
Returns:
    list: List of syllables
"""
if not word or not isinstance(word, str):
    return []

# Convert to lowercase and remove non-alphabetic characters
word = re.sub(r'[^a-zA-Z]', '', word.lower())

if len(word) <= 1:
    return [word] if word else []

# Define vowels (including y when it acts as a vowel)
vowels = 'aeiouy'

# Find vowel positions
vowel_positions = []
for i, char in enumerate(word):
    if char in vowels:
        # Y is a vowel if it's not at the beginning or after another vowel
        if char == 'y' and (i == 0 or word[i-1] in vowels):
            continue
        vowel_positions.append(i)

# If no vowels found or only one vowel, return the whole word
if len(vowel_positions) <= 1:
    return [word]

# Common consonant clusters that shouldn't be split
clusters = ['bl', 'br', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl', 'gr', 'pl', 'pr', 
           'sc', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'tr', 'tw', 'th', 
           'sh', 'ch', 'wh', 'ph', 'gh', 'ck', 'ng', 'nk']

syllables = []
start = 0

for i in range(len(vowel_positions) - 1):
    current_vowel = vowel_positions[i]
    next_vowel = vowel_positions[i + 1]
    
    # Find consonants between vowels
    consonant_start = current_vowel + 1
    consonant_end = next_vowel
    
    # Skip if vowels are adjacent
    if consonant_start >= consonant_end:
        continue
    
    consonants = word[consonant_start:consonant_end]
    
    if len(consonants) == 0:
        # No consonants between vowels - split after first vowel
        split_point = current_vowel + 1
    elif len(consonants) == 1:
        # Single consonant - usually goes with next syllable
        split_point = consonant_start
    elif len(consonants) == 2:
        # Two consonants - check if they form a cluster
        if consonants in clusters:
            # Keep cluster together with next syllable
            split_point = consonant_start
        else:
            # Split between consonants
            split_point = consonant_start + 1
    else:
        # Multiple consonants - split after first consonant
        # But check for clusters at the end
        if consonants[-2:] in clusters:
            split_point = consonant_end - 2
        else:
            split_point = consonant_start + 1
    
    # Add syllable
    syllable = word[start:split_point]
    if syllable:
        syllables.append(syllable)
    start = split_point

# Add the last syllable
last_syllable = word[start:]
if last_syllable:
    syllables.append(last_syllable)

# Handle silent 'e' rule - merge with previous syllable if it ends with silent e
if len(syllables) > 1 and syllables[-1] == 'e':
    syllables[-2] += syllables[-1]
    syllables.pop()

return syllables
```

def count_syllables(word):
“”“Count the number of syllables in a word.”””
return len(split_syllables(word))

# Test function

def test_syllable_splitter():
“”“Test the syllable splitter with various words.”””
test_words = [
‘hello’, ‘python’, ‘computer’, ‘elephant’, ‘wonderful’,
‘beautiful’, ‘syllable’, ‘programming’, ‘artificial’,
‘intelligence’, ‘happy’, ‘letter’, ‘picnic’, ‘baby’,
‘tiger’, ‘music’, ‘april’, ‘secret’, ‘dinner’,
‘butter’, ‘yellow’, ‘unhappy’, ‘teacher’, ‘preview’,
‘make’, ‘alone’, ‘cat’, ‘strength’, ‘rhythm’
]

```
print("Syllable Splitting Results:")
print("-" * 40)

for word in test_words:
    syllables = split_syllables(word)
    syllable_string = '-'.join(syllables)
    count = len(syllables)
    print(f"{word:12} -> {syllable_string:15} ({count} syllable{'s' if count != 1 else ''})")
```

# Interactive function

def interactive_syllable_splitter():
“”“Interactive mode to test words.”””
print(”\n” + “=”*50)
print(“Interactive Syllable Splitter”)
print(“Type words to split into syllables”)
print(“Type ‘quit’ or ‘exit’ to stop”)
print(”=”*50)

```
while True:
    user_input = input("\nEnter a word: ").strip()
    
    if user_input.lower() in ['quit', 'exit', '']:
        print("Goodbye!")
        break
    
    syllables = split_syllables(user_input)
    if syllables:
        syllable_string = '-'.join(syllables)
        count = len(syllables)
        print(f"'{user_input}' -> '{syllable_string}' ({count} syllable{'s' if count != 1 else ''})")
    else:
        print("Please enter a valid word.")
```

if **name** == “**main**”:
# Run tests
test_syllable_splitter()

```
# Start interactive mode
interactive_syllable_splitter()
```