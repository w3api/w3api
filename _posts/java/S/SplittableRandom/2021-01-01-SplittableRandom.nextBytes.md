---
title: SplittableRandom.nextBytes()
permalink: Java/SplittableRandom/nextBytes
date: 2021-01-11
key: JavaJava.S.SplittableRandom
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SplittableRandom.metodos valor="nextBytes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void nextBytes(byte[] bytes)
~~~

## Parámetros
* **byte[] bytes**,  {% include w3api/param_description.html metodo=_dato parametro="byte[] bytes" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[SplittableRandom](/Java/SplittableRandom/)

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
