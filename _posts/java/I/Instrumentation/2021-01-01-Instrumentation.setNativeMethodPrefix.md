---
title: Instrumentation.setNativeMethodPrefix()
permalink: /Java/Instrumentation/setNativeMethodPrefix/
date: 2021-01-11
key: Java.I.Instrumentation
category: Java
tags: ['java se', 'java.lang.instrument', 'java.instrument', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.I.Instrumentation.metodos valor="setNativeMethodPrefix" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setNativeMethodPrefix(ClassFileTransformer transformer, String prefix)
~~~

## Parámetros
* **String prefix**,  {% include w3api/param_description.html metodo=_dato parametro="String prefix" %}
* **ClassFileTransformer transformer**,  {% include w3api/param_description.html metodo=_dato parametro="ClassFileTransformer transformer" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[Instrumentation](/Java/Instrumentation/)

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
