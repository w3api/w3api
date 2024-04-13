---
title: BlockingDeque.putLast()
permalink: /Java/BlockingDeque/putLast/
date: 2021-01-11
key: Java.B.BlockingDeque
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BlockingDeque.metodos valor="putLast" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void putLast(E e) throws InterruptedException
~~~

## Parámetros
* **E e**,  {% include w3api/param_description.html metodo=_dato parametro="E e" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[BlockingDeque](/Java/BlockingDeque/)

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
