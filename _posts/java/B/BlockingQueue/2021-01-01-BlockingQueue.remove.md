---
title: BlockingQueue.remove()
permalink: /Java/BlockingQueue/remove/
date: 2021-01-11
key: Java.B.BlockingQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BlockingQueue.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean remove(Object o)
~~~

## Parámetros
* **Object o**,  {% include w3api/param_description.html metodo=_dato parametro="Object o" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BlockingQueue](/Java/BlockingQueue/)

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
