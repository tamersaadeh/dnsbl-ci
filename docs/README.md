# DOMAIN-ONLY Filter Lists
**Last Updated:** 2020-04-21 17:54:46

- [Details](#details)
- [Usage](#usage)
  - [Using with Pi-Hole](#using-with-pi-hole)
  - [Using with other tools](#using-with-other-tools)
- [The Lists](#the-lists)
  - [EasyList](#easylist-domains-only) (Domains-only)
  - [EasyPrivacy](#easyprivacy-domains-only) (Domains-only)
  - [EasyList Cookie](#easylist-cookie-domains-only) (Domains-only)
  - [Fanboy's Social Blocking](#fanboys-social-blocking-domains-only) (Domains-only)
  - [Fanboy's Social Blocking](#fanboys-social-blocking-domains-only) (Domains-only)
  - [EasyList Germany](#easylist-germany-domains-only) (Domains-only)
  - [EasyList Italy](#easylist-italy-domains-only) (Domains-only)
  - [EasyList Dutch](#easylist-dutch-domains-only) (Domains-only)
  - [EasyList Liste FR](#easylist-liste-fr-domains-only) (Domains-only)
  - [EasyList China](#easylist-china-domains-only) (Domains-only)
  - [EasyList ABPindo](#easylist-abpindo-domains-only) (Domains-only)
  - [EasyList Liste AR](#easylist-liste-ar-domains-only) (Domains-only)
  - [EasyList Czech and Slovak](#easylist-czech-and-slovak-domains-only) (Domains-only)
  - [EasyList Latvian List](#easylist-latvian-list-domains-only) (Domains-only)
  - [EasyList Hebrew](#easylist-hebrew-domains-only) (Domains-only)
  - [EasyList Lithuania](#easylist-lithuania-domains-only) (Domains-only)
  - [AdGuard Base Filter](#adguard-base-filter-domains-only) (Domains-only)
  - [AdGuard Tracking Protection filter](#adguard-tracking-protection-filter-domains-only) (Domains-only)
  - [AdGuard Social media filter](#adguard-social-media-filter-domains-only) (Domains-only)
  - [AdGuard Annoyances filter](#adguard-annoyances-filter-domains-only) (Domains-only)
  - [AdGuard Russian filter](#adguard-russian-filter-domains-only) (Domains-only)
  - [AdGuard German filter](#adguard-german-filter-domains-only) (Domains-only)
  - [AdGuard French filter](#adguard-french-filter-domains-only) (Domains-only)
  - [AdGuard Japanese filter](#adguard-japanese-filter-domains-only) (Domains-only)
  - [AdGuard Dutch filter](#adguard-dutch-filter-domains-only) (Domains-only)
  - [AdGuard Spanish/Portuguese filter](#adguard-spanishportuguese-filter-domains-only) (Domains-only)
  - [AdGuard Turkish filter](#adguard-turkish-filter-domains-only) (Domains-only)
  - [AdGuard Mobile ads filter](#adguard-mobile-ads-filter-domains-only) (Domains-only)
  - [AdGuard Simplified Domain Names Filter](#adguard-simplified-domain-names-filter-domains-only) (Domains-only)
  - [NoCoin Filter List](#nocoin-filter-list-domains-only) (Domains-only)
- [License](#license)
- [Reporting Conversion Issues](#reporting-conversion-issues)

&nbsp;

# Details:
These are "DOMAIN-ONLY" **converted** versions of various popular original filter / blocking lists.
They have been modified from their original versions by scripts at: https://github.com/justdomains/ci

The scripts output **only** the full-domain-blocking entries from the original lists, while attempting to filter any domains that conflict with an exception rule on the original list.

**Because these are automated, converted _subsets_ of the original lists, please do not report omissions from these converted files to the list originator.**

&nbsp;

# Usage:
These converted files can be used with various DNS and domain-blocking tools:

## Using with [Pi-Hole](https://pi-hole.net/):
1. Copy the link to the Pi-Hole format for the desired list (from the appropriate table below).
2. [Add the URL to your Pi-Hole's block lists (**Settings** > **Pi-Hole's Block Lists**).](https://github.com/pi-hole/pi-hole/wiki/Customising-Sources-for-Ad-Lists)

## Using with other tools:
The converted lists are provided in a "Raw Domain List" format that contains only domains, one per line. Many other tools / scripts can ingest this format to add them to your blocklist.

&nbsp;

# The Lists:

| Converted List | License | Domains | Domain List | Last Updated |
:- | - | - | :-: | - |
| [EasyList](#easylist-domains-only) | [GPL3 / CC BY-SA 3.0](https://easylist.to/pages/licence.html) | 17450 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/easylist-justdomains.txt) | 21 Apr 2020 16:44 UTC |
| [EasyPrivacy](#easyprivacy-domains-only) | [GPL3 / CC BY-SA 3.0](https://easylist.to/pages/licence.html) | 6732 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/easyprivacy-justdomains.txt) | 21 Apr 2020 16:44 UTC |
| [EasyList Cookie](#easylist-cookie-domains-only) | [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) | 85 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/easylist-cookie-justdomains.txt) | 21 Apr 2020 17:50 UTC |
| [Fanboy's Social Blocking](#fanboys-social-blocking-domains-only) | [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) | 108 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/fanboy-social-justdomains.txt) | 21 Apr 2020 16:44 UTC |
| [Fanboy's Social Blocking](#fanboys-social-blocking-domains-only) | [CC BY 3.0](http://creativecommons.org/licenses/by/3.0/) | 692 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/fanboy-annoyance-justdomains.txt) | 21 Apr 2020 16:44 UTC |
| [EasyList Germany](#easylist-germany-domains-only) | [GPL3 / CC BY-SA 3.0](https://easylist.to/pages/licence.html) | 564 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistgermany-justdomains.txt) | %timestamp% |
| [EasyList Italy](#easylist-italy-domains-only) | GPL3 / CC BY-SA 3.0 | 194 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistitaly-justdomains.txt) | 21 Apr 2020 17:51 UTC |
| [EasyList Dutch](#easylist-dutch-domains-only) | [GPL3 / CC BY-SA 3.0](https://easylist-downloads.adblockplus.org/COPYING) | 79 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistdutch-justdomains.txt) | 21 Apr 2020 17:43 UTC |
| [EasyList Liste FR](#easylist-liste-fr-domains-only) | CC BY-NC-SA 3.0 | 4920 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/liste_fr-justdomains.txt) |  |
| [EasyList China](#easylist-china-domains-only) | [GPL3 / CC BY-SA 3.0](https://easylist-downloads.adblockplus.org/COPYING) | 5656 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistchina-justdomains.txt) | 21 Apr 2020 17:43 UTC |
| [EasyList ABPindo](#easylist-abpindo-domains-only) | [GPL3 / CC BY-SA 3.0](https://raw.githubusercontent.com/ABPindo/indonesianadblockrules/master/LICENSE) | 523 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/abpindo-justdomains.txt) | 17 Apr 2020 02:13 UTC |
| [EasyList Liste AR](#easylist-liste-ar-domains-only) | CC BY-NC-SA 3.0 | 73 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/Liste_AR-justdomains.txt) |  |
| [EasyList Czech and Slovak](#easylist-czech-and-slovak-domains-only) | [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | 79 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/filters-justdomains.txt) |  |
| [EasyList Latvian List](#easylist-latvian-list-domains-only) | [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) | 50 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/latvian-list-justdomains.txt) | 2020-01-03 18:30 UTC |
| [EasyList Hebrew](#easylist-hebrew-domains-only) | [GPL3 / CC BY-SA 3.0](https://easylist.to/pages/licence.html) | 129 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/EasyListHebrew-justdomains.txt) | 14 Apr 2020 13:37 UTC |
| [EasyList Lithuania](#easylist-lithuania-domains-only) | [GPL3](http://www.gnu.org/licenses/gpl-3.0.txt) | 15 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistlithuania-justdomains.txt) |  |
| [AdGuard Base Filter](#adguard-base-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 20295 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-2-justdomains.txt) |  |
| [AdGuard Tracking Protection filter](#adguard-tracking-protection-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 4860 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-3-justdomains.txt) |  |
| [AdGuard Social media filter](#adguard-social-media-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 47 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-4-justdomains.txt) |  |
| [AdGuard Annoyances filter](#adguard-annoyances-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 367 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-14-justdomains.txt) |  |
| [AdGuard Russian filter](#adguard-russian-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 2545 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-1-justdomains.txt) |  |
| [AdGuard German filter](#adguard-german-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 593 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-6-justdomains.txt) |  |
| [AdGuard French filter](#adguard-french-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 4907 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-16-justdomains.txt) |  |
| [AdGuard Japanese filter](#adguard-japanese-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 251 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-7-justdomains.txt) |  |
| [AdGuard Dutch filter](#adguard-dutch-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 83 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-8-justdomains.txt) |  |
| [AdGuard Spanish/Portuguese filter](#adguard-spanishportuguese-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 189 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-9-justdomains.txt) |  |
| [AdGuard Turkish filter](#adguard-turkish-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 284 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-13-justdomains.txt) |  |
| [AdGuard Mobile ads filter](#adguard-mobile-ads-filter-domains-only) | [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/) | 979 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-11-justdomains.txt) |  |
| [AdGuard Simplified Domain Names Filter](#adguard-simplified-domain-names-filter-domains-only) | [GPL3](https://github.com/AdguardTeam/AdguardSDNSFilter/blob/master/LICENSE) | 35959 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-15-justdomains.txt) | 2020-04-21T14:04:07.997Z |
| [NoCoin Filter List](#nocoin-filter-list-domains-only) | [MIT](https://github.com/hoshsadiq/adblock-nocoin-list/blob/master/LICENSE) | 688 | [**Download**](https://tamersaadeh.github.io/dnsbl-ci/lists/nocoin-justdomains.txt) | 18 Mar 2020 |

&nbsp;

## EasyList (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [easylist-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylist-justdomains.txt) |
| Pi-Hole | [easylist-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylist-justdomains.txt) |

**Source:** [https://easylist.to/easylist/easylist.txt](https://easylist.to/easylist/easylist.txt)
- Title: EasyList
- Version: 202004211644
- Last Modified: 21 Apr 2020 16:44 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed: 68185
Comment Lines: 434
Empty Lines: 0
Non-Domain-only Rules Excluded: 48376
Domain-only Rules Excluded (unsupported options): 1861
Domain-only Rules Excluded (exception conflict): 64
Domain-only Rules Output: 17450
```

&nbsp;

## EasyPrivacy (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [easyprivacy-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easyprivacy-justdomains.txt) |
| Pi-Hole | [easyprivacy-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easyprivacy-justdomains.txt) |

**Source:** [https://easylist.to/easylist/easyprivacy.txt](https://easylist.to/easylist/easyprivacy.txt)
- Title: EasyPrivacy
- Version: 202004211644
- Last Modified: 21 Apr 2020 16:44 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed: 17276
Comment Lines: 223
Empty Lines: 0
Non-Domain-only Rules Excluded: 10056
Domain-only Rules Excluded (unsupported options): 168
Domain-only Rules Excluded (exception conflict): 97
Domain-only Rules Output: 6732
```

&nbsp;

## EasyList Cookie (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [easylist-cookie-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylist-cookie-justdomains.txt) |
| Pi-Hole | [easylist-cookie-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylist-cookie-justdomains.txt) |

**Source:** [https://easylist-downloads.adblockplus.org/easylist-cookie.txt](https://easylist-downloads.adblockplus.org/easylist-cookie.txt)
- Title: EasyList Cookie List
- Version: 202004211750
- Last Modified: 21 Apr 2020 17:50 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed: 14791
Comment Lines: 250
Empty Lines: 0
Non-Domain-only Rules Excluded: 14440
Domain-only Rules Excluded (unsupported options): 7
Domain-only Rules Excluded (exception conflict): 9
Domain-only Rules Output: 85
```

&nbsp;

## Fanboy's Social Blocking (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [fanboy-social-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/fanboy-social-justdomains.txt) |
| Pi-Hole | [fanboy-social-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/fanboy-social-justdomains.txt) |

**Source:** [https://easylist.to/easylist/fanboy-social.txt](https://easylist.to/easylist/fanboy-social.txt)
- Title: Fanboy's Social Blocking List
- Version: 202004211644
- Last Modified: 21 Apr 2020 16:44 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed: 20128
Comment Lines: 133
Empty Lines: 0
Non-Domain-only Rules Excluded: 19867
Domain-only Rules Excluded (unsupported options): 10
Domain-only Rules Excluded (exception conflict): 10
Domain-only Rules Output: 108
```

&nbsp;

## Fanboy's Social Blocking (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [fanboy-annoyance-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/fanboy-annoyance-justdomains.txt) |
| Pi-Hole | [fanboy-annoyance-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/fanboy-annoyance-justdomains.txt) |

**Source:** [https://easylist.to/easylist/fanboy-annoyance.txt](https://easylist.to/easylist/fanboy-annoyance.txt)
- Title: Fanboy's Annoyance List
- Version: 202004211644
- Last Modified: 21 Apr 2020 16:44 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed: 45604
Comment Lines: 539
Empty Lines: 0
Non-Domain-only Rules Excluded: 44305
Domain-only Rules Excluded (unsupported options): 37
Domain-only Rules Excluded (exception conflict): 31
Domain-only Rules Output: 692
```

&nbsp;

## EasyList Germany (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [easylistgermany-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistgermany-justdomains.txt) |
| Pi-Hole | [easylistgermany-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistgermany-justdomains.txt) |

**Source:** [https://easylist.to/easylistgermany/easylistgermany.txt](https://easylist.to/easylistgermany/easylistgermany.txt)
- Title: EasyList Germany
- Version: 202004181114
- Last Modified: %timestamp%
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed: 8306
Comment Lines: 42
Empty Lines: 0
Non-Domain-only Rules Excluded: 7535
Domain-only Rules Excluded (unsupported options): 151
Domain-only Rules Excluded (exception conflict): 14
Domain-only Rules Output: 564
```

&nbsp;

## EasyList Italy (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [easylistitaly-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistitaly-justdomains.txt) |
| Pi-Hole | [easylistitaly-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistitaly-justdomains.txt) |

**Source:** [https://easylist-downloads.adblockplus.org/easylistitaly.txt](https://easylist-downloads.adblockplus.org/easylistitaly.txt)
- Title: EasyList Italy
- Version: 202004211751
- Last Modified: 21 Apr 2020 17:51 UTC
- Homepage: [https://easylist.to/](https://easylist.to/)

**Conversion Details:**
```
Total Lines Processed: 3728
Comment Lines: 38
Empty Lines: 0
Non-Domain-only Rules Excluded: 3455
Domain-only Rules Excluded (unsupported options): 35
Domain-only Rules Excluded (exception conflict): 6
Domain-only Rules Output: 194
```

&nbsp;

## EasyList Dutch (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [easylistdutch-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistdutch-justdomains.txt) |
| Pi-Hole | [easylistdutch-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistdutch-justdomains.txt) |

**Source:** [https://easylist-downloads.adblockplus.org/easylistdutch.txt](https://easylist-downloads.adblockplus.org/easylistdutch.txt)
- Title: EasyList Dutch
- Version: 202004211743
- Last Modified: 21 Apr 2020 17:43 UTC
- Homepage: [https://easylist.adblockplus.org/](https://easylist.adblockplus.org/)

**Conversion Details:**
```
Total Lines Processed: 1327
Comment Lines: 44
Empty Lines: 0
Non-Domain-only Rules Excluded: 1192
Domain-only Rules Excluded (unsupported options): 10
Domain-only Rules Excluded (exception conflict): 2
Domain-only Rules Output: 79
```

&nbsp;

## EasyList Liste FR (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [liste_fr-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/liste_fr-justdomains.txt) |
| Pi-Hole | [liste_fr-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/liste_fr-justdomains.txt) |

**Source:** [https://easylist-downloads.adblockplus.org/liste_fr.txt](https://easylist-downloads.adblockplus.org/liste_fr.txt)
- Title: Liste FR
- Version: 202004211743
- Homepage: [https://forums.lanik.us/viewforum.php?f=91](https://forums.lanik.us/viewforum.php?f=91)

**Conversion Details:**
```
Total Lines Processed: 19049
Comment Lines: 154
Empty Lines: 0
Non-Domain-only Rules Excluded: 12537
Domain-only Rules Excluded (unsupported options): 1437
Domain-only Rules Excluded (exception conflict): 1
Domain-only Rules Output: 4920
```

&nbsp;

## EasyList China (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [easylistchina-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistchina-justdomains.txt) |
| Pi-Hole | [easylistchina-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistchina-justdomains.txt) |

**Source:** [https://easylist-downloads.adblockplus.org/easylistchina.txt](https://easylist-downloads.adblockplus.org/easylistchina.txt)
- Title: EasyList China
- Version: 202004211743
- Last Modified: 21 Apr 2020 17:43 UTC
- Homepage: [http://abpchina.org/forum/](http://abpchina.org/forum/)

**Conversion Details:**
```
Total Lines Processed: 18333
Comment Lines: 96
Empty Lines: 0
Non-Domain-only Rules Excluded: 12332
Domain-only Rules Excluded (unsupported options): 228
Domain-only Rules Excluded (exception conflict): 21
Domain-only Rules Output: 5656
```

&nbsp;

## EasyList ABPindo (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [abpindo-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/abpindo-justdomains.txt) |
| Pi-Hole | [abpindo-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/abpindo-justdomains.txt) |

**Source:** [https://raw.githubusercontent.com/heradhis/indonesianadblockrules/master/subscriptions/abpindo.txt](https://raw.githubusercontent.com/heradhis/indonesianadblockrules/master/subscriptions/abpindo.txt)
- Title: ABPindo
- Version: 202004170213
- Last Modified: 17 Apr 2020 02:13 UTC
- Homepage: [http://abpindo.blogspot.com/](http://abpindo.blogspot.com/)

**Conversion Details:**
```
Total Lines Processed: 7678
Comment Lines: 31
Empty Lines: 0
Non-Domain-only Rules Excluded: 6986
Domain-only Rules Excluded (unsupported options): 138
Domain-only Rules Excluded (exception conflict): 0
Domain-only Rules Output: 523
```

&nbsp;

## EasyList Liste AR (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [Liste_AR-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/Liste_AR-justdomains.txt) |
| Pi-Hole | [Liste_AR-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/Liste_AR-justdomains.txt) |

**Source:** [https://easylist-downloads.adblockplus.org/Liste_AR.txt](https://easylist-downloads.adblockplus.org/Liste_AR.txt)
- Title: Liste AR
- Version: 202004211750
- Homepage: [http://code.google.com/p/liste-ar-adblock/](http://code.google.com/p/liste-ar-adblock/)

**Conversion Details:**
```
Total Lines Processed: 2387
Comment Lines: 98
Empty Lines: 0
Non-Domain-only Rules Excluded: 2057
Domain-only Rules Excluded (unsupported options): 159
Domain-only Rules Excluded (exception conflict): 0
Domain-only Rules Output: 73
```

&nbsp;

## EasyList Czech and Slovak (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [filters-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/filters-justdomains.txt) |
| Pi-Hole | [filters-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/filters-justdomains.txt) |

**Source:** [https://raw.githubusercontent.com/tomasko126/easylistczechandslovak/master/filters.txt](https://raw.githubusercontent.com/tomasko126/easylistczechandslovak/master/filters.txt)
- Title: Easylist Czech and Slovak filter list
- Homepage: [http://adblock.sk](http://adblock.sk)

**Conversion Details:**
```
Total Lines Processed: 524
Comment Lines: 54
Empty Lines: 0
Non-Domain-only Rules Excluded: 388
Domain-only Rules Excluded (unsupported options): 1
Domain-only Rules Excluded (exception conflict): 2
Domain-only Rules Output: 79
```

&nbsp;

## EasyList Latvian List (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [latvian-list-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/latvian-list-justdomains.txt) |
| Pi-Hole | [latvian-list-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/latvian-list-justdomains.txt) |

**Source:** [https://notabug.org/latvian-list/adblock-latvian/raw/master/lists/latvian-list.txt](https://notabug.org/latvian-list/adblock-latvian/raw/master/lists/latvian-list.txt)
- Title: Latvian List
- Version: 202001031830
- Last Modified: 2020-01-03 18:30 UTC
- Homepage: [https://notabug.org/latvian-list/adblock-latvian](https://notabug.org/latvian-list/adblock-latvian)

**Conversion Details:**
```
Total Lines Processed: 416
Comment Lines: 39
Empty Lines: 0
Non-Domain-only Rules Excluded: 320
Domain-only Rules Excluded (unsupported options): 5
Domain-only Rules Excluded (exception conflict): 2
Domain-only Rules Output: 50
```

&nbsp;

## EasyList Hebrew (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [EasyListHebrew-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/EasyListHebrew-justdomains.txt) |
| Pi-Hole | [EasyListHebrew-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/EasyListHebrew-justdomains.txt) |

**Source:** [https://raw.githubusercontent.com/easylist/EasyListHebrew/master/EasyListHebrew.txt](https://raw.githubusercontent.com/easylist/EasyListHebrew/master/EasyListHebrew.txt)
- Title: EasyList Hebrew
- Last Modified: 14 Apr 2020 13:37 UTC
- Homepage: [https://github.com/easylist/EasyListHebrew](https://github.com/easylist/EasyListHebrew)

**Conversion Details:**
```
Total Lines Processed: 1438
Comment Lines: 155
Empty Lines: 0
Non-Domain-only Rules Excluded: 942
Domain-only Rules Excluded (unsupported options): 212
Domain-only Rules Excluded (exception conflict): 0
Domain-only Rules Output: 129
```

&nbsp;

## EasyList Lithuania (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [easylistlithuania-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistlithuania-justdomains.txt) |
| Pi-Hole | [easylistlithuania-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/easylistlithuania-justdomains.txt) |

**Source:** [http://margevicius.lt/easylistlithuania.txt](http://margevicius.lt/easylistlithuania.txt)
- Title: EasyList Lithuania
- Homepage: [https://github.com/EasyList-Lithuania/easylist_lithuania/blob/master/easylistlithuania.txt](https://github.com/EasyList-Lithuania/easylist_lithuania/blob/master/easylistlithuania.txt)

**Conversion Details:**
```
Total Lines Processed: 1420
Comment Lines: 9
Empty Lines: 1
Non-Domain-only Rules Excluded: 1396
Domain-only Rules Excluded (unsupported options): 0
Domain-only Rules Excluded (exception conflict): 0
Domain-only Rules Output: 15
```

&nbsp;

## AdGuard Base Filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-2-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-2-justdomains.txt) |
| Pi-Hole | [adguard-2-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-2-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/2.txt](https://filters.adtidy.org/extension/chromium/filters/2.txt)
- Title: AdGuard Base filter
- Version: 2.1.15.78
- Homepage: [http://adguard.com/filters.html#english](http://adguard.com/filters.html#english)

**Conversion Details:**
```
Total Lines Processed: 103870
Comment Lines: 9717
Empty Lines: 0
Non-Domain-only Rules Excluded: 71404
Domain-only Rules Excluded (unsupported options): 2236
Domain-only Rules Excluded (exception conflict): 218
Domain-only Rules Output: 20295
```

&nbsp;

## AdGuard Tracking Protection filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-3-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-3-justdomains.txt) |
| Pi-Hole | [adguard-3-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-3-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/3.txt](https://filters.adtidy.org/extension/chromium/filters/3.txt)
- Title: AdGuard Tracking Protection filter
- Version: 2.0.13.48
- Homepage: [http://adguard.com/filters.html#privacy](http://adguard.com/filters.html#privacy)

**Conversion Details:**
```
Total Lines Processed: 9626
Comment Lines: 1037
Empty Lines: 0
Non-Domain-only Rules Excluded: 3473
Domain-only Rules Excluded (unsupported options): 58
Domain-only Rules Excluded (exception conflict): 198
Domain-only Rules Output: 4860
```

&nbsp;

## AdGuard Social media filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-4-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-4-justdomains.txt) |
| Pi-Hole | [adguard-4-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-4-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/4.txt](https://filters.adtidy.org/extension/chromium/filters/4.txt)
- Title: AdGuard Social Media filter
- Version: 2.0.24.45
- Homepage: [http://adguard.com/filters.html#social](http://adguard.com/filters.html#social)

**Conversion Details:**
```
Total Lines Processed: 7636
Comment Lines: 454
Empty Lines: 0
Non-Domain-only Rules Excluded: 7126
Domain-only Rules Excluded (unsupported options): 4
Domain-only Rules Excluded (exception conflict): 5
Domain-only Rules Output: 47
```

&nbsp;

## AdGuard Annoyances filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-14-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-14-justdomains.txt) |
| Pi-Hole | [adguard-14-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-14-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/14.txt](https://filters.adtidy.org/extension/chromium/filters/14.txt)
- Title: AdGuard Annoyances filter
- Version: 2.0.46.38
- Homepage: [http://adguard.com/filters.html#annoyances](http://adguard.com/filters.html#annoyances)

**Conversion Details:**
```
Total Lines Processed: 17218
Comment Lines: 2268
Empty Lines: 0
Non-Domain-only Rules Excluded: 14515
Domain-only Rules Excluded (unsupported options): 55
Domain-only Rules Excluded (exception conflict): 13
Domain-only Rules Output: 367
```

&nbsp;

## AdGuard Russian filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-1-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-1-justdomains.txt) |
| Pi-Hole | [adguard-1-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-1-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/1.txt](https://filters.adtidy.org/extension/chromium/filters/1.txt)
- Title: AdGuard Russian filter
- Version: 2.0.33.28
- Homepage: [http://adguard.com/filters.html#russian](http://adguard.com/filters.html#russian)

**Conversion Details:**
```
Total Lines Processed: 20772
Comment Lines: 2727
Empty Lines: 0
Non-Domain-only Rules Excluded: 13967
Domain-only Rules Excluded (unsupported options): 222
Domain-only Rules Excluded (exception conflict): 1311
Domain-only Rules Output: 2545
```

&nbsp;

## AdGuard German filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-6-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-6-justdomains.txt) |
| Pi-Hole | [adguard-6-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-6-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/6.txt](https://filters.adtidy.org/extension/chromium/filters/6.txt)
- Title: AdGuard German filter
- Version: 2.0.11.2
- Homepage: [http://adguard.com/filters.html#german](http://adguard.com/filters.html#german)

**Conversion Details:**
```
Total Lines Processed: 12135
Comment Lines: 966
Empty Lines: 0
Non-Domain-only Rules Excluded: 10386
Domain-only Rules Excluded (unsupported options): 173
Domain-only Rules Excluded (exception conflict): 17
Domain-only Rules Output: 593
```

&nbsp;

## AdGuard French filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-16-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-16-justdomains.txt) |
| Pi-Hole | [adguard-16-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-16-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/16.txt](https://filters.adtidy.org/extension/chromium/filters/16.txt)
- Title: AdGuard French filter
- Version: 2.0.21.70
- Homepage: [http://adguard.com/filters.html#french](http://adguard.com/filters.html#french)

**Conversion Details:**
```
Total Lines Processed: 19933
Comment Lines: 492
Empty Lines: 0
Non-Domain-only Rules Excluded: 13079
Domain-only Rules Excluded (unsupported options): 1439
Domain-only Rules Excluded (exception conflict): 16
Domain-only Rules Output: 4907
```

&nbsp;

## AdGuard Japanese filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-7-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-7-justdomains.txt) |
| Pi-Hole | [adguard-7-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-7-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/7.txt](https://filters.adtidy.org/extension/chromium/filters/7.txt)
- Title: AdGuard Japanese filter
- Version: 2.0.2.95
- Homepage: [http://adguard.com/filters.html#japanese](http://adguard.com/filters.html#japanese)

**Conversion Details:**
```
Total Lines Processed: 1514
Comment Lines: 264
Empty Lines: 0
Non-Domain-only Rules Excluded: 975
Domain-only Rules Excluded (unsupported options): 13
Domain-only Rules Excluded (exception conflict): 11
Domain-only Rules Output: 251
```

&nbsp;

## AdGuard Dutch filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-8-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-8-justdomains.txt) |
| Pi-Hole | [adguard-8-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-8-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/8.txt](https://filters.adtidy.org/extension/chromium/filters/8.txt)
- Title: AdGuard Dutch filter
- Version: 2.0.0.79
- Homepage: [http://adguard.com/filters.html#dutch](http://adguard.com/filters.html#dutch)

**Conversion Details:**
```
Total Lines Processed: 1631
Comment Lines: 171
Empty Lines: 0
Non-Domain-only Rules Excluded: 1363
Domain-only Rules Excluded (unsupported options): 12
Domain-only Rules Excluded (exception conflict): 2
Domain-only Rules Output: 83
```

&nbsp;

## AdGuard Spanish/Portuguese filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-9-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-9-justdomains.txt) |
| Pi-Hole | [adguard-9-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-9-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/9.txt](https://filters.adtidy.org/extension/chromium/filters/9.txt)
- Title: AdGuard Spanish/Portuguese filter
- Version: 2.0.6.11
- Homepage: [http://adguard.com/filters.html#spanish](http://adguard.com/filters.html#spanish)

**Conversion Details:**
```
Total Lines Processed: 3266
Comment Lines: 592
Empty Lines: 0
Non-Domain-only Rules Excluded: 2456
Domain-only Rules Excluded (unsupported options): 28
Domain-only Rules Excluded (exception conflict): 1
Domain-only Rules Output: 189
```

&nbsp;

## AdGuard Turkish filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-13-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-13-justdomains.txt) |
| Pi-Hole | [adguard-13-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-13-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/13.txt](https://filters.adtidy.org/extension/chromium/filters/13.txt)
- Title: AdGuard Turkish filter
- Version: 2.0.15.70
- Homepage: [http://adguard.com/filters.html#turkish](http://adguard.com/filters.html#turkish)

**Conversion Details:**
```
Total Lines Processed: 6000
Comment Lines: 606
Empty Lines: 0
Non-Domain-only Rules Excluded: 5068
Domain-only Rules Excluded (unsupported options): 39
Domain-only Rules Excluded (exception conflict): 3
Domain-only Rules Output: 284
```

&nbsp;

## AdGuard Mobile ads filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-11-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-11-justdomains.txt) |
| Pi-Hole | [adguard-11-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-11-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/11.txt](https://filters.adtidy.org/extension/chromium/filters/11.txt)
- Title: AdGuard Mobile Ads filter
- Version: 2.0.12.17
- Homepage: [http://adguard.com/filters.html#mobile](http://adguard.com/filters.html#mobile)

**Conversion Details:**
```
Total Lines Processed: 3744
Comment Lines: 767
Empty Lines: 0
Non-Domain-only Rules Excluded: 1963
Domain-only Rules Excluded (unsupported options): 20
Domain-only Rules Excluded (exception conflict): 15
Domain-only Rules Output: 979
```

&nbsp;

## AdGuard Simplified Domain Names Filter (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [adguard-15-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-15-justdomains.txt) |
| Pi-Hole | [adguard-15-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/adguard-15-justdomains.txt) |

**Source:** [https://filters.adtidy.org/extension/chromium/filters/15.txt](https://filters.adtidy.org/extension/chromium/filters/15.txt)
- Title: AdGuard Simplified domain names filter
- Version: 2.0.9.38
- Last Modified: 2020-04-21T14:04:07.997Z
- Homepage: [https://github.com/AdguardTeam/AdguardSDNSFilter](https://github.com/AdguardTeam/AdguardSDNSFilter)

**Conversion Details:**
```
Total Lines Processed: 36953
Comment Lines: 408
Empty Lines: 0
Non-Domain-only Rules Excluded: 557
Domain-only Rules Excluded (unsupported options): 5
Domain-only Rules Excluded (exception conflict): 24
Domain-only Rules Output: 35959
```

&nbsp;

## NoCoin Filter List (Domains-only)
| Format | Raw Download Link |
| --- | --- |
| Raw Domain List | [nocoin-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/nocoin-justdomains.txt) |
| Pi-Hole | [nocoin-justdomains.txt](https://tamersaadeh.github.io/dnsbl-ci/lists/nocoin-justdomains.txt) |

**Source:** [https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt](https://raw.githubusercontent.com/hoshsadiq/adblock-nocoin-list/master/hosts.txt)
- Last Modified: 18 Mar 2020
- Homepage: [https://github.com/hoshsadiq/adblock-nocoin-list/](https://github.com/hoshsadiq/adblock-nocoin-list/)

**Conversion Details:**
```
Total Lines Processed: 705
Comment Lines: 10
Empty Lines: 1
Invalid Lines: 0
Non-Loopback Lines (Ignored): 0
Local Hosts (Ignored): 0
Invalid Hosts (Ignored): 0
Duplicate Hosts (Ignored): 6
Hosts Output: 688
```

&nbsp;

# License:
Each converted / modified list file is licensed under the same license as the original list.

For more details, see the [LICENSES](LICENSES) file.

&nbsp;

# Reporting Conversion Issues:
If you find an issue in the output of the conversion process (i.e. comparing to the original upstream list), please report it over on: https://github.com/justdomains/ci/issues

**NOTE: We do not manage the upstream lists themselves, and will not be able to add any new blocks to the lists.**

&nbsp;

<sup>These files are provided "AS IS", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, arising from, out of or in connection with the files or the use of the files.</sup>

<sub>Any and all trademarks are the property of their respective owners.</sub>
