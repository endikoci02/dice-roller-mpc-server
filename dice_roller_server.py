#!/usr/bin/env python3
"""Simple Dice Roller MCP Server - Rolls various types of virtual dice"""
import sys
import logging
import random
from mcp.server.fastmcp import FastMCP

# Configure logging to stderr
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    stream=sys.stderr
)
logger = logging.getLogger("dice-roller-server")

# Initialize MCP server
mcp = FastMCP("dice-roller")

# === MCP TOOLS ===

@mcp.tool()
async def roll_die(sides: str = "") -> str:
    """Roll a single die with a specified number of sides (default 6)."""
    logger.info(f"Executing roll_die with sides={sides}")
    try:
        # Default to 6 sides if empty string provided
        sides_int = int(sides.strip()) if sides.strip() else 6

        if sides_int < 2:
            return "❌ Error: A die must have at least 2 sides."

        result = random.randint(1, sides_int)
        return f"🎲 Rolled a d{sides_int}: {result}"
    except ValueError:
        return f"❌ Error: Invalid number of sides: {sides}"
    except Exception as e:
        logger.error(f"Error in roll_die: {e}")
        return f"❌ Error: {str(e)}"

@mcp.tool()
async def roll_multiple(count: str = "", sides: str = "") -> str:
    """Roll multiple dice of the same type (e.g., 2d6)."""
    logger.info(f"Executing roll_multiple with count={count}, sides={sides}")
    try:
        # Defaults: 2 dice, 6 sides
        count_int = int(count.strip()) if count.strip() else 2
        sides_int = int(sides.strip()) if sides.strip() else 6

        if count_int < 1:
            return "❌ Error: Must roll at least 1 die."
        if sides_int < 2:
            return "❌ Error: A die must have at least 2 sides."
        if count_int > 100:
             return "❌ Error: Too many dice! Please roll 100 or fewer."

        rolls = [random.randint(1, sides_int) for _ in range(count_int)]
        total = sum(rolls)

        rolls_str = ", ".join(map(str, rolls))
        return f"🎲 Rolled {count_int}d{sides_int}: Total = {total} (Rolls: {rolls_str})"
    except ValueError:
         return "❌ Error: Count and sides must be valid numbers."
    except Exception as e:
        logger.error(f"Error in roll_multiple: {e}")
        return f"❌ Error: {str(e)}"

# === SERVER STARTUP ===
if __name__ == "__main__":
    logger.info("Starting Dice Roller MCP server...")
    try:
        mcp.run(transport='stdio')
    except Exception as e:
        logger.error(f"Server error: {e}", exc_info=True)
        sys.exit(1)