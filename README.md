# Goodnotes-Backup
Backup Goodnotes files using WebDAV to a custom server.

## Getting Started

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/johannesschiessl/Goodnotes-Backup.git
   cd Goodnotes-Backup
   ```

2. Install the required Python libraries:

   ```bash
   pip install -r requirements.txt
   ```

3. Rename `.env.example` to `.env` and add your API keys:

   ```
   NGROK_AUTH_TOKEN=your_ngrok_token
   STORAGE_PATH=/path/to/storage
   ```

   You can obtain the token from [Ngrok](https://ngrok.com).

### Usage

1. Run the server script to start the server:

   ```bash
   python server.py
   ```
2. Go to your Goodnotes settings under Cloud and Backup and select WebDAV from the backup options.

3. Then add the ngrok url you see in the terminal to the url section and just type in any user and password. (It doesn't matter because it's anonymous access, but Goodnotes won't let you connect if the fields are empty).

4. After that wait a while, you can check the backup waitlist to see the progress. 

## Contributing

Feel free to contribute by creating issues or pull requests. Suggestions for new features are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
