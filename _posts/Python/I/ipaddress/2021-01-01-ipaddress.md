---
title: ipaddress
permalink: /Python/ipaddress
date: 2021-01-01
key: Python.I.ipaddress
category: python
tags: ['modulo python']
sidebar: 
  nav: python
---

## Descripción
{{site.data.Python.I.ipaddress.description }}

## Funciones
* [collapse_addresses](/Python/ipaddress/collapse_addresses/)
* [get_mixed_type_key](/Python/ipaddress/get_mixed_type_key/)
* [ip_address](/Python/ipaddress/ip_address/)
* [ip_interface](/Python/ipaddress/ip_interface/)
* [ip_network](/Python/ipaddress/ip_network/)
* [summarize_address_range](/Python/ipaddress/summarize_address_range/)
* [v4_int_to_packed](/Python/ipaddress/v4_int_to_packed/)
* [v6_int_to_packed](/Python/ipaddress/v6_int_to_packed/)

## Clases
* [IPv4Address](/Python/ipaddress/IPv4Address/)
* [IPv4Interface](/Python/ipaddress/IPv4Interface/)
* [IPv4Network](/Python/ipaddress/IPv4Network/)
* [IPv6Address](/Python/ipaddress/IPv6Address/)
* [IPv6Interface](/Python/ipaddress/IPv6Interface/)
* [IPv6Network](/Python/ipaddress/IPv6Network/)

## Excepciones
* [AddressValueError](/Python/ipaddress/AddressValueError/)
* [NetmaskValueError](/Python/ipaddress/NetmaskValueError/)

## Ejemplo
~~~python
{{ site.data.Python.I.ipaddress.code}}
~~~

## Artículos
<ul>
{%- for _ldc in site.data.Python.I.ipaddress.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
