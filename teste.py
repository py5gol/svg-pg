

header = "<svg xmlns=\"http://www.w3.org/2000/svg\">"
footer = "</svg>"

template = """
  <g>
    <rect x="{}" y="{}" width="{}" height="{}" fill="{}"></rect>
    <text x="{}" y="{}" font-family="Verdana" font-size="{}" fill="black">{}</text>
  </g>
"""

x0 = 0
y0 = 0

iconwidth = 36
iconheight = 24

labelheight = 18

space_between_icons = 6
space_between_icon_and_label = 10

items = {
    'Test': '#AA1199',
    'Test 2': '#1199AA',
    'Test 3': '#AA9911',
}

svg_string = header

counter = 0
for key in items.keys():
    
    color = items[key]
    
    l_x0 = x0
    l_y0 = y0 + (30 * counter)
    
    svg_string += template.format(l_x0, l_y0, iconwidth, iconheight, color, 46, l_y0 + iconheight - 3, iconheight, key)
    
    counter += 1

svg_string += footer

print(svg_string)

