---
title: URLStreamHandler.openConnection()
permalink: Java/URLStreamHandler/openConnection
date: 2021-01-11
key: JavaJava.U.URLStreamHandler
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLStreamHandler.metodos valor="openConnection" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected abstract URLConnection openConnection(URL u) throws IOException
protected URLConnection openConnection(URL u, Proxy p) throws IOException
~~~

## Parámetros
* **URL u**,  {% include w3api/param_description.html metodo=_dato parametro="URL u" %}
* **Proxy p**,  {% include w3api/param_description.html metodo=_dato parametro="Proxy p" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [IOException](/Java/IOException/)

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
