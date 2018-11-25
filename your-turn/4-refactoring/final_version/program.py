import random

from service import get_episode, get_latest_show_id, download_data


def main():
    show_header()

    download_data()

    # GET LATEST SHOW ID
    latest_show_id = get_latest_show_id()

    print("Working with total of {} episodes".format(latest_show_id))

    end, start = display_reults()
    for show_id in range(start, end):
        info = get_episode(show_id)
        print("{}. {}".format(info.show_id, info.title))


def display_reults():
    start = random.randint(90, 110)
    latest_id = get_latest_show_id()
    end = random.randint(130, latest_id + 1)
    return end, start


def show_header():
    print("Welcome to the talk python info downloader.")
    print()


if __name__ == '__main__':
    main()
