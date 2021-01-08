---
title: CopyOnWriteArrayList.get()
permalink: Java/CopyOnWriteArrayList/get
date: 2021-01-04
key: JavaJava.C.CopyOnWriteArrayList
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CopyOnWriteArrayList.metodos valor="get" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public E get(int index)
~~~

## Parámetros
* **int index**,  {% include w3api/param_description.html metodo=_data parametro="int index" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[CopyOnWriteArrayList](/Java/CopyOnWriteArrayList/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CopyOnWriteArrayList.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
