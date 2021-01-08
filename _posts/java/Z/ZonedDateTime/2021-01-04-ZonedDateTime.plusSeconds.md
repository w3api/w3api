---
title: ZonedDateTime.plusSeconds()
permalink: Java/ZonedDateTime/plusSeconds
date: 2021-01-04
key: JavaJava.Z.ZonedDateTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.Z.ZonedDateTime.metodos valor="plusSeconds" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ZonedDateTime plusSeconds(long seconds)
~~~

## Parámetros
* **long seconds**,  {% include w3api/param_description.html metodo=_data parametro="long seconds" %}

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
{%- for _ldc in site.data.Java.Z.ZonedDateTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
