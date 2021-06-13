---
title: MethodType.appendParameterTypes()
permalink: /Java/MethodType/appendParameterTypes/
date: 2021-01-11
key: Java.M.MethodType
category: Java
tags: ['java se', 'java.lang.invoke', 'java.base', 'metodo java', 'Java 1.7']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MethodType.metodos valor="appendParameterTypes" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public MethodType appendParameterTypes(Class<?>... ptypesToInsert)
public MethodType appendParameterTypes(List<Class<?>> ptypesToInsert)
~~~

## Parámetros
* **List&lt;Class&lt;?&gt;&gt; ptypesToInsert**,  {% include w3api/param_description.html metodo=_dato parametro="List<Class<?>> ptypesToInsert" %}
* **Class&lt;?&gt;... ptypesToInsert**,  {% include w3api/param_description.html metodo=_dato parametro="Class<?>... ptypesToInsert" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[MethodType](/Java/MethodType/)

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
