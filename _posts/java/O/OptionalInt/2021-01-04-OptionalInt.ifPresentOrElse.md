---
title: OptionalInt.ifPresentOrElse()
permalink: Java/OptionalInt/ifPresentOrElse
date: 2021-01-04
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
* **Runnable emptyAction**,  {% include w3api/param_description.html metodo=_data parametro="Runnable emptyAction" %}
* **IntConsumer action**,  {% include w3api/param_description.html metodo=_data parametro="IntConsumer action" %}

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
{%- for _ldc in site.data.Java.O.OptionalInt.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
