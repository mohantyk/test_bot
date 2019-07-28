#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:53:27 2019

"""

import asyncio
import os
import aiohttp
from gidgethub.aiohttp import GitHubAPI


ISSUE = 1

async def main():
    async with aiohttp.ClientSession() as session:
        gh = GitHubAPI(session, "mohantyk", oauth_token=os.getenv("GH_AUTH"))
        await gh.patch('/repos/mohantyk/test_bot/issues/1',
                      data = {
                              'state': 'closed',
                              })
    
loop = asyncio.get_event_loop()
loop.run_until_complete( main() )


