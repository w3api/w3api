---
title: LongStream.peek()
permalink: /Java/LongStream/peek/
date: 2021-01-11
key: Java.L.LongStream
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LongStream.metodos valor="peek" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
LongStream peek(LongConsumer action)
~~~

## Parámetros
* **LongConsumer action**,  {% include w3api/param_description.html metodo=_dato parametro="LongConsumer action" %}

## Clase Padre
[LongStream](/Java/LongStream/)

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
