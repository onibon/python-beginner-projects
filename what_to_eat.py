print("👋 Welcome to the Food Recommender!")
mood = input("How are you feeling today? (happy, tired, stressed): ").lower()
time = input("What time of day is it? (morning, afternoon, night): ").lower()
if mood == "happy":
    if time == "morning":
        print("🥞 Pancakes and a smoothie sound perfect!")
    elif time == "afternoon":
        print("🍛 How about jollof rice with grilled chicken?")
    else:
        print("🍦 Treat yourself to ice cream!")
elif mood == "tired":
    if time == "morning":
        print("☕ Coffee and toast to get you going!")
    elif time == "afternoon":
        print("🥪 Try a quick sandwich and juice.")
    else:
        print("🍲 Warm soup will do the trick.")
elif mood == "stressed":
    if time == "morning":
        print("🍵 Herbal tea and something light like oats.")
    elif time == "afternoon":
        print("🥗 A fresh salad might help you relax.")
    else:
        print("happy🫖 Chamomile tea and rest, you deserve it.")
else:
    print("🤔 I couldn't figure out what you're feeling, but some fruit is always a good idea.")