def compare_sources(costs_catracas, costs_paineis):
    def divide_and_conquer(costs):
        if len(costs) == 1:
            return costs[0]
        
        mid = len(costs) // 2
        left = divide_and_conquer(costs[:mid])
        right = divide_and_conquer(costs[mid:])
        
        return min(left, right)
    
    short_term_catracas = divide_and_conquer(costs_catracas[:10])
    medium_term_catracas = divide_and_conquer(costs_catracas[10:20])
    long_term_catracas = divide_and_conquer(costs_catracas[20:])
    
    short_term_paineis = divide_and_conquer(costs_paineis[:10])
    medium_term_paineis = divide_and_conquer(costs_paineis[10:20])
    long_term_paineis = divide_and_conquer(costs_paineis[20:])
    
    return (short_term_catracas, medium_term_catracas, long_term_catracas), (short_term_paineis, medium_term_paineis, long_term_paineis)
