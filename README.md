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

See the step-by-step instructions provided with the files.

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