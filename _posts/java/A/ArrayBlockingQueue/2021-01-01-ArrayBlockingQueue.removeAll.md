---
title: ArrayBlockingQueue.removeAll()
permalink: /Java/ArrayBlockingQueue/removeAll/
date: 2021-01-11
key: Java.A.ArrayBlockingQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayBlockingQueue.metodos valor="removeAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean removeAll(Collection<?> c)
~~~

## Parámetros
* **Collection&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<?> c" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ArrayBlockingQueue](/Java/ArrayBlockingQueue/)

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
