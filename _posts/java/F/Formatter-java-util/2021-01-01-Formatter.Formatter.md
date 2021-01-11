---
title: Formatter.Formatter()
permalink: Java/Formatter-java-util/Formatter
date: 2021-01-11
key: JavaJava.F.Formatter-java-util
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.Formatter-java-util.constructores valor="Formatter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Formatter()
public Formatter(File file) throws FileNotFoundException
public Formatter(File file, String csn) throws FileNotFoundException, UnsupportedEncodingException
public Formatter(File file, String csn, Locale l) throws FileNotFoundException, UnsupportedEncodingException
public Formatter(File file, Charset charset, Locale l) throws IOException
public Formatter(OutputStream os)
public Formatter(OutputStream os, String csn) throws UnsupportedEncodingException
public Formatter(OutputStream os, String csn, Locale l) throws UnsupportedEncodingException
public Formatter(OutputStream os, Charset charset, Locale l)
public Formatter(PrintStream ps)
public Formatter(Appendable a)
public Formatter(Appendable a, Locale l)
public Formatter(String fileName) throws FileNotFoundException
public Formatter(String fileName, String csn) throws FileNotFoundException, UnsupportedEncodingException
public Formatter(String fileName, String csn, Locale l) throws FileNotFoundException, UnsupportedEncodingException
public Formatter(String fileName, Charset charset, Locale l) throws IOException
public Formatter(Locale l)
~~~

## Parámetros
* **Appendable a**,  {% include w3api/param_description.html metodo=_dato parametro="Appendable a" %}
* **File file**,  {% include w3api/param_description.html metodo=_dato parametro="File file" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_dato parametro="Charset charset" %}
* **PrintStream ps**,  {% include w3api/param_description.html metodo=_dato parametro="PrintStream ps" %}
* **String csn**,  {% include w3api/param_description.html metodo=_dato parametro="String csn" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_dato parametro="String fileName" %}
* **Locale l**,  {% include w3api/param_description.html metodo=_dato parametro="Locale l" %}
* **OutputStream os**,  {% include w3api/param_description.html metodo=_dato parametro="OutputStream os" %}

## Excepciones
[FormatterClosedException](/Java/FormatterClosedException/), [FileNotFoundException](/Java/FileNotFoundException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Formatter](/Java/Formatter-java-util/)

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
