"""
Engeto project - three automated tests for the ENGETO homepage using Playwright and pytest

Patricie Hermanová
patriciehermanova@gmail.com
"""

import pytest

# Test 1: Check if the title of the homepage contains "ENGETO"
def test_title(page):
    page.goto("https://engeto.cz")
    assert "ENGETO" in page.title()


# Test 2: Check if the main heading (h1) is visible on the homepage
def test_main_heading_exists(page):
    page.goto("https://engeto.cz")
    heading = page.locator("h1")
    assert heading.is_visible()
    

# Test 3: Check if the footer contains the text "ENGETO"
def test_footer_contains_engeto(page):
    page.goto("https://engeto.cz")
    footer = page.locator("footer")
    assert "ENGETO" in footer.inner_text()