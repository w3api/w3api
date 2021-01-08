---
title: Collection.add()
permalink: Java/Collection/add
date: 2021-01-04
key: JavaJava.C.Collection
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collection.metodos valor="add" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean add(E e)
~~~

## Parámetros
* **E e**,  {% include w3api/param_description.html metodo=_data parametro="E e" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalStateException](/Java/IllegalStateException/)

## Clase Padre
[Collection](/Java/Collection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Collection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
