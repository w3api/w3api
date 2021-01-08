---
title: Collectors.toUnmodifiableMap()
permalink: Java/Collectors/toUnmodifiableMap
date: 2021-01-04
key: JavaJava.C.Collectors
category: java
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
* **BinaryOperator&lt;U&gt; mergeFunction**,  {% include w3api/param_description.html metodo=_data parametro="BinaryOperator<U> mergeFunction" %}
* **? extends K&gt; keyMapper**,  {% include w3api/param_description.html metodo=_data parametro="? extends K> keyMapper" %}
* **? extends U&gt; valueMapper**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> valueMapper" %}
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
