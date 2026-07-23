"""
contains function to create a custom non-root logger
implemented using logging module.
"""

import logging
import sys

def create_custom_logger(name: str = __name__, log_file: str = "app.log") -> logging.Logger:
    # 1. Create a named logger instance
    logger = logging.getLogger(name)
    
    # Set the lowest threshold of messages this logger will capture
    logger.setLevel(logging.DEBUG)
    
    # Prevent duplicate logs if this function is called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # 2. Define a clean, uniform layout for your logs
    # Includes: Timestamp, Logger Name, Log Level, and Message
    log_format = logging.Formatter(
        "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # 3. Create a Console Handler (Outputs to the terminal)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)  # Show only INFO and above on console
    console_handler.setFormatter(log_format)

    # 4. Create a File Handler (Saves logs permanently to a file)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)  # Save detailed DEBUG logs to file
    file_handler.setFormatter(log_format)

    # 5. Attach handlers to your custom logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

if __name__ == "__main__":
    # Initialize your unique logger
    log = create_custom_logger("PaymentSystem", "payments.log")

    # Send logs at various severity levels
    log.debug("Connecting to database...")              # Only goes to the file
    log.info("Worker service started successfully.")    # Goes to file AND console
    log.warning("Database connection response slow.")   # Goes to file AND console
    
    try:
        1 / 0
    except ZeroDivisionError:
        # log.exception automatically attaches the full traceback trace to the log
        log.exception("An unexpected mathematical error occurred!")
