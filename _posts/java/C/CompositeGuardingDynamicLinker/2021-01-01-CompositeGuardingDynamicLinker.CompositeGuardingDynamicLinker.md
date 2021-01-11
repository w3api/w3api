---
title: CompositeGuardingDynamicLinker.CompositeGuardingDynamicLinker()
permalink: Java/CompositeGuardingDynamicLinker/CompositeGuardingDynamicLinker
date: 2021-01-11
key: JavaJava.C.CompositeGuardingDynamicLinker
category: java
tags: ['java se', 'jdk.dynalink.linker.support', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeGuardingDynamicLinker.constructores valor="CompositeGuardingDynamicLinker" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompositeGuardingDynamicLinker(Iterable<? extends GuardingDynamicLinker> linkers)
~~~

## Parámetros
* **Iterable&lt;? extends GuardingDynamicLinker&gt; linkers**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends GuardingDynamicLinker> linkers" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CompositeGuardingDynamicLinker](/Java/CompositeGuardingDynamicLinker/)

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
