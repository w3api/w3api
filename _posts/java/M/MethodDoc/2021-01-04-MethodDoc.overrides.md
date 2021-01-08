---
title: MethodDoc.overrides()
permalink: Java/MethodDoc/overrides
date: 2021-01-04
key: JavaJava.M.MethodDoc
category: java
tags: ['java se', 'com.sun.javadoc', 'jdk.javadoc', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodDoc.metodos valor="overrides" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
boolean overrides(MethodDoc meth)
~~~

## Parámetros
* **MethodDoc meth**,  {% include w3api/param_description.html metodo=_data parametro="MethodDoc meth" %}

## Clase Padre
[MethodDoc](/Java/MethodDoc/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.M.MethodDoc.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
