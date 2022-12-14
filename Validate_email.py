import re

def is_valid_email(email):
  # Use a regular expression to check the email format
  pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
  if re.match(pattern, email):
    # The email format is valid
    return True
  else:
    # The email format is not valid
    return False

# Test the function with some example email addresses
emails = ['john@example.com', 'john@example', 'john@example.com@example.com']
for email in emails:
  if is_valid_email(email):
    print(f'"{email}" is a valid email address')
  else:
    print(f'"{email}" is not a valid email address')


explanation = """
A regular expression, or regex for short, is a sequence of characters that define a search pattern. 
These patterns are used to match and locate text strings in text documents. Regex is often used in text 
processing and data mining applications to extract, manipulate, and search for text data.

Regex patterns consist of a combination of ordinary characters (such as letters and numbers) and special characters 
(such as metacharacters and character classes). The special characters have specific meanings in regex, and they are 
used to create complex and flexible search patterns that can match a wide range of text strings.

For example, the regular expression a* will match any string that contains zero or more occurrences of the letter "a". 
The regular expression [a-z] will match any lowercase letter. And the regular expression → 
^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$ can be used to match the format of an email address.


^: This character matches the start of a string. For example, the regex pattern ^hello will match any string that starts with "hello".
$: This character matches the end of a string. For example, the regex pattern world$ will match any string that ends with "world".
.: This character matches any single character except for a newline character. For example, the regex pattern .ello will match "hello", "dello", and "mello", but not "hello world".
*: This character matches zero or more occurrences of the preceding character or group. For example, the regex pattern a* will match "", "a", "aa", "aaa", and so on.
+: This character matches one or more occurrences of the preceding character or group. For example, the regex pattern a+ will match "a", "aa", "aaa", and so on, but not "".
?: This character matches zero or one occurrence of the preceding character or group. For example, the regex pattern a? will match "", "a", but not "aa".
[ and ]: These characters are used to create character classes. A character class is a set of characters that can be matched by a regex pattern. For example, the character class [aeiou] will match any lowercase vowel, and the character class [a-zA-Z0-9] will match any letter or digit.
|: This character is used to create alternation, which means that a regex pattern can match one of several different alternatives. For example, the regex pattern hello|world will match any string that contains "hello" or "world".
\: This character is used to escape special characters, which means that the special characters will be treated as ordinary characters and will not have their special meanings in regex. For example, the regex pattern \. will match a period (.) character, and the regex pattern \[a-z\] will match any lowercase letter.
"""