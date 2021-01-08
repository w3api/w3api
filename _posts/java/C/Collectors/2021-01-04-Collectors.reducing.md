---
title: Collectors.reducing()
permalink: Java/Collectors/reducing
date: 2021-01-04
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="reducing" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T> Collector<T,?,Optional<T>> reducing(BinaryOperator<T> op)
static <T> Collector<T,?,T> reducing(T identity, BinaryOperator<T> op)
static <T,U> Collector<T,?,U> reducing(U identity, Function<? super T,? extends U> mapper, BinaryOperator<U> op)
~~~

## Parámetros
* **BinaryOperator&lt;T&gt; op**,  {% include w3api/param_description.html metodo=_data parametro="BinaryOperator<T> op" %}
* **T identity**,  {% include w3api/param_description.html metodo=_data parametro="T identity" %}
* **U identity**,  {% include w3api/param_description.html metodo=_data parametro="U identity" %}
* **BinaryOperator&lt;U&gt; op**,  {% include w3api/param_description.html metodo=_data parametro="BinaryOperator<U> op" %}
* **? extends U&gt; mapper**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> mapper" %}
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="Function<? super T" %}

## Clase Padre
[Collectors](/Java/Collectors/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.Collectors.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
