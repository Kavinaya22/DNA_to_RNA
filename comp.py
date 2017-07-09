with open("rosalind_revc.txt") as dnastring:
    while True:
        main = dnastring.read(1)
    if "A" == main:
            main = main.replace("A", "T", 3)
            print(main)

#    if 'A' == x[0, end]:
#      new_string = y.replace("A", "T", end)

#    print(new_string[i])
