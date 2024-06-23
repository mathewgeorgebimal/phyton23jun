"""take input of traffic and the use elif statement to tell user what to do"""
light = input("enter the current light of the traffic light")
if light=="red":
    print("stop")
elif light=="yellow":
    print("slow down")
else:
    print("continue past signal")