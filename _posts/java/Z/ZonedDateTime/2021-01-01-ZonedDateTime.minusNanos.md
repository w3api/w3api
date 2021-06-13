---
title: ZonedDateTime.minusNanos()
permalink: /Java/ZonedDateTime/minusNanos/
date: 2021-01-11
key: Java.Z.ZonedDateTime
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZonedDateTime.metodos valor="minusNanos" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ZonedDateTime minusNanos(long nanos)
~~~

## Parámetros
* **long nanos**,  {% include w3api/param_description.html metodo=_dato parametro="long nanos" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[ZonedDateTime](/Java/ZonedDateTime/)

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
