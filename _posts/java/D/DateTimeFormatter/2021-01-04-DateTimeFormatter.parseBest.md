---
title: DateTimeFormatter.parseBest()
permalink: Java/DateTimeFormatter/parseBest
date: 2021-01-04
key: JavaJava.D.DateTimeFormatter
category: java
tags: ['java se', 'java.time.format', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DateTimeFormatter.metodos valor="parseBest" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public TemporalAccessor parseBest(CharSequence text, TemporalQuery<?>... queries)
~~~

## Parámetros
* **TemporalQuery&lt;?&gt;... queries**,  {% include w3api/param_description.html metodo=_data parametro="TemporalQuery<?>... queries" %}
* **CharSequence text**,  {% include w3api/param_description.html metodo=_data parametro="CharSequence text" %}

## Excepciones
[DateTimeParseException](/Java/DateTimeParseException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
