### component contract 

- Component: Configuration Loader

- Responsibility:
    Load, validate, and return application configuration.

- Input:
    Path to YAML file.

- Input Structure:
    ```yaml
    seed_urls:
    - https://docs.python.org

    scope:
    allowed_domains:
        - docs.python.org

    crawl:
    max_depth: 2
    user_agent: "corpora/0.1"

    storage:
    output_dir: "./data"
    ```

- Output:
    Configuration object
    ```json
    {
        seed_urls: ["www.wikipedia.com","www.goodreads.com"],
        allowed_domains : ["", ""],
        max_crawl_depth: 2,
        user_agent: "corpora/0.1",
        output_dir: "./data"
    }
    ```

    ```python
    Configuration(
        seed_urls=[
            "https://www.wikipedia.org",
            "https://www.goodreads.com"
        ],
        allowed_domains=[
            "wikipedia.org",
            "goodreads.com"
        ],
        max_crawl_depth=2,
        user_agent="ChronoSeek/0.1",
        output_dir=Path("./data")
    )
    ```
   

- Output Structure:


- Dependencies:
    File system
    YAML parser
    pydantic model

- Side Effects:
    Reads a file from disk.

- Failure Modes:
    File not found
    Invalid YAML
    Validation error