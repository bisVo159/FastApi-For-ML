from app import process_data
from line_profiler import profile


@profile
def run():
    process_data(10000)


if __name__ == '__main__':
    run()