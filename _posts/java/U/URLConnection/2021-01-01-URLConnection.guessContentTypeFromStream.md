---
title: URLConnection.guessContentTypeFromStream()
permalink: Java/URLConnection/guessContentTypeFromStream
date: 2021-01-11
key: JavaJava.U.URLConnection
category: java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLConnection.metodos valor="guessContentTypeFromStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static String guessContentTypeFromStream(InputStream is) throws IOException
~~~

## Parámetros
* **InputStream is**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream is" %}

## Excepciones
[IOException](/Java/IOException/)

## Clase Padre
[URLConnection](/Java/URLConnection/)

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
