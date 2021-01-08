---
title: ChronoPeriod.get()
permalink: Java/ChronoPeriod/get
date: 2021-01-04
key: JavaJava.C.ChronoPeriod
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoPeriod.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long get(TemporalUnit unit)
~~~

## Parámetros
* **TemporalUnit unit**,  {% include w3api/param_description.html metodo=_data parametro="TemporalUnit unit" %}

## Excepciones
[UnsupportedTemporalTypeException](/Java/UnsupportedTemporalTypeException/), [DateTimeException](/Java/DateTimeException/)

## Clase Padre
[ChronoPeriod](/Java/ChronoPeriod/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChronoPeriod.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
