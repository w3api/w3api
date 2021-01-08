---
title: Collectors.toConcurrentMap()
permalink: Java/Collectors/toConcurrentMap
date: 2021-01-04
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="toConcurrentMap" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,K,U> Collector<T,?,ConcurrentMap<K,U>> toConcurrentMap(Function<? super T,? extends K> keyMapper, Function<? super T,? extends U> valueMapper)
static <T,K,U> Collector<T,?,ConcurrentMap<K,U>> toConcurrentMap(Function<? super T,? extends K> keyMapper, Function<? super T,? extends U> valueMapper, BinaryOperator<U> mergeFunction)
static <T,K,U,M extends ConcurrentMap<K,U>>Collector<T,?,M> toConcurrentMap(Function<? super T,? extends K> keyMapper, Function<? super T,? extends U> valueMapper, BinaryOperator<U> mergeFunction, Supplier<M> mapFactory)
~~~

## Parámetros
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="Function<? super T" %}
* **Supplier&lt;M&gt; mapFactory**,  {% include w3api/param_description.html metodo=_data parametro="Supplier<M> mapFactory" %}
* **? extends K&gt; keyMapper**,  {% include w3api/param_description.html metodo=_data parametro="? extends K> keyMapper" %}
* **? extends U&gt; valueMapper**,  {% include w3api/param_description.html metodo=_data parametro="? extends U> valueMapper" %}
* **BinaryOperator&lt;U&gt; mergeFunction**,  {% include w3api/param_description.html metodo=_data parametro="BinaryOperator<U> mergeFunction" %}

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
