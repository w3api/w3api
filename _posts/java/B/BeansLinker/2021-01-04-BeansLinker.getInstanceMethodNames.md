---
title: BeansLinker.getInstanceMethodNames()
permalink: Java/BeansLinker/getInstanceMethodNames
date: 2021-01-04
key: JavaJava.B.BeansLinker
category: java
tags: ['java se', 'jdk.dynalink.beans', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeansLinker.metodos valor="getInstanceMethodNames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static Set<String> getInstanceMethodNames(Class<?> clazz)
~~~

## Parámetros
* **Class&lt;?&gt; clazz**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> clazz" %}

## Clase Padre
[BeansLinker](/Java/BeansLinker/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeansLinker.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
