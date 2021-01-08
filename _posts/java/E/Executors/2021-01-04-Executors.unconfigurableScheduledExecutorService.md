---
title: Executors.unconfigurableScheduledExecutorService()
permalink: Java/Executors/unconfigurableScheduledExecutorService
date: 2021-01-04
key: JavaJava.E.Executors
category: java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Executors.metodos valor="unconfigurableScheduledExecutorService" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static ScheduledExecutorService unconfigurableScheduledExecutorService(ScheduledExecutorService executor)
~~~

## Parámetros
* **ScheduledExecutorService executor**,  {% include w3api/param_description.html metodo=_data parametro="ScheduledExecutorService executor" %}

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
{%- for _ldc in site.data.Java.E.Executors.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
