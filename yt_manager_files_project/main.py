import json


def load_data():
    try:
        with open("data.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open("data.txt", "w") as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("============= List of Youtube Videos =============")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']} - {video['duration']}")

    print("=============  =============")


def add_video(videos):
    input_title = input("Enter the title of the video: ")
    input_duration = input("Enter the duration of the video: ")
    videos.append({"title": input_title, "duration": input_duration})
    save_data_helper(videos)


def update_video(videos):
    list_all_videos(videos)
    input_index = int(input("Enter the serial number of the video to update: "))

    if input_index < 1 or input_index > len(videos):
        print("Invalid serial number. Please try again.")
        return

    input_title = input("Enter the new title of the video: ")
    input_duration = input("Enter the new duration of the video: ")
    videos[input_index - 1] = {"title": input_title, "duration": input_duration}

    print("Video details updated successfully.")


def delete_video(videos):
    list_all_videos(videos)
    input_index = int(input("Enter the serial number of the video to delete: "))

    if input_index < 1 or input_index > len(videos):
        print("Invalid serial number. Please try again.")
        return

    del videos[input_index - 1]

    print("Video deleted successfully.")


def search_video(videos):
    input_title = input("Enter the title of the video to search: ")

    for index, video in enumerate(videos, start=1):
        if video["title"] == input_title:
            print(f"Video found at serial number {index}.")
            print(f"Title: {video['title']}")
            print(f"Duration: {video['duration']}")
            return


def main():
    videos = load_data()
    while True:
        print("\n\n========== Youtube Video Management System ==========\n")
        print("1. List all Youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Search for a video")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            list_all_videos(videos)
        elif choice == 2:
            add_video(videos)
        elif choice == 3:
            update_video(videos)
        elif choice == 4:
            delete_video(videos)
        elif choice == 5:
            search_video(videos)
        elif choice == 6:
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
