---
title: Collection.remove()
permalink: Java/Collection/remove
date: 2021-01-11
key: JavaJava.C.Collection
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collection.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean remove(Object o)
~~~

## Parámetros
* **Object o**,  {% include w3api/param_description.html metodo=_dato parametro="Object o" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Collection](/Java/Collection/)

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