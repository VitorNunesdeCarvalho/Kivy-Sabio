from kivy.uix.gridlayout import GridLayout

# Primeiro importamos o módulo e depois criamos uma instância
# especificando os números de colunas desejado

grid_layout = GridLayout(cols=2)

# Para adicionar o widget segue o mesmo princípio do módulo boxlayout,
# porém muda alguns aspectos como você vê em seguida

grid_layout.add_widget(widget1)
grid_layout.add_widget(widget2)

# O espaçamento segue o mesmo principio, só muda o código no começo

grid_layout.spacing = [10, 10]
grid_layout.padding = [20, 20]

# Código para expandir ou reduzir os widgets preenchendo as células do grid

widget.size_hint_x = 0.5 # Widget se expandirá para ocupar metade da largura da célula
widget.size_hint_y = None # Widget se expandirá na altura

