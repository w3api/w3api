---
title: GregorianCalendar.from()
permalink: Java/GregorianCalendar/from
date: 2021-01-11
key: JavaJava.G.GregorianCalendar
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GregorianCalendar.metodos valor="from" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static GregorianCalendar from(ZonedDateTime zdt)
~~~

## Parámetros
* **ZonedDateTime zdt**,  {% include w3api/param_description.html metodo=_dato parametro="ZonedDateTime zdt" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[GregorianCalendar](/Java/GregorianCalendar/)

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
