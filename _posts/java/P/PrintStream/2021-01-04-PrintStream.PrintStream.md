---
title: PrintStream.PrintStream()
permalink: Java/PrintStream/PrintStream
date: 2021-01-04
key: JavaJava.P.PrintStream
category: java
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
* **Charset charset**,  {% include w3api/param_description.html metodo=_data parametro="Charset charset" %}
* **String csn**,  {% include w3api/param_description.html metodo=_data parametro="String csn" %}
* **boolean autoFlush**,  {% include w3api/param_description.html metodo=_data parametro="boolean autoFlush" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_data parametro="String fileName" %}
* **String encoding**,  {% include w3api/param_description.html metodo=_data parametro="String encoding" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[FileNotFoundException](/Java/FileNotFoundException/), [SecurityException](/Java/SecurityException/), [UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [IOException](/Java/IOException/)

## Clase Padre
[PrintStream](/Java/PrintStream/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintStream.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
