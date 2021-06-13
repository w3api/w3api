---
title: DecimalFormat.format()
permalink: /Java/DecimalFormat/format/
date: 2021-01-11
key: Java.D.DecimalFormat
category: Java
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
* **StringBuffer result**,  {% include w3api/param_description.html metodo=_dato parametro="StringBuffer result" %}
* **FieldPosition fieldPosition**,  {% include w3api/param_description.html metodo=_dato parametro="FieldPosition fieldPosition" %}
* **Object number**,  {% include w3api/param_description.html metodo=_dato parametro="Object number" %}
* **long number**,  {% include w3api/param_description.html metodo=_dato parametro="long number" %}
* **double number**,  {% include w3api/param_description.html metodo=_dato parametro="double number" %}
* **StringBuffer toAppendTo**,  {% include w3api/param_description.html metodo=_dato parametro="StringBuffer toAppendTo" %}
* **FieldPosition pos**,  {% include w3api/param_description.html metodo=_dato parametro="FieldPosition pos" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [ArithmeticException](/Java/ArithmeticException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DecimalFormat](/Java/DecimalFormat/)

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
