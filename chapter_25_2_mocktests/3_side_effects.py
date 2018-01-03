from unittest.mock import Mock

def my_side_effect():
    print("Updating database!")

def main():
    mock = Mock(side_effect=my_side_effect)
    mock()

if __name__ == '__main__':
    main()

# side effect to running a function is that it might be tied
# to closely with your user interface and cause it to redraw unnecessarily.