---
title: ssl.SSLContext
permalink: /Python/ssl/SSLContext/
date: 2021-01-01
key: Python.S.ssl.SSLContext
category: python
tags: ['clase python', 'ssl']
sidebar: 
  nav: python
---

{% include w3api/datos.html clase=site.data.Python.S.ssl.SSLContext.metodos valor="ssl/SSLContext" %}

## Descripción
{{site.data.Python.S.ssl.SSLContext.description }}

## Sintaxis
~~~python
{{ site.data.Python.S.ssl.SSLContext.sintaxis }}~~~

## Constructores
* [SSLContext](/Python/ssl/SSLContext/SSLContext/)

## Métodos
* [cert_store_stats](/Python/ssl/SSLContext/cert_store_stats/)
* [get_ca_certs](/Python/ssl/SSLContext/get_ca_certs/)
* [get_ciphers](/Python/ssl/SSLContext/get_ciphers/)
* [load_cert_chain](/Python/ssl/SSLContext/load_cert_chain/)
* [load_default_certs](/Python/ssl/SSLContext/load_default_certs/)
* [load_dh_params](/Python/ssl/SSLContext/load_dh_params/)
* [load_verify_locations](/Python/ssl/SSLContext/load_verify_locations/)
* [session_stats](/Python/ssl/SSLContext/session_stats/)
* [set_alpn_protocols](/Python/ssl/SSLContext/set_alpn_protocols/)
* [set_ciphers](/Python/ssl/SSLContext/set_ciphers/)
* [set_default_verify_paths](/Python/ssl/SSLContext/set_default_verify_paths/)
* [set_ecdh_curve](/Python/ssl/SSLContext/set_ecdh_curve/)
* [set_npn_protocols](/Python/ssl/SSLContext/set_npn_protocols/)
* [wrap_bio](/Python/ssl/SSLContext/wrap_bio/)
* [wrap_socket](/Python/ssl/SSLContext/wrap_socket/)

## Atributos
* [check_hostname](/Python/ssl/SSLContext/check_hostname/)
* [hostname_checks_common_name](/Python/ssl/SSLContext/hostname_checks_common_name/)
* [keylog_filename](/Python/ssl/SSLContext/keylog_filename/)
* [maximum_version](/Python/ssl/SSLContext/maximum_version/)
* [minimum_version](/Python/ssl/SSLContext/minimum_version/)
* [num_tickets](/Python/ssl/SSLContext/num_tickets/)
* [options](/Python/ssl/SSLContext/options/)
* [post_handshake_auth](/Python/ssl/SSLContext/post_handshake_auth/)
* [protocol](/Python/ssl/SSLContext/protocol/)
* [security_level](/Python/ssl/SSLContext/security_level/)
* [set_servername_callback](/Python/ssl/SSLContext/set_servername_callback/)
* [sni_callback](/Python/ssl/SSLContext/sni_callback/)
* [sslobject_class](/Python/ssl/SSLContext/sslobject_class/)
* [sslsocket_class](/Python/ssl/SSLContext/sslsocket_class/)
* [verify_flags](/Python/ssl/SSLContext/verify_flags/)
* [verify_mode](/Python/ssl/SSLContext/verify_mode/)

## Ejemplo
~~~python
{{ site.data.Python.S.ssl.SSLContext.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.S.ssl.SSLContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
