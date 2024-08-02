
import graphviz

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

data = "example data for shannon fano"
frequencies = calculate_frequencies(data)
codes = shannon_fano(frequencies)

print("Symbol\tFrequency\tCode")
for symbol, freq in frequencies:
    print(f"{symbol}\t{freq}\t\t{codes[symbol]}")


def build_tree_graphviz(frequencies, codes):
    dot = graphviz.Digraph(comment='Shannon-Fano Tree')
    
    def add_edges(dot, symbols, prefix=''):
        if len(symbols) == 1:
            dot.node(symbols[0][0], f"{symbols[0][0]}: {codes[symbols[0][0]]}")
            if prefix:
                dot.edge(prefix, symbols[0][0])
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
        
        dot.node(left_node, '')
        dot.node(right_node, '')
        
        if prefix:
            dot.edge(prefix, left_node)
            dot.edge(prefix, right_node)
        
        add_edges(dot, left_symbols, left_node)
        add_edges(dot, right_symbols, right_node)
    
    add_edges(dot, frequencies)
    return dot

tree_dot = build_tree_graphviz(frequencies, codes)
tree_dot.render('shannon_fano_tree', view=True)
