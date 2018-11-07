import service


def main():
    print("Welcome to the talk python info downloader.")
    print()

    service.download_info()

    for show_id in range(120, 141):
        info = service.get_episode(show_id)
        print("{} {} {}".format(info.show_id, info.guid, info.title))
        service.noop()


if __name__ == '__main__':
    main()
