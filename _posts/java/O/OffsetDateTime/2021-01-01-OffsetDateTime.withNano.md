---
title: OffsetDateTime.withNano()
permalink: /Java/OffsetDateTime/withNano/
date: 2021-01-11
key: Java.O.OffsetDateTime
category: Java
tags: ['java se', 'java.time', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OffsetDateTime.metodos valor="withNano" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public OffsetDateTime withNano(int nanoOfSecond)
~~~

## Parámetros
* **int nanoOfSecond**,  {% include w3api/param_description.html metodo=_dato parametro="int nanoOfSecond" %}

## Excepciones
[DateTimeException](/Java/DateTimeException/)

## Clase Padre
[OffsetDateTime](/Java/OffsetDateTime/)

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
