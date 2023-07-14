#!/usr/bin/env python3

"""
Twitter Verified Users Post Loader

This script is designed to work in conjunction with the Block The Blue browser extension that
blocks all verified Twitter users. The script continuously loads the posts of verified users so
that the browser extension can successfully block them.

Block The Blue Extension Download:
https://chrome.google.com/webstore/detail/block-the-blue-twitter-ve/ppoilcngmmnmdhgnejcnpohiabajclgn
"""

import webbrowser
import pyautogui
import time


def generate_url(query_parameter):
    base_url = "https://twitter.com/search"
    params = f"?q=-filter%3Averified%20filter%3Ablue_verified&src=recent_search_click{query_parameter}"
    return base_url + params


def close_browser_tab():
    # Simulate closing the browser tab using keyboard shortcuts
    pyautogui.hotkey("ctrl", "w")


def load_checkmark_posts():
    # Generate URLs for "new" and "top" posts
    url_new_posts = generate_url("&f=live")
    url_top_posts = generate_url("")

    # Start with "new" posts
    current_url = url_new_posts

    while True:
        # Close the previous webpage before opening a new one
        close_browser_tab()
        # Sleep for a second to allow the browser to close the previous tab
        time.sleep(1)

        # Open the new webpage in the user's default browser
        webbrowser.open(current_url)

        # Sleep for 5 seconds to allow the webpage to load
        time.sleep(5)

        # Get the screen dimensions
        screen_width, screen_height = pyautogui.size()

        # Move the mouse cursor to the middle of the screen
        pyautogui.moveTo(screen_width // 2, screen_height // 2)

        # Sleep for 5 seconds after moving the mouse cursor to the center
        time.sleep(5)

        # Get the current time
        start_time = time.time()

        # Infinite loop to continuously scroll downward
        while True:
            # Scroll continuously
            # Negative value for scrolling downward, decreased scroll amount
            pyautogui.scroll(-10)

            # Check if 60 seconds have elapsed
            elapsed_time = time.time() - start_time
            if elapsed_time >= 60:
                # Switch between "new" and "top" posts URLs
                current_url = (
                    url_top_posts if current_url == url_new_posts else url_new_posts
                )
                break


# Call the function to start loading verified users' posts
if __name__ == "__main__":
    load_checkmark_posts()
