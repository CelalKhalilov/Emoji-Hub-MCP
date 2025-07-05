[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/celalkhalilov-emoji-hub-mcp-badge.png)](https://mseep.ai/app/celalkhalilov-emoji-hub-mcp)

# Emoji Hub MCP Server

A Model Context Protocol (MCP) server that provides access to the Emoji Hub API, allowing you to retrieve emojis by category, group, or get random emojis.

## Features

This MCP server provides the following tools:

### 🎲 Random Emoji Tools
- **get_random_emoji_tool()** - Get a completely random emoji
- **get_random_emoji_by_category_tool(category)** - Get a random emoji from a specific category
- **get_random_emoji_by_group_tool(group)** - Get a random emoji from a specific group

### 📚 Collection Tools
- **get_all_emojis_tool()** - Get all available emojis
- **get_emojis_by_category_tool(category)** - Get all emojis from a specific category
- **get_emojis_by_group_tool(group)** - Get all emojis from a specific group

## Available Categories

- `smileys-and-people`
- `animals-and-nature`
- `food-and-drink`
- `travel-and-places`
- `activities`
- `objects`
- `symbols`
- `flags`

## Available Groups

### Smileys and People
- `body`, `cat-face`, `clothing`, `creature-face`, `emotion`
- `face-negative`, `face-neutral`, `face-positive`, `face-role`
- `face-sick`, `family`, `monkey-face`, `person`, `person-activity`
- `person-gesture`, `person-role`, `skin-tone`

### Animals and Nature
- `animal-amphibian`, `animal-bird`, `animal-bug`, `animal-mammal`
- `animal-marine`, `animal-reptile`, `plant-flower`, `plant-other`

### Food and Drink
- `dishware`, `drink`, `food-asian`, `food-fruit`
- `food-prepared`, `food-sweet`, `food-vegetable`

### Other Groups
- `travel-and-places`, `activities`, `objects`, `symbols`, `flags`

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the MCP server:
```bash
python server.py
```

## Usage Examples

### Get a Random Emoji
```python
# Returns: {"name": "grinning face", "category": "smileys and people", "group": "face positive", "htmlCode": ["&#128512;"], "unicode": ["U+1F600"]}
```

### Get Random Food Emoji
```python
# Using category: food-and-drink
# Returns: {"name": "pizza", "category": "food and drink", "group": "food prepared", "htmlCode": ["&#127829;"], "unicode": ["U+1F355"]}
```

### Get All Bird Emojis
```python
# Using group: animal-bird
# Returns: [{"name": "turkey", "category": "animals and nature", "group": "animal bird", ...}, ...]
```

## API Response Format

Each emoji object contains:
- `name`: The name of the emoji
- `category`: The category it belongs to
- `group`: The specific group within the category
- `htmlCode`: Array of HTML entity codes
- `unicode`: Array of Unicode code points

## Testing

Run the test script to verify functionality:
```bash
python test_emoji_hub.py
```

## Docker Support

Build and run with Docker:
```bash
docker build -t emoji-hub-mcp .
docker run emoji-hub-mcp
```

## API Source

This MCP server uses the [Emoji Hub API](https://emojihub.yurace.pro/) by Yurace.
