---
title: ChronoLocalDate.with()
permalink: Java/ChronoLocalDate/with
date: 2021-01-04
key: JavaJava.C.ChronoLocalDate
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDate.metodos valor="with" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default ChronoLocalDate with(TemporalAdjuster adjuster)
default ChronoLocalDate with(TemporalField field, long newValue)
~~~

## Parámetros
* **long newValue**,  {% include w3api/param_description.html metodo=_data parametro="long newValue" %}
* **TemporalAdjuster adjuster**,  {% include w3api/param_description.html metodo=_data parametro="TemporalAdjuster adjuster" %}
* **TemporalField field**,  {% include w3api/param_description.html metodo=_data parametro="TemporalField field" %}

## Excepciones
[UnsupportedTemporalTypeException](/Java/UnsupportedTemporalTypeException/), [DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[ChronoLocalDate](/Java/ChronoLocalDate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoLocalDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
