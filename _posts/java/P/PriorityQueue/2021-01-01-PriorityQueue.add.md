---
title: PriorityQueue.add()
permalink: /Java/PriorityQueue/add/
date: 2021-01-11
key: Java.P.PriorityQueue
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PriorityQueue.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean add(E e)
~~~

## Parámetros
* **E e**,  {% include w3api/param_description.html metodo=_dato parametro="E e" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[PriorityQueue](/Java/PriorityQueue/)

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
