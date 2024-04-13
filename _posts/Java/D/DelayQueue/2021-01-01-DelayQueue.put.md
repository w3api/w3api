---
title: DelayQueue.put()
permalink: /Java/DelayQueue/put/
date: 2021-01-11
key: Java.D.DelayQueue
category: Java
tags: ['java se', 'java.util.concurrent', 'java.base', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DelayQueue.metodos valor="put" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void put(E e)
~~~

## Parámetros
* **E e**,  {% include w3api/param_description.html metodo=_dato parametro="E e" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DelayQueue](/Java/DelayQueue/)

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
