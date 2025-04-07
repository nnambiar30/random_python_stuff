import json

def load_json_file(file_path):
    """Load and return JSON data from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

def extract_usernames(entries):
    """
    Given a list of entries (each being a dict with a "string_list_data" key),
    extract and return a set of usernames found under the "value" key.
    """
    usernames = set()
    for entry in entries:
        # Check if 'string_list_data' exists and is not empty
        if "string_list_data" in entry and entry["string_list_data"]:
            # Loop through each item in the string_list_data
            for item in entry["string_list_data"]:
                if "value" in item:
                    usernames.add(item["value"])
    return usernames

def main():
    # File paths for the JSON files
    followers_file = 'followers_and_following/followers_1.json'
    following_file = 'followers_and_following/following.json'
    
    try:
        # Load the JSON data from both files
        followers_data = load_json_file(followers_file)
        following_data = load_json_file(following_file)
    except Exception as e:
        print(f"Error reading JSON files: {e}")
        return

    # Extract usernames from followers_1.json
    followers_set = extract_usernames(followers_data)
    
    # Extract usernames from following.json (key: "relationships_following")
    if "relationships_following" in following_data:
        following_entries = following_data["relationships_following"]
    else:
        print("Invalid format in following.json")
        return

    following_set = extract_usernames(following_entries)

    # Find people you follow who are not following you back
    not_following_back = sorted(following_set - followers_set)

    # Print the result
    print("People you are following but who aren't following you back:")
    for username in not_following_back:
        print(username)

if __name__ == '__main__':
    main()
