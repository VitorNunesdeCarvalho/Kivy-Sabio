# Layout em que os widgets podem ser posicionados em
# qualquer lugar da tela, com coordenadas específicas

from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

layout_float = FloatLayout()

# Coordenadas para definir a posição do widget

botao = Button(text='Clique Aqui', size_hint=(None, None), size=(100, 50), pos_hint={'x': 0.5, 'y': 0.5})
layout_float.add_widget(botao)

# pos_hint: Define a posição relativa do widget em relação ao canto superior esquerdo do FloatLayout.
# size_hint: Define o tamanho relativo do widget em relação ao tamanho do FloatLayout.