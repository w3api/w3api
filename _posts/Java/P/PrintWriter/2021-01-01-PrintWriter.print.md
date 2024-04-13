---
title: PrintWriter.print()
permalink: /Java/PrintWriter/print/
date: 2021-01-11
key: Java.P.PrintWriter
category: Java
tags: ['java se', 'java.io', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PrintWriter.metodos valor="print" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void print(boolean b)
public void print(char c)
public void print(char[] s)
public void print(double d)
public void print(float f)
public void print(int i)
public void print(long l)
public void print(Object obj)
public void print(String s)
~~~

## Parámetros
* **float f**,  {% include w3api/param_description.html metodo=_dato parametro="float f" %}
* **long l**,  {% include w3api/param_description.html metodo=_dato parametro="long l" %}
* **String s**,  {% include w3api/param_description.html metodo=_dato parametro="String s" %}
* **double d**,  {% include w3api/param_description.html metodo=_dato parametro="double d" %}
* **boolean b**,  {% include w3api/param_description.html metodo=_dato parametro="boolean b" %}
* **char[] s**,  {% include w3api/param_description.html metodo=_dato parametro="char[] s" %}
* **char c**,  {% include w3api/param_description.html metodo=_dato parametro="char c" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_dato parametro="Object obj" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
