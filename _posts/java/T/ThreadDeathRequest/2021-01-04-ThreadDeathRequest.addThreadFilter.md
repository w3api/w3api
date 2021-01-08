---
title: ThreadDeathRequest.addThreadFilter()
permalink: Java/ThreadDeathRequest/addThreadFilter
date: 2021-01-04
key: JavaJava.T.ThreadDeathRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.ThreadDeathRequest.metodos valor="addThreadFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addThreadFilter(ThreadReference thread)
~~~

## Parámetros
* **ThreadReference thread**,  {% include w3api/param_description.html metodo=_data parametro="ThreadReference thread" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/)

## Clase Padre
[ThreadDeathRequest](/Java/ThreadDeathRequest/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.ThreadDeathRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
