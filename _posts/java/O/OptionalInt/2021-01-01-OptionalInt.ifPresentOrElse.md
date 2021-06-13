---
title: OptionalInt.ifPresentOrElse()
permalink: /Java/OptionalInt/ifPresentOrElse/
date: 2021-01-11
key: JavaJava.O.OptionalInt
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OptionalInt.metodos valor="ifPresentOrElse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void ifPresentOrElse(IntConsumer action, Runnable emptyAction)
~~~

## Parámetros
* **IntConsumer action**,  {% include w3api/param_description.html metodo=_dato parametro="IntConsumer action" %}
* **Runnable emptyAction**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable emptyAction" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[OptionalInt](/Java/OptionalInt/)

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
