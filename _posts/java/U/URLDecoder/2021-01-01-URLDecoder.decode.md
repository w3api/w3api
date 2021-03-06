---
title: URLDecoder.decode()
permalink: /Java/URLDecoder/decode/
date: 2021-01-11
key: Java.U.URLDecoder
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLDecoder.metodos valor="decode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public static String decode(String s)
public static String decode(String s, String enc) throws UnsupportedEncodingException
public static String decode(String s, Charset charset)
~~~

## Parámetros
* **Charset charset**,  {% include w3api/param_description.html metodo=_dato parametro="Charset charset" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **String enc**,  {% include w3api/param_description.html metodo=_dato parametro="String enc" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[URLDecoder](/Java/URLDecoder/)

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
