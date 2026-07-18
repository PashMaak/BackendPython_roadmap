def word_count(text: str):
# Function which counts each word same logic as std::map in C++
# sorts text for O(nlogn) and then count amount of similar neoighbours 
# sicnce text is sorted all similar elements would be neighbours
# Hence we can count them all by (O(n))
    text.sort()
    std_map = []

    pref = text[0]
    cnt = 0
    for cur in text:
        if (pref != cur):
            std_map.append((pref, cnt))
            cnt = 1
            pref = cur
        else:
            cnt += 1
    
    std_map.append((pref, cnt))
    return std_map

textchuk = ["bla", "bla", "ble", "lulu", "lulu", "juju"]
print(word_count(textchuk))