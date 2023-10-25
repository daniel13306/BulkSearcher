import os




def search_for_keyword(keyword, file_type, folder):
    results = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(file_type):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    if keyword in content:
                        results.append((file_path, content.count(keyword)))
    return results


def main():
    keyword = input("Enter the keyword to search for: ")
    file_type = input("Enter the file type (e.g., .txt, .py) (Press Enter for all): ")
    folder = input("Enter the folder to start the search (press Enter for the current directory): ").strip()

    if not folder:
        folder = os.getcwd()

    print(f"Searching for '{keyword}' in {folder} and its subfolders...")

    results = search_for_keyword(keyword, file_type, folder)

    if not results:
        print("No matching files found.")
    else:
        print("Matching files:")
        for file_path, count in results:
            print(f"{file_path} - Found {count} times")


if __name__ == "__main__":
    main()
