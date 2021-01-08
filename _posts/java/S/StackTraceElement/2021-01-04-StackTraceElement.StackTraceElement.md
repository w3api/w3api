---
title: StackTraceElement.StackTraceElement()
permalink: Java/StackTraceElement/StackTraceElement
date: 2021-01-04
key: JavaJava.S.StackTraceElement
category: java
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
* **String declaringClass**,  {% include w3api/param_description.html metodo=_data parametro="String declaringClass" %}
* **String moduleVersion**,  {% include w3api/param_description.html metodo=_data parametro="String moduleVersion" %}
* **String classLoaderName**,  {% include w3api/param_description.html metodo=_data parametro="String classLoaderName" %}
* **String moduleName**,  {% include w3api/param_description.html metodo=_data parametro="String moduleName" %}
* **int lineNumber**,  {% include w3api/param_description.html metodo=_data parametro="int lineNumber" %}
* **String fileName**,  {% include w3api/param_description.html metodo=_data parametro="String fileName" %}
* **String methodName**,  {% include w3api/param_description.html metodo=_data parametro="String methodName" %}

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
{%- for _ldc in site.data.Java.S.StackTraceElement.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
