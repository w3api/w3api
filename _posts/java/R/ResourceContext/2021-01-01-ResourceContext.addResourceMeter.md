---
title: ResourceContext.addResourceMeter()
permalink: Java/ResourceContext/addResourceMeter
date: 2021-01-11
key: JavaJava.R.ResourceContext
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceContext.metodos valor="addResourceMeter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default void addResourceMeter(ResourceMeter meter)
~~~

## Parámetros
* **ResourceMeter meter**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceMeter meter" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ResourceContext](/Java/ResourceContext/)

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
