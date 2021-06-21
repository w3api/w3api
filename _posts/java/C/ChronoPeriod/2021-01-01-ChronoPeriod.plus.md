---
title: ChronoPeriod.plus()
permalink: /Java/ChronoPeriod/plus/
date: 2021-01-11
key: Java.C.ChronoPeriod
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoPeriod.metodos valor="plus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ChronoPeriod plus(TemporalAmount amountToAdd)
~~~

## Parámetros
* **TemporalAmount amountToAdd**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAmount amountToAdd" %}

## Excepciones
[ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[ChronoPeriod](/Java/ChronoPeriod/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
