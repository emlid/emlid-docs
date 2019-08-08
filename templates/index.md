Welcome to your Reach {{ model }}!

{% if model == "RTK" %}
{% include "include/index_rtk_template.md" %}
{% else %}
{% for image in index_images %}
[![]({{ image | safe}}){: style="width: 200px;"} ](quickstart.md)
{%- endfor %}
## Package contents

In the box:

{% for component in inthebox %}
{{ component }}
{% endfor %}
### Collaboration

This document can be edited on GitHub in markdown. If you find any mistakes, typos or  pieces that are not documented well enough simply open an issue or contribute by sending a pull request.

### Discussion

We are happy to answer any questions at [community.emlid.com](http://community.emlid.com)
{% endif %}
