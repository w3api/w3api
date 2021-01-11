---
title: URLStreamHandler.parseURL()
permalink: Java/URLStreamHandler/parseURL
date: 2021-01-11
key: JavaJava.U.URLStreamHandler
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLStreamHandler.metodos valor="parseURL" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void parseURL(URL u, String spec, int start, int limit)
~~~

## Parámetros
* **URL u**,  {% include w3api/param_description.html metodo=_dato parametro="URL u" %}
* **int start**,  {% include w3api/param_description.html metodo=_dato parametro="int start" %}
* **String spec**,  {% include w3api/param_description.html metodo=_dato parametro="String spec" %}
* **int limit**,  {% include w3api/param_description.html metodo=_dato parametro="int limit" %}

## Clase Padre
[URLStreamHandler](/Java/URLStreamHandler/)

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
