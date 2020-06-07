from quart import Quart, jsonify
from quart_cors import cors

app = Quart(__name__)
app = cors(app)
app.bot = None


# Basic shit
@app.route("/")
async def no():
    return jsonify({"no": "go away"})


@app.route("/api/ping")
async def wsping():
    return jsonify({"ws": round(app.bot.latency * 1000, 3)})

# Stats endpoints
@app.route("/api/stats/<whatever>")
async def stats(whatever):
    if whatever == "guilds":
        return jsonify({"guilds": len(app.bot.guilds)})
    elif whatever == "shards":
        return jsonify({"shards": len(app.bot.shards)})
    elif whatever == "ready":
        return jsonify({"ready": app.bot.is_ready()})
    elif whatever == "basic":
        return jsonify(
            {
                "ready": app.bot.is_ready(),
                "guilds": len(app.bot.guilds),
                "shards": len(app.bot.shards),
            }
        )
    else:
        return jsonify({"error": 404})