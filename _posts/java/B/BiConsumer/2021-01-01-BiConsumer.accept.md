---
title: BiConsumer.accept()
permalink: Java/BiConsumer/accept
date: 2021-01-11
key: JavaJava.B.BiConsumer
category: java
tags: ['java se', 'java.util.function', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BiConsumer.metodos valor="accept" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void accept(T t, U u)
~~~

## Parámetros
* **U u**,  {% include w3api/param_description.html metodo=_dato parametro="U u" %}
* **T t**,  {% include w3api/param_description.html metodo=_dato parametro="T t" %}

## Clase Padre
[BiConsumer](/Java/BiConsumer/)

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
