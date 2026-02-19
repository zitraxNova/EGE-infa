f = open('24_9845.txt')
s = f.readline().strip()    # Убираем лишние символы в конце строки

def is_valid_substring(sub):
      for i in range(len(sub) - 1):
          if ((sub[i].isupper() and sub[i+1].isdigit()) or
              (sub[i].isdigit() and sub[i+1].isupper())):
              return False
      return True

max_length = 0
for i in range(len(s)):
      for j in range(i + 1, len(s) + 1):
          substring = s[i:j]
          if is_valid_substring(substring):
              max_length = max(max_length, len(substring))
          else:
              break    # Если подстрока не удовлетворяет условию, нет смысла проверять дальше

print(max_length)
