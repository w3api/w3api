---
title: OptionalLong.orElseGet()
permalink: Java/OptionalLong/orElseGet
date: 2021-01-04
key: JavaJava.O.OptionalLong
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OptionalLong.metodos valor="orElseGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public long orElseGet(LongSupplier supplier)
~~~

## Parámetros
* **LongSupplier supplier**,  {% include w3api/param_description.html metodo=_data parametro="LongSupplier supplier" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[OptionalLong](/Java/OptionalLong/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OptionalLong.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
