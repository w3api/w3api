---
title: MinguoDate.now()
permalink: Java/MinguoDate/now
date: 2021-01-11
key: JavaJava.M.MinguoDate
category: Java
tags: ['java se', 'java.time.chrono', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MinguoDate.metodos valor="now" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static MinguoDate now()
public static MinguoDate now(Clock clock)
public static MinguoDate now(ZoneId zone)
~~~

## Parámetros
* **ZoneId zone**,  {% include w3api/param_description.html metodo=_dato parametro="ZoneId zone" %}
* **Clock clock**,  {% include w3api/param_description.html metodo=_dato parametro="Clock clock" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
