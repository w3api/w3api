---
title: Condition.awaitNanos()
permalink: /Java/Condition/awaitNanos/
date: 2021-01-11
key: Java.C.Condition
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Condition.metodos valor="awaitNanos" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
long awaitNanos(long nanosTimeout) throws InterruptedException
~~~

## Parámetros
* **long nanosTimeout**,  {% include w3api/param_description.html metodo=_dato parametro="long nanosTimeout" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[Condition](/Java/Condition/)

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
