from kivy.uix.boxlayout import BoxLayout

# Definir onde os widgets serão colocados
# Horizontal = Um do lado do outro
# Vertical = Um debaixo do outro

layout_horizontal = BoxLayout(orientation='horizontal')
layout_vertical = BoxLayout(orientation='vertical')

# Adicionar os widgets ao layout, você
# pode definir a ordem a ser colocada

layout_horizontal.add_widget(widget1)
layout_horizontal.add_widget(widget2)

layout_horizontal.spacing = 10 # Espaçamento entre os widgets
layout_horizontal.padding = [10, 20] # Espaçamento interno do layout

