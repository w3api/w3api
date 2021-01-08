---
title: ChronoLocalDateTime.with()
permalink: Java/ChronoLocalDateTime/with
date: 2021-01-04
key: JavaJava.C.ChronoLocalDateTime
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDateTime.metodos valor="with" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default ChronoLocalDateTime<D> with(TemporalAdjuster adjuster)
ChronoLocalDateTime<D> with(TemporalField field, long newValue)
~~~

## Parámetros
* **long newValue**,  {% include w3api/param_description.html metodo=_data parametro="long newValue" %}
* **TemporalAdjuster adjuster**,  {% include w3api/param_description.html metodo=_data parametro="TemporalAdjuster adjuster" %}
* **TemporalField field**,  {% include w3api/param_description.html metodo=_data parametro="TemporalField field" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[ChronoLocalDateTime](/Java/ChronoLocalDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoLocalDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
