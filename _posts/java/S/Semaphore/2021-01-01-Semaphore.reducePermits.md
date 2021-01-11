---
title: Semaphore.reducePermits()
permalink: Java/Semaphore/reducePermits
date: 2021-01-11
key: JavaJava.S.Semaphore
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Semaphore.metodos valor="reducePermits" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void reducePermits(int reduction)
~~~

## Parámetros
* **int reduction**,  {% include w3api/param_description.html metodo=_dato parametro="int reduction" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[Semaphore](/Java/Semaphore/)

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
