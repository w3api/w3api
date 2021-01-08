---
title: AbstractList.add()
permalink: Java/AbstractList/add
date: 2021-01-04
key: JavaJava.A.AbstractList
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractList.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void add(int index, E element)
public boolean add(E e)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}
* **E e**,  {% include w3api/param_description.html metodo=_data parametro="E e" %}
* **E element**,  {% include w3api/param_description.html metodo=_data parametro="E element" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractList](/Java/AbstractList/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractList.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
