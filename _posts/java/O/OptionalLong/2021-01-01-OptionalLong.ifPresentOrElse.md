---
title: OptionalLong.ifPresentOrElse()
permalink: Java/OptionalLong/ifPresentOrElse
date: 2021-01-11
key: JavaJava.O.OptionalLong
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OptionalLong.metodos valor="ifPresentOrElse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void ifPresentOrElse(LongConsumer action, Runnable emptyAction)
~~~

## Parámetros
* **Runnable emptyAction**,  {% include w3api/param_description.html metodo=_dato parametro="Runnable emptyAction" %}
* **LongConsumer action**,  {% include w3api/param_description.html metodo=_dato parametro="LongConsumer action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[OptionalLong](/Java/OptionalLong/)

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
