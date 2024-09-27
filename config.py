logs      = "logs"
webhooks  = [
        {
            "url"     : "https://discord.com/api/webhooks/xxxxxxxxxxxxxxxxxxx/yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
            "logfile" : logs + "/example"
        }
        ]

blacklist = ["indiegala"]
platforms = ["steam", "epic-games-store", "ubisoft", "gog", "ps4", "ps5", "xbox-one", "xbox-series-xs", "switch", "android", "ios", "battlenet", "origin", "xbox-360"]
platform_thumbnail_prefix = "https://github.com/henrikhoefert/freega/blob/main/platform_thumbnails_alt/"
platform_thumbnail_suffix = "?raw=true"


platform_meta = {
        "steam" : {
            "author" : "Steam",
            "alias"  : "Steam",
            "url"    : "https://store.steampowered.com/",
            "icon"   : platform_thumbnail_prefix + "steam.png" + platform_thumbnail_suffix,
            "color"  : 44526
            },
        "epic-games-store" : {
            "author" : "EPIC GAMES",
            "alias"  : "Epic Games Store",
            "url"    : "https://store.epicgames.com/",
            "icon"   : platform_thumbnail_prefix + "epic.png" + platform_thumbnail_suffix,
            "color"  : 16777215
            },
        "ubisoft" : {
            "author" : "UBISOFT",
            "alias"  : "ubisoft",
            "url"    : "https://store.ubisoft.com/de/games",
            "icon"   : platform_thumbnail_prefix + "ubisoft.png" + platform_thumbnail_suffix,
            "color"  : 0
            },
        "gog" : {
            "author" : "Good Old Games",
            "alias"  : "GOG",
            "url"    : "https://www.gog.com/",
            "icon"   : platform_thumbnail_prefix + "gog.png" + platform_thumbnail_suffix,
            "color"  : 13571823
            },
        "ps4" : {
            "author" : "Playstation 4",
            "alias"  : "Playstation 4",
            "url"    : "https://www.playstation.com/ps4/ps4-games/",
            "icon"   : platform_thumbnail_prefix + "playstation.png" + platform_thumbnail_suffix,
            "color"  : 12423
            },
        "ps5" : {
            "author" : "Playstation 5",
            "alias"  : "Playstation 5",
            "url"    : "https://www.playstation.com/ps5/games/",
            "icon"   : platform_thumbnail_prefix + "playstation.png" + platform_thumbnail_suffix,
            "color"  : 12423
            },
        "xbox-360" : {
            "author" : "XBOX 360",
            "alias"  : "Xbox 360",
            "url"    : "https://www.xbox.com/games/xbox-360",
            "icon"   : platform_thumbnail_prefix + "xbox.png" + platform_thumbnail_suffix,
            "color"  : 5419075
            },
        "xbox-one" : {
            "author" : "XBOX One",
            "alias"  : "Xbox One",
            "url"    : "https://www.xbox.com/games/all-games/console?PlayWith=XboxOne",
            "icon"   : platform_thumbnail_prefix + "xbox.png" + platform_thumbnail_suffix,
            "color"  : 5419075
            },
        "xbox-series-xs" : {
            "author" : "XBOX Series XS",
            "alias"  : "Xbox Series X|S",
            "icon"   : platform_thumbnail_prefix + "xbox.png" + platform_thumbnail_suffix,
            "color"  : 5419075
            },
        "switch" : {
            "author" : "Nintendo SWITCH",
            "alias"  : "Nintendo Switch",
            "url"    : "https://www.nintendo.com/store/games/nintendo-switch-games",
            "icon"   : platform_thumbnail_prefix + "switch.png" + platform_thumbnail_suffix,
            "color"  : 15073298
            },
        "android" : {
            "author" : "ANDROID",
            "alias"  : "Android",
            "url"    : "https://play.google.com/store/games",
            "icon"   : platform_thumbnail_prefix + "android.png" + platform_thumbnail_suffix,
            "color"  : 10798649
            },
        "ios" : {
            "author" : "iOS",
            "alias"  : "iOS",
            "url"    : "https://apps.apple.com/...",
            "icon"   : platform_thumbnail_prefix + "ios.png" + platform_thumbnail_suffix,
            "color"  : 9342611
            },
        "battlenet" : {
            "author" : "BATTLE.NET",
            "alias"  : "BattleNet",
            "url"    : "https://shop.battle.net/",
            "icon"   : platform_thumbnail_prefix + "battlenet.png" + platform_thumbnail_suffix,
            "color"  : 39652
            },
        "origin" : {
            "author" : "Origin",
            "alias"  : "Origin",
            "url"    : "https://www.origin.com/store/",
            "icon"   : platform_thumbnail_prefix + "origin.png" + platform_thumbnail_suffix,
            "color"  : 16736512
            }
}
