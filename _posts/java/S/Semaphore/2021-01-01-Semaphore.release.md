---
title: Semaphore.release()
permalink: /Java/Semaphore/release/
date: 2021-01-11
key: Java.S.Semaphore
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.Semaphore.metodos valor="release" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void release()
public void release(int permits)
~~~

## Parámetros
* **int permits**,  {% include w3api/param_description.html metodo=_dato parametro="int permits" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

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
