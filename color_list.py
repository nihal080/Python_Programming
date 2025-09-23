colors_input = input("Enter colors separated by commas: ")
color_list = [color.strip() for color in colors_input.split(',')]

if color_list:
    print("First color:", color_list[0])
    print("Last color:", color_list[-1])
else:
    print("No colors entered.")




color_list1_input = input("Enter first list of colors separated by commas: ")
color_list2_input = input("Enter second list of colors separated by commas: ")

color_list1 = [color.strip() for color in color_list1_input.split(',')]
color_list2 = [color.strip() for color in color_list2_input.split(',')]
diff_colors = [color for color in color_list1 if color not in color_list2]

print("Colors in list1 not in list2:", diff_colors)
