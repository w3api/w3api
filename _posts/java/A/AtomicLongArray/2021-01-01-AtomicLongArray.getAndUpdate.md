---
title: AtomicLongArray.getAndUpdate()
permalink: Java/AtomicLongArray/getAndUpdate
date: 2021-01-11
key: JavaJava.A.AtomicLongArray
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLongArray.metodos valor="getAndUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final long getAndUpdate(int i, LongUnaryOperator updateFunction)
~~~

## Parámetros
* **LongUnaryOperator updateFunction**,  {% include w3api/param_description.html metodo=_dato parametro="LongUnaryOperator updateFunction" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}

## Clase Padre
[AtomicLongArray](/Java/AtomicLongArray/)

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
