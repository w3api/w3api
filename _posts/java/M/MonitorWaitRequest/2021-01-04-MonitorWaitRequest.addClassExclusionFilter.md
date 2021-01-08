---
title: MonitorWaitRequest.addClassExclusionFilter()
permalink: Java/MonitorWaitRequest/addClassExclusionFilter
date: 2021-01-04
key: JavaJava.M.MonitorWaitRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MonitorWaitRequest.metodos valor="addClassExclusionFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addClassExclusionFilter(String classPattern)
~~~

## Parámetros
* **String classPattern**,  {% include w3api/param_description.html metodo=_data parametro="String classPattern" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/)

## Clase Padre
[MonitorWaitRequest](/Java/MonitorWaitRequest/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MonitorWaitRequest.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
