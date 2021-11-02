---
title: ssl.SSLSocket
permalink: /Python/ssl/SSLSocket/
date: 2021-01-01
key: Python.S.ssl.SSLSocket
category: python
tags: ['clase python', 'ssl']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.S.ssl.SSLSocket.metodos valor="ssl/SSLSocket" %}

## Descripción
{{site.data.Python.S.ssl.SSLSocket.description }}

## Sintaxis
~~~python
{{ site.data.Python.S.ssl.SSLSocket.sintaxis }}~~~

## Constructores
* [SSLSocket](/Python/ssl/SSLSocket/SSLSocket/)

## Métodos
* [cipher](/Python/ssl/SSLSocket/cipher/)
* [compression](/Python/ssl/SSLSocket/compression/)
* [do_handshake](/Python/ssl/SSLSocket/do_handshake/)
* [getpeercert](/Python/ssl/SSLSocket/getpeercert/)
* [get_channel_binding](/Python/ssl/SSLSocket/get_channel_binding/)
* [pending](/Python/ssl/SSLSocket/pending/)
* [read](/Python/ssl/SSLSocket/read/)
* [selected_alpn_protocol](/Python/ssl/SSLSocket/selected_alpn_protocol/)
* [selected_npn_protocol](/Python/ssl/SSLSocket/selected_npn_protocol/)
* [shared_ciphers](/Python/ssl/SSLSocket/shared_ciphers/)
* [unwrap](/Python/ssl/SSLSocket/unwrap/)
* [verify_client_post_handshake](/Python/ssl/SSLSocket/verify_client_post_handshake/)
* [version](/Python/ssl/SSLSocket/version/)
* [write](/Python/ssl/SSLSocket/write/)

## Atributos
* [context](/Python/ssl/SSLSocket/context/)
* [server_hostname](/Python/ssl/SSLSocket/server_hostname/)
* [server_side](/Python/ssl/SSLSocket/server_side/)
* [session](/Python/ssl/SSLSocket/session/)
* [session_reused](/Python/ssl/SSLSocket/session_reused/)

## Ejemplo
~~~python
{{ site.data.Python.S.ssl.SSLSocket.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.S.ssl.SSLSocket.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
