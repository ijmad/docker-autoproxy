function FindProxyForURL(url, host) {
  {% for network in networks %}
    if (shExpMatch(host, "*.{{network}}")) {
        return "PROXY {{proxyhost}}:{{proxyport}}";
    }
  {% endfor %}

    return "DIRECT";
}
