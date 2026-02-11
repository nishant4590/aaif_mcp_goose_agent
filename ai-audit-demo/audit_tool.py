import sys
print("AUDITOR PYTHON:", sys.executable)
from mcp.server.fastmcp import FastMCP

import datetime

mcp = FastMCP("Auditor")
@mcp.tool()
def check_user_access(user_name):
    """Check if a user has administrative access"""
    db = {"admin_user":"Full Access", "guest_user":"Read Only"}
    status = db.get(user_name, "Not Found")

    return f"Access status for {user_name}: {status}"

if __name__ == "__main__":
    mcp.run()


"""
Check the access level for 'admin_user'. Then, immediately use your developer tool to append a log entry to activity.log exactly as the AGENTS.md requires. Show me the tool output for the file write.
"""