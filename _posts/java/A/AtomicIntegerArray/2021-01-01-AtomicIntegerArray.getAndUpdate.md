---
title: AtomicIntegerArray.getAndUpdate()
permalink: Java/AtomicIntegerArray/getAndUpdate
date: 2021-01-11
key: JavaJava.A.AtomicIntegerArray
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerArray.metodos valor="getAndUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int getAndUpdate(int i, IntUnaryOperator updateFunction)
~~~

## Parámetros
* **IntUnaryOperator updateFunction**,  {% include w3api/param_description.html metodo=_dato parametro="IntUnaryOperator updateFunction" %}
* **int i**,  {% include w3api/param_description.html metodo=_dato parametro="int i" %}

## Clase Padre
[AtomicIntegerArray](/Java/AtomicIntegerArray/)

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
