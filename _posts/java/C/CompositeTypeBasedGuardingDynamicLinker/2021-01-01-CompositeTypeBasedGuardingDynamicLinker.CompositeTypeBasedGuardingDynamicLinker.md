---
title: CompositeTypeBasedGuardingDynamicLinker.CompositeTypeBasedGuardingDynamicLinker()
permalink: /Java/CompositeTypeBasedGuardingDynamicLinker/CompositeTypeBasedGuardingDynamicLinker/
date: 2021-01-11
key: Java.C.CompositeTypeBasedGuardingDynamicLinker
category: Java
tags: ['java se', 'jdk.dynalink.linker.support', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeTypeBasedGuardingDynamicLinker.constructores valor="CompositeTypeBasedGuardingDynamicLinker" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CompositeTypeBasedGuardingDynamicLinker(Iterable<? extends TypeBasedGuardingDynamicLinker> linkers)
~~~

## Parámetros
* **Iterable&lt;? extends TypeBasedGuardingDynamicLinker&gt; linkers**,  {% include w3api/param_description.html metodo=_dato parametro="Iterable<? extends TypeBasedGuardingDynamicLinker> linkers" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CompositeTypeBasedGuardingDynamicLinker](/Java/CompositeTypeBasedGuardingDynamicLinker/)

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
