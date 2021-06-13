---
title: LocalTime.adjustInto()
permalink: Java/LocalTime/adjustInto
date: 2021-01-11
key: Java.L.LocalTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalTime.metodos valor="adjustInto" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Temporal adjustInto(Temporal temporal)
~~~

## Parámetros
* **Temporal temporal**,  {% include w3api/param_description.html metodo=_dato parametro="Temporal temporal" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[LocalTime](/Java/LocalTime/)

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
