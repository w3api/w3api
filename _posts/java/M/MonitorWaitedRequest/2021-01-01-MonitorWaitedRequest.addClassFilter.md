---
title: MonitorWaitedRequest.addClassFilter()
permalink: /Java/MonitorWaitedRequest/addClassFilter/
date: 2021-01-11
key: Java.M.MonitorWaitedRequest
category: Java
tags: ['java se', 'com.sun.jdi.request', 'jdk.jdi', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MonitorWaitedRequest.metodos valor="addClassFilter" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void addClassFilter(ReferenceType refType)
void addClassFilter(String classPattern)
~~~

## Parámetros
* **ReferenceType refType**,  {% include w3api/param_description.html metodo=_dato parametro="ReferenceType refType" %}
* **String classPattern**,  {% include w3api/param_description.html metodo=_dato parametro="String classPattern" %}

## Excepciones
[InvalidRequestStateException](/Java/InvalidRequestStateException/)

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
