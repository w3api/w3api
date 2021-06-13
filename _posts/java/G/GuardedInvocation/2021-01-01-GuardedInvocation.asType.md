---
title: GuardedInvocation.asType()
permalink: /Java/GuardedInvocation/asType/
date: 2021-01-11
key: Java.G.GuardedInvocation
category: Java
tags: ['java se', 'jdk.dynalink.linker', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.G.GuardedInvocation.metodos valor="asType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public GuardedInvocation asType(MethodType newType)
public GuardedInvocation asType(CallSiteDescriptor desc)
public GuardedInvocation asType(LinkerServices linkerServices, MethodType newType)
~~~

## Parámetros
* **LinkerServices linkerServices**,  {% include w3api/param_description.html metodo=_dato parametro="LinkerServices linkerServices" %}
* **CallSiteDescriptor desc**,  {% include w3api/param_description.html metodo=_dato parametro="CallSiteDescriptor desc" %}
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
