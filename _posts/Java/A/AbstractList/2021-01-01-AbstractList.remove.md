---
title: AbstractList.remove()
permalink: /Java/AbstractList/remove/
date: 2021-01-11
key: Java.A.AbstractList
category: Java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractList.metodos valor="remove" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public E remove(int index)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_dato parametro="int index" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[AbstractList](/Java/AbstractList/)

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
