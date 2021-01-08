---
title: AbstractList.subList()
permalink: Java/AbstractList/subList
date: 2021-01-04
key: JavaJava.A.AbstractList
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractList.metodos valor="subList" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public List<E> subList(int fromIndex, int toIndex)
~~~

## Parámetros
* **int fromIndex**,  {% include w3api/param_description.html metodo=_data parametro="int fromIndex" %}
* **int toIndex**,  {% include w3api/param_description.html metodo=_data parametro="int toIndex" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
