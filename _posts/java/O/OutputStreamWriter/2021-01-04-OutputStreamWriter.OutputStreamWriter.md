---
title: OutputStreamWriter.OutputStreamWriter()
permalink: Java/OutputStreamWriter/OutputStreamWriter
date: 2021-01-04
key: JavaJava.O.OutputStreamWriter
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OutputStreamWriter.constructores valor="OutputStreamWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OutputStreamWriter(OutputStream out)
public OutputStreamWriter(OutputStream out, String charsetName) throws UnsupportedEncodingException
public OutputStreamWriter(OutputStream out, Charset cs)
public OutputStreamWriter(OutputStream out, CharsetEncoder enc)
~~~

## Parámetros
* **CharsetEncoder enc**,  {% include w3api/param_description.html metodo=_data parametro="CharsetEncoder enc" %}
* **String charsetName**,  {% include w3api/param_description.html metodo=_data parametro="String charsetName" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}
* **Charset cs**,  {% include w3api/param_description.html metodo=_data parametro="Charset cs" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/)

## Clase Padre
[OutputStreamWriter](/Java/OutputStreamWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OutputStreamWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
