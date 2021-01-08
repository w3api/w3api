---
title: CallSiteDescriptor.CallSiteDescriptor()
permalink: Java/CallSiteDescriptor/CallSiteDescriptor
date: 2021-01-04
key: JavaJava.C.CallSiteDescriptor
category: java
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
* **MethodType methodType**,  {% include w3api/param_description.html metodo=_data parametro="MethodType methodType" %}
* **MethodHandles.Lookup lookup**,  {% include w3api/param_description.html metodo=_data parametro="MethodHandles.Lookup lookup" %}
* **Operation operation**,  {% include w3api/param_description.html metodo=_data parametro="Operation operation" %}

## Clase Padre
[CallSiteDescriptor](/Java/CallSiteDescriptor/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CallSiteDescriptor.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
