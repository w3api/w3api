---
title: ResourceContext.boundThreads()
permalink: Java/ResourceContext/boundThreads
date: 2021-01-04
key: JavaJava.R.ResourceContext
category: java
tags: ['java se', 'jdk.management.resource', 'jdk.management.resource', 'metodo java', '8u40']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceContext.metodos valor="boundThreads" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
default Stream<Thread> boundThreads()
~~~

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
{%- for _ldc in site.data.Java.R.ResourceContext.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
