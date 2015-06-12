from selenium import webdriver


browser = webdriver.Firefox()



# A functional test story!

# Annie is trying out a cool new online to-do list app.
# She goes to the homepage:
browser.get('http://localhost:8000')

# She notices the header and title mention to-do lists:
assert 'To-Do' in browser.title

# She's immediately invited to enter a to-do item.

# She's into making fishing flies, so she types in
# "buy peacock feathers"

# When she hits enters, the page updates, containing
# the item she entered as so:
# 1. "Buy peacock feathers"

# There is still a test box to add an item. She enteres
# "Use peacock feathers to make a fly"

# The page updates again, and now shows both items in the list

# Annie wonders if the page will remember her list. She
# sees that the site has generated a unique URL for her.
# There's some explanatory text.

# She visits the URL - her todo list is still there!

# She quits the browser in satisfaction.

browser.quit()



