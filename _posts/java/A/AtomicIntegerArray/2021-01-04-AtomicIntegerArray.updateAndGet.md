---
title: AtomicIntegerArray.updateAndGet()
permalink: Java/AtomicIntegerArray/updateAndGet
date: 2021-01-04
key: JavaJava.A.AtomicIntegerArray
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicIntegerArray.metodos valor="updateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int updateAndGet(int i, IntUnaryOperator updateFunction)
~~~

## Parámetros
* **int i**,  {% include w3api/param_description.html metodo=_data parametro="int i" %}
* **IntUnaryOperator updateFunction**,  {% include w3api/param_description.html metodo=_data parametro="IntUnaryOperator updateFunction" %}

## Clase Padre
[AtomicIntegerArray](/Java/AtomicIntegerArray/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicIntegerArray.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
