---
title: PrintWriter.print()
permalink: Java/PrintWriter/print
date: 2021-01-04
key: JavaJava.P.PrintWriter
category: java
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
* **int i**,  {% include w3api/param_description.html metodo=_data parametro="int i" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}
* **float f**,  {% include w3api/param_description.html metodo=_data parametro="float f" %}
* **char[] s**,  {% include w3api/param_description.html metodo=_data parametro="char[] s" %}
* **boolean b**,  {% include w3api/param_description.html metodo=_data parametro="boolean b" %}
* **double d**,  {% include w3api/param_description.html metodo=_data parametro="double d" %}
* **String s**,  {% include w3api/param_description.html metodo=_data parametro="String s" %}
* **char c**,  {% include w3api/param_description.html metodo=_data parametro="char c" %}
* **long l**,  {% include w3api/param_description.html metodo=_data parametro="long l" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

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
