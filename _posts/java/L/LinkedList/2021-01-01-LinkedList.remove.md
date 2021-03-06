---
title: LinkedList.remove()
permalink: /Java/LinkedList/remove/
date: 2021-01-11
key: Java.L.LinkedList
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedList.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public E remove()
public E remove(int index)
public boolean remove(Object o)
~~~

## Parámetros
* **Object o**,  {% include w3api/param_description.html metodo=_dato parametro="Object o" %}
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[NoSuchElementException](/Java/NoSuchElementException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[LinkedList](/Java/LinkedList/)

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
