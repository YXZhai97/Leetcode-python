try:
    n=int(input("please enter a number "))
    result=8/n
    print(result)
except (ZeroDivisionError, ValueError):
    print("please enter a none zero number")
except Exception as error_mess:
    print("Error message: %s" % error_mess)
else:
    print("else")
finally:
    print("finally")


def main():
    pass


if __name__=="__main__":
    main()

