---
title: DateTimeFormatterBuilder.appendLocalized()
permalink: Java/DateTimeFormatterBuilder/appendLocalized
date: 2021-01-04
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
* **FormatStyle dateStyle**,  {% include w3api/param_description.html metodo=_data parametro="FormatStyle dateStyle" %}
* **FormatStyle timeStyle**,  {% include w3api/param_description.html metodo=_data parametro="FormatStyle timeStyle" %}

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
