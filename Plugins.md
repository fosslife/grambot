# Plugins

The plugin system has a nice syntax. to execute any kind of plugin, you need to use as if it was a function. like doc said, to get weather just type `.weather(city)` and so on.

## anim
Takes two parameters, and toggles between two in the message as animated text.

example: `.anim(lOl, LoL)`
first sends message as `lOl` then after 0.5s delay edits it to `LoL` and after 0.5s to again `lOl` and so on for few seconds. it gives a feel that message text is animating :P

## die
Sends a random insult to the replied message. just send `.die()` or reply to some message with it

## google
Scrapes google seach result for <u>google cards only</u>. Please note that it doesn't just scrape all of the google search results/images or anything else. the query MUST have only 1 specific answer, it won't work on questions like "How to iterate in JS" or "top 10 sports in 2016"

example: `.google(height of mount everest)` and it should give you correct answer. if it doesn't, google prolly changed HTML structure (plugin scrapes, doesn't use API). in that case just PM me or Open an Issue

## groupinfo
Gets `id` of tg group for whitelisting the userbot. you are going to definitly need this plugin as the `config.py` file takes an argument in each of it's config called `chats`. you need to set this option in your `.env` file to enable this userbot only on those selected groups. the commands won't work on other places

example: `.id()` in any chat you want to get id of.

## help
Basic syntax and small description of each plugin command

example: `.help()` duh!

## meme
Noice. Finally some good content! it has a very small collection of memes that I need mostly but it's configurable totally according to your needs. It replies to the message with a meme of your choice. I have included 5-6 of 'em as per my need.
  - pys  - Congratulations, You played yourself!
  - nou  - No, U!
  - ret  -  Oh no! it's retarded
  - moc  - You are a man of culture as well
  - hoe  - You won't get anything done hoeing like that
  - sgh  - Stop it, get some help

To add your own meme, paste the file in `images` dir under `plugins/data` dir. then go to `meme.py` and update `file_path_mapping` variable accordingly.

example: `.meme(hoe)` will send the image "You won't get anything done hoeing like that"

## messages
Simple mapping plugin that sends an equivalent text message according to configuration

example: `.say(todo)` will send text "✅ Added to TODO!"

## myname
It's a very important plugin, especially when you are not online. it reads for your name in all incoming message and if someone says your name without tagging you i.e. they are talking about you, bot will forward that message to your `Saved Messages`. very useful! 
To set it up just edit `my_name_aliases` env variable in `.env` file. Note that the bot doesn't have anything to do with your name so you can `listen` for other words too i.e if you are interested in JavaScript, just add it to the variable!


## quote
Sends a famous quote randomly. 

example: `.quote()` PS: I know it's not very useful, but it's my first plugin I even integrated so kept it :P

## server
DANGER ZONE!
Again, this plugin is Very Very <b>Dangerous</b>, please Disable it. I made it just becase a friend of mine requested. it can actually run any command that you send, on the sever, where the bot is running. I have taken some precautionary measures but still don't use it unless you know what you are doing. 

example: send `.exec(ls)` only in `Saved Messages`, it will exec `ls` on server shell, and if there's any output, it will forward it to you. I haven't done any formatting to output as they vary according to command.
Note: 1) it will work only in `Saved Message` 2) only the commands mentioned in `server.py` file under `allowed_commands` section will work. 3) Don't use it it's risky

## tag
Fun part again. tag anyone with any label. It just creates a `link` to the given username with given text with `markdown` format. 

example: `[Smart Guy](@Sparkenstein)` will send message as `Smart Guy` but it will actually tag whoever @Sparkenstein is in the group.

## user
Get as much details as possible of any given user. bot also tries to get common traits shared between the bot owner and given user.

example: `.user(Sparkenstein)` will get as much information as possible and safe to collect and share it with you in the form of message.

## waiting
Animated `waiting` text. I use it extensively. just use go ahead and use it

example: `.wait()`

## weather
You already know what it does. takes a city name, returns weather condition of that city. Note: if city name is ambiguous, mention state/province name with a comma like London,uk. If you still can't find any details, search your city name on OpenWeatherMap first. the bot uses it's API directlys

example: `.weather(London)`