import logging
from .arguments import args

logging.basicConfig(
  format='%(asctime)s %(name)s - [%(levelname)s] %(message)s',
  datefmt='%H:%M:%S',
  level=logging.DEBUG if args.verbose else logging.INFO,
)
logger = logging.getLogger(__name__)