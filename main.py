from app.io.input import input_text_console, read_text_file, read_with_pandas
import pandas as pd


def main():
    # 1) input text from console
    user_input = input_text_console()
    print(f"The text is: {user_input}")

    # 2) read file with built-in funcs
    read_text_file()

    # 3) read file with pandas
    read_with_pandas()


if __name__ == "__main__":
    main()
