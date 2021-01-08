---
title: Condition.awaitUntil()
permalink: Java/Condition/awaitUntil
date: 2021-01-04
key: JavaJava.C.Condition
category: java
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
* **Date deadline**,  {% include w3api/param_description.html metodo=_data parametro="Date deadline" %}

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
{%- for _ldc in site.data.Java.C.Condition.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
