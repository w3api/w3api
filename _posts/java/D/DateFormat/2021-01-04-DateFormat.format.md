---
title: DateFormat.format()
permalink: Java/DateFormat/format
date: 2021-01-04
key: JavaJava.D.DateFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateFormat.metodos valor="format" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final StringBuffer format(Object obj, StringBuffer toAppendTo, FieldPosition fieldPosition)
public final String format(Date date)
public abstract StringBuffer format(Date date, StringBuffer toAppendTo, FieldPosition fieldPosition)
~~~

## Parámetros
* **Date date**,  {% include w3api/param_description.html metodo=_data parametro="Date date" %}
* **StringBuffer toAppendTo**,  {% include w3api/param_description.html metodo=_data parametro="StringBuffer toAppendTo" %}
* **FieldPosition fieldPosition**,  {% include w3api/param_description.html metodo=_data parametro="FieldPosition fieldPosition" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DateFormat](/Java/DateFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DateFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
