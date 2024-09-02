import sqlite3

conn = sqlite3.connect("yt_data.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        duration TEXT NOT NULL
    )         
    """
)


def list_all_videos():
    print("============= List of Youtube Videos =============")
    videos = cursor.execute("SELECT * FROM videos")
    for video in videos:
        print(f"{video[0]} - {video[1]} - {video[2]}")
    print("=============  =============")


def add_video(title, duration):
    cursor.execute(
        "INSERT INTO videos (title, duration) VALUES (?, ?)", (title, duration)
    )
    conn.commit()
    print("Video added successfully.")


def update_video(id):
    video = cursor.execute("SELECT * FROM videos WHERE id = ?", (id,))
    print("Current video details:")
    for v in video:
        print(f"{v[0]} - {v[1]} - {v[2]}")

    print("Enter the new details for the video.")
    new_title = input("Enter the new title: ")
    new_duration = input("Enter the new duration: ")

    cursor.execute(
        "UPDATE videos SET title = ?, duration = ? WHERE id = ?",
        (new_title, new_duration, id),
    )
    conn.commit()
    print("Video details updated successfully.")


def delete_video(id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
    conn.commit()
    print("Video deleted successfully.")


def search_video(title):
    videos = cursor.execute("SELECT * FROM videos WHERE title LIKE ?", (f"%{title}%",))
    for video in videos:
        print(f"{video[0]} - {video[1]} - {video[2]}")


def main():
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
            list_all_videos()
        elif choice == 2:
            input_title = input("Enter the title of the video: ")
            input_duration = input("Enter the duration of the video: ")

            add_video(input_title, input_duration)
        elif choice == 3:
            list_all_videos()
            video_id = int(input("Enter the video id to update: "))
            update_video(video_id)
        elif choice == 4:
            list_all_videos()
            video_id = int(input("Enter the video id to delete: "))
            delete_video(video_id)
        elif choice == 5:
            input_title = input("Enter the title of the video to search: ")

            search_video(input_title)
        elif choice == 6:
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please try again.")

    # Close the connection to the database
    conn.close()


if __name__ == "__main__":
    main()
