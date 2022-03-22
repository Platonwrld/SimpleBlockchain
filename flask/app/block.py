import json        
import os
import hashlib


bd = os.curdir + '/blocks/'



def get_hash(filename):
    
    file = open(bd + filename, "rb").read()     
    return hashlib.md5(file).hexdigest()


def get_files():

    files = os.listdir(bd)                                 
    return sorted([int(i) for i in files])                            
    


def check_integrity():                                            

    files = get_files()

    results = []

    for file in files[1:]:                                         
        f = open(bd + str(file))
        h = json.load(f)['hash']                                   
        prev_file = str(file - 1)                                  
        actual_hash = get_hash(prev_file)                           
            res = 'OK'
        else:
            res = 'Corrupted'
        
        results.append({'block': prev_file, 'result': res})

    return results


def write_block(name, amount, to_whom, prev_hash=''):                      
    
    files = get_files()

    prev_file = files[-1]
    file_name = str(prev_file + 1)

    prev_hash = get_hash(str(prev_file))       
    
    data = {"name": name,
            "amount": amount,
            "to_whom": to_whom,
            "hash": prev_hash}
    
    with open(bd + file_name, "w") as file:                             
        json.dump(data, file, indent=4, ensure_ascii=False)     


def main():
    write_block("Katya", '890', "Stepan")
    print(check_integrity())


if __name__ == "__main__":      
    main()
