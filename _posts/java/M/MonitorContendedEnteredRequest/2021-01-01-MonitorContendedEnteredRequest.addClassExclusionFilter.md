---
title: MonitorContendedEnteredRequest.addClassExclusionFilter()
permalink: Java/MonitorContendedEnteredRequest/addClassExclusionFilter
date: 2021-01-11
key: JavaJava.M.MonitorContendedEnteredRequest
category: java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MonitorContendedEnteredRequest.metodos valor="addClassExclusionFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addClassExclusionFilter(String classPattern)
~~~

## Parámetros
* **String classPattern**,  {% include w3api/param_description.html metodo=_dato parametro="String classPattern" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/)

## Clase Padre
[MonitorContendedEnteredRequest](/Java/MonitorContendedEnteredRequest/)

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
