---
title: ThreadLocalRandom.setSeed()
permalink: /Java/ThreadLocalRandom/setSeed/
date: 2021-01-11
key: Java.T.ThreadLocalRandom
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadLocalRandom.metodos valor="setSeed" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSeed(long seed)
~~~

## Parámetros
* **long seed**,  {% include w3api/param_description.html metodo=_dato parametro="long seed" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ThreadLocalRandom](/Java/ThreadLocalRandom/)

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
