def get_indices_of_item_weights(weights, length, limit):

    weight_index = {k: v for k, v in zip(weights, range(0, len(weights)))}

    for index in range(0, len(weights)):
        current_weight = weights[index]
        target_weight = limit - current_weight
        if target_weight in weight_index:
            if index > weight_index[target_weight]:
                return (index, weight_index[target_weight])
            else:
                return (weight_index[target_weight], index)

    return None
