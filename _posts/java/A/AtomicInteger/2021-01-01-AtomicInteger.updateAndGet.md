---
title: AtomicInteger.updateAndGet()
permalink: /Java/AtomicInteger/updateAndGet/
date: 2021-01-11
key: Java.A.AtomicInteger
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicInteger.metodos valor="updateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final int updateAndGet(IntUnaryOperator updateFunction)
~~~

## Parámetros
* **IntUnaryOperator updateFunction**,  {% include w3api/param_description.html metodo=_dato parametro="IntUnaryOperator updateFunction" %}

## Clase Padre
[AtomicInteger](/Java/AtomicInteger/)

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
