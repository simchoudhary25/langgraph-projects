#!/bin/bash
# Simple script to run a LangGraph workflow

export PATH="$HOME/.local/bin:$PATH"
export PYTHONPATH="libs/checkpoint:libs/langgraph:libs/prebuilt:libs/checkpoint-sqlite:libs/checkpoint-postgres:libs/sdk-py:libs/cli:$PYTHONPATH"

cd "$(dirname "$0")"

uv run --with langgraph --with langgraph-prebuilt --with langchain-core python run_workflow.py

