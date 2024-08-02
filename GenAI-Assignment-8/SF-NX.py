import matplotlib.pyplot as plt
import networkx as nx

def shannon_fano(symbols):
    if len(symbols) == 1:
        return {symbols[0][0]: ''}
    
    symbols.sort(key=lambda x: x[1], reverse=True)
    total = sum(freq for symbol, freq in symbols)
    acc = 0
    split_index = 0
    for i, (symbol, freq) in enumerate(symbols):
        if acc + freq > total / 2:
            break
        acc += freq
        split_index = i

    left_symbols = symbols[:split_index + 1]
    right_symbols = symbols[split_index + 1:]
    
    left_codes = shannon_fano(left_symbols)
    right_codes = shannon_fano(right_symbols)
    
    for symbol in left_codes:
        left_codes[symbol] = '0' + left_codes[symbol]
    for symbol in right_codes:
        right_codes[symbol] = '1' + right_codes[symbol]
    
    left_codes.update(right_codes)
    return left_codes

def calculate_frequencies(data):
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return sorted(frequency.items(), key=lambda item: item[1], reverse=True)

data = "Jayashre"
frequencies = calculate_frequencies(data)
codes = shannon_fano(frequencies)

print("Symbol\tFrequency\tCode")
for symbol, freq in frequencies:
    print(f"{symbol}\t{freq}\t\t{codes[symbol]}")


def build_tree(frequencies):
    def add_edges(tree, symbols, prefix=''):
        if len(symbols) == 1:
            return
        symbols.sort(key=lambda x: x[1], reverse=True)
        total = sum(freq for symbol, freq in symbols)
        acc = 0
        split_index = 0
        for i, (symbol, freq) in enumerate(symbols):
            if acc + freq > total / 2:
                break
            acc += freq
            split_index = i

        left_symbols = symbols[:split_index + 1]
        right_symbols = symbols[split_index + 1:]
        
        left_node = prefix + '0'
        right_node = prefix + '1'
        
        tree.add_edge(prefix, left_node)
        tree.add_edge(prefix, right_node)
        
        add_edges(tree, left_symbols, left_node)
        add_edges(tree, right_symbols, right_node)

    tree = nx.DiGraph()
    add_edges(tree, frequencies)
    return tree

tree = build_tree(frequencies)

# Drawing the tree
pos = nx.spring_layout(tree)
labels = {node: node for node in tree.nodes()}

plt.figure(figsize=(12, 8))
nx.draw(tree, pos, with_labels=True, labels=labels, node_size=5000, node_color='skyblue', font_size=10, font_weight='bold', arrows=True)
plt.title("Shannon-Fano Encoding Tree")
plt.show()
