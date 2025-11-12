
import plotly.graph_objects as go

# Create figure
fig = go.Figure()

# Define node positions (x, y) and properties
nodes = {
    'start': {'pos': (0.5, 9.5), 'text': 'Launch App', 'color': '#B3E5EC', 'shape': 'circle'},
    'decision1': {'pos': (0.5, 8.5), 'text': 'CSV Exists?', 'color': '#FFEB8A', 'shape': 'diamond'},
    'autoload': {'pos': (0.2, 7.5), 'text': 'Auto-load CSV', 'color': '#B3E5EC', 'shape': 'rect'},
    'filedialog': {'pos': (0.8, 7.5), 'text': 'File Dialog', 'color': '#B3E5EC', 'shape': 'rect'},
    'display': {'pos': (0.5, 6.5), 'text': 'Display Table', 'color': '#B3E5EC', 'shape': 'rect'},
    'useraction': {'pos': (0.5, 5.5), 'text': 'User Action?', 'color': '#FFEB8A', 'shape': 'diamond'},
    'loadcsv': {'pos': (0.9, 4.5), 'text': 'Load CSV', 'color': '#B3E5EC', 'shape': 'rect'},
    'stats': {'pos': (0.1, 4.5), 'text': 'Statistics', 'color': '#B3E5EC', 'shape': 'rect'},
    'temp': {'pos': (0.25, 3.5), 'text': 'Line Chart', 'color': '#A5D6A7', 'shape': 'rect'},
    'rainfall': {'pos': (0.45, 3.5), 'text': 'Bar Chart', 'color': '#A5D6A7', 'shape': 'rect'},
    'conditions': {'pos': (0.65, 3.5), 'text': 'Pie Chart', 'color': '#A5D6A7', 'shape': 'rect'},
    'correlation': {'pos': (0.85, 3.5), 'text': 'Heatmap', 'color': '#A5D6A7', 'shape': 'rect'},
    'canvas': {'pos': (0.5, 2.5), 'text': 'Display Canvas', 'color': '#A5D6A7', 'shape': 'rect'},
}

# Add rectangles and diamonds for nodes
for key, node in nodes.items():
    x, y = node['pos']
    if node['shape'] == 'rect':
        fig.add_shape(type="rect", x0=x-0.08, y0=y-0.25, x1=x+0.08, y1=y+0.25,
                      fillcolor=node['color'], line=dict(color="#13343B", width=2))
    elif node['shape'] == 'diamond':
        fig.add_shape(type="path",
                      path=f"M {x},{y+0.3} L {x+0.1},{y} L {x},{y-0.3} L {x-0.1},{y} Z",
                      fillcolor=node['color'], line=dict(color="#13343B", width=2))
    elif node['shape'] == 'circle':
        fig.add_shape(type="circle", x0=x-0.08, y0=y-0.25, x1=x+0.08, y1=y+0.25,
                      fillcolor=node['color'], line=dict(color="#13343B", width=2))
    
    # Add text
    fig.add_annotation(x=x, y=y, text=node['text'], showarrow=False,
                       font=dict(size=10, color="#13343B"))

# Define connections (arrows)
connections = [
    ('start', 'decision1'),
    ('decision1', 'autoload', 'Yes'),
    ('decision1', 'filedialog', 'No'),
    ('autoload', 'display'),
    ('filedialog', 'display'),
    ('display', 'useraction'),
    ('useraction', 'loadcsv', 'Load'),
    ('loadcsv', 'filedialog'),
    ('useraction', 'stats', 'Stats'),
    ('useraction', 'temp', 'Temp'),
    ('useraction', 'rainfall', 'Rain'),
    ('useraction', 'conditions', 'Weather'),
    ('useraction', 'correlation', 'Corr'),
    ('stats', 'canvas'),
    ('temp', 'canvas'),
    ('rainfall', 'canvas'),
    ('conditions', 'canvas'),
    ('correlation', 'canvas'),
    ('canvas', 'useraction'),
]

# Add arrows
for conn in connections:
    from_node = nodes[conn[0]]
    to_node = nodes[conn[1]]
    x0, y0 = from_node['pos']
    x1, y1 = to_node['pos']
    
    # Adjust arrow positions based on node shapes
    if from_node['shape'] == 'diamond':
        y0 -= 0.3
    else:
        y0 -= 0.25
    
    if to_node['shape'] == 'diamond':
        y1 += 0.3
    else:
        y1 += 0.25
    
    fig.add_annotation(
        x=x1, y=y1, ax=x0, ay=y0,
        xref="x", yref="y", axref="x", ayref="y",
        showarrow=True, arrowhead=2, arrowsize=1, arrowwidth=2,
        arrowcolor="#13343B"
    )
    
    # Add edge labels if present
    if len(conn) > 2:
        mid_x = (x0 + x1) / 2
        mid_y = (y0 + y1) / 2
        fig.add_annotation(x=mid_x, y=mid_y, text=conn[2], showarrow=False,
                           font=dict(size=8, color="#13343B"),
                           bgcolor="rgba(255,255,255,0.8)")

# Update layout
fig.update_xaxes(range=[0, 1], visible=False)
fig.update_yaxes(range=[2, 10], visible=False)
fig.update_layout(
    title="Weather Data Analysis Flow",
    showlegend=False,
    plot_bgcolor='#F3F3EE',
    paper_bgcolor='#F3F3EE'
)

# Save the figure
fig.write_image('flowchart.png')
fig.write_image('flowchart.svg', format='svg')

print("Chart saved successfully")
