---
title: PrintWriter.println()
permalink: /Java/PrintWriter/println/
date: 2021-01-11
key: Java.P.PrintWriter
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintWriter.metodos valor="println" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void println()
public void println(boolean x)
public void println(char x)
public void println(char[] x)
public void println(double x)
public void println(float x)
public void println(int x)
public void println(long x)
public void println(Object x)
public void println(String x)
~~~

## Parámetros
* **char[] x**,  {% include w3api/param_description.html metodo=_dato parametro="char[] x" %}
* **double x**,  {% include w3api/param_description.html metodo=_dato parametro="double x" %}
* **float x**,  {% include w3api/param_description.html metodo=_dato parametro="float x" %}
* **long x**,  {% include w3api/param_description.html metodo=_dato parametro="long x" %}
* **char x**,  {% include w3api/param_description.html metodo=_dato parametro="char x" %}
* **String x**,  {% include w3api/param_description.html metodo=_dato parametro="String x" %}
* **int x**,  {% include w3api/param_description.html metodo=_dato parametro="int x" %}
* **boolean x**,  {% include w3api/param_description.html metodo=_dato parametro="boolean x" %}
* **Object x**,  {% include w3api/param_description.html metodo=_dato parametro="Object x" %}

## Clase Padre
[PrintWriter](/Java/PrintWriter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
