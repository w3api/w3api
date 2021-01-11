---
title: LocalDateTime.plusYears()
permalink: Java/LocalDateTime/plusYears
date: 2021-01-11
key: JavaJava.L.LocalDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDateTime.metodos valor="plusYears" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDateTime plusYears(long years)
~~~

## Parámetros
* **long years**,  {% include w3api/param_description.html metodo=_dato parametro="long years" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalDateTime](/Java/LocalDateTime/)

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
