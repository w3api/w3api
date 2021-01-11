---
title: DateTimeFormatterBuilder.appendFraction()
permalink: Java/DateTimeFormatterBuilder/appendFraction
date: 2021-01-11
key: JavaJava.D.DateTimeFormatterBuilder
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatterBuilder.metodos valor="appendFraction" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeFormatterBuilder appendFraction(TemporalField field, int minWidth, int maxWidth, boolean decimalPoint)
~~~

## Parámetros
* **int minWidth**,  {% include w3api/param_description.html metodo=_dato parametro="int minWidth" %}
* **TemporalField field**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalField field" %}
* **int maxWidth**,  {% include w3api/param_description.html metodo=_dato parametro="int maxWidth" %}
* **boolean decimalPoint**,  {% include w3api/param_description.html metodo=_dato parametro="boolean decimalPoint" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[DateTimeFormatterBuilder](/Java/DateTimeFormatterBuilder/)

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