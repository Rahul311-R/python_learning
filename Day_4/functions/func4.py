def vowel(str):
    vowel = "aeiouAEIOU"
    count = 0
    for ch in str:
        if ch in vowel:
            count += 1
    return count

print(vowel(input()))