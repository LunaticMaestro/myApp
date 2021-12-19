from StarterApp.greeters import greeter_north, greeter_south

def main():
    '''greets people
    '''
    print("Hello People.")
    print(f"North: {greeter_north()}")
    print(f"South: {greeter_south()}")
    greeter_south()


if __name__ == "__main__":
    main()