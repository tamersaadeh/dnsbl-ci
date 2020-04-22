# DOMAIN-ONLY Filter Lists
**Last Updated:** {{ "now" | @date: "%Y-%m-%d %H:%M" }}

- [Details](#details)
- [Usage](#usage)
  - [Using with Pi-Hole](#using-with-pi-hole)
  - [Using with other tools](#using-with-other-tools)
- [The Lists](#the-lists)
{% for item in lists %}
  - [{{ item.title }}]({{ item.source }}) (Domains-only)
{% endfor %}
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
{% for item in lists %}
| [{{ item.title }}]({{ item.source }}) | [{{ item.license_identifier }}]({{ item.header.get('license') }}) | {{ item.domains_output }} | [**Download**]({{ base_url }}/{{ item.output_formats.get('just_domains') }}) | {{ item.header.get('last_modified') }} |
{% endfor %}

{% for item in lists %}
## {{ item.title }} (Domains-only)
| Format | Raw Download Link |
| - | - |
| Raw Domain List | [{{ item.output_formats.get('just_domains') }}]({{ base_url }}/{{ item.output_formats.get('just_domains') }})) |
| Pi-Hole | [{{ item.output_formats.get('just_domains') }}]({{ base_url }}/{{ item.output_formats.get('just_domains') }})) |

**Source:** [{{ item.source | @split: "/" | [-1] }}]({{ item.source }})
- Title: {{ item.title }}
- Version: {{ item.header.get('version') }}
- Last Modified: {{ item.header.get('last_modified') }}
- Homepage: [{{ item.header.get('homepage') }}]({{ item.header.get('homepage') }})

**Conversion Details:**
```{% for row1, row2 in item.get('conversion') %}
{{ row1 }}
{{ row2 }}
{% endfor %}```

{% endfor %}

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
