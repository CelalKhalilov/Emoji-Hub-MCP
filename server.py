from mcp.server.fastmcp import FastMCP
from app import (
    get_random_emoji,
    get_random_emoji_by_category,
    get_random_emoji_by_group,
    get_all_emojis,
    get_emojis_by_category,
    get_emojis_by_group
)

# Initialize MCP server
mcp = FastMCP("emoji-hub-mcp")

@mcp.tool()
async def get_random_emoji_tool() -> dict:
    """
    Get a random emoji from the Emoji Hub API.
    Returns an emoji object with name, category, group, htmlCode, and unicode.
    """
    result = get_random_emoji()
    return result

@mcp.tool()
async def get_random_emoji_by_category_tool(category: str) -> dict:
    """
    Get a random emoji from a specific category.

    Available categories:
    - smileys-and-people
    - animals-and-nature
    - food-and-drink
    - travel-and-places
    - activities
    - objects
    - symbols
    - flags
    """
    result = get_random_emoji_by_category(category)
    return result

@mcp.tool()
async def get_random_emoji_by_group_tool(group: str) -> dict:
    """
    Get a random emoji from a specific group.

    Some available groups include:
    - face-positive, face-negative, face-neutral
    - animal-bird, animal-mammal, animal-marine
    - food-fruit, food-vegetable, food-sweet
    - travel-and-places
    - activities, objects, symbols, flags
    """
    result = get_random_emoji_by_group(group)
    return result

@mcp.tool()
async def get_all_emojis_tool() -> dict:
    """
    Get all emojis from the Emoji Hub API.
    Returns a list of all available emojis.
    """
    result = get_all_emojis()
    return result

@mcp.tool()
async def get_emojis_by_category_tool(category: str) -> dict:
    """
    Get all emojis from a specific category.

    Available categories:
    - smileys-and-people
    - animals-and-nature
    - food-and-drink
    - travel-and-places
    - activities
    - objects
    - symbols
    - flags
    """
    result = get_emojis_by_category(category)
    return result

@mcp.tool()
async def get_emojis_by_group_tool(group: str) -> dict:
    """
    Get all emojis from a specific group.

    Some available groups include:
    - face-positive, face-negative, face-neutral
    - animal-bird, animal-mammal, animal-marine
    - food-fruit, food-vegetable, food-sweet
    - travel-and-places
    - activities, objects, symbols, flags
    """
    result = get_emojis_by_group(group)
    return result

if __name__ == "__main__":
    mcp.run(transport="stdio")