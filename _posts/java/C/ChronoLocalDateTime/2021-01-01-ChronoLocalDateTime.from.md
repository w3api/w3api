---
title: ChronoLocalDateTime.from()
permalink: /Java/ChronoLocalDateTime/from/
date: 2021-01-11
key: Java.C.ChronoLocalDateTime
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDateTime.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static ChronoLocalDateTime<?> from(TemporalAccessor temporal)
~~~

## Parámetros
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAccessor temporal" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[ChronoLocalDateTime](/Java/ChronoLocalDateTime/)

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
