---
title: GuardedInvocation.asTypeSafeReturn()
permalink: /Java/GuardedInvocation/asTypeSafeReturn/
date: 2021-01-11
key: Java.G.GuardedInvocation
category: Java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GuardedInvocation.metodos valor="asTypeSafeReturn" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GuardedInvocation asTypeSafeReturn(LinkerServices linkerServices, MethodType newType)
~~~

## Parámetros
* **LinkerServices linkerServices**,  {% include w3api/param_description.html metodo=_dato parametro="LinkerServices linkerServices" %}
* **MethodType newType**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType newType" %}

## Clase Padre
[GuardedInvocation](/Java/GuardedInvocation/)

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
