---
title: WatchpointRequest.addInstanceFilter()
permalink: Java/WatchpointRequest/addInstanceFilter
date: 2021-01-04
key: JavaJava.W.WatchpointRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.3']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.W.WatchpointRequest.metodos valor="addInstanceFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addInstanceFilter(ObjectReference instance)
~~~

## Parámetros
* **ObjectReference instance**,  {% include w3api/param_description.html metodo=_data parametro="ObjectReference instance" %}

## Excepciones
[UnsupportedOperationException](/Java/UnsupportedOperationException/), [InvalidRequestStateException](/Java/InvalidRequestStateException/)

## Clase Padre
[WatchpointRequest](/Java/WatchpointRequest/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.W.WatchpointRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
