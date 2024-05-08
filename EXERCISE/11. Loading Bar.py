def print_progress_bar(percentage: int):
    if percentage < 100:
        n = int(percentage / 10)
        print(f'{percentage}% [{n * "%"}{(10 - n) * "."}]\nStill loading...')
    else:
        print(f'100% Complete!\n[%%%%%%%%%%]')


print_progress_bar(int(input()))
