''' code from tiny web site guide '''
import tinify
tinify.key = "YOUR_API_KEY"

source = tinify.from_file("unoptimized.webp")
source.to_file("optimized.webp")

compressions_this_month = tinify.compression_count
