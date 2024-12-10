import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo no dirigido para representar las conexiones
# El grafo representará a los desarrolladores y los proyectos como estaciones
grafo = nx.Graph()

# Agregar nodos (representan a los desarrolladores y proyectos)
grafo.add_node("Desarrollador1", tipo="desarrollador", habilidades=["Python", "Django"])
grafo.add_node("Desarrollador2", tipo="desarrollador", habilidades=["JavaScript", "React"])
grafo.add_node("Proyecto1", tipo="proyecto", habilidades_necesarias=["Python", "Django"])
grafo.add_node("Proyecto2", tipo="proyecto", habilidades_necesarias=["JavaScript", "React"])

# Agregar aristas para conectar desarrolladores con proyectos según habilidades compatibles
# Cada arista representa una relación entre un desarrollador y un proyecto
grafo.add_edge("Desarrollador1", "Proyecto1", peso=1)
grafo.add_edge("Desarrollador2", "Proyecto2", peso=1)

# Agregar conexiones adicionales para que se vea como una red de metro
grafo.add_edge("Desarrollador1", "Desarrollador2", peso=2)  # Conexión ficticia entre desarrolladores
grafo.add_edge("Proyecto1", "Proyecto2", peso=2)  # Conexión ficticia entre proyectos

# Configuración de posiciones para que el grafo se visualice bien
pos = nx.spring_layout(grafo)

# Dibujar el grafo
plt.figure(figsize=(10, 8))  # Tamaño del gráfico
nx.draw(
    grafo, 
    pos, 
    with_labels=True, 
    node_size=3000, 
    node_color="lightblue", 
    font_size=10, 
    font_weight="bold"
)

# Agregar etiquetas para las aristas (pesos)
etiquetas_aristas = nx.get_edge_attributes(grafo, 'peso')
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=etiquetas_aristas)

# Mostrar el grafo
plt.title("Red de Recursos para Desarrolladores y Proyectos")
plt.show()