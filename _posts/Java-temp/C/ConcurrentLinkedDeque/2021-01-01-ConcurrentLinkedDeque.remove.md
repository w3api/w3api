---
title: ConcurrentLinkedDeque.remove()
permalink: /Java/ConcurrentLinkedDeque/remove/
date: 2021-01-11
key: Java.C.ConcurrentLinkedDeque
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentLinkedDeque.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public E remove()
public boolean remove(Object o)
~~~

## Parámetros
* **Object o**,  {% include w3api/param_description.html metodo=_dato parametro="Object o" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentLinkedDeque](/Java/ConcurrentLinkedDeque/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
