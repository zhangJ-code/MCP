from typing import Any
from bypy import ByPy
from mcp.server.fastmcp import FastMCP

# 初始化 FastMCP server
mcp = FastMCP("baidu")

@mcp.tool()
async def upload_file(src_file: str):
    """上传文件到百度网盘

    Args:
        src_file: 需要上传的文件路径
    """
    bp = ByPy()
    bp.upload(
        localpath=src_file,
        remotepath=src_file.split("/")[-1]
    )  
    return "上传成功" 

@mcp.tool()
def upload_path(src_path: str):
    """上传文件夹到百度网盘

    Args:
        src_path: 需要上传的文件夹路径
    """
    bp = ByPy()
    bp.syncup(
        src_path,
        src_path.split("/")[-1]
    )
    return "上传成功"   

@mcp.tool()
async def download_file(src_file: str, target_file: str):
    """下载文件到本地

    Args:
        src_file: 需要下载的文件路径
        target_file: 下载到的文件路径
    """
    bp = ByPy()
    bp.download(
        src_file,
        target_file
    )  
    return "下载成功"

@mcp.tool()
def download_path(src_path: str, target_path: str):
    """下载文件夹到本地

    Args:
        src_path: 需要下载的文件夹路径
        target_path: 下载到的文件夹路径
    """
    bp = ByPy()
    bp.syncdown(
        src_path,
        target_path
    )
    return "下载成功" 

if __name__ == "__main__":
    # 修改传输方式以适应 Cursor 环境，比如使用 'ws' 传输
    mcp.run(transport='stdio')
