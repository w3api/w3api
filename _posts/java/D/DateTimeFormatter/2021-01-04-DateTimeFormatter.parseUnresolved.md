---
title: DateTimeFormatter.parseUnresolved()
permalink: Java/DateTimeFormatter/parseUnresolved
date: 2021-01-04
key: JavaJava.D.DateTimeFormatter
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatter.metodos valor="parseUnresolved" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TemporalAccessor parseUnresolved(CharSequence text, ParsePosition position)
~~~

## Parámetros
* **ParsePosition position**,  {% include w3api/param_description.html metodo=_data parametro="ParsePosition position" %}
* **CharSequence text**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence text" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [DateTimeException](/Java/DateTimeException/)

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
