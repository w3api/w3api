---
title: BlockingDeque.putFirst()
permalink: Java/BlockingDeque/putFirst
date: 2021-01-04
key: JavaJava.B.BlockingDeque
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BlockingDeque.metodos valor="putFirst" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void putFirst(E e) throws InterruptedException
~~~

## Parámetros
* **E e**,  {% include w3api/param_description.html metodo=_data parametro="E e" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [ClassCastException](/Java/ClassCastException/), [NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[BlockingDeque](/Java/BlockingDeque/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BlockingDeque.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
