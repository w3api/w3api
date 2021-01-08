---
title: CompositeGuardingDynamicLinker.getGuardedInvocation()
permalink: Java/CompositeGuardingDynamicLinker/getGuardedInvocation
date: 2021-01-04
key: JavaJava.C.CompositeGuardingDynamicLinker
category: java
tags: ['java se', 'jdk.dynalink.linker.support', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CompositeGuardingDynamicLinker.metodos valor="getGuardedInvocation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GuardedInvocation getGuardedInvocation(LinkRequest linkRequest, LinkerServices linkerServices) throws Exception
~~~

## Parámetros
* **LinkRequest linkRequest**,  {% include w3api/param_description.html metodo=_data parametro="LinkRequest linkRequest" %}
* **LinkerServices linkerServices**,  {% include w3api/param_description.html metodo=_data parametro="LinkerServices linkerServices" %}

## Excepciones
[Exception](/Java/Exception/)

## Clase Padre
[CompositeGuardingDynamicLinker](/Java/CompositeGuardingDynamicLinker/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CompositeGuardingDynamicLinker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
