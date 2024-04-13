---
title: LinkedBlockingDeque.addLast()
permalink: /Java/LinkedBlockingDeque/addLast/
date: 2021-01-11
key: Java.L.LinkedBlockingDeque
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LinkedBlockingDeque.metodos valor="addLast" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addLast(E e)
~~~

## Parámetros
* **E e**,  {% include w3api/param_description.html metodo=_dato parametro="E e" %}

## Excepciones
[IllegalStateException](/Java/IllegalStateException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LinkedBlockingDeque](/Java/LinkedBlockingDeque/)

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
