---
title: DynamicLinkerFactory.setFallbackLinkers()
permalink: Java/DynamicLinkerFactory/setFallbackLinkers
date: 2021-01-11
key: JavaJava.D.DynamicLinkerFactory
category: java
tags: ['java se', 'jdk.dynalink', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DynamicLinkerFactory.metodos valor="setFallbackLinkers" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setFallbackLinkers(List<? extends GuardingDynamicLinker> fallbackLinkers)
public void setFallbackLinkers(GuardingDynamicLinker... fallbackLinkers)
~~~

## Parámetros
* **List&lt;? extends GuardingDynamicLinker&gt; fallbackLinkers**,  {% include w3api/param_description.html metodo=_dato parametro="List<? extends GuardingDynamicLinker> fallbackLinkers" %}
* **GuardingDynamicLinker... fallbackLinkers**,  {% include w3api/param_description.html metodo=_dato parametro="GuardingDynamicLinker... fallbackLinkers" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[DynamicLinkerFactory](/Java/DynamicLinkerFactory/)

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
