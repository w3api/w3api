---
title: PrintWriter.PrintWriter()
permalink: /Java/PrintWriter/PrintWriter/
date: 2021-01-11
key: Java.P.PrintWriter
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintWriter.constructores valor="PrintWriter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public PrintWriter(File file) throws FileNotFoundException
public PrintWriter(File file, String csn) throws FileNotFoundException, UnsupportedEncodingException
public PrintWriter(File file, Charset charset) throws IOException
public PrintWriter(OutputStream out)
public PrintWriter(OutputStream out, boolean autoFlush)
public PrintWriter(OutputStream out, boolean autoFlush, Charset charset)
public PrintWriter(Writer out)
public PrintWriter(Writer out, boolean autoFlush)
public PrintWriter(String fileName) throws FileNotFoundException
public PrintWriter(String fileName, String csn) throws FileNotFoundException, UnsupportedEncodingException
public PrintWriter(String fileName, Charset charset) throws IOException
~~~

## Parámetros
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_dato parametro="Charset charset" %}
* **boolean autoFlush**,  {% include w3api/param_description.html metodo=_dato parametro="boolean autoFlush" %}
* **String csn**,  {% include w3api/param_description.html metodo=_dato parametro="String csn" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream out" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_dato parametro="String fileName" %}
* **Writer out**,  {% include w3api/param_description.html metodo=_dato parametro="Writer out" %}

## Excepciones
[UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [SecurityException](/Java/SecurityException/), [FileNotFoundException](/Java/FileNotFoundException/), [IOException](/Java/IOException/)

## Clase Padre
[PrintWriter](/Java/PrintWriter/)

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
