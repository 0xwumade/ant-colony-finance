# 🔴 Real-Time Dashboard Setup

Your colony now broadcasts live data to the dashboard via WebSocket!

## What You Get
- Live agent signals as they vote
- Real-time consensus decisions
- Actual cycle numbers from your running colony
- Paper portfolio updates every 5 seconds

## Requirements
1. Redis server running (for pheromone bus)
2. WebSocket server (broadcasts colony data)
3. Dashboard server (serves the UI)
4. Colony (the actual swarm)

## Quick Start

### Option 1: Use the Batch Script (Windows)
```bash
start_colony.bat
```

This automatically starts all 3 servers + colony.

### Option 2: Manual Start (3 terminals)

**Terminal 1 - WebSocket Server:**
```bash
cd C:\ACF
.venv\Scripts\activate
python websocket_server.py
```

**Terminal 2 - Dashboard Server:**
```bash
cd C:\ACF
.venv\Scripts\activate
python serve_dashboard.py
```

**Terminal 3 - Colony:**
```bash
cd C:\ACF
.venv\Scripts\activate
python main.py --paper
```

## Open Dashboard
Go to: **http://localhost:8000**

You'll see:
- 🔗 "Connected to live colony data" in the log
- Real agent votes appearing in Signal Feed
- Live consensus decisions
- Actual cycle numbers matching your terminal

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Can't connect to Redis" | Install Redis: https://redis.io/download or use Docker: `docker run -d -p 6379:6379 redis` |
| WebSocket won't connect | Make sure `python websocket_server.py` is running on port 8765 |
| Dashboard shows demo data | Check browser console for WebSocket errors |
| No signals appearing | Colony might not be generating signals (check API keys in `.env`) |

## How It Works

```
Colony (main.py)
    ↓
Publishes signals to Redis pub/sub
    ↓
WebSocket Server (websocket_server.py)
    ↓
Broadcasts to Dashboard (index.html)
    ↓
Live updates in browser!
```

## Without Redis

If you don't have Redis installed, the dashboard will fall back to demo mode (fake data). The paper portfolio will still work, but signals won't be live.

To install Redis on Windows:
1. Download from: https://github.com/microsoftarchive/redis/releases
2. Or use WSL: `wsl --install` then `sudo apt install redis-server`
3. Or use Docker: `docker run -d -p 6379:6379 redis`

