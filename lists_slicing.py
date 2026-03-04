
alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
print(alphabet[0:10:3])
print(alphabet[:5:2])
print(alphabet[12:17])

print("----------------------")

# Räkna ut summan av talen i strängen
# split - separerar strängen
# strip - tar bort whitespace
data = "10, 12, 20, 30, 40"  # ska bli 112
token_list = data.split(",")  # gör sträng till lista
sum_so_far = 0
for token in token_list:
    token_number = int(token.strip()) # tar bort mellanslag
    sum_so_far += token_number
print(sum_so_far)