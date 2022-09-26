# You probably know the "like" system from Facebook and other pages. People can "like" blog posts, 
# pictures or other items. We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples:





def like(a_list):
    if len(a_list) == 0:
        return "no one likes this"
    elif len(a_list) == 1:
        return f"{a_list[0]} likes this"
    elif len(a_list) == 2:
        return f"{a_list[0]} and {a_list[1]} like this"
    elif len(a_list) == 3:
        return f"{a_list[0]}, {a_list[1]} and {a_list[2]} like this"
    else:
        return f"{a_list[0]}, {a_list[1]} and {len(a_list)-2} like this "