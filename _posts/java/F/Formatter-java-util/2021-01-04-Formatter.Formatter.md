---
title: Formatter.Formatter()
permalink: Java/Formatter-java-util/Formatter
date: 2021-01-04
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
* **Locale l**,  {% include w3api/param_description.html metodo=_data parametro="Locale l" %}
* **Charset charset**,  {% include w3api/param_description.html metodo=_data parametro="Charset charset" %}
* **String csn**,  {% include w3api/param_description.html metodo=_data parametro="String csn" %}
* **PrintStream ps**,  {% include w3api/param_description.html metodo=_data parametro="PrintStream ps" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_data parametro="String fileName" %}
* **OutputStream os**,  {% include w3api/param_description.html metodo=_data parametro="OutputStream os" %}
* **Appendable a**,  {% include w3api/param_description.html metodo=_data parametro="Appendable a" %}
* **File file**,  {% include w3api/param_description.html metodo=_data parametro="File file" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [FormatterClosedException](/Java/FormatterClosedException/), [UnsupportedEncodingException](/Java/UnsupportedEncodingException/), [FileNotFoundException](/Java/FileNotFoundException/), [NullPointerException](/Java/NullPointerException/), [IOException](/Java/IOException/)

## Clase Padre
[Formatter](/Java/Formatter-java-util/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.Formatter-java-util.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
