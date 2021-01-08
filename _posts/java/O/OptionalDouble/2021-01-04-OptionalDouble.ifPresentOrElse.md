---
title: OptionalDouble.ifPresentOrElse()
permalink: Java/OptionalDouble/ifPresentOrElse
date: 2021-01-04
key: JavaJava.O.OptionalDouble
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.O.OptionalDouble.metodos valor="ifPresentOrElse" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void ifPresentOrElse(DoubleConsumer action, Runnable emptyAction)
~~~

## Parámetros
* **Runnable emptyAction**,  {% include w3api/param_description.html metodo=_data parametro="Runnable emptyAction" %}
* **DoubleConsumer action**,  {% include w3api/param_description.html metodo=_data parametro="DoubleConsumer action" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[OptionalDouble](/Java/OptionalDouble/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.O.OptionalDouble.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
