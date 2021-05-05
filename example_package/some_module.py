import tqdm

def some_module_hello():
    print("hello from some_module")

def some_module_42():
    for i in tqdm.tqdm(range(5)):
        print(i)
    return 42

