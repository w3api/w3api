---
title: ChronoLocalDate.from()
permalink: /Java/ChronoLocalDate/from/
date: 2021-01-11
key: Java.C.ChronoLocalDate
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDate.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static ChronoLocalDate from(TemporalAccessor temporal)
~~~

## Parámetros
* **TemporalAccessor temporal**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAccessor temporal" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[ChronoLocalDate](/Java/ChronoLocalDate/)

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
