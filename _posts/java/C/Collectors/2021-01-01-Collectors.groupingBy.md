---
title: Collectors.groupingBy()
permalink: /Java/Collectors/groupingBy/
date: 2021-01-11
key: Java.C.Collectors
category: Java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collectors.metodos valor="groupingBy" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,K> Collector<T,?,Map<K,List<T>>> groupingBy(Function<? super T,? extends K> classifier)
static <T,K,D,A,M extends Map<K,D>>Collector<T,?,M> groupingBy(Function<? super T,? extends K> classifier, Supplier<M> mapFactory, Collector<? super T,A,D> downstream)
static <T,K,A,D> Collector<T,?,Map<K,D>> groupingBy(Function<? super T,? extends K> classifier, Collector<? super T,A,D> downstream)
~~~

## Parámetros
* **Function&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="Function<? super T" %}
* **A**,  {% include w3api/param_description.html metodo=_dato parametro="A" %}
* **? extends K&gt; classifier**,  {% include w3api/param_description.html metodo=_dato parametro="? extends K> classifier" %}
* **Supplier&lt;M&gt; mapFactory**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<M> mapFactory" %}
* **D&gt; downstream**,  {% include w3api/param_description.html metodo=_dato parametro="D> downstream" %}
* **Collector&lt;? super T**,  {% include w3api/param_description.html metodo=_dato parametro="Collector<? super T" %}

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
