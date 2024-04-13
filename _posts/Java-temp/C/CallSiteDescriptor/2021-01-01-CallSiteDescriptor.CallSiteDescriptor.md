---
title: CallSiteDescriptor.CallSiteDescriptor()
permalink: /Java/CallSiteDescriptor/CallSiteDescriptor/
date: 2021-01-11
key: Java.C.CallSiteDescriptor
category: Java
tags: ['java se', 'jdk.dynalink', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CallSiteDescriptor.constructores valor="CallSiteDescriptor" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public CallSiteDescriptor(MethodHandles.Lookup lookup, Operation operation, MethodType methodType)
~~~

## Parámetros
* **MethodHandles.Lookup lookup**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandles.Lookup lookup" %}
* **MethodType methodType**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType methodType" %}
* **Operation operation**,  {% include w3api/param_description.html metodo=_dato parametro="Operation operation" %}

## Clase Padre
[CallSiteDescriptor](/Java/CallSiteDescriptor/)

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
