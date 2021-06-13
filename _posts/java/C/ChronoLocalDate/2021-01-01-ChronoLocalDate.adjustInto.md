---
title: ChronoLocalDate.adjustInto()
permalink: /Java/ChronoLocalDate/adjustInto/
date: 2021-01-11
key: Java.C.ChronoLocalDate
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChronoLocalDate.metodos valor="adjustInto" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Temporal adjustInto(Temporal temporal)
~~~

## Parámetros
* **Temporal temporal**,  {% include w3api/param_description.html metodo=_dato parametro="Temporal temporal" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

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
