---
title: PrintStream.PrintStream()
permalink: /Java/PrintStream/PrintStream/
date: 2021-01-11
key: Java.P.PrintStream
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintStream.constructores valor="PrintStream" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrintStream(File file) throws FileNotFoundException
public PrintStream(File file, String csn) throws FileNotFoundException, UnsupportedEncodingException
public PrintStream(File file, Charset charset) throws IOException
public PrintStream(OutputStream out)
public PrintStream(OutputStream out, boolean autoFlush)
public PrintStream(OutputStream out, boolean autoFlush, String encoding) throws UnsupportedEncodingException
public PrintStream(OutputStream out, boolean autoFlush, Charset charset)
public PrintStream(String fileName) throws FileNotFoundException
public PrintStream(String fileName, String csn) throws FileNotFoundException, UnsupportedEncodingException
public PrintStream(String fileName, Charset charset) throws IOException
~~~

## Parámetros
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_dato parametro="Charset charset" %}
* **boolean autoFlush**,  {% include w3api/param_description.html metodo=_dato parametro="boolean autoFlush" %}
* **String csn**,  {% include w3api/param_description.html metodo=_dato parametro="String csn" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_dato parametro="String encoding" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_dato parametro="String fileName" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [SecurityException](/Java/SecurityException/), [FileNotFoundException](/Java/FileNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[PrintStream](/Java/PrintStream/)

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
