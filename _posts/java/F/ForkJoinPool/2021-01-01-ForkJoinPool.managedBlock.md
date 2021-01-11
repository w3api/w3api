---
title: ForkJoinPool.managedBlock()
permalink: Java/ForkJoinPool/managedBlock
date: 2021-01-11
key: JavaJava.F.ForkJoinPool
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.ForkJoinPool.metodos valor="managedBlock" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void managedBlock(ForkJoinPool.ManagedBlocker blocker) throws InterruptedException
~~~

## Parámetros
* **ForkJoinPool.ManagedBlocker blocker**,  {% include w3api/param_description.html metodo=_dato parametro="ForkJoinPool.ManagedBlocker blocker" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/)

## Clase Padre
[ForkJoinPool](/Java/ForkJoinPool/)

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
