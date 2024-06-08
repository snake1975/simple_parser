# Simple Website Parser

This is a simple website parser in Python that fetches a webpage, parses the HTML, and extracts all the links (`<a>` tags) from it.

## Documentation

### `fetch_webpage(url)`

**Description**: Fetches the content of a webpage.

**Args**:
- `url` (str): The URL of the webpage to fetch.

**Returns**: The content of the webpage as a string.

**Raises**: `requests.RequestException` if there is an error in fetching the webpage.

### `parse_links(html_content)`

**Description**: Parses the HTML content and extracts all links.

**Args**:
- `html_content` (str): The HTML content of the webpage.

**Returns**: A list of URLs found in the HTML content.

### `main(url)`

**Description**: The main function that fetches a webpage and prints all links found on it.

**Args**:
- `url` (str): The URL of the webpage to parse.

## How to Use

1. **Install the required packages**:

    ```sh
    pip install requests beautifulsoup4
    ```
2. **Run the script**:

    ```sh
    python simple_parser.py
    ```

You can replace the example URL in the `main` function with any webpage URL you want to parse. This script will fetch the webpage and print all the links found on it.
