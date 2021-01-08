---
title: ConcurrentLinkedQueue.add()
permalink: Java/ConcurrentLinkedQueue/add
date: 2021-01-04
key: JavaJava.C.ConcurrentLinkedQueue
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentLinkedQueue.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean add(E e)
~~~

## Parámetros
* **E e**,  {% include w3api/param_description.html metodo=_data parametro="E e" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentLinkedQueue](/Java/ConcurrentLinkedQueue/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ConcurrentLinkedQueue.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
