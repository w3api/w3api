---
title: DateTimeFormatterBuilder.appendLocalized()
permalink: Java/DateTimeFormatterBuilder/appendLocalized
date: 2021-01-11
key: JavaJava.D.DateTimeFormatterBuilder
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatterBuilder.metodos valor="appendLocalized" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public DateTimeFormatterBuilder appendLocalized(FormatStyle dateStyle, FormatStyle timeStyle)
~~~

## Parámetros
* **FormatStyle timeStyle**,  {% include w3api/param_description.html metodo=_dato parametro="FormatStyle timeStyle" %}
* **FormatStyle dateStyle**,  {% include w3api/param_description.html metodo=_dato parametro="FormatStyle dateStyle" %}

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
