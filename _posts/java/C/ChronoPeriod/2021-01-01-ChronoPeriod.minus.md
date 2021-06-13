---
title: ChronoPeriod.minus()
permalink: /Java/ChronoPeriod/minus/
date: 2021-01-11
key: Java.C.ChronoPeriod
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoPeriod.metodos valor="minus" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ChronoPeriod minus(TemporalAmount amountToSubtract)
~~~

## Parámetros
* **TemporalAmount amountToSubtract**,  {% include w3api/param_description.html metodo=_dato parametro="TemporalAmount amountToSubtract" %}

## Excepciones
[ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[ChronoPeriod](/Java/ChronoPeriod/)

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
