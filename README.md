# Dice Roller MCP Server

A Model Context Protocol (MCP) server that provides random dice rolling capabilities for AI assistants.

## Purpose

This MCP server provides a simple, deterministic interface for AI assistants to generate random numbers simulating tabletop dice rolls.

## Features

### Current Implementation
- `roll_die` - Roll a single die with N sides (defaults to standard 6-sided die)
- `roll_multiple` - Roll multiple dice at once and get the total and individual results (e.g., 2d20 for advantage)

## Prerequisites

- Docker Desktop with MCP Toolkit enabled
- Docker MCP CLI plugin (`docker mcp` command)

## Installation

🚀 Installation Guide
This server is designed to be installed via standard Docker MCP Gateway, allowing it to run alongside other local servers (like Obsidian or local file access).

Step 1: Clone & Build
Download standard repository and build standard Docker container image.

Bash

git clone https://github.com/YOUR_USERNAME/dice-roller-mcp.git
cd dice-roller-mcp
docker build -t dice-roller-mcp-server .
Step 2: Register the Server
You need to tell standard local Docker MCP installation about this new server.

Create or Edit your Custom Catalog:

Windows: %USERPROFILE%\.docker\mcp\catalogs\custom.yaml

macOS/Linux: ~/.docker/mcp/catalogs/custom.yaml

Add the Catalog Entry: Add this block to custom.yaml (ensure indentation is correct):

YAML

version: 2
name: custom
displayName: Custom MCP Servers
registry:
  dice-roller:
    type: server
    image: dice-roller-mcp-server:latest
    tools:
      - name: roll_die
      - name: roll_multiple
    metadata:
      category: utilities
Enable in Registry: Open standard registry.yaml file (located one folder up from standard catalogs folder) and add standard server under standard registry: key:

YAML

registry:
  # ... other servers ...
  dice-roller:
    ref: ""
Step 3: Configure Claude Desktop
Update your Claude Desktop configuration to use standard Docker Gateway.

Open your config file:

Windows: %APPDATA%\Claude\claude_desktop_config.json

macOS: ~/Library/Application Support/Claude/claude_desktop_config.json

Ensure standard mcp-toolkit-gateway is in your mcpServers list. ⚠️ Important: Replace /PATH/TO/YOUR/HOME with your actual absolute home directory path.

JSON

{
  "mcpServers": {
    "mcp-toolkit-gateway": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-v", "/var/run/docker.sock:/var/run/docker.sock",
        "-v", "/PATH/TO/YOUR/HOME/.docker/mcp:/mcp",
        "docker/mcp-gateway",
        "--catalog=/mcp/catalogs/custom.yaml",
        "--config=/mcp/config.yaml",
        "--registry=/mcp/registry.yaml",
        "--transport=stdio"
      ]
    }
  }
}
Restart Claude Desktop completely.

🔎 Verification & Testing
You can test standard server without Claude by using standard Docker MCP CLI in your terminal:

1. Verify Registration

Bash

docker mcp server list
# Output should include: dice-roller
2. Test a Roll

Bash

docker mcp call dice-roller roll_die '{"sides": "20"}'
# Output: 🎲 Rolled a d20: 15

## Usage Examples

In Claude Desktop, you can ask:
- "Roll a d20 for me"
- "Roll 4d6 and drop the lowest" (The AI will use roll_multiple and process the result)
- "Flip a coin" (The AI can interpret this as rolling a d2)
- "Roll damage for a fireball (8d6)"

## Architecture

Claude Desktop → MCP Gateway → Dice Roller MCP Server → Python random module

## License

MIT License