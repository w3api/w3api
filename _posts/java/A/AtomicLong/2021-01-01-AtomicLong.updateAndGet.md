---
title: AtomicLong.updateAndGet()
permalink: /Java/AtomicLong/updateAndGet/
date: 2021-01-11
key: Java.A.AtomicLong
category: Java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLong.metodos valor="updateAndGet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final long updateAndGet(LongUnaryOperator updateFunction)
~~~

## Parámetros
* **LongUnaryOperator updateFunction**,  {% include w3api/param_description.html metodo=_dato parametro="LongUnaryOperator updateFunction" %}

## Clase Padre
[AtomicLong](/Java/AtomicLong/)

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
