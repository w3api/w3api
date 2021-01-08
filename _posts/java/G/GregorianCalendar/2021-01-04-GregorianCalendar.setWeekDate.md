---
title: GregorianCalendar.setWeekDate()
permalink: Java/GregorianCalendar/setWeekDate
date: 2021-01-04
key: JavaJava.G.GregorianCalendar
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GregorianCalendar.metodos valor="setWeekDate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setWeekDate(int weekYear, int weekOfYear, int dayOfWeek)
~~~

## Parámetros
* **int weekOfYear**,  {% include w3api/param_description.html metodo=_data parametro="int weekOfYear" %}
* **int dayOfWeek**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfWeek" %}
* **int weekYear**,  {% include w3api/param_description.html metodo=_data parametro="int weekYear" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[GregorianCalendar](/Java/GregorianCalendar/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.G.GregorianCalendar.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
