---
title: AbstractSequentialList.addAll()
permalink: Java/AbstractSequentialList/addAll
date: 2021-01-04
key: JavaJava.A.AbstractSequentialList
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractSequentialList.metodos valor="addAll" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean addAll(int index, Collection<? extends E> c)
~~~

## Parámetros
* **Collection&lt;? extends E&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Collection<? extends E> c" %}
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractSequentialList](/Java/AbstractSequentialList/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractSequentialList.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
