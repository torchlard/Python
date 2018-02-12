from sources import daily
from sources import weekly

print("daily forecase: ", daily.forecast())
print("weekly:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

