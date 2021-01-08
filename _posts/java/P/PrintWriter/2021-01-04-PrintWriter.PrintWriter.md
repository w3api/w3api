---
title: PrintWriter.PrintWriter()
permalink: Java/PrintWriter/PrintWriter
date: 2021-01-04
key: JavaJava.P.PrintWriter
category: java
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
* **Charset charset**,  {% include w3api/param_description.html metodo=_data parametro="Charset charset" %}
* **String csn**,  {% include w3api/param_description.html metodo=_data parametro="String csn" %}
* **boolean autoFlush**,  {% include w3api/param_description.html metodo=_data parametro="boolean autoFlush" %}
* **OutputStream out**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream out" %}
* **Writer out**,  {% include w3api/param_description.html metodo=_data parametro="Writer out" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_data parametro="String fileName" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[FileNotFoundException](/Java/FileNotFoundException/), [SecurityException](/Java/SecurityException/), [UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [IOException](/Java/IOException/)

## Clase Padre
[PrintWriter](/Java/PrintWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PrintWriter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
