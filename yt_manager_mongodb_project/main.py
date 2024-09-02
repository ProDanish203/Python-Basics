from pymongo import MongoClient
from bson import ObjectId


client = MongoClient(
    "mongodb://localhost:27017/",
    #  tlsAllowInvalidCertificates=True
)
db = client["yt-manager"]
video_collection = db["videos"]


def list_all_videos():
    print("============= List of Youtube Videos =============")
    videos = video_collection.find()
    for video in videos:
        print(f"ID: {video['_id']}")
        print(f"Title: {video['title']}")
        print(f"Duration: {video['duration']}")
        print("-------------")
    print("=============  =============")


def add_video(title, duration):
    video_collection.insert_one({"title": title, "duration": duration})
    print("Video added successfully.")


def update_video(id):
    print("Current video details:")
    video = video_collection.find_one({"_id": ObjectId(id)})
    print(f"Title: {video['title']}")
    print(f"Duration: {video['duration']}")
    print("-------------")

    print("Enter the new details for the video.")
    new_title = input("Enter the new title: ")
    new_duration = input("Enter the new duration: ")
    video_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": {"title": new_title, "duration": new_duration}}
    )
    print("Video details updated successfully.")


def delete_video(id):
    video_collection.delete_one({"_id": ObjectId(id)})
    print("Video deleted successfully.")


def search_video(title):
    videos = video_collection.find({"title": {"$regex": title, "$options": "i"}})
    print("============= Search Results =============")
    for video in videos:
        print(f"ID: {video['_id']}")
        print(f"Title: {video['title']}")
        print(f"Duration: {video['duration']}")
        print("-------------")
    print("=============  =============")


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
            video_id = input("Enter the video id to update: ")
            update_video(video_id)
        elif choice == 4:
            list_all_videos()
            video_id = input("Enter the video id to delete: ")
            delete_video(video_id)
        elif choice == 5:
            input_title = input("Enter the title of the video to search: ")

            search_video(input_title)
        elif choice == 6:
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
