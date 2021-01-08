---
title: DecimalFormat.format()
permalink: Java/DecimalFormat/format
date: 2021-01-04
key: JavaJava.D.DecimalFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DecimalFormat.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StringBuffer format(double number, StringBuffer result, FieldPosition fieldPosition)
public StringBuffer format(long number, StringBuffer result, FieldPosition fieldPosition)
public final StringBuffer format(Object number, StringBuffer toAppendTo, FieldPosition pos)
~~~

## Parámetros
* **FieldPosition pos**,  {% include w3api/param_description.html metodo=_data parametro="FieldPosition pos" %}
* **StringBuffer result**,  {% include w3api/param_description.html metodo=_data parametro="StringBuffer result" %}
* **FieldPosition fieldPosition**,  {% include w3api/param_description.html metodo=_data parametro="FieldPosition fieldPosition" %}
* **StringBuffer toAppendTo**,  {% include w3api/param_description.html metodo=_data parametro="StringBuffer toAppendTo" %}
* **Object number**,  {% include w3api/param_description.html metodo=_data parametro="Object number" %}
* **long number**,  {% include w3api/param_description.html metodo=_data parametro="long number" %}
* **double number**,  {% include w3api/param_description.html metodo=_data parametro="double number" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[DecimalFormat](/Java/DecimalFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DecimalFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
