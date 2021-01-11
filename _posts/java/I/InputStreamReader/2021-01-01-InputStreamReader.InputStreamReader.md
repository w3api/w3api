---
title: InputStreamReader.InputStreamReader()
permalink: Java/InputStreamReader/InputStreamReader
date: 2021-01-11
key: JavaJava.I.InputStreamReader
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.InputStreamReader.constructores valor="InputStreamReader" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public InputStreamReader(InputStream in)
public InputStreamReader(InputStream in, String charsetName) throws UnsupportedEncodingException
public InputStreamReader(InputStream in, Charset cs)
public InputStreamReader(InputStream in, CharsetDecoder dec)
~~~

## Parámetros
* **InputStream in**,  {% include w3api/param_description.html metodo=_dato parametro="InputStream in" %}
* **CharsetDecoder dec**,  {% include w3api/param_description.html metodo=_dato parametro="CharsetDecoder dec" %}
* **String charsetName**,  {% include w3api/param_description.html metodo=_dato parametro="String charsetName" %}
* **Charset cs**,  {% include w3api/param_description.html metodo=_dato parametro="Charset cs" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/)

## Clase Padre
[InputStreamReader](/Java/InputStreamReader/)

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
