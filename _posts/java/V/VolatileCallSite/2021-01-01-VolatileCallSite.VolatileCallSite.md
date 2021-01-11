---
title: VolatileCallSite.VolatileCallSite()
permalink: Java/VolatileCallSite/VolatileCallSite
date: 2021-01-11
key: JavaJava.V.VolatileCallSite
category: java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VolatileCallSite.constructores valor="VolatileCallSite" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public VolatileCallSite(MethodHandle target)
public VolatileCallSite(MethodType type)
~~~

## Parámetros
* **MethodHandle target**,  {% include w3api/param_description.html metodo=_dato parametro="MethodHandle target" %}
* **MethodType type**,  {% include w3api/param_description.html metodo=_dato parametro="MethodType type" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[VolatileCallSite](/Java/VolatileCallSite/)

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
