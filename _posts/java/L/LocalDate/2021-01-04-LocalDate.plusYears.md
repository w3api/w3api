---
title: LocalDate.plusYears()
permalink: Java/LocalDate/plusYears
date: 2021-01-04
key: JavaJava.L.LocalDate
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalDate.metodos valor="plusYears" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalDate plusYears(long yearsToAdd)
~~~

## Parámetros
* **long yearsToAdd**,  {% include w3api/param_description.html metodo=_data parametro="long yearsToAdd" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalDate](/Java/LocalDate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocalDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
