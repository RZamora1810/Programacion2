# Lists

demo_list = [1, 'hello', 1.34, True, [1, 2, 3]]
colors = ['red', 'green', 'blue']

numerbs_list = list((1, 2, 3, 4))
# print(type(numerbs_list))

r = list(range(1, 101))
print(r)

print(len(colors))
print(len(demo_list))

print(colors[1])
print('green' in colors)

# print(colors)
# colors[1] = "yellow"
# print(colors)

# print(dir(colors))

# colors.append('violet')
colors.extend(('violet', 'orange'))
colors.extend(('pink', 'black'))
print(colors)

#colors.insert(-1, 'white')
colors.insert(len(colors), 'white')
print(colors)

colors.pop()
colors.pop()
print(colors)

colors.remove('red')
print(colors)

colors.sort()
print(colors)

colors.sort(reverse=True)
print(colors)

print(colors.index('green'))
print(colors.index('blue'))
print(colors.count('blue'))

