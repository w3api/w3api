---
title: TypeUtilities.isSubtype()
permalink: /Java/TypeUtilities/isSubtype/
date: 2021-01-11
key: Java.T.TypeUtilities
category: Java
tags: ['java se', 'jdk.dynalink.linker.support', 'jdk.dynalink', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TypeUtilities.metodos valor="isSubtype" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static boolean isSubtype(Class<?> subType, Class<?> superType)
~~~

## Parámetros
* **Class&lt;?&gt; superType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> superType" %}
* **Class&lt;?&gt; subType**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?> subType" %}

## Clase Padre
[TypeUtilities](/Java/TypeUtilities/)

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
