---
title: AbstractSequentialList.set()
permalink: /Java/AbstractSequentialList/set/
date: 2021-01-11
key: Java.A.AbstractSequentialList
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractSequentialList.metodos valor="set" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public E set(int index, E element)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}
* **E element**,  {% include w3api/param_description.html metodo=_dato parametro="E element" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractSequentialList](/Java/AbstractSequentialList/)

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
