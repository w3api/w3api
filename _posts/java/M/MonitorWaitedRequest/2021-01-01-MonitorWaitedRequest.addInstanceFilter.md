---
title: MonitorWaitedRequest.addInstanceFilter()
permalink: /Java/MonitorWaitedRequest/addInstanceFilter/
date: 2021-01-11
key: Java.M.MonitorWaitedRequest
category: Java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MonitorWaitedRequest.metodos valor="addInstanceFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addInstanceFilter(ObjectReference instance)
~~~

## Parámetros
* **ObjectReference instance**,  {% include w3api/param_description.html metodo=_dato parametro="ObjectReference instance" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[MonitorWaitedRequest](/Java/MonitorWaitedRequest/)

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
