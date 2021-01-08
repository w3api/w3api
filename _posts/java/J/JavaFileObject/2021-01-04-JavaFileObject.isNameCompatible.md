---
title: JavaFileObject.isNameCompatible()
permalink: Java/JavaFileObject/isNameCompatible
date: 2021-01-04
key: JavaJava.J.JavaFileObject
category: java
tags: ['java se', 'javax.tools', 'java.compiler', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JavaFileObject.metodos valor="isNameCompatible" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean isNameCompatible(String simpleName, JavaFileObject.Kind kind)
~~~

## Parámetros
* **JavaFileObject.Kind kind**,  {% include w3api/param_description.html metodo=_data parametro="JavaFileObject.Kind kind" %}
* **String simpleName**,  {% include w3api/param_description.html metodo=_data parametro="String simpleName" %}

## Clase Padre
[JavaFileObject](/Java/JavaFileObject/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JavaFileObject.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
