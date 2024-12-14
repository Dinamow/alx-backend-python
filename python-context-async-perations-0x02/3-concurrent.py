#!/usr/bin/env python3
import asyncio
import aiosqlite


async def async_fetch_users():
    """
    Asynchronously fetches all users from the users.db database.
    """
    
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            while True:
                row = await cursor.fetchone()
                if row is None:
                    break
                print(row)

async def async_fetch_older_users():
    """
    Asynchronously fetches all users older than 40 from the users.db database.
    """
    
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            while True:
                row = await cursor.fetchone()
                if row is None:
                    break
                print(row)
    
async def fetch_concurrently():
    """
    Fetches all users and users older than 40 concurrently.
    """
    
    await asyncio.gather(async_fetch_users(), async_fetch_older_users())

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())