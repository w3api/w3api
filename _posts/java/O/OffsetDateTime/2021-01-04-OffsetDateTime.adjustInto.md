---
title: OffsetDateTime.adjustInto()
permalink: Java/OffsetDateTime/adjustInto
date: 2021-01-04
key: JavaJava.O.OffsetDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OffsetDateTime.metodos valor="adjustInto" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Temporal adjustInto(Temporal temporal)
~~~

## Parámetros
* **Temporal temporal**,  {% include w3api/param_description.html metodo=_data parametro="Temporal temporal" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/), [ArithmeticException](/Java/ArithmeticException/)

## Clase Padre
[OffsetDateTime](/Java/OffsetDateTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OffsetDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
