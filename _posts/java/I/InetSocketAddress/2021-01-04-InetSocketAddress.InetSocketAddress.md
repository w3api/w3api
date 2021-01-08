---
title: InetSocketAddress.InetSocketAddress()
permalink: Java/InetSocketAddress/InetSocketAddress
date: 2021-01-04
key: JavaJava.I.InetSocketAddress
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InetSocketAddress.constructores valor="InetSocketAddress" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InetSocketAddress(int port)
public InetSocketAddress(String hostname, int port)
public InetSocketAddress(InetAddress addr, int port)
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_data parametro="int port" %}
* **String hostname**,  {% include w3api/param_description.html metodo=_data parametro="String hostname" %}
* **InetAddress addr**,  {% include w3api/param_description.html metodo=_data parametro="InetAddress addr" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[InetSocketAddress](/Java/InetSocketAddress/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.I.InetSocketAddress.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
