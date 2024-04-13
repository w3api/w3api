---
title: ChronoZonedDateTime.from()
permalink: /Java/ChronoZonedDateTime/from/
date: 2021-01-11
key: Java.C.ChronoZonedDateTime
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoZonedDateTime.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static ChronoZonedDateTime<?> from(TemporalAccessor temporal)
~~~

## Parámetros
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAccessor temporal" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[ChronoZonedDateTime](/Java/ChronoZonedDateTime/)

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
