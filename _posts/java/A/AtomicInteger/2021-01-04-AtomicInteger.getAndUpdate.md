---
title: AtomicInteger.getAndUpdate()
permalink: Java/AtomicInteger/getAndUpdate
date: 2021-01-04
key: JavaJava.A.AtomicInteger
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicInteger.metodos valor="getAndUpdate" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int getAndUpdate(IntUnaryOperator updateFunction)
~~~

## Parámetros
* **IntUnaryOperator updateFunction**,  {% include w3api/param_description.html metodo=_data parametro="IntUnaryOperator updateFunction" %}

## Clase Padre
[AtomicInteger](/Java/AtomicInteger/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AtomicInteger.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
