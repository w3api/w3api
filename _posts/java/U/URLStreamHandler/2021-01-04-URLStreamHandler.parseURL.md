---
title: URLStreamHandler.parseURL()
permalink: Java/URLStreamHandler/parseURL
date: 2021-01-04
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
* **String spec**,  {% include w3api/param_description.html metodo=_data parametro="String spec" %}
* **int limit**,  {% include w3api/param_description.html metodo=_data parametro="int limit" %}
* **int start**,  {% include w3api/param_description.html metodo=_data parametro="int start" %}
* **URL u**,  {% include w3api/param_description.html metodo=_data parametro="URL u" %}

## Clase Padre
[URLStreamHandler](/Java/URLStreamHandler/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.URLStreamHandler.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
