---
title: Executors.unconfigurableExecutorService()
permalink: Java/Executors/unconfigurableExecutorService
date: 2021-01-11
key: JavaJava.E.Executors
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Executors.metodos valor="unconfigurableExecutorService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ExecutorService unconfigurableExecutorService(ExecutorService executor)
~~~

## Parámetros
* **ExecutorService executor**,  {% include w3api/param_description.html metodo=_dato parametro="ExecutorService executor" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Executors](/Java/Executors/)

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
