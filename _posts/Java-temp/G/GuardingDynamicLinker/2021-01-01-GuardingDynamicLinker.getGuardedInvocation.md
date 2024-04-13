---
title: GuardingDynamicLinker.getGuardedInvocation()
permalink: /Java/GuardingDynamicLinker/getGuardedInvocation/
date: 2021-01-11
key: Java.G.GuardingDynamicLinker
category: Java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GuardingDynamicLinker.metodos valor="getGuardedInvocation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
GuardedInvocation getGuardedInvocation(LinkRequest linkRequest, LinkerServices linkerServices) throws Exception
~~~

## Parámetros
* **LinkRequest linkRequest**,  {% include w3api/param_description.html metodo=_dato parametro="LinkRequest linkRequest" %}
* **LinkerServices linkerServices**,  {% include w3api/param_description.html metodo=_dato parametro="LinkerServices linkerServices" %}

## Excepciones
[Exception](/Java/Exception/)

## Clase Padre
[GuardingDynamicLinker](/Java/GuardingDynamicLinker/)

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
