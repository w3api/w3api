---
title: Exchanger.exchange()
permalink: /Java/Exchanger/exchange/
date: 2021-01-11
key: Java.E.Exchanger
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.E.Exchanger.metodos valor="exchange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public V exchange(V x) throws InterruptedException
public V exchange(V x, long timeout, TimeUnit unit) throws InterruptedException, TimeoutException
~~~

## Parámetros
* **V x**,  {% include w3api/param_description.html metodo=_dato parametro="V x" %}
* **long timeout**,  {% include w3api/param_description.html metodo=_dato parametro="long timeout" %}
* **TimeUnit unit**,  {% include w3api/param_description.html metodo=_dato parametro="TimeUnit unit" %}

## Excepciones
[InterruptedException](/Java/InterruptedException/), [TimeoutException](/Java/TimeoutException/)

## Clase Padre
[Exchanger](/Java/Exchanger/)

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
