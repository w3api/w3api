---
title: ArrayDeque.ArrayDeque()
permalink: /Java/ArrayDeque/ArrayDeque/
date: 2021-01-11
key: Java.A.ArrayDeque
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ArrayDeque.constructores valor="ArrayDeque" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ArrayDeque()
public ArrayDeque(int numElements)
public ArrayDeque(Collection<? extends E> c)
~~~

## Parámetros
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_dato parametro="Collection<? extends E> c" %}
* **int numElements**,  {% include w3api/param_description.html metodo=_dato parametro="int numElements" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ArrayDeque](/Java/ArrayDeque/)

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
