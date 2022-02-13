def dublicate(text):
    lower_text = text.lower()
    found = []
    for char in lower_text:
        if(not(char in found) and lower_text.count(char) > 1):
            found.append(char)

    return len(found)

# Codewars best practice
def duplicate_count(text):
  return len([c for c in set(text.lower()) if text.lower().count(c)>1])