---
title: Collectors.groupingByConcurrent()
permalink: Java/Collectors/groupingByConcurrent
date: 2021-01-04
key: JavaJava.C.Collectors
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="groupingByConcurrent" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,K> Collector<T,?,ConcurrentMap<K,List<T>>> groupingByConcurrent(Function<? super T,? extends K> classifier)
static <T,K,A,D,M extends ConcurrentMap<K,D>>Collector<T,?,M> groupingByConcurrent(Function<? super T,? extends K> classifier, Supplier<M> mapFactory, Collector<? super T,A,D> downstream)
static <T,K,A,D> Collector<T,?,ConcurrentMap<K,D>> groupingByConcurrent(Function<? super T,? extends K> classifier, Collector<? super T,A,D> downstream)
~~~

## Parámetros
* **Supplier&lt;M&gt; mapFactory**,  {% include w3api/param_description.html metodo=_data parametro="Supplier<M> mapFactory" %}
* **? extends K&gt; classifier**,  {% include w3api/param_description.html metodo=_data parametro="? extends K> classifier" %}
* **D&gt; downstream**,  {% include w3api/param_description.html metodo=_data parametro="D> downstream" %}
* **A**,  {% include w3api/param_description.html metodo=_data parametro="A" %}
* **Collector&lt;? super T**,  {% include w3api/param_description.html metodo=_data parametro="Collector<? super T" %}
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
