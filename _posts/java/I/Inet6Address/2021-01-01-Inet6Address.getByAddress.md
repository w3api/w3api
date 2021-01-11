---
title: Inet6Address.getByAddress()
permalink: Java/Inet6Address/getByAddress
date: 2021-01-11
key: JavaJava.I.Inet6Address
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Inet6Address.metodos valor="getByAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Inet6Address getByAddress(String host, byte[] addr, int scope_id) throws UnknownHostException
public static Inet6Address getByAddress(String host, byte[] addr, NetworkInterface nif) throws UnknownHostException
~~~

## Parámetros
* **int scope_id**,  {% include w3api/param_description.html metodo=_dato parametro="int scope_id" %}
* **NetworkInterface nif**,  {% include w3api/param_description.html metodo=_dato parametro="NetworkInterface nif" %}
* **byte[] addr**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] addr" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}

## Excepciones
[UnknownHostException](/Java/UnknownHostException/)

## Clase Padre
[Inet6Address](/Java/Inet6Address/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
