---
title: Collector.of()
permalink: Java/Collector/of
date: 2021-01-11
key: JavaJava.C.Collector
category: java
tags: ['java se', 'java.util.stream', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.Collector.metodos valor="of" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static <T,A,R> Collector<T,A,R> of(Supplier<A> supplier, BiConsumer<A,T> accumulator, BinaryOperator<A> combiner, Function<A,R> finisher, Collector.Characteristics... characteristics)
static <T,R> Collector<T,R,R> of(Supplier<R> supplier, BiConsumer<R,T> accumulator, BinaryOperator<R> combiner, Collector.Characteristics... characteristics)
~~~

## Parámetros
* **Supplier&lt;A&gt; supplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<A> supplier" %}
* **Collector.Characteristics... characteristics**,  {% include w3api/param_description.html metodo=_dato parametro="Collector.Characteristics... characteristics" %}
* **Supplier&lt;R&gt; supplier**,  {% include w3api/param_description.html metodo=_dato parametro="Supplier<R> supplier" %}
* **T&gt; accumulator**,  {% include w3api/param_description.html metodo=_dato parametro="T> accumulator" %}
* **BinaryOperator&lt;R&gt; combiner**,  {% include w3api/param_description.html metodo=_dato parametro="BinaryOperator<R> combiner" %}
* **BiConsumer&lt;A**,  {% include w3api/param_description.html metodo=_dato parametro="BiConsumer<A" %}
* **R&gt; finisher**,  {% include w3api/param_description.html metodo=_dato parametro="R> finisher" %}
* **BinaryOperator&lt;A&gt; combiner**,  {% include w3api/param_description.html metodo=_dato parametro="BinaryOperator<A> combiner" %}
* **Function&lt;A**,  {% include w3api/param_description.html metodo=_dato parametro="Function<A" %}
* **BiConsumer&lt;R**,  {% include w3api/param_description.html metodo=_dato parametro="BiConsumer<R" %}

## Clase Padre
[Collector](/Java/Collector/)

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
