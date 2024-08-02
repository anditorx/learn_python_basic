# Better practice
try:
    f = open('./sampleFile.txt', mode="w", encoding="utf-8")
finally:
    f.close()
# Best practice
with open('./sampleFile.txt', mode="w", encoding="utf-8") as f:
    # code 
    pass