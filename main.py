import asyncio
import logging

from wrapper import run_bot

def main():
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        print("Interrupted by user, shutting down")
        return

if __name__ == "__main__":
    main()

