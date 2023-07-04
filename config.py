token = "MTAzODkwNzg3MTA3ODkyODQ1Ng.GTjcYj.Rwpzsyr8h0kNlCgyiQlh7IbWW6_h8SMzd707Yk"

YDL_OPTIONS = {
    'format': "worstaudio/best",
    'noplaylist': 'False',
    'simulate': 'True',
    'key': 'FFmpegExtractAudio'
}

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streames 1 -reconnect_delay_max 5',
    'options': '-vn'
}