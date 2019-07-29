Welcome to your Emlid Reach M+!


{% for image in images %}
{{ image | safe}}
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
