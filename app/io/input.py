import pandas as pd


def input_text_console():
    """
        Reads text input from the console.

        Returns:
            str: The text entered by the user.
        """
    user_input = input("Enter your text: ")
    return user_input


def read_text_file():
    """
        Reads the contents of a text file using built-in Python functions.

        Args:
            data.txt (str): Path to the file from which data should be read.

        Returns:
            str: The content of the file as a string.
        """
    file = open("data.txt")
    content = file.read()
    print(content)
    file.close()


def read_with_pandas():
    """
        Reads the contents of a text file using the pandas library.

        Args:
            data.txt (str): Path to the file from which data should be read.

        Returns:
            pandas.DataFrame: Data from the file as a DataFrame.
        """
    df = pd.read_csv("data.txt", sep=" ")

    print(df)
