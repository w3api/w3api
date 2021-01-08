---
title: ClassLoader.setSigners()
permalink: Java/ClassLoader/setSigners
date: 2021-01-04
key: JavaJava.C.ClassLoader
category: java
tags: ['java se', 'java.lang', 'java.base', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ClassLoader.metodos valor="setSigners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void setSigners(Class<?> c, Object[] signers)
~~~

## Parámetros
* **Class&lt;?&gt; c**,  {% include w3api/param_description.html metodo=_data parametro="Class<?> c" %}
* **Object[] signers**,  {% include w3api/param_description.html metodo=_data parametro="Object[] signers" %}

## Clase Padre
[ClassLoader](/Java/ClassLoader/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ClassLoader.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
