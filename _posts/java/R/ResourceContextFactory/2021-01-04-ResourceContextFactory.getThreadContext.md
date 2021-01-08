---
title: ResourceContextFactory.getThreadContext()
permalink: Java/ResourceContextFactory/getThreadContext
date: 2021-01-04
key: JavaJava.R.ResourceContextFactory
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceContextFactory.metodos valor="getThreadContext" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ResourceContext getThreadContext()
public ResourceContext getThreadContext(Thread thread)
~~~

## Parámetros
* **Thread thread**,  {% include w3api/param_description.html metodo=_data parametro="Thread thread" %}

## Clase Padre
[ResourceContextFactory](/Java/ResourceContextFactory/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResourceContextFactory.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
