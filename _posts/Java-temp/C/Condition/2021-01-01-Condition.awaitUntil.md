---
title: Condition.awaitUntil()
permalink: /Java/Condition/awaitUntil/
date: 2021-01-11
key: Java.C.Condition
category: Java
tags: ['java se', 'java.util.concurrent.locks', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Condition.metodos valor="awaitUntil" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean awaitUntil(Date deadline) throws InterruptedException
~~~

## Parámetros
* **Date deadline**,  {% include w3api/param_description.html metodo=_dato parametro="Date deadline" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[Condition](/Java/Condition/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Artículos
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
