---
title: Collectors.toUnmodifiableMap()
permalink: /Java/Collectors/toUnmodifiableMap/
date: 2021-01-11
key: Java.C.Collectors
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="toUnmodifiableMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,K,U> Collector<T,?,Map<K,U>> toUnmodifiableMap(Function<? super T,? extends K> keyMapper, Function<? super T,? extends U> valueMapper)
static <T,K,U> Collector<T,?,Map<K,U>> toUnmodifiableMap(Function<? super T,? extends K> keyMapper, Function<? super T,? extends U> valueMapper, BinaryOperator<U> mergeFunction)
~~~

## Parámetros
* **BinaryOperator&lt;U&gt; mergeFunction**,  {% include w3api/param_description.html metodo=_dato parametro="BinaryOperator<U> mergeFunction" %}
* **? extends K&gt; keyMapper**,  {% include w3api/param_description.html metodo=_dato parametro="? extends K> keyMapper" %}
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super T" %}
* **? extends U&gt; valueMapper**,  {% include w3api/param_description.html metodo=_dato parametro="? extends U> valueMapper" %}

## Clase Padre
[Collectors](/Java/Collectors/)

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
