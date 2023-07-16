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
import time
import pyautogui


def generate_url(query_parameter):
    base_url = "https://twitter.com/search"
    params = f"?q=-filter%3Averified%20filter%3Ablue_verified&src=recent_search_click{query_parameter}"
    return base_url + params


def close_browser_tab():
    # Simulate closing the browser tab using keyboard shortcuts
    pyautogui.hotkey("ctrl", "w")


def wiggle_and_scroll(duration):
    # Move the mouse cursor around a bit
    pyautogui.move(10, 10, duration=0.5)
    pyautogui.move(-10, -10, duration=0.5)

    # Get the screen dimensions
    screen_width, screen_height = pyautogui.size()

    # Move the mouse cursor back to the middle of the screen
    pyautogui.moveTo(screen_width // 2, screen_height // 2)

    # Get the current time
    start_time = time.time()

    # Continuously scroll downward
    while True:
        # Negative value for scrolling downward, decreased scroll amount
        pyautogui.scroll(-10)

        # Check if {duration} seconds have elapsed
        elapsed_time = time.time() - start_time
        if elapsed_time >= duration:
            break


def load_checkmark_posts():
    # Generate URLs for "new" and "top" posts
    url_new_posts = generate_url("&f=live")
    url_top_posts = generate_url("")

    # Start with "top" posts
    webbrowser.open(url_top_posts)

    # Sleep for 5 seconds to allow the webpage to load
    time.sleep(5)

    # Scroll the "top" posts page once for one minute
    wiggle_and_scroll(60)

    # Close the "top" posts page before opening "new"
    close_browser_tab()

    # Sleep for a second to allow the browser to close the previous tab
    time.sleep(1)

    # Open the "new" posts page in the user's default browser
    webbrowser.open(url_new_posts)

    # Get the current time
    start_time = time.time()

    # Scroll the posts until the script is exited
    while True:
        # Sleep for 5 seconds to allow the webpage to load
        time.sleep(5)

        # Scroll the "new" posts page for two minutes
        wiggle_and_scroll(120)

        # Restart after 15 minutes
        elapsed_time = time.time() - start_time
        if elapsed_time >= 900:
            close_browser_tab()
            # RECURSION
            load_checkmark_posts()

        # Refresh the page to load new posts
        pyautogui.press("f5")


# Call the function to start loading verified users' posts
if __name__ == "__main__":
    load_checkmark_posts()
