sayilar=[1,2,3,4,5]
iterator=iter(sayilar)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

