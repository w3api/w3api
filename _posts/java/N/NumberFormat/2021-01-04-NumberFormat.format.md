---
title: NumberFormat.format()
permalink: Java/NumberFormat/format
date: 2021-01-04
key: JavaJava.N.NumberFormat
category: java
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
* **FieldPosition pos**,  {% include w3api/param_description.html metodo=_data parametro="FieldPosition pos" %}
* **StringBuffer toAppendTo**,  {% include w3api/param_description.html metodo=_data parametro="StringBuffer toAppendTo" %}
* **Object number**,  {% include w3api/param_description.html metodo=_data parametro="Object number" %}
* **long number**,  {% include w3api/param_description.html metodo=_data parametro="long number" %}
* **double number**,  {% include w3api/param_description.html metodo=_data parametro="double number" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[NumberFormat](/Java/NumberFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.N.NumberFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
