

# 导包

from loguru import logger

# 日志级别

"""

debug : 调试日志
info ：普通日志
warning ：警告日志
success ：成功日志
error ：错误日志

"""

#logger.add("file.log", format="{time} {level} {message}", level="INFO")

logger.add("file.log", format="{time:YYYY-MM-DD at HH:mm:ss}   {level}  {message}", level="INFO")

logger.debug("这是一条Debug日志")
logger.info("这是一条info日志")
logger.warning("这是一条warning日志")
logger.success("这是一条success日志")
logger.error("这是一条error日志")


logger.info("{}".format(12))
logger.info("{}",12)

