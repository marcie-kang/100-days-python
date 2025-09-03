def format_name(f_name, l_name):
    final_name = f_name[0].upper()

    for i in range(1, len(f_name)):
        final_name += f_name[i].lower()
    
    final_name += " "
    final_name += l_name[0].upper()
    
    for i in range(1, len(l_name)):
        final_name += l_name[i].lower()
        
    return final_name

print(format_name("soyeon", "kang"))
