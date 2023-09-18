# InstagramUnfollowers
Use your Instagram archive to see who does not follow you back mutually.

## Requirements
[Download your Instagram archive](https://help.instagram.com/181231772500920) in **JSON format only**.

## Usage
Within the zip file from the archive, navigate through the following structure:
```
├── followers_and_following
│   └── followers_1.json
│   └── following.json
```

Run the following command:
`python3 main.py followers_1.json following.json` where you point to the locations of each JSON file.

The users who you follow but do not follow you back will be listed.
