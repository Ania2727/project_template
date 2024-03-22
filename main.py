from app.io.input import input_text_console, read_text_file, read_with_pandas
from app.io.output import output_text_console, write_to_file, write_with_pandas


def main():
    # functions from input

    # 1.1) input text from console
    user_input = input_text_console()
    print(f"The text is: {user_input}")

    # 1.2) read file with built-in funcs
    read_text_file()

    # 1.3) read file with pandas
    read_with_pandas()

    # 2.1) output in the console
    output_text_console()

    # 2.2) write to file with built-in funcs
    write_to_file()

    # 2.3) write to file with pandas
    write_with_pandas()


if __name__ == "__main__":
    main()
