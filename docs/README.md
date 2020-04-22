# DOMAIN-ONLY Filter Lists
**Last Updated:** 2020-04-22 17:28

- [Details](#details)
- [Usage](#usage)
  - [Using with Pi-Hole](#using-with-pi-hole)
  - [Using with other tools](#using-with-other-tools)
- [The Lists](#the-lists)

  - [EasyList](https://easylist.to/easylist/easylist.txt) (Domains-only)

  - [EasyPrivacy](https://easylist.to/easylist/easyprivacy.txt) (Domains-only)

  - [EasyList Cookie](https://easylist-downloads.adblockplus.org/easylist-cookie.txt) (Domains-only)

  - [Fanboy's Social Blocking](https://easylist.to/easylist/fanboy-social.txt) (Domains-only)

  - [Fanboy's Social Blocking](https://easylist.to/easylist/fanboy-annoyance.txt) (Domains-only)

  - [EasyList Germany](https://easylist.to/easylistgermany/easylistgermany.txt) (Domains-only)

  - [EasyList Italy](https://easylist-downloads.adblockplus.org/easylistitaly.txt) (Domains-only)

  - [EasyList Dutch](https://easylist-downloads.adblockplus.org/easylistdutch.txt) (Domains-only)

  - [EasyList Liste FR](https://easylist-downloads.adblockplus.org/liste_fr.txt) (Domains-only)

  - [EasyList China](https://easylist-downloads.adblockplus.org/easylistchina.txt) (Domains-only)

  - [EasyList ABPindo](https://raw.githubusercontent.com/heradhis/indonesianadblockrules/master/subscriptions/abpindo.txt) (Domains-only)

  - [EasyList Liste AR](https://easylist-downloads.adblockplus.org/Liste_AR.txt) (Domains-only)

  - [EasyList Czech and Slovak](https://raw.githubusercontent.com/tomasko126/easylistczechandslovak/master/filters.txt) (Domains-only)

  - [EasyList Latvian List](https://notabug.org/latvian-list/adblock-latvian/raw/master/lists/latvian-list.txt) (Domains-only)

  - [EasyList Hebrew](https://raw.githubusercontent.com/easylist/EasyListHebrew/master/EasyListHebrew.txt) (Domains-only)

  - [EasyList Lithuania](http://margevicius.lt/easylistlithuania.txt) (Domains-only)

  - [AdGuard Base Filter](https://filters.adtidy.org/extension/chromium/filters/2.txt) (Domains-only)

  - [AdGuard Tracking Protection filter](https://filters.adtidy.org/extension/chromium/filters/3.txt) (Domains-only)

  - [AdGuard Social media filter](https://filters.adtidy.org/extension/chromium/filters/4.txt) (Domains-only)

  - [AdGuard Annoyances filter](https://filters.adtidy.org/extension/chromium/filters/14.txt) (Domains-only)

  - [AdGuard Russian filter](https://filters.adtidy.org/extension/chromium/filters/1.txt) (Domains-only)

  - [AdGuard German filter](https://filters.adtidy.org/extension/chromium/filters/6.txt) (Domains-only)

  - [AdGuard French filter](https://filters.adtidy.org/extension/chromium/filters/16.txt) (Domains-only)

  - [AdGuard Japanese filter](https://filters.adtidy.org/extension/chromium/filters/7.txt) (Domains-only)

  - [AdGuard Dutch filter](https://filters.adtidy.org/extension/chromium/filters/8.txt) (Domains-only)

  - [AdGuard Spanish/Portuguese filter](https://filters.adtidy.org/extension/chromium/filters/9.txt) (Domains-only)

  - [AdGuard Turkish filter](https://filters.adtidy.org/extension/chromium/filters/13.txt) (Domains-only)

  - [AdGuard Mobile ads filter](https://filters.adtidy.org/extension/chromium/filters/11.txt) (Domains-only)

  - [AdGuard Simplified Domain Names Filter](https://filters.adtidy.org/extension/chromium/filters/15.txt) (Domains-only)

  - [NoCoin Filter List](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt) (Domains-only)

- [License](#license)
- [Reporting Conversion Issues](#reporting-conversion-issues)


# Details:
These are "DOMAIN-ONLY" **converted** versions of various popular original filter / blocking lists.
They have been modified from their original versions by scripts at: https://github.com/justdomains/ci

The scripts output **only** the full-domain-blocking entries from the original lists, while attempting to filter any domains that conflict with an exception rule on the original item.

**Because these are automated, converted _subsets_ of the original lists, please do not report omissions from these converted files to the list originator.**

&nbsp;

# Usage:
These converted files can be used with various DNS and domain-blocking tools:

## Using with [Pi-Hole](https://pi-hole.net/):
1. Copy the link to the Pi-Hole format for the desired list (from the appropriate table below).
2. [Add the URL to your Pi-Hole's block lists (**Settings** > **Pi-Hole's Block Lists**).](https://github.com/pi-hole/pi-hole/wiki/Customising-Sources-for-Ad-Lists)

## Using with other tools:
The converted lists are provided in a "Raw Domain List" format that contains only domains, one per line. Many other tools / scripts can ingest this format to add them to your blockitem.

&nbsp;

# The Lists:

| Converted List | License | Domains | Domain List | Last Updated |
:- | - | - | :-: | - |

| [EasyList](https://easylist.to/easylist/easylist.txt) | [GPL3 / CC BY-SA 3.0](https://easylist.to/pages/licence.html) | 17460 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//easylist-justdomains.txt) | 22 Apr 2020 17:00 UTC |

| [EasyPrivacy](https://easylist.to/easylist/easyprivacy.txt) | [GPL3 / CC BY-SA 3.0](https://easylist.to/pages/licence.html) | 6732 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//easyprivacy-justdomains.txt) | 22 Apr 2020 17:00 UTC |

| [EasyList Cookie](https://easylist-downloads.adblockplus.org/easylist-cookie.txt) | [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) | 85 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//easylist-cookie-justdomains.txt) | 22 Apr 2020 17:20 UTC |

| [Fanboy's Social Blocking](https://easylist.to/easylist/fanboy-social.txt) | [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) | 108 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//fanboy-social-justdomains.txt) | 22 Apr 2020 17:00 UTC |

| [Fanboy's Social Blocking](https://easylist.to/easylist/fanboy-annoyance.txt) | [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) | 692 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//fanboy-annoyance-justdomains.txt) | 22 Apr 2020 17:00 UTC |

| [EasyList Germany](https://easylist.to/easylistgermany/easylistgermany.txt) | [GPL3 / CC BY-SA 3.0](https://easylist.to/pages/licence.html) | 564 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//easylistgermany-justdomains.txt) | %timestamp% |

| [EasyList Italy](https://easylist-downloads.adblockplus.org/easylistitaly.txt) | [GPL3 / CC BY-SA 3.0](None) | 194 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//easylistitaly-justdomains.txt) | 22 Apr 2020 17:21 UTC |

| [EasyList Dutch](https://easylist-downloads.adblockplus.org/easylistdutch.txt) | [GPL3 / CC BY-SA 3.0](https://easylist-downloads.adblockplus.org/COPYING) | 79 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//easylistdutch-justdomains.txt) | 22 Apr 2020 17:13 UTC |

| [EasyList Liste FR](https://easylist-downloads.adblockplus.org/liste_fr.txt) | [CC BY-NC-SA 3.0](None) | 4920 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//liste_fr-justdomains.txt) | None |

| [EasyList China](https://easylist-downloads.adblockplus.org/easylistchina.txt) | [GPL3 / CC BY-SA 3.0](https://easylist-downloads.adblockplus.org/COPYING) | 5666 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//easylistchina-justdomains.txt) | 22 Apr 2020 17:13 UTC |

| [EasyList ABPindo](https://raw.githubusercontent.com/heradhis/indonesianadblockrules/master/subscriptions/abpindo.txt) | [GPL3 / CC BY-SA 3.0](https://raw.githubusercontent.com/ABPindo/indonesianadblockrules/master/LICENSE) | 523 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//abpindo-justdomains.txt) | 17 Apr 2020 02:13 UTC |

| [EasyList Liste AR](https://easylist-downloads.adblockplus.org/Liste_AR.txt) | [CC BY-NC-SA 3.0](None) | 73 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//Liste_AR-justdomains.txt) | None |

| [EasyList Czech and Slovak](https://raw.githubusercontent.com/tomasko126/easylistczechandslovak/master/filters.txt) | [CC-BY-SA 4.0](CC-BY-SA v4.0) | 79 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//filters-justdomains.txt) | None |

| [EasyList Latvian List](https://notabug.org/latvian-list/adblock-latvian/raw/master/lists/latvian-list.txt) | [CC-BY-SA 4.0](CC BY-SA 4.0  https://creativecommons.org/licenses/by-sa/4.0/) | 50 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//latvian-list-justdomains.txt) | 2020-01-03 18:30 UTC |

| [EasyList Hebrew](https://raw.githubusercontent.com/easylist/EasyListHebrew/master/EasyListHebrew.txt) | [GPL3 / CC BY-SA 3.0](https://easylist.to/pages/licence.html) | 129 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//EasyListHebrew-justdomains.txt) | 14 Apr 2020 13:37 UTC |

| [EasyList Lithuania](http://margevicius.lt/easylistlithuania.txt) | [GPL3](None) | 15 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//easylistlithuania-justdomains.txt) | None |

| [AdGuard Base Filter](https://filters.adtidy.org/extension/chromium/filters/2.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 20310 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-2-justdomains.txt) | None |

| [AdGuard Tracking Protection filter](https://filters.adtidy.org/extension/chromium/filters/3.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 4861 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-3-justdomains.txt) | None |

| [AdGuard Social media filter](https://filters.adtidy.org/extension/chromium/filters/4.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 47 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-4-justdomains.txt) | None |

| [AdGuard Annoyances filter](https://filters.adtidy.org/extension/chromium/filters/14.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 367 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-14-justdomains.txt) | None |

| [AdGuard Russian filter](https://filters.adtidy.org/extension/chromium/filters/1.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 2548 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-1-justdomains.txt) | None |

| [AdGuard German filter](https://filters.adtidy.org/extension/chromium/filters/6.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 593 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-6-justdomains.txt) | None |

| [AdGuard French filter](https://filters.adtidy.org/extension/chromium/filters/16.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 4907 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-16-justdomains.txt) | None |

| [AdGuard Japanese filter](https://filters.adtidy.org/extension/chromium/filters/7.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 251 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-7-justdomains.txt) | None |

| [AdGuard Dutch filter](https://filters.adtidy.org/extension/chromium/filters/8.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 83 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-8-justdomains.txt) | None |

| [AdGuard Spanish/Portuguese filter](https://filters.adtidy.org/extension/chromium/filters/9.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 189 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-9-justdomains.txt) | None |

| [AdGuard Turkish filter](https://filters.adtidy.org/extension/chromium/filters/13.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 284 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-13-justdomains.txt) | None |

| [AdGuard Mobile ads filter](https://filters.adtidy.org/extension/chromium/filters/11.txt) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 979 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-11-justdomains.txt) | None |

| [AdGuard Simplified Domain Names Filter](https://filters.adtidy.org/extension/chromium/filters/15.txt) | [GPL3](https://github.com/AdguardTeam/AdguardSDNSFilter/blob/master/LICENSE) | 35989 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//adguard-15-justdomains.txt) | 2020-04-22T14:04:58.501Z |

| [NoCoin Filter List](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt) | [MIT](https://mit-license.org/) | 688 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci//nocoin-justdomains.txt) | 18 Mar 2020 |



## EasyList (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [easylist-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylist-justdomains.txt)) |
| Pi-Hole | [easylist-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylist-justdomains.txt)) |

**Source:** [easylist.txt](https://easylist.to/easylist/easylist.txt)
- Title: EasyList
- Version: 202004221700
- Last Modified: 22 Apr 2020 17:00 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed
68198

Comment Lines
434

Empty Lines
0

Non-Domain-only Rules Excluded
48381

Domain-only Rules Excluded (unsupported options)
1859

Domain-only Rules Excluded (exception conflict)
64

Domain-only Rules Output
17460
```


## EasyPrivacy (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [easyprivacy-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easyprivacy-justdomains.txt)) |
| Pi-Hole | [easyprivacy-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easyprivacy-justdomains.txt)) |

**Source:** [easyprivacy.txt](https://easylist.to/easylist/easyprivacy.txt)
- Title: EasyPrivacy
- Version: 202004221700
- Last Modified: 22 Apr 2020 17:00 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed
17284

Comment Lines
223

Empty Lines
0

Non-Domain-only Rules Excluded
10063

Domain-only Rules Excluded (unsupported options)
168

Domain-only Rules Excluded (exception conflict)
98

Domain-only Rules Output
6732
```


## EasyList Cookie (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [easylist-cookie-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylist-cookie-justdomains.txt)) |
| Pi-Hole | [easylist-cookie-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylist-cookie-justdomains.txt)) |

**Source:** [easylist-cookie.txt](https://easylist-downloads.adblockplus.org/easylist-cookie.txt)
- Title: EasyList Cookie
- Version: 202004221720
- Last Modified: 22 Apr 2020 17:20 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed
14792

Comment Lines
250

Empty Lines
0

Non-Domain-only Rules Excluded
14441

Domain-only Rules Excluded (unsupported options)
7

Domain-only Rules Excluded (exception conflict)
9

Domain-only Rules Output
85
```


## Fanboy's Social Blocking (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [fanboy-social-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//fanboy-social-justdomains.txt)) |
| Pi-Hole | [fanboy-social-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//fanboy-social-justdomains.txt)) |

**Source:** [fanboy-social.txt](https://easylist.to/easylist/fanboy-social.txt)
- Title: Fanboy's Social Blocking
- Version: 202004221700
- Last Modified: 22 Apr 2020 17:00 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed
20133

Comment Lines
133

Empty Lines
0

Non-Domain-only Rules Excluded
19872

Domain-only Rules Excluded (unsupported options)
10

Domain-only Rules Excluded (exception conflict)
10

Domain-only Rules Output
108
```


## Fanboy's Social Blocking (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [fanboy-annoyance-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//fanboy-annoyance-justdomains.txt)) |
| Pi-Hole | [fanboy-annoyance-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//fanboy-annoyance-justdomains.txt)) |

**Source:** [fanboy-annoyance.txt](https://easylist.to/easylist/fanboy-annoyance.txt)
- Title: Fanboy's Social Blocking
- Version: 202004221700
- Last Modified: 22 Apr 2020 17:00 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed
45610

Comment Lines
539

Empty Lines
0

Non-Domain-only Rules Excluded
44311

Domain-only Rules Excluded (unsupported options)
37

Domain-only Rules Excluded (exception conflict)
31

Domain-only Rules Output
692
```


## EasyList Germany (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [easylistgermany-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylistgermany-justdomains.txt)) |
| Pi-Hole | [easylistgermany-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylistgermany-justdomains.txt)) |

**Source:** [easylistgermany.txt](https://easylist.to/easylistgermany/easylistgermany.txt)
- Title: EasyList Germany
- Version: 202004212041
- Last Modified: %timestamp%
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed
8327

Comment Lines
42

Empty Lines
0

Non-Domain-only Rules Excluded
7556

Domain-only Rules Excluded (unsupported options)
151

Domain-only Rules Excluded (exception conflict)
14

Domain-only Rules Output
564
```


## EasyList Italy (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [easylistitaly-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylistitaly-justdomains.txt)) |
| Pi-Hole | [easylistitaly-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylistitaly-justdomains.txt)) |

**Source:** [easylistitaly.txt](https://easylist-downloads.adblockplus.org/easylistitaly.txt)
- Title: EasyList Italy
- Version: 202004221721
- Last Modified: 22 Apr 2020 17:21 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed
3728

Comment Lines
38

Empty Lines
0

Non-Domain-only Rules Excluded
3455

Domain-only Rules Excluded (unsupported options)
35

Domain-only Rules Excluded (exception conflict)
6

Domain-only Rules Output
194
```


## EasyList Dutch (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [easylistdutch-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylistdutch-justdomains.txt)) |
| Pi-Hole | [easylistdutch-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylistdutch-justdomains.txt)) |

**Source:** [easylistdutch.txt](https://easylist-downloads.adblockplus.org/easylistdutch.txt)
- Title: EasyList Dutch
- Version: 202004221713
- Last Modified: 22 Apr 2020 17:13 UTC
- Homepage: [https://easylist.adblockplus.org/](https://easylist.adblockplus.org/)

**Conversion Details:**
```
Total Lines Processed
1327

Comment Lines
44

Empty Lines
0

Non-Domain-only Rules Excluded
1192

Domain-only Rules Excluded (unsupported options)
10

Domain-only Rules Excluded (exception conflict)
2

Domain-only Rules Output
79
```


## EasyList Liste FR (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [liste_fr-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//liste_fr-justdomains.txt)) |
| Pi-Hole | [liste_fr-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//liste_fr-justdomains.txt)) |

**Source:** [liste_fr.txt](https://easylist-downloads.adblockplus.org/liste_fr.txt)
- Title: EasyList Liste FR
- Version: 202004221713
- Last Modified: None
- Homepage: [https://forums.lanik.us/viewforum.php?f=91](https://forums.lanik.us/viewforum.php?f=91)

**Conversion Details:**
```
Total Lines Processed
19049

Comment Lines
154

Empty Lines
0

Non-Domain-only Rules Excluded
12537

Domain-only Rules Excluded (unsupported options)
1437

Domain-only Rules Excluded (exception conflict)
1

Domain-only Rules Output
4920
```


## EasyList China (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [easylistchina-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylistchina-justdomains.txt)) |
| Pi-Hole | [easylistchina-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylistchina-justdomains.txt)) |

**Source:** [easylistchina.txt](https://easylist-downloads.adblockplus.org/easylistchina.txt)
- Title: EasyList China
- Version: 202004221713
- Last Modified: 22 Apr 2020 17:13 UTC
- Homepage: [http://abpchina.org/forum/](http://abpchina.org/forum/)

**Conversion Details:**
```
Total Lines Processed
18344

Comment Lines
96

Empty Lines
0

Non-Domain-only Rules Excluded
12333

Domain-only Rules Excluded (unsupported options)
228

Domain-only Rules Excluded (exception conflict)
21

Domain-only Rules Output
5666
```


## EasyList ABPindo (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [abpindo-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//abpindo-justdomains.txt)) |
| Pi-Hole | [abpindo-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//abpindo-justdomains.txt)) |

**Source:** [abpindo.txt](https://raw.githubusercontent.com/heradhis/indonesianadblockrules/master/subscriptions/abpindo.txt)
- Title: EasyList ABPindo
- Version: 202004170213
- Last Modified: 17 Apr 2020 02:13 UTC
- Homepage: [http://abpindo.blogspot.com/](http://abpindo.blogspot.com/)

**Conversion Details:**
```
Total Lines Processed
7678

Comment Lines
31

Empty Lines
0

Non-Domain-only Rules Excluded
6986

Domain-only Rules Excluded (unsupported options)
138

Domain-only Rules Excluded (exception conflict)
0

Domain-only Rules Output
523
```


## EasyList Liste AR (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [Liste_AR-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//Liste_AR-justdomains.txt)) |
| Pi-Hole | [Liste_AR-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//Liste_AR-justdomains.txt)) |

**Source:** [Liste_AR.txt](https://easylist-downloads.adblockplus.org/Liste_AR.txt)
- Title: EasyList Liste AR
- Version: 202004221720
- Last Modified: None
- Homepage: [http://code.google.com/p/liste-ar-adblock/](http://code.google.com/p/liste-ar-adblock/)

**Conversion Details:**
```
Total Lines Processed
2387

Comment Lines
98

Empty Lines
0

Non-Domain-only Rules Excluded
2057

Domain-only Rules Excluded (unsupported options)
159

Domain-only Rules Excluded (exception conflict)
0

Domain-only Rules Output
73
```


## EasyList Czech and Slovak (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [filters-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//filters-justdomains.txt)) |
| Pi-Hole | [filters-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//filters-justdomains.txt)) |

**Source:** [filters.txt](https://raw.githubusercontent.com/tomasko126/easylistczechandslovak/master/filters.txt)
- Title: EasyList Czech and Slovak
- Version: None
- Last Modified: None
- Homepage: [http://adblock.sk](http://adblock.sk)

**Conversion Details:**
```
Total Lines Processed
524

Comment Lines
54

Empty Lines
0

Non-Domain-only Rules Excluded
388

Domain-only Rules Excluded (unsupported options)
1

Domain-only Rules Excluded (exception conflict)
2

Domain-only Rules Output
79
```


## EasyList Latvian List (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [latvian-list-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//latvian-list-justdomains.txt)) |
| Pi-Hole | [latvian-list-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//latvian-list-justdomains.txt)) |

**Source:** [latvian-list.txt](https://notabug.org/latvian-list/adblock-latvian/raw/master/lists/latvian-list.txt)
- Title: EasyList Latvian List
- Version: 202001031830
- Last Modified: 2020-01-03 18:30 UTC
- Homepage: [https://notabug.org/latvian-list/adblock-latvian](https://notabug.org/latvian-list/adblock-latvian)

**Conversion Details:**
```
Total Lines Processed
416

Comment Lines
39

Empty Lines
0

Non-Domain-only Rules Excluded
320

Domain-only Rules Excluded (unsupported options)
5

Domain-only Rules Excluded (exception conflict)
2

Domain-only Rules Output
50
```


## EasyList Hebrew (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [EasyListHebrew-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//EasyListHebrew-justdomains.txt)) |
| Pi-Hole | [EasyListHebrew-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//EasyListHebrew-justdomains.txt)) |

**Source:** [EasyListHebrew.txt](https://raw.githubusercontent.com/easylist/EasyListHebrew/master/EasyListHebrew.txt)
- Title: EasyList Hebrew
- Version: None
- Last Modified: 14 Apr 2020 13:37 UTC
- Homepage: [https://github.com/easylist/EasyListHebrew](https://github.com/easylist/EasyListHebrew)

**Conversion Details:**
```
Total Lines Processed
1438

Comment Lines
155

Empty Lines
0

Non-Domain-only Rules Excluded
942

Domain-only Rules Excluded (unsupported options)
212

Domain-only Rules Excluded (exception conflict)
0

Domain-only Rules Output
129
```


## EasyList Lithuania (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [easylistlithuania-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylistlithuania-justdomains.txt)) |
| Pi-Hole | [easylistlithuania-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//easylistlithuania-justdomains.txt)) |

**Source:** [easylistlithuania.txt](http://margevicius.lt/easylistlithuania.txt)
- Title: EasyList Lithuania
- Version: None
- Last Modified: None
- Homepage: [https://github.com/EasyList-Lithuania/easylist_lithuania/blob/master/easylistlithuania.txt](https://github.com/EasyList-Lithuania/easylist_lithuania/blob/master/easylistlithuania.txt)

**Conversion Details:**
```
Total Lines Processed
1420

Comment Lines
9

Empty Lines
1

Non-Domain-only Rules Excluded
1396

Domain-only Rules Excluded (unsupported options)
0

Domain-only Rules Excluded (exception conflict)
0

Domain-only Rules Output
15
```


## AdGuard Base Filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-2-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-2-justdomains.txt)) |
| Pi-Hole | [adguard-2-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-2-justdomains.txt)) |

**Source:** [2.txt](https://filters.adtidy.org/extension/chromium/filters/2.txt)
- Title: AdGuard Base Filter
- Version: 2.1.16.0
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#english](http://adguard.com/filters.html#english)

**Conversion Details:**
```
Total Lines Processed
103925

Comment Lines
9727

Empty Lines
0

Non-Domain-only Rules Excluded
71434

Domain-only Rules Excluded (unsupported options)
2236

Domain-only Rules Excluded (exception conflict)
218

Domain-only Rules Output
20310
```


## AdGuard Tracking Protection filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-3-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-3-justdomains.txt)) |
| Pi-Hole | [adguard-3-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-3-justdomains.txt)) |

**Source:** [3.txt](https://filters.adtidy.org/extension/chromium/filters/3.txt)
- Title: AdGuard Tracking Protection filter
- Version: 2.0.13.53
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#privacy](http://adguard.com/filters.html#privacy)

**Conversion Details:**
```
Total Lines Processed
9634

Comment Lines
1039

Empty Lines
0

Non-Domain-only Rules Excluded
3478

Domain-only Rules Excluded (unsupported options)
58

Domain-only Rules Excluded (exception conflict)
198

Domain-only Rules Output
4861
```


## AdGuard Social media filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-4-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-4-justdomains.txt)) |
| Pi-Hole | [adguard-4-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-4-justdomains.txt)) |

**Source:** [4.txt](https://filters.adtidy.org/extension/chromium/filters/4.txt)
- Title: AdGuard Social media filter
- Version: 2.0.24.46
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#social](http://adguard.com/filters.html#social)

**Conversion Details:**
```
Total Lines Processed
7634

Comment Lines
454

Empty Lines
0

Non-Domain-only Rules Excluded
7124

Domain-only Rules Excluded (unsupported options)
4

Domain-only Rules Excluded (exception conflict)
5

Domain-only Rules Output
47
```


## AdGuard Annoyances filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-14-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-14-justdomains.txt)) |
| Pi-Hole | [adguard-14-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-14-justdomains.txt)) |

**Source:** [14.txt](https://filters.adtidy.org/extension/chromium/filters/14.txt)
- Title: AdGuard Annoyances filter
- Version: 2.0.46.50
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#annoyances](http://adguard.com/filters.html#annoyances)

**Conversion Details:**
```
Total Lines Processed
17235

Comment Lines
2274

Empty Lines
0

Non-Domain-only Rules Excluded
14526

Domain-only Rules Excluded (unsupported options)
55

Domain-only Rules Excluded (exception conflict)
13

Domain-only Rules Output
367
```


## AdGuard Russian filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-1-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-1-justdomains.txt)) |
| Pi-Hole | [adguard-1-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-1-justdomains.txt)) |

**Source:** [1.txt](https://filters.adtidy.org/extension/chromium/filters/1.txt)
- Title: AdGuard Russian filter
- Version: 2.0.33.40
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#russian](http://adguard.com/filters.html#russian)

**Conversion Details:**
```
Total Lines Processed
20792

Comment Lines
2733

Empty Lines
0

Non-Domain-only Rules Excluded
13976

Domain-only Rules Excluded (unsupported options)
223

Domain-only Rules Excluded (exception conflict)
1312

Domain-only Rules Output
2548
```


## AdGuard German filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-6-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-6-justdomains.txt)) |
| Pi-Hole | [adguard-6-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-6-justdomains.txt)) |

**Source:** [6.txt](https://filters.adtidy.org/extension/chromium/filters/6.txt)
- Title: AdGuard German filter
- Version: 2.0.11.6
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#german](http://adguard.com/filters.html#german)

**Conversion Details:**
```
Total Lines Processed
12168

Comment Lines
970

Empty Lines
0

Non-Domain-only Rules Excluded
10415

Domain-only Rules Excluded (unsupported options)
173

Domain-only Rules Excluded (exception conflict)
17

Domain-only Rules Output
593
```


## AdGuard French filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-16-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-16-justdomains.txt)) |
| Pi-Hole | [adguard-16-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-16-justdomains.txt)) |

**Source:** [16.txt](https://filters.adtidy.org/extension/chromium/filters/16.txt)
- Title: AdGuard French filter
- Version: 2.0.21.71
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#french](http://adguard.com/filters.html#french)

**Conversion Details:**
```
Total Lines Processed
19933

Comment Lines
492

Empty Lines
0

Non-Domain-only Rules Excluded
13079

Domain-only Rules Excluded (unsupported options)
1439

Domain-only Rules Excluded (exception conflict)
16

Domain-only Rules Output
4907
```


## AdGuard Japanese filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-7-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-7-justdomains.txt)) |
| Pi-Hole | [adguard-7-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-7-justdomains.txt)) |

**Source:** [7.txt](https://filters.adtidy.org/extension/chromium/filters/7.txt)
- Title: AdGuard Japanese filter
- Version: 2.0.2.96
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#japanese](http://adguard.com/filters.html#japanese)

**Conversion Details:**
```
Total Lines Processed
1514

Comment Lines
264

Empty Lines
0

Non-Domain-only Rules Excluded
975

Domain-only Rules Excluded (unsupported options)
13

Domain-only Rules Excluded (exception conflict)
11

Domain-only Rules Output
251
```


## AdGuard Dutch filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-8-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-8-justdomains.txt)) |
| Pi-Hole | [adguard-8-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-8-justdomains.txt)) |

**Source:** [8.txt](https://filters.adtidy.org/extension/chromium/filters/8.txt)
- Title: AdGuard Dutch filter
- Version: 2.0.0.79
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#dutch](http://adguard.com/filters.html#dutch)

**Conversion Details:**
```
Total Lines Processed
1631

Comment Lines
171

Empty Lines
0

Non-Domain-only Rules Excluded
1363

Domain-only Rules Excluded (unsupported options)
12

Domain-only Rules Excluded (exception conflict)
2

Domain-only Rules Output
83
```


## AdGuard Spanish/Portuguese filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-9-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-9-justdomains.txt)) |
| Pi-Hole | [adguard-9-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-9-justdomains.txt)) |

**Source:** [9.txt](https://filters.adtidy.org/extension/chromium/filters/9.txt)
- Title: AdGuard Spanish/Portuguese filter
- Version: 2.0.6.11
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#spanish](http://adguard.com/filters.html#spanish)

**Conversion Details:**
```
Total Lines Processed
3266

Comment Lines
592

Empty Lines
0

Non-Domain-only Rules Excluded
2456

Domain-only Rules Excluded (unsupported options)
28

Domain-only Rules Excluded (exception conflict)
1

Domain-only Rules Output
189
```


## AdGuard Turkish filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-13-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-13-justdomains.txt)) |
| Pi-Hole | [adguard-13-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-13-justdomains.txt)) |

**Source:** [13.txt](https://filters.adtidy.org/extension/chromium/filters/13.txt)
- Title: AdGuard Turkish filter
- Version: 2.0.15.75
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#turkish](http://adguard.com/filters.html#turkish)

**Conversion Details:**
```
Total Lines Processed
6023

Comment Lines
607

Empty Lines
0

Non-Domain-only Rules Excluded
5090

Domain-only Rules Excluded (unsupported options)
39

Domain-only Rules Excluded (exception conflict)
3

Domain-only Rules Output
284
```


## AdGuard Mobile ads filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-11-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-11-justdomains.txt)) |
| Pi-Hole | [adguard-11-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-11-justdomains.txt)) |

**Source:** [11.txt](https://filters.adtidy.org/extension/chromium/filters/11.txt)
- Title: AdGuard Mobile ads filter
- Version: 2.0.12.17
- Last Modified: None
- Homepage: [http://adguard.com/filters.html#mobile](http://adguard.com/filters.html#mobile)

**Conversion Details:**
```
Total Lines Processed
3744

Comment Lines
767

Empty Lines
0

Non-Domain-only Rules Excluded
1963

Domain-only Rules Excluded (unsupported options)
20

Domain-only Rules Excluded (exception conflict)
15

Domain-only Rules Output
979
```


## AdGuard Simplified Domain Names Filter (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [adguard-15-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-15-justdomains.txt)) |
| Pi-Hole | [adguard-15-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//adguard-15-justdomains.txt)) |

**Source:** [15.txt](https://filters.adtidy.org/extension/chromium/filters/15.txt)
- Title: AdGuard Simplified Domain Names Filter
- Version: 2.0.9.40
- Last Modified: 2020-04-22T14:04:58.501Z
- Homepage: [https://github.com/AdguardTeam/AdguardSDNSFilter](https://github.com/AdguardTeam/AdguardSDNSFilter)

**Conversion Details:**
```
Total Lines Processed
36985

Comment Lines
409

Empty Lines
0

Non-Domain-only Rules Excluded
558

Domain-only Rules Excluded (unsupported options)
5

Domain-only Rules Excluded (exception conflict)
24

Domain-only Rules Output
35989
```


## NoCoin Filter List (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [nocoin-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//nocoin-justdomains.txt)) |
| Pi-Hole | [nocoin-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci//nocoin-justdomains.txt)) |

**Source:** [hosts.txt](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt)
- Title: NoCoin Filter List
- Version: None
- Last Modified: 18 Mar 2020
- Homepage: [https://github.com/hoshsadiq/adblock-nocoin-list/](https://github.com/hoshsadiq/adblock-nocoin-list/)

**Conversion Details:**
```
Total Lines Processed
705

Comment Lines
10

Empty Lines
1

Invalid Lines
0

Non-Loopback Lines (Ignored)
0

Local Hosts (Ignored)
0

Invalid Hosts (Ignored)
0

Duplicate Hosts (Ignored)
6

Hosts Output
688
```



# License:
Each converted / modified list file is licensed under the same license as the original item.

For more details, see the [LICENSES](LICENSES) file.

&nbsp;

# Reporting Conversion Issues:
If you find an issue in the output of the conversion process (i.e. comparing to the original upstream list), please report it over on: https://github.com/justdomains/ci/issues

**NOTE: We do not manage the upstream lists themselves, and will not be able to add any new blocks to the lists.**

&nbsp;

<sup>These files are provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, arising from, out of or in connection with the files or the use of the files.</sup>

<sub>Any and all trademarks are the property of their respective owners.</sub>
