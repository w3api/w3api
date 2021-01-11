---
title: AtomicLong.getAndSet()
permalink: Java/AtomicLong/getAndSet
date: 2021-01-11
key: JavaJava.A.AtomicLong
category: java
tags: ['java se', 'java.util.concurrent.atomic', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AtomicLong.metodos valor="getAndSet" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public final long getAndSet(long newValue)
~~~

## Parámetros
* **long newValue**,  {% include w3api/param_description.html metodo=_dato parametro="long newValue" %}

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
