---
title: OptionalInt.orElseGet()
permalink: Java/OptionalInt/orElseGet
date: 2021-01-11
key: JavaJava.O.OptionalInt
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OptionalInt.metodos valor="orElseGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public int orElseGet(IntSupplier supplier)
~~~

## Parámetros
* **IntSupplier supplier**,  {% include w3api/param_description.html metodo=_dato parametro="IntSupplier supplier" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[OptionalInt](/Java/OptionalInt/)

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
