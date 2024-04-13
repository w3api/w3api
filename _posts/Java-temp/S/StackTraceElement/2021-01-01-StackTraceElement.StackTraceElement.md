---
title: StackTraceElement.StackTraceElement()
permalink: /Java/StackTraceElement/StackTraceElement/
date: 2021-01-11
key: Java.S.StackTraceElement
category: Java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StackTraceElement.constructores valor="StackTraceElement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public StackTraceElement(String declaringClass, String methodName, String fileName, int lineNumber)
public StackTraceElement(String classLoaderName, String moduleName, String moduleVersion, String declaringClass, String methodName, String fileName, int lineNumber)
~~~

## Parámetros
* **String moduleName**,  {% include w3api/param_description.html metodo=_dato parametro="String moduleName" %}
* **String moduleVersion**,  {% include w3api/param_description.html metodo=_dato parametro="String moduleVersion" %}
* **String classLoaderName**,  {% include w3api/param_description.html metodo=_dato parametro="String classLoaderName" %}
* **String declaringClass**,  {% include w3api/param_description.html metodo=_dato parametro="String declaringClass" %}
* **String methodName**,  {% include w3api/param_description.html metodo=_dato parametro="String methodName" %}
* **int lineNumber**,  {% include w3api/param_description.html metodo=_dato parametro="int lineNumber" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_dato parametro="String fileName" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[StackTraceElement](/Java/StackTraceElement/)

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
