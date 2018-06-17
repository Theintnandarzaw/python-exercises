people = 30
cars =40
trucks = 15

if cars > people :
    print("We should take the cars ")
elif cars<people:
    print("We should not take cars.")
else:
    print("We can't decide")

if trucks > cars:
    print("That is too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still cannot decide")

if people > trucks:
    print("Alright , let is just take the trucks ")
else:
    print("Fine , let's stay home then.")
