---
title: OptionalDouble.ifPresent()
permalink: Java/OptionalDouble/ifPresent
date: 2021-01-11
key: JavaJava.O.OptionalDouble
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OptionalDouble.metodos valor="ifPresent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void ifPresent(DoubleConsumer action)
~~~

## Parámetros
* **DoubleConsumer action**,  {% include w3api/param_description.html metodo=_dato parametro="DoubleConsumer action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[OptionalDouble](/Java/OptionalDouble/)

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
