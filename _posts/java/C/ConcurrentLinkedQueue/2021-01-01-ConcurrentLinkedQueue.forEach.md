---
title: ConcurrentLinkedQueue.forEach()
permalink: /Java/ConcurrentLinkedQueue/forEach/
date: 2021-01-11
key: Java.C.ConcurrentLinkedQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ConcurrentLinkedQueue.metodos valor="forEach" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void forEach(Consumer<? super E> action)
~~~

## Parámetros
* **Consumer&lt;? super E&gt; action**,  {% include w3api/param_description.html metodo=_dato parametro="Consumer<? super E> action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ConcurrentLinkedQueue](/Java/ConcurrentLinkedQueue/)

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
