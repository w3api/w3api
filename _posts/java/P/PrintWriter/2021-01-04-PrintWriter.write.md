---
title: PrintWriter.write()
permalink: Java/PrintWriter/write
date: 2021-01-04
key: JavaJava.P.PrintWriter
category: java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintWriter.metodos valor="write" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void write(char[] buf)
public void write(char[] buf, int off, int len)
public void write(int c)
public void write(String s)
public void write(String s, int off, int len)
~~~

## Parámetros
* **int off**,  {% include w3api/param_description.html metodo=_data parametro="int off" %}
* **char[] buf**,  {% include w3api/param_description.html metodo=_data parametro="char[] buf" %}
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **int len**,  {% include w3api/param_description.html metodo=_data parametro="int len" %}
* **int c**,  {% include w3api/param_description.html metodo=_data parametro="int c" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

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
