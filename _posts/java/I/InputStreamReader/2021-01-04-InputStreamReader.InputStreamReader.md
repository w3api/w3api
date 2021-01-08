---
title: InputStreamReader.InputStreamReader()
permalink: Java/InputStreamReader/InputStreamReader
date: 2021-01-04
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
* **CharsetDecoder dec**,  {% include w3api/param_description.html metodo=_data parametro="CharsetDecoder dec" %}
* **Charset cs**,  {% include w3api/param_description.html metodo=_data parametro="Charset cs" %}
* **InputStream in**,  {% include w3api/param_description.html metodo=_data parametro="InputStream in" %}
* **String charsetName**,  {% include w3api/param_description.html metodo=_data parametro="String charsetName" %}

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
{%- for _ldc in site.data.Java.I.InputStreamReader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
