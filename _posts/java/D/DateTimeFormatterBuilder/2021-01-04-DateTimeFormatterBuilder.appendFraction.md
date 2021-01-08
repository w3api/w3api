---
title: DateTimeFormatterBuilder.appendFraction()
permalink: Java/DateTimeFormatterBuilder/appendFraction
date: 2021-01-04
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
* **int minWidth**,  {% include w3api/param_description.html metodo=_data parametro="int minWidth" %}
* **boolean decimalPoint**,  {% include w3api/param_description.html metodo=_data parametro="boolean decimalPoint" %}
* **int maxWidth**,  {% include w3api/param_description.html metodo=_data parametro="int maxWidth" %}
* **TemporalField field**,  {% include w3api/param_description.html metodo=_data parametro="TemporalField field" %}

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
{%- for _ldc in site.data.Java.D.DateTimeFormatterBuilder.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
