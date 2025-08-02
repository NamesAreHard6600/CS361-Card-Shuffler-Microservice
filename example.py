from time import sleep

FILE_NAME = "shuffler.txt"


def form_request():
    # Uncomment these to try different examples:

    size, seed, algorithm = 52, None, None
    # size, seed, algorithm = 10, 587765, None
    # size, seed, algorithm = 26, None, "biased"
    # size, seed, algorithm = 52, 657820, "biased"
    request = f"size={size}"
    if seed:
        request += f",seed={seed}"
    if algorithm:
        request += f",algorithm={algorithm}"

    return request


def write_request(request, file_name):
    with open(file_name, 'w') as f:
        f.write(request)


def read_request(file_name):
    while True:
        with open(file_name, 'r') as f:
            line = f.readline().strip()
            if line and line[3] and line[0:4] != "size":
                return line
        sleep(0.1)


def main():
    request = form_request()
    print(f"Sending Request:\n{request}")
    write_request(request, FILE_NAME)
    response = read_request(FILE_NAME)
    print(f"Response Received:\n{response}")


if __name__ == '__main__':
    main()
