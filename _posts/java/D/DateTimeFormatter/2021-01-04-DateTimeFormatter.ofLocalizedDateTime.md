---
title: DateTimeFormatter.ofLocalizedDateTime()
permalink: Java/DateTimeFormatter/ofLocalizedDateTime
date: 2021-01-04
key: JavaJava.D.DateTimeFormatter
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatter.metodos valor="ofLocalizedDateTime" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static DateTimeFormatter ofLocalizedDateTime(FormatStyle dateTimeStyle)
public static DateTimeFormatter ofLocalizedDateTime(FormatStyle dateStyle, FormatStyle timeStyle)
~~~

## Parámetros
* **FormatStyle dateStyle**,  {% include w3api/param_description.html metodo=_data parametro="FormatStyle dateStyle" %}
* **FormatStyle dateTimeStyle**,  {% include w3api/param_description.html metodo=_data parametro="FormatStyle dateTimeStyle" %}
* **FormatStyle timeStyle**,  {% include w3api/param_description.html metodo=_data parametro="FormatStyle timeStyle" %}

## Clase Padre
[DateTimeFormatter](/Java/DateTimeFormatter/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DateTimeFormatter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
