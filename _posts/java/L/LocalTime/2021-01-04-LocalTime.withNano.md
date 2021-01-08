---
title: LocalTime.withNano()
permalink: Java/LocalTime/withNano
date: 2021-01-04
key: JavaJava.L.LocalTime
category: java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocalTime.metodos valor="withNano" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public LocalTime withNano(int nanoOfSecond)
~~~

## Parámetros
* **int nanoOfSecond**,  {% include w3api/param_description.html metodo=_data parametro="int nanoOfSecond" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[LocalTime](/Java/LocalTime/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocalTime.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
