# Dice Roller MCP Implementation

## Server Details
- **Name**: `dice-roller`
- **Transport**: stdio
- **Runtime**: Docker (python:3.11-slim)

## Tools
1. `roll_die(sides: str = "")`
   - Defaults to "6" if empty
   - Returns formatted string with single roll result

2. `roll_multiple(count: str = "", sides: str = "")`
   - Defaults to "2" dice with "6" sides if empty
   - Returns total and individual rolls

## Development

### Local Testing
```bash
# Build
docker build -t dice-roller-mcp-server .

# Test run
docker run -i --rm dice-roller-mcp-server

# Test protocol manually
# Type: {"jsonrpc":"2.0","method":"tools/list","id":1} v