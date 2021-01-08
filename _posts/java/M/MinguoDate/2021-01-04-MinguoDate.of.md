---
title: MinguoDate.of()
permalink: Java/MinguoDate/of
date: 2021-01-04
key: JavaJava.M.MinguoDate
category: java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MinguoDate.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MinguoDate of(int prolepticYear, int month, int dayOfMonth)
~~~

## Parámetros
* **int prolepticYear**,  {% include w3api/param_description.html metodo=_data parametro="int prolepticYear" %}
* **int month**,  {% include w3api/param_description.html metodo=_data parametro="int month" %}
* **int dayOfMonth**,  {% include w3api/param_description.html metodo=_data parametro="int dayOfMonth" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[MinguoDate](/Java/MinguoDate/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MinguoDate.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
