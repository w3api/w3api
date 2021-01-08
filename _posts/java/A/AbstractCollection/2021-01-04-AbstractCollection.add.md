---
title: AbstractCollection.add()
permalink: Java/AbstractCollection/add
date: 2021-01-04
key: JavaJava.A.AbstractCollection
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractCollection.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean add(E e)
~~~

## Parámetros
* **E e**,  {% include w3api/param_description.html metodo=_data parametro="E e" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[AbstractCollection](/Java/AbstractCollection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractCollection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
