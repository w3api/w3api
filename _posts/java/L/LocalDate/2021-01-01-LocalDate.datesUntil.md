---
title: LocalDate.datesUntil()
permalink: /Java/LocalDate/datesUntil/
date: 2021-01-11
key: Java.L.LocalDate
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="datesUntil" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Stream<LocalDate> datesUntil(LocalDate endExclusive)
public Stream<LocalDate> datesUntil(LocalDate endExclusive, Period step)
~~~

## Parámetros
* **LocalDate endExclusive**,  {% include w3api/param_description.html metodo=_dato parametro="LocalDate endExclusive" %}
* **Period step**,  {% include w3api/param_description.html metodo=_dato parametro="Period step" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LocalDate](/Java/LocalDate/)

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
