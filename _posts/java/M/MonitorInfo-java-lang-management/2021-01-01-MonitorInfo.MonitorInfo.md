---
title: MonitorInfo.MonitorInfo()
permalink: Java/MonitorInfo-java-lang-management/MonitorInfo
date: 2021-01-11
key: JavaJava.M.MonitorInfo-java-lang-management
category: Java
tags: ['java se', 'java.lang.management', 'java.management', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MonitorInfo-java-lang-management.constructores valor="MonitorInfo" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MonitorInfo(String className, int identityHashCode, int stackDepth, StackTraceElement stackFrame)
~~~

## Parámetros
* **int stackDepth**,  {% include w3api/param_description.html metodo=_dato parametro="int stackDepth" %}
* **int identityHashCode**,  {% include w3api/param_description.html metodo=_dato parametro="int identityHashCode" %}
* **StackTraceElement stackFrame**,  {% include w3api/param_description.html metodo=_dato parametro="StackTraceElement stackFrame" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[MonitorInfo](/Java/MonitorInfo-java-lang-management/)

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
