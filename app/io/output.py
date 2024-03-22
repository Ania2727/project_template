import pandas as pd


def output_text_console(my_str="CATS ARE THE BEST"):
    """
        Outputs text to the console.

        Args:
            "some text" (str): The text to be displayed.
        """
    print(my_str)


def write_to_file():
    """
        Writes text to a file using built-in Python functions.

        Args:
            data_input.txt (str): Path to the file where data should be written.
            "some text" (str): The text to be written to the file.
        """
    line = "CATS ARE THE COOLEST"
    with open("data_output1.txt", "w") as f:
        for word in line:
            f.write(word)


def write_with_pandas():
    """
        Writes data from a DataFrame to a file using the pandas library.

        Args:
            data_input.txt (str): Path to the file where data should be written.
            dataframe. (pandas.DataFrame): The data to be written to the file.
        """
    data = {'my cats': ['Serena', 'Blair', 'Chuck'],
            'age': [18, 19, 20],
            'gender': ['female', 'female', 'male']}

    df = pd.DataFrame(data)
    df.to_csv('data_output2.txt', sep='\t', index=False)

