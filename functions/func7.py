def user_profile(**data):
    for a,i in data.items():
        print(f"{a}:{i}")

user_profile(name="Rahul",age=21,city = "coimbatore" )