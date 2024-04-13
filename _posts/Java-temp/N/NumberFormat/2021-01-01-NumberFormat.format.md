---
title: NumberFormat.format()
permalink: /Java/NumberFormat/format/
date: 2021-01-11
key: Java.N.NumberFormat
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.N.NumberFormat.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final String format(double number)
public abstract StringBuffer format(double number, StringBuffer toAppendTo, FieldPosition pos)
public final String format(long number)
public abstract StringBuffer format(long number, StringBuffer toAppendTo, FieldPosition pos)
public StringBuffer format(Object number, StringBuffer toAppendTo, FieldPosition pos)
~~~

## Parámetros
* **Object number**,  {% include w3api/param_description.html metodo=_dato parametro="Object number" %}
* **long number**,  {% include w3api/param_description.html metodo=_dato parametro="long number" %}
* **StringBuffer toAppendTo**,  {% include w3api/param_description.html metodo=_dato parametro="StringBuffer toAppendTo" %}
* **double number**,  {% include w3api/param_description.html metodo=_dato parametro="double number" %}
* **FieldPosition pos**,  {% include w3api/param_description.html metodo=_dato parametro="FieldPosition pos" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ArithmeticException](/Java/ArithmeticException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[NumberFormat](/Java/NumberFormat/)

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
