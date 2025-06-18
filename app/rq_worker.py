#!/usr/bin/env python3
"""
Worker entry point for LeadRespawn
This file serves as the entry point for running different types of workers
"""

import sys
import os
from redis import Redis

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.config import settings
from app.contact_channel.interfaces.workers.worker import GenericWorker

def run_generic_worker():
    """Run the generic worker"""
    redis_client = Redis.from_url(settings.REDIS_URL)
    worker = GenericWorker(redis_client)
    worker.process()

def run_worker(worker_type: str):
    """Run a specific worker type"""
    if worker_type == "generic":
        run_generic_worker()
    else:
        print(f"Unknown worker type: {worker_type}")
        print("Available workers: generic")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python rq_worker.py <worker_type>")
        print("Available workers: generic")
        sys.exit(1)
    
    worker_type = sys.argv[1]
    run_worker(worker_type) 