import string

from talon.webview import Webview
from user import basic_keys

alphabet = list(zip(basic_keys.alpha_alt, string.ascii_lowercase))

webview = Webview()
template = '''
<style type="text/css">
body {a
    padding: 0;
    margin: 0;
}
.contents {
    width: 100%;
}
td {
    text-align: left;
    margin: 0;
    padding: 0;
    padding-left: 5px;
}
</style>
<h3>alphabet</h3>
<div class="contents">
<table>
{% for word, letter in alphabet %}
    <tr><td>{{ letter }}</td><td>{{ word }}</td></tr>
{% endfor %}
</table>
</div>
'''
webview.render(template, alphabet=alphabet)
webview.show()