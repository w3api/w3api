---
title: URLEncoder.encode()
permalink: /Java/URLEncoder/encode/
date: 2021-01-11
key: Java.U.URLEncoder
category: Java
tags: ['java se', 'java.net', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.URLEncoder.metodos valor="encode" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated public static String encode(String s)
public static String encode(String s, String enc) throws UnsupportedEncodingException
public static String encode(String s, Charset charset)
~~~

## Parámetros
* **Charset charset**,  {% include w3api/param_description.html metodo=_dato parametro="Charset charset" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **String enc**,  {% include w3api/param_description.html metodo=_dato parametro="String enc" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[URLEncoder](/Java/URLEncoder/)

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
