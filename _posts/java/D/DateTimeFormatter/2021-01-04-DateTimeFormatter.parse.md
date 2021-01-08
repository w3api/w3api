---
title: DateTimeFormatter.parse()
permalink: Java/DateTimeFormatter/parse
date: 2021-01-04
key: JavaJava.D.DateTimeFormatter
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatter.metodos valor="parse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TemporalAccessor parse(CharSequence text)
public TemporalAccessor parse(CharSequence text, ParsePosition position)
<T> T parse(CharSequence text, TemporalQuery<T> query)
~~~

## Parámetros
* **ParsePosition position**,  {% include w3api/param_description.html metodo=_data parametro="ParsePosition position" %}
* **CharSequence text**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence text" %}
* **TemporalQuery&lt;T&gt; query**,  {% include w3api/param_description.html metodo=_data parametro="TemporalQuery<T> query" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [DateTimeParseException](/Java/DateTimeParseException/)

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
