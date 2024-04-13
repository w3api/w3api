---
title: GuardedInvocationTransformer.filter()
permalink: /Java/GuardedInvocationTransformer/filter/
date: 2021-01-11
key: Java.G.GuardedInvocationTransformer
category: Java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GuardedInvocationTransformer.metodos valor="filter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
GuardedInvocation filter(GuardedInvocation inv, LinkRequest linkRequest, LinkerServices linkerServices)
~~~

## Parámetros
* **LinkRequest linkRequest**,  {% include w3api/param_description.html metodo=_dato parametro="LinkRequest linkRequest" %}
* **LinkerServices linkerServices**,  {% include w3api/param_description.html metodo=_dato parametro="LinkerServices linkerServices" %}
* **GuardedInvocation inv**,  {% include w3api/param_description.html metodo=_dato parametro="GuardedInvocation inv" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[GuardedInvocationTransformer](/Java/GuardedInvocationTransformer/)

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
