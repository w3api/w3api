---
title: ResourceContext.removeResourceMeter()
permalink: /Java/ResourceContext/removeResourceMeter/
date: 2021-01-11
key: Java.R.ResourceContext
category: Java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceContext.metodos valor="removeResourceMeter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default boolean removeResourceMeter(ResourceMeter meter)
~~~

## Parámetros
* **ResourceMeter meter**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceMeter meter" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/)

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
