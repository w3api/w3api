---
title: InetSocketAddress.createUnresolved()
permalink: /Java/InetSocketAddress/createUnresolved/
date: 2021-01-11
key: Java.I.InetSocketAddress
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InetSocketAddress.metodos valor="createUnresolved" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static InetSocketAddress createUnresolved(String host, int port)
~~~

## Parámetros
* **int port**,  {% include w3api/param_description.html metodo=_dato parametro="int port" %}
* **String host**,  {% include w3api/param_description.html metodo=_dato parametro="String host" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[InetSocketAddress](/Java/InetSocketAddress/)

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
